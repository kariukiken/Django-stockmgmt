"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from stockmgmt import views

from django.urls import include, path
from registration.backends.default.views import (
    ActivationView, RegistrationView, ResendActivationView,
)
from registration.backends.default.views import (
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)

urlpatterns = [
    path('', views.home, name='home'),
    path("api/", include('api.urls')),
    path('issue_many_items/', views.issue_many_items, name='issue_many_items'),
    path('list_history/', views.list_history, name='list_history'),
    path('add_items/', views.add_items, name='add_items'),
    path('list_item/', views.list_item, name='list_item'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
    path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
    path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),
    path('admin_view', views.admin_view, name='admin-view'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('view_cart', views.view_cart, name='view_cart'),
    

    path('accounts/password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls'))
]
