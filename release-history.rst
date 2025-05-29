.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.1.3 (2025-05-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Fix a bug that it should not print github token

**Miscellaneous**

- Yank 0.1.2


0.1.2 (2025-05-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Fix a bug that it should not sync home_secret.json to HOME folder by default

**Miscellaneous**

- Yank 0.1.1


0.1.1 (2025-05-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- First public API stable release
- Add the following public APIs:
    - ``PyWf.create_virtualenv``
    - ``PyWf.remove_virtualenv``
    - ``PyWf.poetry_lock``
    - ``PyWf.poetry_install_only_root``
    - ``PyWf.poetry_install``
    - ``PyWf.poetry_install_dev``
    - ``PyWf.poetry_install_test``
    - ``PyWf.poetry_install_doc``
    - ``PyWf.poetry_install_all``
    - ``PyWf.run_unit_test``
    - ``PyWf.run_cov_test``
    - ``PyWf.view_cov``
    - ``PyWf.build_doc``
    - ``PyWf.view_doc``
    - ``PyWf.poetry_build``
    - ``PyWf.twine_upload``
    - ``PyWf.setup_codecov_io_upload_token_on_github``
    - ``PyWf.setup_readthedocs_project``
    - ``PyWf.edit_github_repo_metadata``
    - ``PyWf.publish_to_github_release``
