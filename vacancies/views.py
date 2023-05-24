from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt

from vacancies.models import Goods, Cat


def hello(request):
    return HttpResponse('{"status": "ok"}')

@csrf_exempt
def ad(request):
    if request.method == "GET":
        goods = Goods.objects.all()

        response = []
        for good in goods:
            response.append({
                "Id": good.id,
                "name": good.name,
                "author": good.author,
                "price": good.price,
                "description": good.description,
                "address": good.address,
                "is_published": good.is_published
            })

        return JsonResponse(response, safe=False)

    elif request.method == "POST":
        good_data = json.loads(request.body)

        good = Goods()
        good.name = good_data["name"]
        good.author = good_data["author"]
        good.price = good_data["price"]
        good.description = good_data["description"]
        good.address = good_data["address"]
        good.is_published = good_data["is_published"]

        good.save()

        return JsonResponse({
                "Id": good.id,
                "name": good.name,
                "author": good.author,
                "price": good.price,
                "description": good.description,
                "address": good.address,
                "is_published": good.is_published
            })


def ad_pk(request, ad_id):
    if request.method == "GET":
        try:
            good = Goods.objects.get(pk=ad_id)
        except Cat.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "Id": good.id,
            "name": good.name,
            "author": good.author,
            "price": good.price,
            "description": good.description,
            "address": good.address,
            "is_published": good.is_published

        })

@csrf_exempt
def cat(request):
    if request.method == "GET":
        cats = Cat.objects.all()

        response = []
        for cat in cats:
            response.append({
                "id": cat.id,
                "name": cat.name,
            })

        return JsonResponse(response, safe=False)

    elif request.method == "POST":
        cat_data = json.loads(request.body)

        cat = Cat()
        cat.name = cat_data["name"]

        cat.save()

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        })


def cat_pk(request, cat_id):
    if request.method == "GET":
        try:
            cat = Cat.objects.get(pk=cat_id)
        except Cat.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        })