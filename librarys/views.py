from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required
def book_list(request):
    query = request.GET.get('usr_query')
    if query:
        books = Book.objects.filter(Q(name__contains = query)| Q(category__title__contains = query) | Q(author__contains = query))
    else:
        books= Book.objects.all()
    return render(request, 'librarys/index.html', context={"books":books})
