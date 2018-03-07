# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from todo.models import Todo


def index(request):
    todo_list = Todo.objects.order_by('id')

    context = {'todo_list': todo_list}

    return render(request, 'index.html', context)


def add_todo(request):
    if request.method == 'POST' and request.is_ajax():
        message = request.POST['text']

    Todo.objects.create(
        text = message,
        complete = False
    )

    context = Todo.objects.get(text=message)

    return JsonResponse({'todo': {'id': context.id, 'text': context.text}})
