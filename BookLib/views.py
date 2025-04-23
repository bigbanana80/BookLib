from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    FormView,
    DetailView,
    DeleteView,
    UpdateView,
)
from .models import Author, Book
from .forms import AuthorForm, BookForm


# Create your views here.
class index(ListView):
    model = Author
    template_name = "BookLib/index.html"
    context_object_name = "authors"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "BookLib"
        return context


class AddAuthor(FormView):
    form_class = AuthorForm
    template_name = "BookLib/Author/add_author.html"
    success_url = reverse_lazy("BookLib:index")

    def form_valid(self, form):
        author = Author(
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            age=form.cleaned_data["age"],
            national_code=form.cleaned_data["national_code"],
            gender=form.cleaned_data["gender"],
        )
        author.save()
        return super().form_valid(form)


class AuthorDetail(DetailView):
    model = Author
    template_name = "BookLib/Author/author_detail.html"
    context_object_name = "author"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")  
        if query:
            context["books"] = Book.objects.filter(
                author=self.object, name__icontains=query
            )
        else:
            context["books"] = Book.objects.filter(author=self.object)
        context["title"] = f"Books by {self.object.first_name} {self.object.last_name}"
        return context


class DeleteAuthor(DeleteView):
    model = Author
    template_name = "BookLib/Author/delete_author.html"
    success_url = reverse_lazy("BookLib:index")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Author"
        context["author"] = self.object
        return context

class UpdateAuthor(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "BookLib/Author/update_author.html"
    context_object_name = "author"
    
    def get_success_url(self):
        return reverse_lazy("BookLib:author_detail", kwargs={"pk": self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Author"
        return context

class SearchAuthor(ListView):
    model = Author
    template_name = "BookLib/Author/search_author.html"
    context_object_name = "authors"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Author.objects.filter(
                first_name__icontains=query
            ) | Author.objects.filter(
                last_name__icontains=query
            )| Author.objects.filter(
                national_code__icontains=query
            )
        return Author.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Search Author"
        return context

class AddBook(FormView):
    form_class = BookForm
    template_name = "BookLib/Book/add_book.html"
    
    def get_success_url(self):
        return reverse_lazy("BookLib:author_detail", kwargs={"pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = Author.objects.get(pk=self.kwargs["pk"]) 
        return context
    
    def form_valid(self, form):
        book = Book(
            name=form.cleaned_data["name"],
            date_published=form.cleaned_data["date_published"],
        )
        book.author = Author.objects.get(pk=self.kwargs["pk"])
        book.save()
        return super().form_valid(form)
    
class BookDetail(DetailView):
    model = Book
    template_name = "BookLib/Book/book_detail.html"
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = Author.objects.get(pk=self.object.author.pk)
        return context
    
class DeleteBook(DeleteView):
    model = Book
    template_name = "BookLib/Book/delete_book.html"
    
    def get_success_url(self):
        return reverse_lazy("BookLib:author_detail", kwargs={"pk": self.object.author.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Book"
        context["book"] = self.object
        return context
    
class UpdateBook(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "BookLib/Book/update_book.html"
    
    def get_success_url(self):
        return reverse_lazy("BookLib:author_detail", kwargs={"pk": self.object.author.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Book"
        context["book"] = self.object
        return context