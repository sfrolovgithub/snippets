from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet


def get_base_context(request, pagename):
    return {
        'pagename': pagename
    }


def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = get_base_context(request, 'Добавление нового сниппета')
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = get_base_context(request, 'Просмотр сниппетов')
    context['snippets'] = snippets
    return render(request, 'pages/view_snippets.html', context)

def snippets_create(request):
    if request.method == 'POST':
        #print(request.POST)
        snippet_name = request.POST['snippet_name']
        snippet_lang = request.POST['snippet_lang']
        snippet_code = request.POST['snippet_code']
        snippet = Snippet(name=snippet_name, lang=snippet_lang, code=snippet_code)
        snippet.save()
        return redirect('snippets_list')
    raise Http404