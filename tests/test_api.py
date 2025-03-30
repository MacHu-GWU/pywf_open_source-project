# -*- coding: utf-8 -*-

from pywf_open_source import api


def test():
    _ = api


if __name__ == "__main__":
    from pywf_open_source.tests import run_cov_test

    run_cov_test(
        __file__,
        "pywf_open_source.api",
        preview=False,
    )
