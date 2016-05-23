# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User as DjangoAuthUser
from django.utils import timezone


# Create your models here.


class QuestionManager(models.Manager):                                          
        def new():                                                              
                pass                                                            
        def popular():                                                          
                pass 


class Question(models.Model):
    """ вопрос
    """
    # заголовок вопроса
    title = models.CharField(
        max_length=255
    )

    # полный текст вопроса
    text = models.TextField()

    # дата добавления вопроса
    added_at = models.DateTimeField(
        blank=True, 
        default=timezone.now
    )

    # рейтинг вопроса (число)
    rating  = models.IntegerField(
        blank=True, 
        default=0
    )

    # автор вопроса
    author = models.ForeignKey(
        DjangoAuthUser, 
        db_index=True,
        related_name="%(app_label)s_%(class)s_author_related",
        related_query_name="%(app_label)s_%(class)s_authors",
    )

    # список пользователей, поставивших "лайк"
    likes = models.ManyToManyField(
        DjangoAuthUser,
        related_name="%(app_label)s_%(class)s_like_related",
        related_query_name="%(app_label)s_%(class)s_likes",
    )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/question/%d/' % self.pk
    """
    class Meta:
        db_table = 'blogposts'
        ordering = ['-creation_date']
    """

    # objects = QuestionManager()    


class Answer(models.Model):
    """ ответ
    """
    # вопрос
    question = models.ForeignKey(Question)

    # текст ответа
    text = models.TextField()

    # дата добавления ответа
    added_at = models.DateTimeField(
        blank=True, 
        default=timezone.now
    )

    # автор ответа
    author = models.ForeignKey(
        DjangoAuthUser, 
        db_index=True
    )

    def __unicode__(self):
        return self.pk

    def get_absolute_url(self):
        return '/answer/%d/' % self.pk
