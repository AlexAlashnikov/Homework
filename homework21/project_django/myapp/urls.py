from django.urls import path
from . import views


urlpatterns = [
    path('', views.Quote.as_view()),
    path('<int:numb>/', views.Quote.as_view()),
    path('factorial/', views.factorial_of_json)
]
