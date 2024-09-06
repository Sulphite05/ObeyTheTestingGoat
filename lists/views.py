from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List


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
    return render(request, "list.html", {"list": our_list})


def new_list(request):
    nulist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=nulist)
    return redirect(f"/lists/{nulist.id}/")


def add_item(request, list_id):
    our_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST["item_text"], list=our_list)
    return redirect(f"/lists/{our_list.id}/")

