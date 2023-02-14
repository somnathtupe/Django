from django.shortcuts import render

# Create your views here.

from django.views.generic import (CreateView,DetailView,UpdateView,
                                  ListView,TemplateView)
from .forms import AuthorForm,BookForm
from .models import Author,Book

class WelcomeView(TemplateView):
    template_name = 'welcome.html'

class AuthorCreateView(CreateView):
    model = Author
    template_name ='my-author-create.html'
    form_class = AuthorForm
    success_url = '/my-books'

class BooksView(ListView):
    model = Book
    template_name = 'my-book.html'

class BookDetailByIdView(DetailView):
    model = Book
    template_name = 'my-book-detial.html'

class BookDetailByCodeView(DetailView):
    model = Book
    template_name = 'my-books-detail.html'

    def get_object(self):
        return Book.objects.get(code=self.kwargs['code'])


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'my-book-edit.html'
    form_class = BookForm
    success_url ='/my-books'

class BookCreateView(CreateView):
    model = Book
    template_name = 'my-book-create.html'
    form_class = BookForm
    success_url = '/my-books'