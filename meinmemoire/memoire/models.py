from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class Memoire(models.Model):
    creation_date = models.DateTimeField(
        "Creation Date", default=timezone.now)
    user = models.ForeignKey(User, verbose_name="User",
                             on_delete=models.CASCADE)

    subscription_price = None

    @classmethod
    def create(cls, user):
        return cls.objects.create(user=user)


class BasePlanMemoire(Memoire):
    pass


class PremiumPlanMemoire(Memoire):
    pass


# TODO: Group or tag ceratain question to suggest them as alternatives
class Question(models.Model):
    creation_date = models.DateTimeField(
        "Creation Date", default=timezone.now)
    text = models.CharField("Question Text", max_length=250, unique=True)

    @classmethod
    def create(cls, text):
        return cls.objects.create(text=text)

    def answer_set(self) -> list:
        a_set = []
        print(f"{self.baseplananswer_set.all()=}")
        for a in self.baseplananswer_set.all():
            a_set.append(a)
        for a in self.premiumplananswer_set.all():
            a_set.append(a)
        return a_set


class Answer(models.Model):
    creation_date = models.DateTimeField(
        "Creation Date", default=timezone.now)
    user = models.ForeignKey(User, verbose_name="User",
                             on_delete=models.CASCADE)

    @classmethod
    def create(cls, question, user, text=None):
        if cls == BasePlanAnswer or cls == PremiumPlanAnswer:
            return cls.objects.create(text=text, user=user, question=question)
        return cls.objects.create(user=user)


class BasePlanAnswer(Answer):
    text = models.TextField(
        "Answer Text", max_length=settings.BASE_MAX_ANSWER_LENGTH)
    question = models.ForeignKey(
        Question, verbose_name="Question Answered", on_delete=models.CASCADE)


class PremiumPlanAnswer(Answer):
    text = models.TextField(
        "Answer Text", max_length=settings.PREMIUM_MAX_ANSWER_LENGTH)
    question = models.ForeignKey(
        Question, verbose_name="Question Answered", on_delete=models.CASCADE)


# class BasePlanQuestionAnswerSet(models.Model):
#     creation_date = models.DateTimeField(
#         "Creation Date", default=timezone.now)
#     order = models.PositiveSmallIntegerField("Question Order")
#     question_chosen = models.ForeignKey(
#         Question, verbose_name="Question Chosen", on_delete=models.CASCADE)
#     answer = models.ForeignKey(
#         BasePlanAnswer, verbose_name="Answer to Question", on_delete=models.CASCADE)
#     memoire = models.ForeignKey(
#         BasePlanMemoire, verbose_name="Memoire Belonging to", on_delete=models.CASCADE)
#
#
# class PremiumPlanQuestionAnswerSet(models.Model):
#     creation_date = models.DateTimeField(
#         "Creation Date", default=timezone.now)
#     order = models.PositiveSmallIntegerField("Question Order")
#     question_chosen = models.ForeignKey(
#         Question, verbose_name="Question Chosen", on_delete=models.CASCADE)
#     memoire = models.ForeignKey(
#         PremiumPlanMemoire, verbose_name="Memoire Belonging to", on_delete=models.CASCADE)
#
