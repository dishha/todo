from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list.as_view()),
    path('<int:pk>/', views.individual.as_view()),
    path('create/',views.create.as_view())
]
