from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
import urllib

from UserManagement.lib.Encrypt import check_user
from UserManagement.models import UserInfo
from WordGameServer import settings


@csrf_exempt
def add_friend(request):
    user = check_user(request)
    if user != None:
        
        try:
            login_val = request.POST['friend']
            
            new_frien = User.objects.filter(username = login_val).first()
            
            if new_frien != None and new_frien.id != user.id:
                data_json = {'error' : False, 'message' : "Veuillez attendre la réponse de votre contacte"}
            else:
                data_json = {'error' : True, 'message' : "Contacte non trouvé"}
        except:
            data_json = {'error' : True, 'message' : "Connection error"}
        
    else:
        data_json = {'error' : True, 'message' : "Login error"}
    return JsonResponse(data_json, safe = False)
# Create your views here.
def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode("utf-8")
            req = urllib.request.Request(url, data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode('utf-8'))
            if result['success']:
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                user_info = UserInfo()
                user_info.user = user
                user.save()
                login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def root(request):
    if not request.user.is_authenticated():
        return redirect('register/')
    return render(request, 'root.html', {})
@csrf_exempt
def check_connection(request):
    user = check_user(request)
    if user != None:
        data_json = {'answer' : True, 'error' : ""}
    else:
        data_json = {'answer' : False, 'error' : "Mdp/login invalide"}
    return JsonResponse(data_json, safe = False)
    