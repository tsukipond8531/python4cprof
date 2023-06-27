#!/usr/bin/env python3

import sys

for line in sys.stdin.readlines():
    if line.startswith('includefile '):
        file = line.split()[1]
        sys.stdout.write(open(file).read())
    else:
        print(line, end='')
