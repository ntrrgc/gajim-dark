#!/usr/bin/python3
import os
import shutil
import re

GAJIM_HOME = os.environ.get('GAJIM_HOME',
                            os.path.expanduser("~/.config/gajim"))

def parse_line(line):
    key, val = (x.strip() for x in line.split('=', 1))
    return key, val

theme_config = {}
for line in open('gajim-color.conf', 'r').readlines():
    key, val = parse_line(line)
    theme_config[key] = val

process_spawning_settings = {
    'custombrowser',
    'custom_file_manager',
    'custommailapp'
}

def apply_theme_config():
    file_path = os.path.join(GAJIM_HOME, 'config')
    new_lines = []

    with open(file_path, 'r') as f:
        for line in f.readlines():
            key, val = parse_line(line)

            if key in theme_config:
                new_lines.append('%s = %s' % (key, theme_config[key]))
            elif key in process_spawning_settings:
                val = re.sub('^.*/pop-gnome-theme ', '', val)
                val = os.path.join(
                    os.path.abspath(os.path.dirname(__file__)),
                    'pop-gnome-theme'
                ) + ' ' + val
                new_lines.append('%s = %s' % (key, val))
            else:
                # Leave it unchanged
                new_lines.append(line.strip())

    shutil.copy(os.path.join(GAJIM_HOME, 'config'),
                os.path.join(GAJIM_HOME, 'config.bak'))

    with open(file_path, 'w') as f:
        f.write('\n'.join(new_lines))

if __name__ == "__main__":
    apply_theme_config()
