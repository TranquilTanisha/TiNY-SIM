import random
import string

def generate_password():
    letters = string.ascii_lowercase + "#" + string.digits + "@" + string.ascii_uppercase + "$" + "%" + "^"
    return ''.join(random.choice(letters) for i in range(random.randint(5,10)))