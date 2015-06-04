#!/usr/bin/python3
import os

GAJIM_HOME = os.environ.get('GAJIM_HOME',
                            os.path.expanduser("~/.config/gajim"))

def parse_line(line):
    key, val = (x.strip() for x in line.split('=', 1))
    return key, val

for line in open(os.path.join(GAJIM_HOME, 'config'), 'r').readlines():
    key, val = parse_line(line)
    if 'themes' in key and not 'themes.dark' in key:
        continue # discard
    if 'color' in key or 'themes.dark' in key or key == 'roster_theme':
        print(line.strip())
