#!/usr/bin/env python

import os
import argparse
import glob
import subprocess
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('dir')
args = parser.parse_args()

for path in glob.glob(args.dir):
    if os.path.isdir(path):
        distdir = os.path.join(path, 'dist')
        if os.path.isdir(distdir):
            shutil.rmtree(distdir)
        subprocess.check_call(['python', 'setup.py', 'bdist_wheel'], cwd=path)
        subprocess.check_call(['twine', 'upload', 'dist/*'], cwd=path)

