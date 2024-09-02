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
