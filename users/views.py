from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from users.forms import UserRegisterFrom


def user_register_view(request):
    if request.method == "POST":
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            new_user = form.save()
            print(new_user)
            print(form.cleaned_data['password'])
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('dogs:index'))
    context = {
        'title': 'Создать аккаунт',
        'form': UserRegisterFrom
    }
    return render(request, 'users/user_register.html', context=context)
