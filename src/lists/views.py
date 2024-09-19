from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from .models import Item, List


# Create your views here.
def home_page(request):
    # return HttpResponse("<html><title>To-Do lists</title></html>")
    # if request.method == "POST":
    # return HttpResponse("You submitted: " + request.POST["item_text"])

    # if request.method == "POST":
    #     # item = Item()
    #     # item.text = request.POST.get("item_text", "")
    #     # item.save()
    #     Item.objects.create(text=request.POST["item_text"])
    #     return redirect("/lists/the-only-list-in-the-world/")
    # return render(request,
    #               "home.html",
    #               {"new_item_text": request.POST.get("item_text", "")},
    #               )
    return render(request, "home.html")


def view_list(request, list_id):
    our_list = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=our_list)
    if request.method == "POST":
        Item.objects.create(text=request.POST["item_text"], list=our_list)
        return redirect(f"/lists/{our_list.id}/")
    return render(request, "list.html", {"list": our_list})


def new_list(request):
    nulist = List.objects.create()
    item = Item.objects.create(text=request.POST["item_text"], list=nulist)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        nulist.delete()
        error = "You can't have an empty list item"
        return render(request, "home.html", {"error": error})
    return redirect(f"/lists/{nulist.id}/")


# def add_item(request, list_id):
#     our_list = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST["item_text"], list=our_list)
#     return redirect(f"/lists/{our_list.id}/")

