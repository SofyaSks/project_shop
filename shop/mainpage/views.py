from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth

def login_user(request):
    # если с сайта приходит пост запрос, то создаётся объект класса UserLoginForm, принимающий в себя данные пост запроса
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)

        # если данные валидные/правильные/соответствующие модели,
        # то с помощью cleaned_data мы вычленяем данные из QueryDict (парсинг?) и записываем их в переменную
        if user_form.is_valid():
            cd = user_form.cleaned_data

            # встроенным в библиотеку contrib модулем auth производим аутентификацию, (сверяем полученные данные с существующими в базе джанго?) 
            user = auth.authenticate(
                username = cd['username'],
                password = cd['password']
            )

            # если такой пользователь существует
            if user is not None:
                # и если пользователь активен
                if user.is_active:
                    # позволяем пользователю залогинится
                    auth.login(request, user)
                    # и перенаправляем на нужную страницу
                return redirect('new_good')
            else:
                # если пользователя не существует перенаправляем обратно на страницу логина (зачем?)
                return redirect('login')
    # если это не пост запрос (видимо гет?) то создаём пустой объект класса? 
    else:
        user_form = UserLoginForm()
    
    return render(
        request,
        'mainpage/login.html',
        {
            'user_form': user_form
        }

    )

def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # commit false чтобы раньше времени не добавлять пользователя в базу данных (сначала нужно проверить пароль)
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(
                request,
                'mainpage/registration_complete.html',
                {'new_user' : new_user}
            )
    else:
        user_form = UserRegistrationForm()
    return render(
        request,
        'mainpage/registration.html',
        {
            'user_form': user_form
        }
    )
