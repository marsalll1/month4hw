from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RegisterForm, ResumeForm, LoginForm
from django.contrib.auth import login

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['resume_form'] = ResumeForm(self.request.POST)
        else:
            context['resume_form'] = ResumeForm()
        return context

    def form_valid(self, form):
        resume_form = ResumeForm(self.request.POST)
        if resume_form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            resume = resume_form.save(commit=False)
            resume.user = user
            resume.save()
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'