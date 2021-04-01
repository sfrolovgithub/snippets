from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from MainApp.models import Snippet, Comment


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        # Описываем поля, которые будем заполнять в форме
        fields = ['username', 'email', 'password1', 'password2']

class SnippetForm(ModelForm):
   class Meta:
       model = Comment
       # Описываем поля, которые будем заполнять в форме
       fields = ['text']