
import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
specials = '!@#$%&?/|\\'

sample_size = lower + upper + nums + specials

password = [    # Adding minimum cases
    random.choice(lower),
    random.choice(upper),
    random.choice(nums),
    random.choice(specials)
]

for i in range ( 8 - len(password)):   # Adding other chars after adding minimum cases
    password.append(random.choice(sample_size))    

random.shuffle(password) #Shuffling to avoid fixed positioning

final_password = "".join(password)   #Converting list to string
print(f"Your new and strong password is {final_password}")