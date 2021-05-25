from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from app1.models import Notice, Profile
# from app1.forms import ProfileForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app1.forms import RegistrationForm
from django.views.generic import View
from django.urls import reverse,reverse_lazy
from django.contrib.auth import login as login_process,logout,authenticate
from django.shortcuts import redirect,get_object_or_404
from django.template.loader import get_template
from django.contrib import messages
# from remember_me.forms import AuthenticationRememberMeForm
# from django.views.decorators.cache import never_cache
# from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth import REDIRECT_FIELD_NAME
# from django.contrib.sites.models import Site
# from django.template import RequestContext
# import re
# from django.contrib.sites.shortcuts import get_current_site
# from django.conf import settings
# from auth_remember import remember_user






# Create your views here.

class HomeView(TemplateView):
    template_name = "app1/try_index.html"

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

class NoticeListView(ListView):
    model = Notice

@method_decorator(login_required, name='dispatch')
class NoticeDetailView(DetailView):
    model = Notice

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["name", "age", "address", "status", "gender"]

def register(request):
    if(request.method=='POST'):
        RF=RegistrationForm(request.POST)
        if(RF.is_valid()):
            RF.save(request)
            return HttpResponseRedirect(reverse('login'))
        else:
            print("some one is trying for register but failed", RF.errors)
            HttpResponse("invalid Data")
            HttpResponse(RF.errors)
    else:
        RF=RegistrationForm()
    return render(request,'register.html',{'RF':RF})

class EmailAuthBackend:
    def authenticate(username,password,backend):
        try:
            user=User.objects.get(email=username)
            success=user.check_password(password)
            if success:
                return user
        except User.DoesNotExist:
            pass
        return None

# def user_login(request):
#     uname=''
#     pwd=''
#     if(request.method=='POST'):
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         remind=request.POST.get('remember-me')
#         print(remind)
#         # u=User.objects.get(email=username)
#         a1=EmailAuthBackend
#         user = a1.authenticate(username=username,password=password,backend='django.contrib.auth.backends.ModelBackend')
#         if user:
#             if(user.is_active):
#                 login_process(request, user, 'django.contrib.auth.backends.ModelBackend')
#                 if remind:
#                     remember_user(request, user)
#                     # request.session['uname']=username
#                     # request.session['password']=password
#                     # request.session.set_expiry(None)
#                     # print(request.session.get_expiry_age())
#                 return HttpResponseRedirect(reverse_lazy('index'))
#             else:
#                 return HttpResponse('user is not active')
#         else:
#             print('someone is trying to login with this username={} and password{}'.format(username,password))
#             return HttpResponse('invalid username and password')
#     # if request.session.has_key('uname'):
#     #     print('in if of uname')
#     #     uname=request.session['uname']
#     #     pwd=request.session['password']
#     #     return render(request,'ecompages/login.html',{'uname':uname,'pwd':pwd})
#     if request.session.has_key('uname') and request.session.has_key('password'):
#         uname=request.session['uname']
#         pwd=request.session['password']
#     return render(request,'login.html',{'uname':uname,'pwd':pwd})

def user_login(request):
    uname=''
    pwd=''
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        remind=request.POST.get('remember-me')
        print(remind)
        # u=User.objects.get(email=username)
        a1=EmailAuthBackend
        user = a1.authenticate(username=username,password=password,backend='django.contrib.auth.backends.ModelBackend')
        if user:
            if(user.is_active):
                login_process(request, user, 'django.contrib.auth.backends.ModelBackend')
                if remind:
                    request.session['uname']=username
                    request.session['password']=password
                    request.session.set_expiry(None)
                    print(request.session.get_expiry_age())
                return HttpResponseRedirect(reverse_lazy('index'))
            else:
                return HttpResponse('user is not active')
        else:
            print('someone is trying to login with this username={} and password{}'.format(username,password))
            return HttpResponse('invalid username and password')

    if request.session.has_key('uname') and request.session.has_key('password'):
        uname=request.session['uname']
        pwd=request.session['password']
    return render(request,'login.html',{'uname':uname,'pwd':pwd})


