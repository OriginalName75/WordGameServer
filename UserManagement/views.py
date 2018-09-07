from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
import urllib

from GameManager.models import Game
from UserManagement.lib.Encrypt import check_user
from UserManagement.models import UserInfo
from WordGameServer import settings


@csrf_exempt
def new_friend_answer(request):
    user = check_user(request)
    data_json = {}
    if user != None:
        try:
            answer = request.POST['answer']
            id_info = int(request.POST['id'])
            answ = answer == "true"
            demander = user.info.friend_demands.filter(id = id_info).first()
            if demander != None:
                if answ:
                    game = Game()
                    game.save()
                    user.info.games.add(game)
                    demander.games.add(game)
                    
                    
                user.info.friend_demands.remove(demander)
                if answ:
                    demander.save()
                user.info.save()
             
                
            
        except:
            pass
        
        
    
    return JsonResponse(data_json, safe = False)

@csrf_exempt
def get_new_friend_list(request):
    user = check_user(request)
    if user != None:
        user_info_obj = user.info
        list_new_friend = []
        
        for friend_request in user_info_obj.friend_demands.all():
            list_new_friend.append({"id": friend_request.id,
                                    "name" : friend_request.user.username,
                                    })
        list_friend = []
        for game_found in user_info_obj.games.all():
            for user_aux in game_found.users.all():
                if user_aux.id != user_info_obj.id:
                    letter_choose = game_found.letter_choosed != None
                    if letter_choose != None and game_found.letter_choosed != "":
                        letter = game_found.letter_choosed
                    else:
                        letter = ""
                    yourturn = game_found.userturn.id == user_info_obj.id
                    waiting_for_other = (\
                    (letter != "" and game_found.userplayed != None and \
                     game_found.userplayed.id == user_info_obj.id) or \
                    (not yourturn and letter == ""))
                    gamefinished = game_found.number_of_letters >= 25
                    list_friend.append({"id": game_found.id,
                                            "name" : user_aux.user.username,
                                            "mmr" : user_aux.mmr,
                                            "game_started" : game_found.isStarted,
                                            "can_play" : not waiting_for_other,
                                            "game_finished" : gamefinished,
                                            "wait_quit" : game_found.userleft != None\
                                             and game_found.userleft.id == user_info_obj.id,
                                            })   
        
        data_json = {'error' : False, \
                     'new_friend_list' : list_new_friend, 'list_friend' : list_friend}
        
    else:
        data_json = {'error' : True, 'new_friend_list' : [], 'list_friend' : []}
    
    return JsonResponse(data_json, safe = False)
        

@csrf_exempt
def add_friend(request):
    user = check_user(request)
    if user != None:
        
        try:
            login_val = request.POST['friend']
            
            new_frien = User.objects.filter(username = login_val).first()
            
            if new_frien != None and new_frien.id != user.id:
                try:
                  
                    games =  user.info.games.all()
                    check_is_friend = True
                    for g in games:
                        
                        if g.users.filter(id = new_frien.info.id).first() != None :
                            check_is_friend = False
                            break
                    
                    if check_is_friend:
                        user.info.friends_asked.add(new_frien.info)
                        user.info.save()
                        data_json = {'error' : False, 'message' : "Veuillez attendre la réponse de votre contacte"}
                    else:
                        data_json = {'error' : True, 'message' : "C'est déjà votre amis"}
                        
                except:
                    data_json = {'error' : True, 'message' : "Internal error"}
                
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
                user_info.save()
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
    