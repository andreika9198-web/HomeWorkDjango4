from django.shortcuts import render, reverse
from django.http import  HttpResponseRedirect

from  users.forms import  UserRegisterForm

def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_passsword(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('games:index'))
    context = {
        'title': 'Регистрация',
        'form': UserRegisterForm
    }
    return render(request, 'users/register.html', context=context)

