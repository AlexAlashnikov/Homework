from django.urls import path
from .views import home_page, about_me, hard_skill


app_name = 'resume'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('about-me/', about_me, name='about_me'),
    path('hard-skills/', hard_skill, name='hard_skills')
]
