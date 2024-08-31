from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item


# Create your views here.
def home_page(request):
    # return HttpResponse("<html><title>To-Do lists</title></html>")
    # if request.method == "POST":
    # return HttpResponse("You submitted: " + request.POST["item_text"])

    if request.method == "POST":
        # item = Item()
        # item.text = request.POST.get("item_text", "")
        # item.save()
        Item.objects.create(text=request.POST["item_text"])
        return redirect("/")

    items = Item.objects.all()
    # return render(request,
    #               "home.html",
    #               {"new_item_text": request.POST.get("item_text", "")},
    #               )
    return render(request, "home.html", {"items": items})
