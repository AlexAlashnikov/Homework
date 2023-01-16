from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

import requests
import json


class Quote(View):
    """
    Класс представления, для вывода цитат.
    """
    url = "https://api.kanye.rest"

    def get(self, request, **kwargs):
        number = kwargs.get('numb', 1)
        result = [requests.get(self.url).json()['quote'] for i in range(number)]
        context = {
            'quotes': result
        }
        return render(request, template_name='myapp/index.html', context=context)


@csrf_exempt
@require_http_methods(["POST"])
def factorial_of_json(request):
    """
    Функция представления,
    для нахождения факториала числа через POST запрос.
    """
    dict_json = json.loads(request.body)
    number = dict_json['number']
    factorial = 1
    for i in range(number):
        factorial = factorial * (i+1)
    data = {
        "number": dict_json['number'],
        "factorial": factorial
    }
    return JsonResponse(data)
