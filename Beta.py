import os
import platform
from os import system as cmd
bit = platform.architecture()[0]
if bit=='64bit':
    cmd('chmod +x awm64')
    cmd('./awm64')
elif bit=='32bit':
    cmd('chmod +x awm32')
    cmd('./awm32')
else:exit(f'\x1b[1;91m[!] Unknown Device Type {bit}')
