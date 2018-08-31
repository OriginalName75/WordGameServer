from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
import urllib

from CryptoMess.lib.generateKeys import Encrypter
from CryptoMess.models import KeysMemory
from WordGameServer import settings


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

    try:
   
        login_val = request.POST['login']
        password_val = request.POST['password']
        public_key = request.POST['public_key']
      
        secret_message_hider = Encrypter()
        key_database = KeysMemory.objects.filter(public_1 = public_key).first()

        if key_database != None:
            secret_message_hider.pub_key = (int(key_database.public_0), int(public_key))
            secret_message_hider.prv_key = (int(key_database.private_0), int(key_database.private_1))
            l = []
            for elem in password_val.split(";"):
                if elem != "":
                    l.append(int(elem))
  
            password_val_dec = secret_message_hider.decrypt(l)
            
            logout(request)             
            user = authenticate(username=login_val, password=password_val_dec)
            if key_database.user != None:
                key_database.user.delete()
            key_database.user = user
            key_database.save()
            
        if user != None:
            data_json = {'answer' : True, 'error' : ""}
            return JsonResponse(data_json, safe = False)
            
    except:
        pass

    data_json = {'answer' : False, 'error' : "Mdp/login invalide"}
    return JsonResponse(data_json, safe = False)