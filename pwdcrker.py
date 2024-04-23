import hashlib
# password cracker which allows you to enter hash and crack the hash which matches with the password that is in password.txt file
print('+++++++++++++++++++PASSWORD CRACKING++++++++++++++++++\n')
Enter_hash = input('Enter your hash form password: \n')

pwd_file = input('Enter the password file:\n')
pwd_found = 0
try:
    file = open(pwd_file, 'r') 
except:
    print(f"{pwd_file} not found. Enter correct file name.")
    quit()
# count = 0
for word in file:
    # print(word)
    enc_file = word.encode('utf-8')
    word_hash = hashlib.md5(enc_file.strip())
    digest = word_hash.hexdigest()
    if digest == Enter_hash:
        print(f'Password hash match found.Password is {word}')
        pwd_found = 1
        break
if not pwd_found:
    print(f'Password isn\'t found in {pwd_file} \n')
print('+++++++++++++THANK YOU+++++++++++++++++++++++')