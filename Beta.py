import os, platform
os.system('git pull')
try:
    import requests
except:
    os.system('python3 -m pip install requests')
    os.system('python3 -m pip install bs4')
    os.system('python3 -m pip install futures')
    os.system('python3 -m pip install machine')
    os.system('python3 -m pip install mechanize')
try:
    import mechanize
except:
    os.system('python3 -m pip install mechanize')
try:
    import rich
except:
    os.system('python3 -m pip install rich')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from AFCT5 import bnsbuy
    bnsbuy()
elif bit == '32bit':
    from AFC import bnsbuy
    bnsbuy()
