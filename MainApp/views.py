from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


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

def add_snippet_page_auto_form(request):
    form = SnippetForm()
    return render(request, 'pages/add_snippet_auto_form.html', {'form': form})


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

def snippets_edit(request, id):
    if request.method == 'GET':
        try:
            snippet = Snippet.objects.get(id=id)
            context = get_base_context(request, 'Редактирование сниппета')
            context['snippet'] = snippet
            return render(request, 'pages/edit_snippet.html', context)
        except Snippet.DoesNotExist:
            raise Http404
    if request.method == 'POST':
        snippet = Snippet.objects.get(id=id)
        snippet.name = request.POST['snippet_name']
        snippet.lang = request.POST['snippet_lang']
        snippet.code = request.POST['snippet_code']
        snippet.update()

def snippets_create_auto_form(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snippets_list')
        raise Http404
