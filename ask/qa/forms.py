# -*- coding: utf-8 -*-
from django import forms

from qa.models import Question, Answer


class QuestionForm(forms.Form):
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
        self.cleaned_data['author_id'] = 1
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

    def clean_question(self):
        try:
            question = Question.objects.get(pk=self.cleaned_data['question'])
        except Question.DoesNotExist:
            raise forms.ValidationError(u'Вопрос не найден', code='wrong_question')
        return question

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author_id'] = 1
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
