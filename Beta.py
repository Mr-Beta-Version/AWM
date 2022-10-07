import os
from os import system as run
import platform
bit = platform.architecture()[0]
if bit=='64bit':
    run('curl -L https://github.com/Mr-Beta-Version/Compiled/raw/main/awm64 -o awm64')
    if not os.path.isfile('dump64.so'):run('curl -L https://github.com/Mr-Beta-Version/Compiled/raw/main/dump64.cpython-310.so -o dump64.so')
    cmd('chmod +x awm64')
    cmd('./awm64')
elif bit=='32bit':
    run('curl -L https://github.com/Mr-Beta-Version/Compiled/raw/main/awm32 -o awm32')
    if not os.path.isfile('dump32.so'):run('curl -L https://github.com/Mr-Beta-Version/Compiled/raw/main/dump64.cpython-310.so -o dump32.so')
    cmd('chmod +x awm32')
    cmd('./awm32')
else:exit(f'\x1b[1;91m[!] Unknown Device Type {bit}')
