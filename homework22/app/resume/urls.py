from django.urls import path
from .views import home_page, about_me, hard_skill


urlpatterns = [
    path('', home_page),
    path('about-me/', about_me),
    path('hard-skills/', hard_skill)
]
