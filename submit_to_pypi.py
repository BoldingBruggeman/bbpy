#!/usr/bin/env python

import os
import argparse
import glob
import subprocess
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('target')
args = parser.parse_args()

for path in glob.glob(args.target):
    if os.path.isdir(path):
        for tmpname in ('build', 'dist'):
            tmpdir = os.path.join(path, tmpname)
            if os.path.isdir(tmpdir):
                shutil.rmtree(tmpdir)
        subprocess.check_call(['python', 'setup.py', 'bdist_wheel'], cwd=path)
        subprocess.check_call(['twine', 'upload', 'dist/*'], cwd=path)
    elif os.path.isfile(path):
        assert path.lower().endswith('.whl')
        subprocess.check_call(['twine', 'upload', path])

