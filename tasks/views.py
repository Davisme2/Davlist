from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import Collection


# Create your views here.
def index(request):
    context = {}
    collection = Collection.get_default_collection()

    context["collections"] = Collection.objects.order_by("slug")
    return render(request, 'tasks/index.html', context=context)


def add_collection(request):
    collection_name = request.POST.get("collection-name")
    collection, created = Collection.objects.get_or_create(name=collection_name)
    if not created:
        return HttpResponse("La collection existe déjà.", status=409)
    return HttpResponse(f'<h2>{collection_name}<h2>')
