from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from .models import Item, List
from .forms import ItemForm


# Create your views here.
def home_page(request):
    # return HttpResponse("<html><title>To-Do lists</title></html>")
    # if request.method == "POST":
    # return HttpResponse("You submitted: " + request.POST["text"])

    # if request.method == "POST":
    #     # item = Item()
    #     # item.text = request.POST.get("text", "")
    #     # item.save()
    #     Item.objects.create(text=request.POST["text"])
    #     return redirect("/lists/the-only-list-in-the-world/")
    # return render(request,
    #               "home.html",
    #               {"new_text": request.POST.get("text", "")},
    #               )
    return render(request, "home.html", {"form": ItemForm()})


def view_list(request, list_id):
    our_list = List.objects.get(id=list_id)
    error = None
    # items = Item.objects.filter(list=our_list)

    if request.method == "POST":
        try:
            item = Item(text=request.POST["text"], list=our_list)
            # Item.objects.create(text=request.POST["text"], list=our_list)
            item.full_clean()
            item.save()
            return redirect(our_list)

        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, "list.html", {"list": our_list, "error": error})


def new_list(request):
    nulist = List.objects.create()
    item = Item.objects.create(text=request.POST["text"], list=nulist)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        nulist.delete()
        error = "You can't have an empty list item"
        return render(request, "home.html", {"error": error})
    # return redirect(f"/lists/{nulist.id}/")
    # return redirect("view_list", nulist.id)
    return redirect(nulist)



# def add_item(request, list_id):
#     our_list = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST["text"], list=our_list)
#     return redirect(f"/lists/{our_list.id}/")

