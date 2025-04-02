# -*- coding: utf-8 -*-

from pathlib import Path
from pywf_open_source.api import PyWf
from pywf_open_source.paths import path_pyproject_toml


def test():
    pywf = PyWf.from_pyproject_toml(path_pyproject_toml)
    pywf.


if __name__ == "__main__":
    from pywf_open_source.tests import run_cov_test

    run_cov_test(
        __file__,
        "pywf_open_source",
        preview=False,
    )
