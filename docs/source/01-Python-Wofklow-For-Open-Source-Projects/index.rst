Python Workflow (PyWf) for Open Source Projects
==============================================================================


Overview
------------------------------------------------------------------------------
PyWf provides a comprehensive automation framework for managing the entire lifecycle of open source Python projects. By consolidating various development tasks into a consistent interface, it eliminates the cognitive overhead of switching between different tools and commands.


Getting Started
------------------------------------------------------------------------------
.. dropdown:: how_to_use.py

    .. literalinclude:: ./how_to_use.py
       :language: python
       :linenos:


Core Functionality
------------------------------------------------------------------------------
**Virtual Environment Management**

- :meth:`~pywf_open_source.define_02_venv.PyWfVenv.create_virtualenv`: Creates a virtual environment using Poetry with the specified Python version
- :meth:`~pywf_open_source.define_02_venv.PyWfVenv.remove_virtualenv`: Removes the virtual environment directory

**Dependency Management**

- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_lock`: Resolves and locks dependencies in the poetry.lock file
- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_install_only_root`: Installs only the package in development mode without dependencies
- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_install`: Installs the package and its core dependencies
- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_install_dev`: Installs development dependencies
- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_install_test`: Installs testing dependencies
- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_install_doc`: Installs documentation dependencies
- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_install_all`: Installs all dependency groups

**Testing**

- :meth:`~pywf_open_source.define_04_tests.PyWfTests.run_unit_test`: Executes unit tests with pytest
- :meth:`~pywf_open_source.define_04_tests.PyWfTests.run_cov_test`: Runs code coverage tests and generates reports
- :meth:`~pywf_open_source.define_04_tests.PyWfTests.view_cov`: Opens the coverage report in your browser

**Documentation**

- :meth:`~pywf_open_source.define_05_docs.PyWfDocs.build_doc`: Builds documentation using Sphinx
- :meth:`~pywf_open_source.define_05_docs.PyWfDocs.view_doc`: Opens the documentation in your browser

**Building and Publishing**

- :meth:`~pywf_open_source.define_06_build.PyWfBuild.poetry_build`: Creates distribution packages using poetry
- :meth:`~pywf_open_source.define_07_publish.PyWfPublish.twine_upload`: Publishes the package to PyPI using twine

**CI/CD Integration**

- :meth:`~pywf_open_source.define_08_saas.PyWfSaas.setup_codecov_io_upload_token_on_github`: Configures Codecov.io integration with GitHub Actions
- :meth:`~pywf_open_source.define_08_saas.PyWfSaas.setup_readthedocs_project`: Sets up a ReadTheDocs project for hosting documentation
- :meth:`~pywf_open_source.define_08_saas.PyWfSaas.edit_github_repo_metadata`: Edit GitHub repo metadata such as description and homepage URL
- :meth:`~pywf_open_source.define_07_publish.PyWfPublish.publish_to_github_release`: Creates a GitHub Release for version tracking


**Configuration**

PyWf reads configuration from the `[tool.pywf]` section in your `pyproject.toml`:

.. code-block:: toml

    # python workflow tool config
    [tool.pywf]
    # The specific python version you use for local development
    dev_python = "3.11.8"
    # --- github.com
    github_account = "MacHu-GWU"
    # Create GitHub token in https://github.com/settings/tokens and put the token in
    # ``${HOME}/home_secret.json``
    github_token_field = "providers.github.accounts.sh.users.sh.secrets.dev.value"
    # --- codecov.io (for code coverage test report)
    codecov_account = "MacHu-GWU"
    # Create Codecov token in https://app.codecov.io/account/gh/${codecov_account}/access
    # and put the token in ``${HOME}/home_secret.json``
    codecov_token_field = "providers.codecov_io.accounts.sh.users.sh.secrets.dev.value"
    # --- readthedocs.org (for documentation hosting)
    # Create Readthedocs token in https://app.readthedocs.org/accounts/tokens/
    # and put the token at ``${HOME}/home_secret.json``
    readthedocs_token_field = "providers.readthedocs.accounts.sh.users.sh.secrets.dev.value"
    # Readthedocs project name, usually it is the same as your project name
    readthedocs_project_name = "cookiecutter_pywf_open_source_demo"


Unified Command System
------------------------------------------------------------------------------
To simplify your workflow and avoid memorizing complex commands, ``PyWf`` includes a lightweight command pattern that can be integrated with Makefile support:

**Command Wrappers**

The `bin/ directory <https://github.com/MacHu-GWU/pywf_open_source-project/tree/main/bin>`_ contains thin Python wrappers for all PyWf functionality:

