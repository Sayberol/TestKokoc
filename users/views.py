from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from tests.models import Tests, TestQuestions, QuestionAnswer
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from tests.models import Question


def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Сохраняем пароль, но не добавляем в базу
            new_user = user_form.save(commit=False)
            # Устанавливаем пароль и хэшируем
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем юзера
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'users/index.html', {'user': user})
                else:
                    return HttpResponse('Ваш аккаунт не активен')
            else:
                return HttpResponse('Не правильный логин')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def quiz(request):
    list_test = Tests.objects.all()
    return render(request, 'users/quiz.html', {'section': 'quiz', 'list_test': list_test})


def test(request):
    list_answer = QuestionAnswer.objects.all()
    list_question = list_answer.values("question__text").distinct()
    return render(request, 'users/tests.html', {'list_question': list_question, 'list_answer': list_answer})


# def test_result(request):

