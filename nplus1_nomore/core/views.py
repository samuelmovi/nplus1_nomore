from django.shortcuts import render

# Create your views here.


def main(request):
    template_name = 'core/main.html'
    return render(request, template_name)


def views_templates(request):
    template_name = 'core/views_templates.html'
    return render(request, template_name)


def rest(request):
    template_name = 'core/rest.html'
    return render(request, template_name)


def graphql(request):
    template_name = 'core/graphql.html'
    return render(request, template_name)


def profiling(request):
    template_name = 'core/profiling.html'
    return render(request, template_name)


