import random
from .models import *

def generate():
    uniqueObj = Guest.objects.all()
    unique = []
    for i in uniqueObj:
        unique.append(i.token)
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    if not len(unique):
        return "".join(random.choice(chars) for _ in range(7))
    while True:
        value = "".join(random.choice(chars) for _ in range(7))
        if value not in unique:
            return value
            break
