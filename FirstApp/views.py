from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Wish
from .forms import WishForm
from datetime import timedelta


# View to list all wishes
def WishList(request):
    today = timezone.now().date()
    tomorrow = today + timedelta(days=1)
    wishes = Wish.objects.all()
    due_wishes = Wish.objects.filter(deadline=today)  # Wishes with today's deadline
    reminder_wishes = Wish.objects.filter(
        deadline=tomorrow
    )  # Wishes with tomorrow's deadline

    params = {
        "wishes": wishes,
        "due_wishes": due_wishes,
        "reminder_wishes": reminder_wishes,
    }
    return render(request, "Wishes.html", params)


# View to create a new wish
def CreateWish(request):
    form = WishForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("WishList")
    return render(request, "WishForm.html", {"form": form})


# View to update an existing wish
def UpdateWish(request, id):
    wish = get_object_or_404(Wish, id=id)
    form = WishForm(request.POST or None, instance=wish)
    if form.is_valid():
        form.save()
        return redirect("WishList")
    return render(request, "WishForm.html", {"form": form, "wish": wish})


# View to delete a wish
def DeleteWish(request, id):
    wish = get_object_or_404(Wish, id=id)
    if request.method == "POST":
        wish.delete()
        return redirect("WishList")
    return render(request, "DeleteConfirm.html", {"wish": wish})


# View to search for a wish by title
def Search(request, text):
    wishes = Wish.objects.filter(wishtitle__icontains=text)  # Filter by wish title
    today = timezone.now().date()
    tomorrow = today + timedelta(days=1)
    due_wishes = Wish.objects.filter(deadline=today)  # Wishes with today's deadline
    reminder_wishes = Wish.objects.filter(
        deadline=tomorrow
    )  # Wishes with tomorrow's deadline

    return render(
        request,
        "Wishes.html",
        {
            "wishes": wishes,
            "due_wishes": due_wishes,
            "reminder_wishes": reminder_wishes,
        },
    )
