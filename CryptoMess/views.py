from django.http.response import JsonResponse
import random

from CryptoMess.lib.Checker import check_old
from CryptoMess.lib.generateKeys import Encrypter
from CryptoMess.models import KeysMemory
from GameManager.models import Cell


# Create your views here.
def send_key(_):
    check_old()    
    key_saved = KeysMemory()
    
    secret_message_hider = Encrypter()
    
    key_saved.public_0 = str(secret_message_hider.pub_key[0])
    key_saved.public_1 = str(secret_message_hider.pub_key[1])
    key_saved.private_0 = str(secret_message_hider.prv_key[0])
    key_saved.private_1 = str(secret_message_hider.prv_key[1])
    key_saved.save()
    data_json = {'public_0' : key_saved.public_0, "public_1" : key_saved.public_1}
    return JsonResponse(data_json, safe = False)
def generate_full(request):
    data_json = None
    if request.user.is_authenticated():
        user = request.user
        game = user.info.games.first()
        game.number_of_letters = 0
        for c in game.cells.all():
            c.delete()
        other_f = None
        others = game.users.all()
        for other in others:
            if other.id != user.info.id:
                other_f = other
                break
        if other_f != None:
            for i in range(5):
                for j in range(5):
                    cell = Cell()
                    cell.game = game
                    cell.row = i
                    cell.col = j
                    cell.user = user.info
                    cell.letter = random.choice("sel")
                    cell.save()
                    game.number_of_letters += 2
                    cell = Cell()
                    cell.game = game
                    cell.row = i
                    cell.col = j
                    cell.user = other_f
                    cell.letter = random.choice("sel")
                    cell.save()
            data_json = {'ok' : 'ok'}
            game.save()
    if data_json == None:
        data_json = {'nothing' : 'ok'}
        
    """game.isStarted = False
    game.save()"""
    return JsonResponse(data_json, safe = False)
def test(request):
    data_json = None
    if request.user.is_authenticated():
        user = request.user
        game = user.info.games.first()
        yourturn = game.userturn.id == user.info.id
        
        if game.letter_choosed != None and game.letter_choosed != "":
            letter = game.letter_choosed
            waiting_for_other = (\
            (letter != "" and game.userplayed != None and \
             game.userplayed.id ==  user.info.id) or \
            (not yourturn and letter == ""))
            if not waiting_for_other:
                cells = game.cells.filter(user__id = user.info.id)
                for i in range(5):
                    break_ = False
                    for j in range(5):
                        cell_found = False
                        for cel in cells:
                            if cel.row == i and cel.col == j:
                                cell_found = True
                                
                        if not cell_found:
                            user_info_obj = user.info
                            cell = Cell()
                            cell.game = game
                            cell.row = i
                            cell.col = j
                            cell.user = user.info
                            cell.letter = letter
                            cell.save()
                            if game.userplayed != None:
                                game.userplayed = None
                                game.letter_choosed = ""
                                
                                if game.userturn.id == user_info_obj.id:
                                    others = game.users.all()
                                    other_f = None
                                    for other in others:
                                        if other.id != user_info_obj.id:
                                            other_f = other
                                    if other_f != None:
                                        game.userturn = other_f
                                else:
                                    game.userturn = user_info_obj
                            else:
                                game.userplayed = user_info_obj
               
                            game.save()
                            data_json = {'letter_pushed' : 'ok'}
                            break_ = True
                            break
                    if break_:
                        break
        if game.letter_choosed != None and game.letter_choosed != "":
   
        
            if yourturn:
                game.letter_choosed = "A"
                data_json = {'letter_choosed' : 'ok'}
                game.save()
    if data_json == None:
        data_json = {'nothing' : 'ok'}
    """game.isStarted = False
    game.save()"""
    return JsonResponse(data_json, safe = False)