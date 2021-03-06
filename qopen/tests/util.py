# Copyright 2015-2016 Tom Eulenfeld, MIT license

# The following lines are for Py2/Py3 support with the future module.
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import (  # analysis:ignore
    bytes, dict, int, list, object, range, str,
    ascii, chr, hex, input, next, oct, open,
    pow, round, super,
    filter, map, zip)

import contextlib
import os
import shutil
import sys
import tempfile


class _Devnull(object):

    def write(self, _):
        pass


@contextlib.contextmanager
def quiet():
    stdout_save = sys.stdout
    sys.stdout = _Devnull()
    try:
        yield
    finally:
        sys.stdout = stdout_save


@contextlib.contextmanager
def tempdir(delete=True, change_dir=True):
    if delete:
        tempdir = tempfile.mkdtemp(prefix='qopen_test')
    else:
        tempdir = os.path.join(tempfile.gettempdir(), 'qopen_test_permanent')
        if not os.path.exists(tempdir):
            os.mkdir(tempdir)
    if change_dir:
        cwd = os.getcwd()
        os.chdir(tempdir)
    try:
        yield tempdir
    finally:
        if change_dir:
            os.chdir(cwd)
        if delete and os.path.exists(tempdir):
            shutil.rmtree(tempdir)
