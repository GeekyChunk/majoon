import json
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from app.models import *
from app.forms import *

@csrf_exempt
def addReport(request):
    if request.method == "POST":
        body = json.loads(request.body.decode("utf-8"))
        magic_code = get_object_or_404(MagicCode, code=body["magic"])
        user = magic_code.user
        paste = Paste.objects.filter(user=user).first()
        if paste and (paste.level-5) >= 0:
            paste.level = paste.level -5
            paste.save()
            report = Report.objects.create(user_id=user.id, title=body['title'], name=body['name'])
            report.save()
            return JsonResponse({ "success": True })
    return JsonResponse({ "success": False })
    

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

@login_required
def profile(request):
    role = "پزشک" if request.user.is_superuser else "سرپرست"
    return render(request, "registration/profile.html", { 'role': role })

@login_required
def dashboardView(request):
    role = "admin" if request.user.is_superuser else "user"
    roleFa = "پزشک" if request.user.is_superuser else "سرپرست"

    context = { 'role': role, 'roleFa': roleFa }
    return render(request, "dash/dash.html", context)


@login_required
def addPaste(request):
    if request.method == "POST":
        if len(Paste.objects.filter(user=request.user)) < 1:
            paste = Paste.objects.create(user_id=request.user.id)
            paste.save()
        
    return redirect('/dash/paste/')

class PasteListView(ListView):
    model = Paste
    context_object_name = "pastes"
    template_name = "dash/paste/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pastes"] = Paste.objects.filter(user=self.request.user)
        return context

class PasteUpdateView(UpdateView):
    model = Paste
    template_name = "dash/paste/edit.html"
    success_url = "/dash/paste/"
    form_class = PasteForm

 
class PasteDeleteView(DeleteView):
    model = Paste
    template_name = "dash/paste/delete.html"
    success_url = "/dash/paste/"

class BrushListView(ListView):
    model = Brush
    context_object_name = "brushes"
    template_name = "dash/brush/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brushes"] = Brush.objects.filter(user=self.request.user)
        return context


class BrushCreateView(CreateView):
    form_class = BrushForm
    template_name = "dash/brush/add.html"
    success_url = "/dash/brush/"
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()        
        return redirect(self.success_url)

class BrushUpdateView(UpdateView):
    model = Brush
    form_class = BrushForm
    template_name = "dash/brush/edit.html"
    success_url = "/dash/brush/"
 
class BrushDeleteView(DeleteView):
    model = Brush
    template_name = "dash/brush/delete.html"
    success_url = "/dash/brush/"


class ReportListView(ListView):
    model = Report
    context_object_name = "reports"
    template_name = "dash/reports/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reports"] = Report.objects.filter(user=self.request.user)
        return context

class UserListView(ListView):
    model = Report
    context_object_name = "users"
    template_name = "dash/users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.filter(is_superuser=False)
        return context

class UserCreateView(CreateView):
    form_class = RegisterForm
    template_name = "dash/users/add.html"
    success_url = "/dash/users/"

class UserDeleteView(DeleteView):
    model = User
    template_name = "dash/users/delete.html"
    success_url = "/dash/users/"

class UserDetailView(DetailView):
    template_name = "dash/users/detail.html"
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['brushes'] = Brush.objects.filter(user=user)
        context['paste'] = Paste.objects.filter(user=user).first()
        context['reports'] = Report.objects.filter(user=user).order_by('-datetime')
        return context
    
class MagicCodeListView(ListView):
    model = MagicCode
    context_object_name = "codes"
    template_name = "dash/codes/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["codes"] = MagicCode.objects.all().reverse()
        return context

class MagicCodeCreateView(CreateView):
    form_class = MagicCodeForm
    template_name = "dash/codes/add.html"
    success_url = "/dash/codes/"

class MagicCodeDeleteView(DeleteView):
    model = MagicCode
    template_name = "dash/codes/delete.html"
    success_url = "/dash/codes/"