from django.views import View
from django.db.models import Sum
from django.shortcuts import render

# from silk.profiling.profiler import silk_profile

from .models import Expenses, Reports



class ReportsListBadView(View):
    model = Reports
    context_object_name = 'reports'
    template_name = 'example_1/report_list.html'

    # @silk_profile(name='Bad Report List')
    def get(self, request, **kwargs):
        context = {
            'report_count': self.model.objects.count(),
            'expense_count': Expenses.objects.count()
        }
        ...
        context['reports'] = self.model.objects.all()
        context['explanation'] = "The whole queryset is passed lazily and then iterated over.<br> Nplusone will log warnings."
        return render(request, self.template_name, context=context)
    


class ReportsListGoodView(View):
    model = Reports
    context_object_name = 'reports'
    template_name = 'example_1/report_list.html'
    
    # @silk_profile(name='Good Report List')
    def get(self, request, **kwargs):
        context = {
            'report_count': self.model.objects.count(),
            'expense_count': Expenses.objects.count()
        }
        ...
        context['reports'] = self.model.objects.prefetch_related('expenses')

        context['explanation'] = "The whole queryset is passed with all expenses prefetched.<br> Nplusone will NOT log warnings."
        return render(request, self.template_name, context=context)
    


class ReportsListBestView(View):
    model = Reports
    context_object_name = 'reports'
    template_name = 'example_1/report_list_optimum.html'

    # @silk_profile(name='Best Report List')
    def get(self, request, **kwargs):
        context = {
            'report_count': self.model.objects.count(),
            'expense_count': Expenses.objects.count()
        }
        ...
        context['reports'] = self.model.objects.prefetch_related('expenses').annotate(total_amount=Sum('expenses__amount'))
        context['explanation'] = "The whole queryset is passed with all expenses prefetched, and annotated to save on python-side calculations."
        return render(request, self.template_name, context=context)
    