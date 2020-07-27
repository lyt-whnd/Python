#! python3
#pw.py - An insecure password locker program.

import sys,pyperclip
if len(sys.argv)<2:
    print('Useage: python pw.py [account] = copy account password')
    sys.exit()

PASSWORDS = {'email':'F7minlBDDuvMJuxESSKHFHT',
             'blog':'VMAlvQykAxiVH5G8v01if1ML',
             'luggage':'12345'}

account = sys.argv[1] 

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+account+' copied to clipboard.')
else:
    print('There is no account named '+account)

