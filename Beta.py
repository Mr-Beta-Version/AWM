import os
from os import system as run
import platform
bit = platform.architecture()[0]
run('git pull')
if bit=='64bit':
    run('curl -L https://github.com/Mr-Beta-Version/Compiled/raw/main/awm64 -o awm64')
    if not os.path.isfile('dump64.so'):run('curl -L https://github.com/Mr-Beta-Version/D-FILE/raw/main/dfile -o dump64.so')
    run('chmod 777 awm64')
    run('./awm64')
elif bit=='32bit':
    exit('32 Bit Not Available')
    run('curl -L https://github.com/Mr-Beta-Version/Compiled/raw/main/awm32 -o awm32')
    if not os.path.isfile('dump32.so'):run('curl -L https://github.com/Mr-Beta-Version/Compiled/raw/main/dump64.cpython-310.so -o dump32.so')
    run('chmod 777 awm32')
    run('./awm32')
else:exit(f'\x1b[1;91m[!] Unknown Device Type {bit}')
