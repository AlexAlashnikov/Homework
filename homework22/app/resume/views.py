from django.shortcuts import render


def home_page(request):
    return render(request, 'resume/home.html')


def about_me(request):
    return render(request, 'resume/about_me.html')


def hard_skill(request):
    return render(request, 'resume/hard_skills.html')