.. dropdown:: bin/g1_t2_s1_venv_create.py

    .. literalinclude:: ../../../bin/g1_t2_s1_venv_create.py
       :language: python
       :linenos:

.. dropdown:: bin/g1_t2_s2_venv_remove.py

    .. literalinclude:: ../../../bin/g1_t2_s2_venv_remove.py
       :language: python
       :linenos:

.. dropdown:: bin/g2_t1_s1_poetry_lock.py

    .. literalinclude:: ../../../bin/g2_t1_s1_poetry_lock.py
       :language: python
       :linenos:

.. dropdown:: bin/g2_t1_s6_poetry_export.py

    .. literalinclude:: ../../../bin/g2_t1_s6_poetry_export.py
       :language: python
       :linenos:

.. dropdown:: bin/g2_t2_s1_install_only_root.py

    .. literalinclude:: ../../../bin/g2_t2_s1_install_only_root.py
       :language: python
       :linenos:

.. dropdown:: bin/g2_t2_s2_install.py

    .. literalinclude:: ../../../bin/g2_t2_s2_install.py
       :language: python
       :linenos:

.. dropdown:: bin/g2_t2_s3_install_dev.py

    .. literalinclude:: ../../../bin/g2_t2_s3_install_dev.py
       :language: python
       :linenos:

.. dropdown:: bin/g2_t2_s4_install_test.py

    .. literalinclude:: ../../../bin/g2_t2_s4_install_test.py
       :language: python
       :linenos:

.. dropdown:: bin/g2_t2_s5_install_doc.py

    .. literalinclude:: ../../../bin/g2_t2_s5_install_doc.py
       :language: python
       :linenos:

.. dropdown:: bin/g2_t2_s6_install_automation.py

    .. literalinclude:: ../../../bin/g2_t2_s6_install_automation.py
       :language: python
       :linenos:

.. dropdown:: bin/g2_t2_s7_install_all.py

    .. literalinclude:: ../../../bin/g2_t2_s7_install_all.py
       :language: python
       :linenos:

.. dropdown:: bin/g3_t1_s1_run_unit_test.py

    .. literalinclude:: ../../../bin/g3_t1_s1_run_unit_test.py
       :language: python
       :linenos:

.. dropdown:: bin/g3_t2_s1_run_cov_test.py

    .. literalinclude:: ../../../bin/g3_t2_s1_run_cov_test.py
       :language: python
       :linenos:

.. dropdown:: bin/g3_t2_s2_view_cov_result.py

    .. literalinclude:: ../../../bin/g3_t2_s2_view_cov_result.py
       :language: python
       :linenos:

.. dropdown:: bin/g3_t3_s1_run_int_test.py

    .. literalinclude:: ../../../bin/g3_t3_s1_run_int_test.py
       :language: python
       :linenos:

.. dropdown:: bin/g3_t4_s1_run_load_test.py

    .. literalinclude:: ../../../bin/g3_t4_s1_run_load_test.py
       :language: python
       :linenos:

.. dropdown:: bin/g4_t1_s1_nb_to_md.py

    .. literalinclude:: ../../../bin/g4_t1_s1_nb_to_md.py
       :language: python
       :linenos:

.. dropdown:: bin/g4_t2_s1_build_doc.py

    .. literalinclude:: ../../../bin/g4_t2_s1_build_doc.py
       :language: python
       :linenos:

.. dropdown:: bin/g4_t2_s2_view_doc.py

    .. literalinclude:: ../../../bin/g4_t2_s2_view_doc.py
       :language: python
       :linenos:

