#!/usr/bin/python3

"""
This CLI script allows you to run smt N times like this:
```
$ repeat 10 echo Hello World!
```
"""

import sys
import os



if len(sys.argv) <= 1:
    print("No repeats number provided.")
    sys.exit(1)

try:
    repeat_times = int(sys.argv[1])
except:
    print("Unable to parse repeats number.")
    sys.exit(1)

command_parts = sys.argv[2:]

if not command_parts:    # if list is empty
    print("No command to repeat provided.")
    sys.exit(1)

command_to_repeat = " ".join(command_parts)

for _ in range(repeat_times):
    os.system(command_to_repeat)

