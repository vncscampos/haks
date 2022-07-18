import sys
import requests

try:
    url = sys.argv[1]
    name_file = sys.argv[2]
    user_param = sys.argv[3]
    pass_param = sys.argv[4]
    wordlist = open(name_file, 'r').readlines()
except:
    print('Usage: python3 http-form.py url wordlist.txt user-param-name pass-param-name')
    print('Example: python3 http-form.py url wordlist.txt uname pass')
    sys.exit()

for user_word in wordlist:
    for pass_word in wordlist:
        data = { user_param: user_word.rstrip('\n'), pass_param: pass_word.rstrip('\n') }
        response = requests.post(url, data=data)
        if 'logout' in response.text:
            print("[FOUND] User: {} - Password: {}".format(user_word.rstrip('\n'), pass_word.rstrip('\n')))
