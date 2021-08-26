from django.shortcuts import render
from django.views import View

from .models import Author, Book
# Create your views here.


class BookListBadView(View):
    model = Book
    context_object_name = 'reports'
    template_name = 'example_2/book_list.html'

    # @silk_profile(name='Bad Book List')
    def get(self, request, **kwargs):
        context = {
            'book_count': self.model.objects.count(),
            'author_count': Author.objects.count()
        }
        ...
        context['books'] = self.model.objects.all()
        context['explanation'] = "The whole queryset is passed lazily and then iterated over. Nplusone will log warnings."
        return render(request, self.template_name, context=context)


class BookListGoodView(View):
    model = Book
    context_object_name = 'reports'
    template_name = 'example_2/book_list.html'

    # @silk_profile(name='Good Book List')
    def get(self, request, **kwargs):
        context = {
            'book_count': self.model.objects.count(),
            'author_count': Author.objects.count()
        }
        ...
        context['books'] = self.model.objects.order_by("title").select_related('author', 'author__country')
        # context['books'] = self.model.objects.order_by("title").prefetch_related('author')
        context['explanation'] = "The whole queryset is joined with 'select_related'. No warnings from Nplusone."
        return render(request, self.template_name, context=context)
