"""Simple tool to rename files."""

import fnmatch
import os
import sys


usage = """
rename.py is a targeted renaming tool to ensure python files are well named.

It removes periods followed by a space, replaces remaining periods with
dashes, and spaces with underscores.

rename.py expects a `find` glob and a path as arguments, e.g:

    `rename.py "*.foo" /my/path`

By default, rename.py is dry run, only printing the new filenames.

To actually rename the files, add `-w` or `--write` as a final cli token, e.g:

    `rename.py "*.foo" /my/path --write`

Limitation: Do not use `.` as the path, use the full `pwd`.

"""


def find(pattern, path):
    """Return a list of files that match a glob pattern within a path."""
    result = []
    for root, _, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


if len(sys.argv) < 3 or len(sys.argv) > 4 or sys.argv[2] is '.':
    # FIXME(md) - we should handle .
    print(usage)
    sys.exit()

if len(sys.argv) is 4 and sys.argv[3] in ['-w', '--write']:
    write = True
else:
    print('No write flag passed -- dry run only.\n\r')
    write = False

find_pattern = sys.argv[1]
path = sys.argv[2]

results = find(find_pattern, path)

for result in results:
    if result.endswith('.py'):
        continue
    new_file = result.replace('. ', '')
    new_file = new_file.replace('.', '-')
    new_file = new_file.replace(' ', '_')
    new_file += '.py'
    if write:
        print('Renaming %s -> %s' % (result, new_file))
        os.rename(result, new_file)
    else:
        print(new_file)
