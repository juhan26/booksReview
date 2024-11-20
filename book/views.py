from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    searchJudul = request.GET.get('judul')
    if searchJudul:
        books = Book.objects.filter(judul__icontains=searchJudul)
    else:
        books = Book.objects.all()
    return render(request, "home.html", {"name": "Juan", 'searchJudul': searchJudul, "books": books})


def about(request):
    return render(request, "about.html", {'appName': 'BookReview'})

def detail(request,book_id):
  book = get_object_or_404(Book,pk=book_id)
  return render(request,"detail.html",{"book": book})