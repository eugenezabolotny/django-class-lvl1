# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
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
        text=message,
        complete=False
    )

    context = Todo.objects.get(text=message)

    return JsonResponse({'todo': {'id': context.id, 'text': context.text}})


def change_status(request):
    if request.method == 'POST' and request.is_ajax():
        message = request.POST['id']

    todo = Todo.objects.get(id=message)
    # todo.complete = True
    if not todo.complete:
        todo.complete = True
    else:
        todo.complete = False
    todo.save()

    return HttpResponse('')


def del_completed(request):
    if request.method == 'POST' and request.is_ajax():
        id_list = request.POST['id_list']
        data = json.loads(id_list)

    for id in data:
        Todo.objects.filter(id=id).delete()

    return HttpResponse('')


def del_all(request):
    Todo.objects.all().delete()

    return HttpResponse('')
