# tests.py
from django.test import TestCase
from django.test.client import RequestFactory
import json
from it_test.models import Question, Field
from it_test.views import submit_test

class TestSubmitTestView(TestCase):
    def setUp(self):
        # 필드 데이터 입력
        backend = Field.objects.create(name="백엔드")
        frontend = Field.objects.create(name="프론트엔드")
        cyber_security = Field.objects.create(name="사이버보안")
        game_development = Field.objects.create(name="게임개발")
        iot = Field.objects.create(name="사물인터넷")
        big_data = Field.objects.create(name="빅데이터")
        ai = Field.objects.create(name="인공지능")

        # 질문 데이터 입력
        q1 = Question.objects.create(text="논리적으로 문제를 해결하는 걸 좋아한다")
        q1.fields.add(backend)  # 백엔드 분야에 속함

        q2 = Question.objects.create(text="시각적인 디자인을 다루는 걸 좋아한다")
        q2.fields.add(frontend)  # 프론트엔드 분야에 속함

        q3 = Question.objects.create(text="시스템 보안이나 해킹 방어에 관심이 있다")
        q3.fields.add(cyber_security)  # 사이버보안 분야에 속함

        q4 = Question.objects.create(text="게임의 스토리나 그래픽을 만드는 게 재밌다")
        q4.fields.add(game_development)  # 게임개발 분야에 속함

        q5 = Question.objects.create(text="센서나 기기를 다뤄서 직접 작동시키는 게 흥미롭다")
        q5.fields.add(iot)  # 사물인터넷 분야에 속함

        q6 = Question.objects.create(text="데이터나 통계를 분석하는 걸 좋아한다")
        q6.fields.add(big_data)  # 빅데이터 분야에 속함

        q7 = Question.objects.create(text="인공지능이나 머신러닝 기술에 흥미가 있다")
        q7.fields.add(ai)  # 인공지능 분야에 속함

        q8 = Question.objects.create(text="코드를 짜서 효율적으로 프로그램을 만들고 싶다")
        q8.fields.add(backend)  # 백엔드 분야에 속함

        q9 = Question.objects.create(text="사용자들이 편하게 쓸 수 있는 인터페이스에 관심이 있다")
        q9.fields.add(frontend)  # 프론트엔드 분야에 속함

        q10 = Question.objects.create(text="새로운 기술을 탐구하고 배우는 게 즐겁다")
        q10.fields.add(big_data)  # 빅데이터, 인공지능 분야에 속함
        q10.fields.add(ai)

    def test_submit_test(self):
        # POST 요청에 필요한 데이터 생성
        data = {
            "q1": "예",
            "q2": "예",
            "q3": "아니오",
            "q4": "예",
            "q5": "아니오",
            "q6": "예",
            "q7": "예",
            "q8": "예",
            "q9": "예",
            "q10": "예"
        }

        # RequestFactory를 사용하여 POST 요청 만들기
        rf = RequestFactory()
        request = rf.post('/submit_test/', json.dumps(data), content_type='application/json')

        # submit_test 뷰 호출
        response = submit_test(request)

        # 결과 확인
        response_data = json.loads(response.content.decode())

        # best_fields가 예상대로 나오는지 확인
        self.assertIn("best_fields", response_data)
        self.assertIn("scores", response_data)

        # scores 값 검증 (최대 점수 필드를 검증)
        self.assertEqual(response_data["scores"]["백엔드"], 2)
        self.assertEqual(response_data["scores"]["프론트엔드"], 2)
        self.assertEqual(response_data["scores"]["사이버보안"], 0)
        self.assertEqual(response_data["scores"]["게임개발"], 1)
        self.assertEqual(response_data["scores"]["사물인터넷"], 0)
        self.assertEqual(response_data["scores"]["빅데이터"], 2)
        self.assertEqual(response_data["scores"]["인공지능"], 2)

        # best_fields가 가장 높은 점수를 가진 분야로 나오는지 확인
        self.assertEqual(response_data["best_fields"], ["백엔드", "프론트엔드", "빅데이터", "인공지능"])
