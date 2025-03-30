# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from pywf_open_source.tests import run_cov_test

    run_cov_test(
        __file__,
        "pywf_open_source",
        is_folder=True,
        preview=False,
    )
