from django.shortcuts import render
from .models import Bookmark
from django.shortcuts import get_object_or_404


def BookmarkLV(request):
    queryset = Bookmark.objects.all()
    q = request.GET.get('q', '')
    if q:
        queryset = queryset.filter(content_icontains=q)
    return render(request, 'bookmark/Bookmark_list.html', {
        'bookmark_list':queryset
    })

def BookmarkDV(request, id):
    get_object_or_404(Bookmark, id=id)
    bookmark = Bookmark.objects.get(id=id)
    return render(request, 'bookmark/Bookmark_detail.html',{
        'bookmark': bookmark
    })


# Create your views here.
