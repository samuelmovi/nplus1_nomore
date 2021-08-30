from django.shortcuts import render
from django.views import View

# from silk.profiling.profiler import silk_profile

from .models import Author, Book

# Create your views here.

class BookListBadView(View):
    model = Book
    context_object_name = 'reports'
    template_name = 'example_2/book_list.html'

    # @silk_profile(name='Autoprefetched Bad Book List')
    def get(self, request, **kwargs):
        context = {
            'book_count': self.model.objects.count(),
            'author_count': Author.objects.count()
        }
        ...
        context['books'] = self.model.objects.all()
        context['explanation'] = "Despite calling '.all()' auto_prefetch makes sure no N+1 issues. No nplusone warnings."
        return render(request, self.template_name, context=context)

