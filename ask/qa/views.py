from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET, require_POST

from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def error(request, *args, **kwargs):
    return HttpResponse(404)


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page


@require_GET
def question_list_all(request):
    questions = Question.objects.all()
    questions = questions.order_by('-id')

    paginator, page = paginate(request, questions)

    paginator.baseurl = '/?page='

    return render(
        request, 
        'qa/question_list_all.html', 
        {'questions': page.object_list,
         'paginator': paginator, 'page': page,
        }
    )


@require_GET
def question_list_popular(request):
    questions = Question.objects.all()
    questions = questions.order_by('-rating')

    paginator, page = paginate(request, questions)

    paginator.baseurl = '/popular/?page='

    return render(
        request, 
        'qa/question_list_all.html', 
        {'questions': page.object_list,
         'paginator': paginator, 'page': page,
        }
    )


#@require_GET
def question_by_id(request, pk):
    if request.method == 'POST':
        return render('OK')
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404
    return render(
        request, 
        'qa/question_details.html',
        {'question': question,
         'form': AnswerForm(initial={'question': question.id})}
    )


def question_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(
        request, 
        'qa/question_add.html', 
        {'form': form}
    )


#@require_POST
def answer_add(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.question.get_absolute_url()
            return HttpResponseRedirect(url)
    HttpResponseRedirect('/')

"""
python manage.py shell
from django.contrib.auth.models import User
user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword').save().
"""