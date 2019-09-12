from django.shortcuts import render, redirect  # For Render and Redireting to Function views
from .models import Wish
from .forms import WishForm


# Create your views here.
def WishList(request):
    wish = Wish.objects.all();  # Create Object of Wish Class Model
    params = {'wishes': wish}  # Create Parameter to Send To View
    return render(request, 'Wishes.html', params)  # Return Wishes To The Html Page


def CreateWish(request):
    form = WishForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('WishList')
    return render(request, 'WishForm.html', {'form': form})


def UpdateWish(request, id):
    wish = Wish.objects.get(id=id)
    form = WishForm(request.POST or None, instance=wish)
    if form.is_valid():
        form.save()
        return redirect('WishList')
    return render(request, 'WishForm.html', {'form': form, 'wish': wish})


def DeleteWish(request, id):
    wish = Wish.objects.get(id=id)
    if request.method == 'POST':
        wish.delete()
        return redirect('WishList')
    return render(request, 'DeleteConfirm.html', {'wish': wish})

def Search(request,text):
    wish=Wish.objects.filter()