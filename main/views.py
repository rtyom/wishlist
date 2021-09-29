from django.shortcuts import render, get_object_or_404

from .models import WishList

def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {"title": "Wishlist | about project"})

def list_page(request, pk):
    wish_list = get_object_or_404(WishList, pk=pk)
    return render(
        request,
        'wish_list.html',
        {
            'list': wish_list,
            'is_owner_list': wish_list.owner == request.user
        }
    )