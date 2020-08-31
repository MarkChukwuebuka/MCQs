from django.urls import path
from . import views



urlpatterns = [
	path('', views.home, name = "home"),
    path('question_<int:id>', views.test, name = "test"),
    path('result/', views.result, name = "result"),
]