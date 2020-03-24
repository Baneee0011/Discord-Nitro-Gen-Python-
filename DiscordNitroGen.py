import random
import os
import string

def random_char(y: int):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

random_string = random_char(16)
link = "discord.gift/"
print(link + random_string)
os.system('pause >NUL')
