# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Question, Field

# JSON 반환: 모든 질문 가져오기
def get_questions(request):
    # DB에서 질문 순서대로 가져오기
    questions = Question.objects.all().order_by('id')
    
    # Q1, Q2, ... 형식으로 매핑
    data = {f"q{i+1}": {"id": q.id, "question": q.text} for i, q in enumerate(questions)}
    
    return JsonResponse({"questions": data})

# 제출한 응답을 처리하고 결과를 반환하는 뷰
@csrf_exempt
def submit_test(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST 요청만 가능합니다."}, status=400)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON 형식으로 데이터를 보내주세요."}, status=400)

    # 각 분야별 점수 초기화
    fields = Field.objects.all()  # 모든 분야 가져오기
    scores = {field.name: 0 for field in fields}

    # 각 질문에 대한 응답 처리
    for i, field_answer in data.items():
        try:
            question_id = int(i[1:])  # 'q1', 'q2' 등에서 숫자만 추출
            question = Question.objects.get(id=question_id)

            if field_answer == "예":  # '예'라면 해당 분야에 점수 추가
                for field in question.fields.all():
                    scores[field.name] += 1  # 해당 분야 점수 증가
        except Exception as e:
            return JsonResponse({"error": f"잘못된 데이터: {e}"}, status=400)

    # 최고 점수를 가진 분야 찾기
    max_score = max(scores.values())
    best_fields = [field for field, score in scores.items() if score == max_score]

    # 디버깅용 print (반환되는 데이터를 확인)
    print("Scores:", scores)
    print("Best Fields:", best_fields)

    return JsonResponse({
        "best_fields": best_fields,
        "scores": scores
    }, json_dumps_params={'ensure_ascii': False})
