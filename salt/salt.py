#!/usr/bin/env python
import os
import subprocess
MASTER=os.environ.get('MASTER')
MINION=os.environ.get('MINION')
print(MASTER)
print(MINION)

if MASTER:
    subprocess.call(["salt-master", "-ldebug"])
elif MINION:
    subprocess.call(["salt-minion", "-ldebug"])
