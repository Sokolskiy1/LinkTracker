from django.urls import path
from . import views

urlpatterns = [
    path('api/work/', views.LeadListCreate.as_view() ),
]