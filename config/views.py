from django.views.generic import TemplateView
from allauth.account.forms import LoginForm


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the login form to the template
        context["form"] = LoginForm()
        return context
