from collections import Sequence

from xonsh.completers.path import complete_path
from xonsh.completers.python import complete_python
from xonsh.completers.commands import complete_command


def complete_base(prefix, line, start, end, ctx):
    if line.strip() == '':
        out = (complete_python(prefix, line, start, end, ctx) |
               complete_command(prefix, line, start, end, ctx))
        paths = complete_path(prefix, line, start, end, ctx, False)
        return (out | paths[0]), paths[1]
    elif prefix == line:
        return (complete_python(prefix, line, start, end, ctx) |
                complete_command(prefix, line, start, end, ctx))
    return set()
