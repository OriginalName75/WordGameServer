from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random

from GameManager.models import Game, Cell
from SpellChecker.Checker import matrix_checker
from UserManagement.lib.Encrypt import check_user
def calc_elo(winner, looser, isdraw):
    d = winner.mmr - looser.mmr
    
    p = 1/(1+10**(-1*d/400));
    if p < 0:
        p *= -1

    
    if isdraw:
        
        w_p = 0.5
        l_p = 0.5
    else:
        w_p = 1
        l_p = 0
        
    winner.mmr += 20 *(w_p - p)
    looser.mmr += 20 *(l_p - (1 - p))
    
    winner.save()
    looser.save()
    
@csrf_exempt
def quit_game(request):
    user = check_user(request)
    if user != None:
        try:
            id_game = int(request.POST['id_game'])
            game = Game.objects.filter(id = id_game).first()
            if game != None and game.number_of_letters >=50:
             
                if game.number_of_quit == 0:
                    game.number_of_quit = 1
                    game.userleft = user.info
                    game.save()
                    
                else:
                    if game.userleft.id != user.info.id:
                    
                        game.isStarted = False
                        game.save()
              
            else:
                
                data_json = {'error' : True}
        except:
           
            data_json = {'error' : True}
    else:
       
        data_json = {'error' : True}
    print(data_json)
    return JsonResponse(data_json, safe = False)
@csrf_exempt
def send_letter_grid(request):
    user = check_user(request)
    if user != None:
        user_info_obj = user.info
        try:
            letter = request.POST['letter']
            id_game = int(request.POST['id_game'])
            i = int(request.POST['i'])
            j = int(request.POST['j'])
            game = Game.objects.filter(id = id_game).first()
            if game != None and game.number_of_letters < 50 and i>= 0 and i < 5 and j >= 0 and j < 5:
                
                already_ex = game.cells.filter(Q(user__id = user_info_obj.id)  & \
                                  Q(row = i) & Q(col = j)).first()
                if already_ex == None:
                    cell = Cell()
                    cell.game = game
                    cell.row = i
                    cell.col = j
                    cell.user = user_info_obj
                    cell.letter = letter.upper()
                    cell.save()
                    game.number_of_letters += 1
                    if game.userplayed != None:
                        game.userplayed = None
                        game.letter_choosed = ""
                        
                        if game.userturn.id == user_info_obj.id:
                            others = game.users.all()
                            other_f = None
                            for other in others:
                                if other.id != user_info_obj.id:
                                    other_f = other
                                    break
                            if other_f != None:
                                game.userturn = other_f
                        else:
                            game.userturn = user_info_obj
                    else:
                        game.userplayed = user_info_obj
               
                    game.save()
                    data_json = send_game_info(game, user_info_obj)
                else:
                    data_json = {'error' : True}
            else:
                data_json = {'error' : True}
        except:
            data_json = {'error' : True}
    else:
        data_json = {'error' : True}
    return JsonResponse(data_json, safe = False)

@csrf_exempt
def send_letter(request):
    user = check_user(request)
    if user != None:
        user_info_obj = user.info
        try:
            letter = request.POST['letter']
            if len(letter) == 1 and letter.lower() in "abcdefghijklmnopqrstuvwxyz":
                id_game = int(request.POST['id_game'])
                game = Game.objects.filter(id = id_game).first()
                if game != None:
                    if game.letter_choosed == "" or game.letter_choosed == None:
                        game.letter_choosed = letter
                        game.save()
                        data_json = send_game_info(game, user_info_obj)
                    else:
                        data_json = {'error' : True}
                else:
                    data_json = {'error' : True}
            else:
                    data_json = {'error' : True}
        except:
            data_json = {'error' : True}
    else:
        data_json = {'error' : True}
    return JsonResponse(data_json, safe = False)
def get_grid(my_cells):
    grid = []
    for cell in my_cells:
        json = {"row" : cell.row,
                "col" : cell.col,
                "letter" : cell.letter}
        grid.append(json)
    return grid
def send_game_info(game, user_info_obj):
   
    error = False
    if game.userturn is None or not game.isStarted:
        game.isStarted = True;
        rand = random.randint(0,1)
        game.number_of_letters = 0
        game.number_of_quit = 0
        game.mmr_calculated = False
        game.userleft = None
        if rand == 1:
            game.userturn  = user_info_obj
        else:
            oth_user = None
            for other_user in game.users.all():
                if other_user.id != user_info_obj.id:
                    oth_user = other_user
            if oth_user != None:
                
                game.userturn  = oth_user
            else:
                error
               
        if not error:
            game.letter_choosed = ""
            for c in game.cells.all():
                c.delete()
            
            game.save()
    my_cells = game.cells.filter(user__id = user_info_obj.id)
    grid = get_grid(my_cells)
    if error:
        data_json = {'error' : True}
    else:
        try:

            if game.letter_choosed != None and game.letter_choosed != "":
                letter = game.letter_choosed
            else:
                letter = ""
                
            game_finished = game.number_of_letters >= 50
            if game_finished:
                
                
                other_cells = game.cells.filter(~Q(user__id = user_info_obj.id))
                my_val = matrix_checker(my_cells)
                other_val = matrix_checker(other_cells)
                game_fi = {"my" : my_val, 
                           "other" :other_val}
                other_grid = get_grid(other_cells)
                if not game.mmr_calculated:
                    oth_user = None
                    for other_user in game.users.all():
                        if other_user.id != user_info_obj.id:
                            oth_user = other_user
                    if oth_user != None:
                        
                        if my_val["points"] == other_val["points"]:
                            calc_elo(user_info_obj, oth_user, True)
                        else:
                            if my_val["points"] > other_val["points"]:
                                calc_elo(user_info_obj, oth_user, False)
                            else:
                                calc_elo(oth_user, user_info_obj, False)
                        game.mmr_calculated = True
                        game.save()
            else:
                game_fi = {}
                other_grid = []
                
            yourturn = game.userturn.id == user_info_obj.id
            waiting_for_other = (\
            (letter != "" and game.userplayed != None and \
             game.userplayed.id == user_info_obj.id) or \
            (not yourturn and letter == ""))
            play_against = None
            
            for other_user in game.users.all():
                if other_user.id != user_info_obj.id:
                    play_against = other_user
            if play_against == None:
                play_against = "error"
            else:
                play_against = play_against.user.username
            data_json = {'error' : False,\
             'yourturn' : yourturn, 
             'grid' : grid,
             'letter' : letter,
             'waiting_for_other' : waiting_for_other,
             'play_against' : play_against,
             'game_finished' : game_finished,
             'game_fi' : game_fi,
             'othergrid' : other_grid,
             }
            
            
        except:
            data_json = {'error' : True}
    return data_json
@csrf_exempt
def read_game(request):
    user = check_user(request)
    if user != None:
        user_info_obj = user.info
        try:
            id_game = int(request.POST['id_game'])
            
            game = Game.objects.filter(id = id_game).first()
            if game != None:
                data_json = send_game_info(game, user_info_obj)
            else:
                data_json = {'error' : True}
        except:
            data_json = {'error' : True}
    else:
        data_json = {'error' : True}
    return JsonResponse(data_json, safe = False)

