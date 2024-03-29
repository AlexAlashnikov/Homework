from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Game, Category


def games_all(request):
    """
    Функция представления игр у которых поле is_active=True.
    """
    games = Game.objects.filter(is_active=True).all()
    return render(request, 'games/home.html', {'games': games})


def every_game(request, game_slug):
    """
    Функция представления игры по slug полю.
    """
    game = get_object_or_404(Game, slug=game_slug)
    return render(request, 'games/game.html', {'game': game})


def all_categories(request):
    """
    Функция представления категории у которых поле is_active=True.
    """
    categories = Category.objects.filter(is_active=True)
    return render(request, 'category/all_categories.html', {'categories': categories})


def category_games(request, category_slug):
    """
    Функция представления игр каждой категории.
    """
    category = get_object_or_404(Category, slug=category_slug)
    games = category.game_set.filter(is_active=True).all()
    context = {
        'category': category,
        'games': games
    }
    return render(request, 'category/category_games.html', context)


def sorting_in_alphabetical_order(request):
    """
    Функция представления сортировки игр в алфавитном порядке.
    """
    sorted_games = Game.objects.order_by('name').all()
    paginator = Paginator(sorted_games, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sorting/sort_alphab.html', {'page_obj': page_obj})


def sorting_not_in_alphabetical_order(request):
    """
    Функция представления сортировки игр не в алфавитном порядке.
    """
    sorted_games = Game.objects.order_by('-name').all()
    paginator = Paginator(sorted_games, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sorting/sort_alphab.html', {'page_obj': page_obj})
