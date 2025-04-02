# -*- coding: utf-8 -*-

from pathlib import Path
from pywf_open_source.api import PyWf

# Initialize the PyWf object.
pywf = PyWf.from_pyproject_toml(Path("/path/to/pyproject.toml"))

# Perform common development operations.
pywf.create_virtualenv()
pywf.remove_virtualenv()
pywf.poetry_lock()
pywf.poetry_install_only_root()
pywf.poetry_install()
pywf.poetry_install_dev()
pywf.poetry_install_test()
pywf.poetry_install_doc()
pywf.poetry_install_all()
pywf.run_unit_test()
pywf.run_cov_test()
pywf.view_cov()
pywf.build_doc()
pywf.view_doc()
pywf.poetry_build()
pywf.twine_upload()
pywf.setup_codecov_io_upload_token_on_github()
pywf.setup_readthedocs_project()
pywf.publish_to_github_release()
