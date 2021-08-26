from django.shortcuts import render
from django.views import View

from .models import Country, Person
# Create your views here.


class PersonListBadView(View):
    model = Person
    template_name = 'example_0/person_list.html'

    # @silk_profile(name='Bad Report List')
    def get(self, request, **kwargs):
        context = {
            'people_count': self.model.objects.count(),
            'country_count': Country.objects.count()
        }
        ...
        context['people'] = self.model.objects.all()
        context['explanation'] = "The whole queryset is passed lazily and then iterated over.<br> Nplusone will log warnings."
        return render(request, self.template_name, context=context)


class PersonListGoodView(View):
    model = Person
    template_name = 'example_0/person_list.html'

    # @silk_profile(name='Bad Report List')
    def get(self, request, **kwargs):
        context = {
            'people_count': self.model.objects.count(),
            'country_count': Country.objects.count()
        }
        ...
        context['people'] = self.model.objects.select_related('country')
        context['explanation'] = "The whole queryset is passed with all expenses prefetched.<br> Nplusone will NOT log warnings."
        return render(request, self.template_name, context=context)
