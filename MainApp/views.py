from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet, Comment
from MainApp.forms import SnippetForm, UserForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

@login_required
def snippets_page_my(request):
    try:
        my_snippets = Snippet.objects.filter(author=request.user.id)
        print(my_snippets)
    except Snippet.DoesNotExist:
        raise Http404
    context = get_base_context(request, 'Мои сниппеты')
    context['snippets'] = my_snippets
    return render(request, 'pages/view_snippets.html', context)

@login_required
def snippets_create(request):
    if request.method == 'POST':
        #print(request.POST)
        snippet_name = request.POST['snippet_name']
        snippet_lang = request.POST['snippet_lang']
        snippet_code = request.POST['snippet_code']
        snippet = Snippet(name=snippet_name, lang=snippet_lang, code=snippet_code, author=request.user)
        snippet.save()
        return redirect('snippets_list')
    raise Http404

def snippets_edit(request, id):
    if request.method == 'GET':
        try:
            snippet = Snippet.objects.get(id=id)
            context = get_base_context(request, 'Редактирование сниппета')
            context['snippet'] = snippet
            comments = Comment.objects.filter(snippet=id)
            context['comments'] = comments
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

def auth_login(request):
    print("request.method =", request.method)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("username =", username)
        print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            print('Error!')
            context = {}
            context['auth_login_error'] = 'Failed login or passord'
            return render(request, 'pages/index.html', context)
            #pass
        return redirect('home')

def auth_login_out(request):
    print("request.method =", request.method)
    auth.logout(request)
    return redirect('home')

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = get_base_context(request, 'Просмотр сниппетов')
            context['form'] = form
            return render(request, 'pages/register.html', context)
    else: #GET
        form = UserForm()
        context = get_base_context(request, 'Просмотр сниппетов')
        context['form'] = form
        return render(request, 'pages/register.html', context)

@login_required
def snippets_comment_create(request):
    if request.method == "POST": # Create comment
        snippet_comment = request.POST.get("snippet_comment")
        snippet_id = request.POST.get("snippet_id")
        author = request.user
        snippet = Snippet.objects.get(id=snippet_id)
        comment = Comment()
        comment.text = snippet_comment
        comment.snippet = snippet
        comment.author = author
        comment.save()
        return redirect('snippets_edit', snippet_id)