from django.core import serializers as pp
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from .models import *
from . import serializers
import json


@csrf_exempt
def book_get_or_post(request):
    s = Book.objects.all()

    if request.method == 'POST':
        print("AHAHAH")
        data = JSONParser().parse(request)
        serializer = serializers.BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data, status=200, safe=False)
        else:
            return JsonResponse(data, status=500)

    if request.method == 'GET':
        data = pp.serialize('json', s)
        return JsonResponse(data, safe=False)

    return HttpResponse(status=400)

@csrf_exempt
def book_patch_or_delete(request, pk):
    s = Book.objects.all()

    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        s.filter(pk=pk).update(**data)
        return JsonResponse(data, status=500)

    if request.method == 'DELETE':
        s.filter(pk=pk).delete()
        return HttpResponse(status=200)

    return HttpResponse(status=400)

@csrf_exempt
def author_post_or_get(request):
    s = Author.objects.all()

    if request.method == 'GET':
        print(len(s.values_list()))
        data = pp.serialize('json', s)
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data, status=200, safe=False)
        else:
            return JsonResponse(data, status=500)

    return HttpResponse(status=400)

@csrf_exempt
def author_patch_or_delete(request, pk):
    s = Author.objects.all()

    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        s.filter(pk=pk).update(**data)
        return JsonResponse(data, status=500)

    if request.method == 'DELETE':
        s.filter(pk=pk).delete()
        return HttpResponse(status=200)

    return HttpResponse(status=400)