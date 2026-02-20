from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'page_obj'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = Book.objects.all()
        if query:
            qs = qs.filter(title__icontains=query)
        return qs

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'