import random
print('*************START CRACKING PASSWORD********************\n')

pwd = str(input('Enter password(only number):\n'))
trial = 0
guess = ""
while guess!=pwd:
    guess = str(random.randint(0,9999))
    print(f"=> {guess}")
    trial += 1

    if (pwd == guess):
        print(f'password is \"{pwd}\".\n')
        break

print(f'Password aquired after {trial} trials.')
print('**********YOUR PASSWORD CRACKING IS FINISHED************')









