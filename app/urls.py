from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home),
    path('dash/', dashboardView),

    path('dash/paste/', login_required(PasteListView.as_view())),
    path('dash/paste/add/', addPaste),
    path('dash/paste/<pk>/', login_required(PasteUpdateView.as_view())),
    path('dash/paste/<pk>/delete/', login_required(PasteDeleteView.as_view())),
    
    path('dash/brush/', login_required(BrushListView.as_view())),
    path('dash/brush/add/', login_required(BrushCreateView.as_view())),
    path('dash/brush/<pk>/', login_required(BrushUpdateView.as_view())),
    path('dash/brush/<pk>/delete/', login_required(BrushDeleteView.as_view())),

    path('dash/reports/', login_required(ReportListView.as_view())),

    path('dash/users/', login_required(UserListView.as_view())),
    path('dash/users/add/', login_required(UserCreateView.as_view())),
    path('dash/users/<pk>/', login_required(UserDetailView.as_view())),
    path('dash/users/<pk>/delete/', login_required(UserDeleteView.as_view())),

    path('dash/codes/', login_required(MagicCodeListView.as_view())),
    path('dash/codes/add/', login_required(MagicCodeCreateView.as_view())),
    path('dash/codes/<pk>/delete/', login_required(MagicCodeDeleteView.as_view())),

    path('api/report/', addReport),

    path('accounts/profile/', profile),
    path('accounts/', include('django.contrib.auth.urls')),
]
