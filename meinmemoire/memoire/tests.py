from django.test import TestCase
from .models import Memoire, BasePlanMemoire, PremiumPlanMemoire, Question, Answer, BasePlanAnswer, PremiumPlanAnswer, QuestionAnswerSet, BasePlanQuestionAnswerSet, PremiumPlanQuestionAnswerSet
from django.contrib.auth import get_user_model
from django.conf import settings
from unittest import skip

User = get_user_model()


class MemoireModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Foo", password="bar")
        self.memoire_type = Memoire

    def test_model_exists(self):
        self.assertTrue(issubclass(self.memoire_type, Memoire))

        count = self.memoire_type.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        memoire = self.memoire_type.create(user=self.user)
        self.assertTrue(isinstance(memoire, Memoire))

        count = self.memoire_type.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(memoire.user, self.user)


class BasePlanMemoireModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Foo", password="bar")
        self.memoire_type = BasePlanMemoire

    def test_model_exists(self):
        self.assertTrue(issubclass(self.memoire_type, Memoire))

        count = self.memoire_type.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        memoire = self.memoire_type.create(user=self.user)
        self.assertTrue(isinstance(memoire, BasePlanMemoire))

        count = self.memoire_type.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(memoire.user, self.user)


class PremiumPlanMemoireModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Foo", password="bar")
        self.memoire_type = PremiumPlanMemoire

    def test_model_exists(self):
        self.assertTrue(issubclass(self.memoire_type, Memoire))

        count = self.memoire_type.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        memoire = self.memoire_type.create(user=self.user)
        self.assertTrue(isinstance(memoire, PremiumPlanMemoire))

        count = self.memoire_type.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(memoire.user, self.user)


class QuestionModelTest(TestCase):
    def setUp(self):
        self.text = "Some very interesting question?"

    def test_model_exists(self):
        self.assertTrue(issubclass(Question, Question))

        count = Question.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        question = Question.create(text=self.text)
        self.assertTrue(isinstance(question, Question))

        count = Question.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(question.text, self.text)

    def test_answer_set(self):
        question = Question.create(text=self.text)
        user = User.objects.create_user(username="Foo", password="bar")

        base_answer = BasePlanAnswer.create(
            text="Some answer", user=user, question=question)
        self.assertEqual(question.answer_set(), [base_answer])

        premium_answer = PremiumPlanAnswer.create(
            text="Some premium answer", user=user, question=question)
        self.assertTrue(premium_answer in question.answer_set())
        self.assertTrue(base_answer in question.answer_set())


class AnswerModelTest(TestCase):
    def setUp(self):
        self.question = Question.create(text="Some very interesting question?")
        self.text = None
        self.answer_type = Answer
        self.user = User.objects.create_user(username="Foo", password="bar")

    def test_model_exists(self):
        self.assertTrue(issubclass(self.answer_type, Answer))

        count = self.answer_type.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        answer = self.answer_type.create(
            question=self.question, text=self.text, user=self.user)
        self.assertTrue(isinstance(answer, Answer))

        count = self.answer_type.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(answer.user, self.user)


class BasePlanAnswerModelTest(TestCase):
    def setUp(self):
        self.question = Question.create(text="Some very interesting question?")
        self.text = "Some very interesting answer!"
        self.answer_type = BasePlanAnswer
        self.user = User.objects.create_user(username="Foo", password="bar")

    def test_model_exists(self):
        self.assertTrue(issubclass(self.answer_type, Answer))

        count = self.answer_type.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        answer = self.answer_type.create(
            question=self.question, text=self.text, user=self.user)
        self.assertTrue(isinstance(answer, BasePlanAnswer))

        count = self.answer_type.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(answer.question, self.question)
        self.assertEqual(answer.text, self.text)
        self.assertEqual(
            self.question.baseplananswer_set.first(), answer)
        self.assertEqual(answer.user, self.user)


class PremiumPlanAnswerModelTest(TestCase):
    def setUp(self):
        self.question = Question.create(text="Some very interesting question?")
        self.text = "Some very interesting answer!"
        self.answer_type = PremiumPlanAnswer
        self.user = User.objects.create_user(username="Foo", password="bar")

    def test_model_exists(self):
        self.assertTrue(issubclass(self.answer_type, Answer))

        count = self.answer_type.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        answer = self.answer_type.create(
            question=self.question, text=self.text, user=self.user)
        self.assertTrue(isinstance(answer, PremiumPlanAnswer))

        count = self.answer_type.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(answer.question, self.question)
        self.assertEqual(answer.text, self.text)
        self.assertEqual(
            self.question.premiumplananswer_set.first(), answer)
        self.assertEqual(answer.user, self.user)


class QuestionAnswerSetModelTest(TestCase):
    def setUp(self):
        self.qas_type = QuestionAnswerSet
        self.question = Question.create(text="Some very interesting question?")
        self.order = 1

    def test_model_exists(self):
        self.assertTrue(issubclass(self.qas_type, QuestionAnswerSet))

        count = self.qas_type.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        qas = self.qas_type.create(
            order=self.order, question_chosen=self.question)
        self.assertTrue(isinstance(qas, QuestionAnswerSet))

        count = self.qas_type.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(qas.order, self.order)
        self.assertEqual(qas.question_chosen, self.question)


class BasePlanQuestionAnswerSetModelTest(TestCase):
    def setUp(self):
        self.qas_type = BasePlanQuestionAnswerSet
        self.question = Question.create(text="Some very interesting question?")

        self.user = User.objects.create_user(username="Foo", password="bar")
        answer_type = BasePlanAnswer
        self.answer = answer_type.create(
            question=self.question, text="Answer.", user=self.user)

        self.order = 1

        memoire_type = BasePlanMemoire
        self.memoire = memoire_type.create(user=self.user)

    def test_model_exists(self):
        self.assertTrue(issubclass(self.qas_type, QuestionAnswerSet))

        count = self.qas_type.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        qas = self.qas_type.create(
            order=self.order, question_chosen=self.question, answer=self.answer, memoire=self.memoire)
        self.assertTrue(isinstance(qas, BasePlanQuestionAnswerSet))

        count = self.qas_type.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(qas.order, self.order)
        self.assertEqual(qas.question_chosen, self.question)
        self.assertEqual(qas.answer, self.answer)
        self.assertEqual(qas.memoire, self.memoire)


class PremiumPlanQuestionAnswerSetModelTest(TestCase):
    def setUp(self):
        self.qas_type = PremiumPlanQuestionAnswerSet
        self.question = Question.create(text="Some very interesting question?")

        self.user = User.objects.create_user(username="Foo", password="bar")
        answer_type = PremiumPlanAnswer
        self.answer = answer_type.create(
            question=self.question, text="Answer.", user=self.user)

        self.order = 1

        memoire_type = PremiumPlanMemoire
        self.memoire = memoire_type.create(user=self.user)

    def test_model_exists(self):
        self.assertTrue(issubclass(self.qas_type, QuestionAnswerSet))

        count = self.qas_type.objects.count()
        self.assertEqual(count, 0)

    def test_create(self):
        qas = self.qas_type.create(
            order=self.order, question_chosen=self.question, answer=self.answer, memoire=self.memoire)
        self.assertTrue(isinstance(qas, PremiumPlanQuestionAnswerSet))

        count = self.qas_type.objects.count()
        self.assertEqual(count, 1)

        self.assertEqual(qas.order, self.order)
        self.assertEqual(qas.question_chosen, self.question)
        self.assertEqual(qas.answer, self.answer)
        self.assertEqual(qas.memoire, self.memoire)
