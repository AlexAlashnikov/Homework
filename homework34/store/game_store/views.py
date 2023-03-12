from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.db.models import Avg
from django.urls import reverse_lazy
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponseRedirect

import datetime   

from .tasks import replace_text_with_censored, game_store_logger_info
from .models import Game, Category, Comment
from .forms import CommentForm


def games_all(request):
    """
    Функция представления игр у которых поле is_active=True.
    """

    games = Game.objects.filter(is_active=True).select_related('category')
    paginator = Paginator(games, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'games/home.html', {'page_obj': page_obj})


@login_required(login_url='user:login')
def every_game(request, game_slug):
    """
    Функция представления игры по slug полю.
    """

    game = get_object_or_404(Game, slug=game_slug)
    getting_path = str(request.path)
    getting_user = str(request.user)
    getting_time = str(datetime.datetime.now())
    game_store_logger_info.delay(getting_time, getting_path, getting_user)
    comments = game.comments.all().order_by('-pub_date')
    last = request.COOKIES.get(game_slug)
    average_grade = game.comments.aggregate(Avg('grade'))
    session_key = f'{game_slug}_visits'
    visits = request.session.get(session_key, 0)
    visits += 1
    request.session[session_key] = visits
    context = {
        'game': game,
        'comments': comments,
        'last': last,
        'visits': visits,
        'average_grade': average_grade['grade__avg'],
    }
    response = render(request, 'games/game.html', context=context)
    visit_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response.set_cookie(game_slug, visit_time)
    return response


@cache_page(60 * 5)
def all_categories(request):
    """
    Функция представления категории у которых поле is_active=True.
    """

    categories = Category.objects.filter(is_active=True)
    return render(request, 'category/all_categories.html', {'categories': categories})


@login_required(login_url='user:login')
def category_games(request, category_slug):
    """
    Функция представления игр каждой категории.
    """

    category = get_object_or_404(Category, slug=category_slug)
    games = category.game_set.filter(is_active=True, category=category)
    context = {
        'category': category,
        'games': games
    }
    return render(request, 'category/category_games.html', context)


@cache_page(60 * 5)
def sorting(request):
    """
    Функция представления, сортировки игр.                      
    """
    sort = request.GET.get('sort')  
    sort_order = {
        'name_desc': Game.objects.order_by('-name'),
        'name_asc': Game.objects.order_by('name'),
    }
    games = sort_order.get(sort).select_related('category')
    return render(request, 'sorting/sorting.html', {'games': games})


def search_games(request):
    """
    Поиск игры по имени.
    """

    if request.method == 'POST':
        searched = request.POST['searched']
        games = Game.objects.filter(name__icontains=searched)
        return render(request, 'search/search_games.html', {'searched': searched, 'games': games})
    else:
        return render(request, 'search/search_games.html', {})


class CommentCreateView(CreateView, LoginRequiredMixin):
    """
    Добавление комментария в игру пользователем.
    """

    template_name = 'comments/comment_create.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse("game:game_slug", kwargs={'game_slug': self.object.game.slug})
    
    def form_valid(self, form):
        form.instance.game = Game.objects.get(slug=self.kwargs['game_slug'])
        form.instance.user = self.request.user
        self.object = form.save()
        replace_text_with_censored.delay(serializers.serialize('json', [self.object]))
        return HttpResponseRedirect(self.get_success_url())


class CommentUpdateView(UpdateView):
    """
    Редактирование комментария в игре.
    """

    model = Comment
    template_name = 'comments/comment_update.html'
    form_class = CommentForm


class CommentDeleteView(DeleteView):
    """
    Удаление комментария в игре.
    """

    model = Comment
    template_name = 'comments/comment_delete.html'
    success_url = reverse_lazy('game:games')
