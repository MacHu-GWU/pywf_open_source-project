# -*- coding: utf-8 -*-

import pytest

from pywf_open_source.helpers import (
    sha256_of_bytes,
    bump_version,
)


def test_sha256_of_bytes():
    _ = sha256_of_bytes(b"hello world")


def test_bump_version():
    assert bump_version("1.2.3", major=True) == "2.0.0"
    assert bump_version("1.2.3", minor=True) == "1.3.0"
    assert bump_version("1.2.3", patch=True) == "1.2.4"

    with pytest.raises(ValueError):
        bump_version("1.2.3", major=True, minor=True, patch=True)


if __name__ == "__main__":
    from pywf_open_source.tests import run_cov_test

    run_cov_test(
        __file__,
        "pywf_open_source.helpers",
        preview=False,
    )
