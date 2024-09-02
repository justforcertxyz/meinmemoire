from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "landing/index.html"


class PrivacyPolicyView(TemplateView):
    template_name = "landing/privacy_policy.html"
