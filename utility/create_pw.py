import secrets
import string

def get_pw():
    symbol = ("%", "&", "$", "#", "@", "!", "<", ">")
    pw_words = string.ascii_letters + string.digits + "".join(symbol)
    pw = "".join(secrets.choice(pw_words) for _ in range(16))
    return pw