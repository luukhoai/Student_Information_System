from django.shortcuts import render


from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from forms import MyRegistrationForm


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        request.session[username] = username
        return HttpResponseRedirect(reverse('accounts:loggedin'))
    return HttpResponseRedirect(reverse('accounts:invalid'))


def loggedin(request):
    return render(request, 'accounts/loggedin.html', {'full_name': request.user.username})


def invalid_login(request):
    return render(request, 'accounts/invalid.html')


def logout(request):
    auth.logout(request)
    request.session.flush()
    return render(request, 'accounts/logout.html')


def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:register_success'))
    else:
        form = MyRegistrationForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    print args
    return render(request, 'accounts/register.html', args)


def register_success(request):
    return render(request, 'accounts/register_success.html')
