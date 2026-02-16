from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Book


def book_list(request):
    query = request.GET.get('q')
    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    paginator = Paginator(books, 5)  # 5 книг на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'book/book_list.html', {
        'page_obj': page_obj
    })


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})
