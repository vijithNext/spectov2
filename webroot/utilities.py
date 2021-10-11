import random
import string

from api_admin.config import *
from django.core.mail import send_mail

def Password_Generator():
    pswd_str = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(PASSWORD_LENGTH))
    return pswd_str

def Code_Generator():
    code_str = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(CODE_LENGTH))
    code_str = 'SiamTR' + code_str
    return code_str