.. dropdown:: bin/g5_t1_s1_build_package.py

    .. literalinclude:: ../../../bin/g5_t1_s1_build_package.py
       :language: python
       :linenos:

.. dropdown:: bin/g5_t2_s1_publish_package.py

    .. literalinclude:: ../../../bin/g5_t2_s1_publish_package.py
       :language: python
       :linenos:

.. dropdown:: bin/g5_t2_s3_create_release.py

    .. literalinclude:: ../../../bin/g5_t2_s3_create_release.py
       :language: python
       :linenos:

.. dropdown:: bin/g6_t1_s1_setup_codecov.py

    .. literalinclude:: ../../../bin/g6_t1_s1_setup_codecov.py
       :language: python
       :linenos:

.. dropdown:: bin/g6_t1_s2_setup_readthedocs.py

    .. literalinclude:: ../../../bin/g6_t1_s2_setup_readthedocs.py
       :language: python
       :linenos:

.. dropdown:: bin/g6_t1_s3_edit_github_repo.py

    .. literalinclude:: ../../../bin/g6_t1_s3_edit_github_repo.py
       :language: python
       :linenos: 

These wrappers initialize PyWf using your project configuration and execute specific functions with sensible defaults.

**Makefile Integration**

The included Makefile provides a unified command interface:

.. literalinclude:: ../../../Makefile
   :language: make
   :linenos:

When you type ``make``, you will see:

.. code-block:: bash

    $ make
    help                                     ⭐ Show this help message
    venv-create                              ⭐ Create Virtual Environment
    venv-remove                              Remove Virtual Environment
    poetry-lock                              ⭐ Resolve dependencies using poetry, update poetry.lock file
    poetry-export                            Export dependencies to requirements.txt
    install-root                             Install Package itself without any dependencies
    install                                  ⭐ Install main dependencies and Package itself
    install-dev                              Install Development Dependencies
    install-test                             Install Test Dependencies
    install-doc                              Install Document Dependencies
    install-automation                       Install Dependencies for Automation Script
    install-all                              Install All Dependencies
    test-only                                Run test without checking test dependencies
    test                                     ⭐ Run test
    cov-only                                 Run code coverage test without checking test dependencies
    cov                                      ⭐ Run code coverage test
    view-cov                                 ⭐ View code coverage test report
    int-only                                 Run integration test without checking test dependencies
    int                                      ⭐ Run integration test
    nb-to-md                                 Convert Notebook to Markdown
    build-doc                                ⭐ Build documentation website locally
    view-doc                                 ⭐ View documentation website locally
    build                                    Build Python library distribution package
    publish                                  ⭐ Publish Python library to Public PyPI
    release                                  ⭐ Create Github Release using current version
    setup-codecov                            ⭐ Setup Codecov Upload token in GitHub Action Secrets
    setup-rtd                                ⭐ Create ReadTheDocs Project
    edit-github                              ⭐ Edit GitHub Repository Metadata

When you type ``make cov``, it actually runs ``python bin/s03_2_run_cov_test.py``

You may also edit the ``Makefile`` yourself to use different global Python instead of ``~/.pyenv/shims/python``.

This approach offers several advantages:

- Consistent command syntax across projects
- Self-documenting commands with ``make help``
- No need to remember underlying tools or syntax


Getting Started with Cookiecutter
------------------------------------------------------------------------------
For new projects, use our **Cookiecutter Template** `cookiecutter-pywf_open_source <https://github.com/MacHu-GWU/cookiecutter-pywf_open_source>`_ automatically set up the entire PyWf structure:

**The template provides**:

- Pre-configured directory structure
- Default Makefile with all common commands
- Command wrappers in the `bin/` directory
- Properly configured `pyproject.toml`
- GitHub Actions integration files
- Documentation templates

Simply run:

.. code-block:: bash

    pip install "cookiecutter>=2.6.0,<3.0.0" && cookiecutter https://github.com/MacHu-GWU/cookiecutter-pywf_open_source

Then follow the prompts to create a new project with the entire PyWf infrastructure ready to use.
