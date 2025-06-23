# -*- coding: utf-8 -*-

"""
Use terminal to run this script, e.g.::

    $ cd /path/to/Poetry-Use-Test
    $ python script.py
"""
import shutil
import subprocess
from pathlib import Path

dir_here = Path(__file__).parent
dir_project_root = dir_here / "mypackage-project"
dir_venv = dir_project_root / ".venv"
shutil.rmtree(dir_venv, ignore_errors=True)

args = [
    "poetry",
    "env",
    "use",
    "python3.11"
]
subprocess.run(args, cwd=dir_project_root, check=True)
