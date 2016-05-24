# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

from qa.models import Question, Answer


class AskForm(forms.Form):
    """ форма добавления вопроса
    """
    # поле заголовка
    title = forms.CharField(
        max_length=255, 
        widget=forms.Textarea
    )

    # поле текста вопроса
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    """ форма добавления ответа
    """
    # поле текста ответа
    text = forms.CharField(widget=forms.Textarea)

    # поле для связи с вопросом
    question = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
        try:
            question = int(self.cleaned_data['question'])
            self.cleaned_data['question'] = Question.objects.get(pk=question)
        except ValueError:
            raise ValidationError('Question: ' + str(question) + ' is not an integer')
        except Question.DoesNotExist :
            raise ValidationError('Question: ' + str(question) + ' not exists')

        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignupForm(forms.Form):
    """ 
    """
    # имя пользователя, логин
    username = forms.CharField()

    # email пользователя
    email = forms.EmailField()

    # пароль пользователя
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password'])
        return user


class LoginForm(forms.Form):
    """ 
    """
    # имя пользователя, логин
    username = forms.CharField()

    # пароль пользователя
    password = forms.CharField(widget=forms.PasswordInput)
