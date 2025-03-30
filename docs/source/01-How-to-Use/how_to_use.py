# -*- coding: utf-8 -*-

from pathlib import Path
from pywf_open_source.api import PyWf

pywf = PyWf.from_pyproject_toml(Path("/path/to/pyproject.toml"))
pywf.create_virtualenv()