# @csrf_protect
# @never_cache
# def remember_me_login(request, template_name='login.html',
#           redirect_field_name='REDIRECT_FIELD_NAME',
#           authentication_form=AuthenticationRememberMeForm):
#     redirect_to = request.POST.get(redirect_field_name, '/app1/index')
#
#     remind = request.POST.get('remember-me')
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password=request.POST.get('password')
#         remind=request.POST.get('remember-me')
#         a1 = EmailAuthBackend
#         user = a1.authenticate(username=username,password=password,backend='django.contrib.auth.backends.ModelBackend')
#         # form = authentication_form(data=request.POST)
#         # if user.is_valid():
#         if user.is_active:
#         # Light security check -- make sure redirect_to isn't garbage.
#             if not redirect_to or ' ' in redirect_to:
#                  redirect_to = settings.LOGIN_REDIRECT_URL
#
#          # Heavier security check -- redirects to http://example.com should
#             # not be allowed, but things like /view/?param=http://example.com
#             # should be allowed. This regex checks if there is a '//' *before* a
#             # question mark.
#             elif '//' in redirect_to and re.match(r'[^\?]*//', redirect_to):
#                  redirect_to = settings.LOGIN_REDIRECT_URL
#
#
#
#             if not request.POST.get('remember_me'):
#                 request.session.set_expiry(0)
#
#             # Okay, security checks complete. Log the user in.
#             login_process(request, user, 'django.contrib.auth.backends.ModelBackend')
#
#             if request.session.test_cookie_worked():
#                 print("cookie worked")
#                 request.session.delete_test_cookie()
#
#         return HttpResponseRedirect(redirect_to)
#
#
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     remind = request.POST.get('remember-me')
#     a1 = EmailAuthBackend
#     user = a1.authenticate(username=username,password=password,backend='django.contrib.auth.backends.ModelBackend')
#
#
#         # user = authentication_form(request)
#
#     request.session.set_test_cookie()
#
#     current_site = get_current_site(request)
#
#     return render(request,'login.html', {
#         'user': user,
#         redirect_field_name: redirect_to,
#         'site': current_site,
#         'site_name': current_site.name,
#     })

@login_required
def user_logout(request):
    logout(request)
    return render(request,'index.html')


def sport(request):
    return render(request, 'sports.html')

def cricket_view(request):
    return render(request, 'cricket.html')


def basketball_view(request):
    return render(request, 'basketball.html')


# def profile_view(request):
#     return render(request, 'profile.html')

@login_required
def profile_view(request):
    p2=None
    user=request.user
    pr=Profile.objects.filter(user=user)
    # print(pr.count())
    if request.method=='POST':
        if pr.count() is not 0:
            p1=Profile.objects.get(user=user)
            n=request.POST.get('name')
            sta=request.POST.get('status')
            gen=request.POST.get('gender')
            add=request.POST.get('address')
            a=request.POST.get('age')
            if p1 is not None:
                p1.set_data(n,sta,gen,a,add)
                # p2=Profile.objects.get(user=user)
                # p1.Lname=lname
                messages.success(request,'profile update successfull',extra_tags='alert')
                return redirect('profile')
        else:
            p1 = Profile.objects.get(user=user)
            n = request.POST.get('name')
            sta = request.POST.get('status')
            gen = request.POST.get('gender')
            add = request.POST.get('address')
            a = request.POST.get('age')
            # print('in else',fname,lname,mob,addr,lamark,pin)
            if p1 is not None:
                if p1.set_data(n,sta,gen,a,add)=='done':
                    pr=1
                    return HttpResponse("profile update successfully")
                else:
                    return HttpResponse("profile is not updated")
    if Profile.objects.filter(user=user).count() is not 0:
        print(Profile.objects.filter(user=user).count())
        p2=Profile.objects.get(user=user)
    return render(request,'profile.html',{'p2':p2})

