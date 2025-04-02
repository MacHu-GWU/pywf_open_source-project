# -*- coding: utf-8 -*-

from pywf_open_source.api import PyWf
from pywf_open_source.paths import path_pyproject_toml


def test():
    pywf = PyWf.from_pyproject_toml(path_pyproject_toml)

    # --- property
    _ = pywf.dir_project_root
    _ = pywf.toml_data

    _ = pywf.package_name
    _ = pywf.package_version
    _ = pywf.package_license
    _ = pywf.package_description
    _ = pywf.package_author_name
    _ = pywf.package_author_email
    _ = pywf.package_maintainer_name
    _ = pywf.package_maintainer_email
    _ = pywf.py_ver_major
    _ = pywf.py_ver_minor
    _ = pywf.py_ver_micro
    _ = pywf.github_account
    _ = pywf.github_token_name
    _ = pywf.git_repo_name
    _ = pywf.github_repo_fullname
    _ = pywf.github_repo_url
    _ = pywf.github_actions_secrets_settings_url
    _ = pywf.github_versioned_release_url
    _ = pywf.codecov_account
    _ = pywf.codecov_token_name
    _ = pywf.readthedocs_username
    _ = pywf.readthedocs_project_name
    _ = pywf.readthedocs_token_name

    _ = pywf.dir_home
    _ = pywf.dir_venv
    _ = pywf.dir_venv_bin
    _ = pywf.get_path_venv_bin_cli
    _ = pywf.path_venv_bin_python
    _ = pywf.path_venv_bin_pip
    _ = pywf.path_venv_bin_pytest
    _ = pywf.path_venv_bin_sphinx_build
    _ = pywf.path_sys_executable
    _ = pywf.get_path_dynamic_bin_cli
    _ = pywf.path_bin_virtualenv
    _ = pywf.path_bin_poetry
    _ = pywf.path_bin_twine
    _ = pywf.dir_python_lib
    _ = pywf.path_version_py
    _ = pywf.package_version
    _ = pywf.dir_tests
    _ = pywf.dir_tests_int
    _ = pywf.dir_tests_load
    _ = pywf.dir_htmlcov
    _ = pywf.path_htmlcov_index_html
    _ = pywf.dir_sphinx_doc
    _ = pywf.dir_sphinx_doc_source
    _ = pywf.dir_sphinx_doc_source_conf_py
    _ = pywf.dir_sphinx_doc_source_python_lib
    _ = pywf.dir_sphinx_doc_build
    _ = pywf.dir_sphinx_doc_build_html
    _ = pywf.path_sphinx_doc_build_index_html
    _ = pywf.path_requirements
    _ = pywf.path_requirements_dev
    _ = pywf.path_requirements_test
    _ = pywf.path_requirements_doc
    _ = pywf.path_requirements_automation
    _ = pywf.path_poetry_lock
    _ = pywf.path_poetry_lock_hash_json
    _ = pywf.path_pyproject_toml
    _ = pywf.dir_build
    _ = pywf.dir_dist
    _ = pywf.path_github_token_file
    _ = pywf.path_codecov_token_file
    _ = pywf.path_readthedocs_token_file
    _ = pywf.path_bin_aws

    # --- action
    pywf.create_virtualenv()
    pywf.create_virtualenv() # do it twice to test the idempotency
    pywf.poetry_lock()
    pywf.poetry_install_only_root()
    pywf.poetry_install()
    pywf.poetry_install_dev()
    pywf.poetry_install_test()
    pywf.poetry_install_doc()
    pywf.build_doc()
    pywf.view_doc()
    pywf.remove_virtualenv()
    pywf.remove_virtualenv() # do it twice to test the idempotency
    # Don't call run_unit_test or run_cov_test here to avoid recursive test calls


if __name__ == "__main__":
    from pywf_open_source.tests import run_cov_test

    run_cov_test(
        __file__,
        "pywf_open_source",
        preview=False,
    )
