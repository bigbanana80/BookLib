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
from .forms import AuthorForm


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
    template_name = "BookLib/add_author.html"
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
    template_name = "BookLib/author_detail.html"
    context_object_name = "author"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.filter(author=self.object)
        return context


class DeleteAuthor(DeleteView):
    model = Author
    template_name = "BookLib/delete_author.html"
    success_url = reverse_lazy("BookLib:index")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Author"
        context["author"] = self.object
        return context
