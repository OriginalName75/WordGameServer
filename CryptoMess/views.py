from django.http.response import JsonResponse

from CryptoMess.lib.Checker import check_old
from CryptoMess.lib.generateKeys import Encrypter
from CryptoMess.models import KeysMemory


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
