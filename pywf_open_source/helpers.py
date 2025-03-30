# -*- coding: utf-8 -*-

"""
Helper functions.

.. note::

    This module is "ZERO-DEPENDENCY".
"""

import typing as T
import hashlib

from .logger import logger


def sha256_of_bytes(b: bytes) -> str:  # pragma: no cover
    sha256 = hashlib.sha256()
    sha256.update(b)
    return sha256.hexdigest()


def extract_digit_tokens(text: str) -> T.List[str]:
    """
    Extract all consecutive digit tokens from a string.

    Example:

        >>> extract_digit_tokens("1.23.456")
        ["1", "23", "456"]
    """
    for c in list(text):
        if not c.isdigit():
            text = text.replace(c, " ")
    return [token.strip() for token in text.split() if token.strip()]


def bump_version(
    current_version: str,
    major: bool = False,
    minor: bool = False,
    patch: bool = False,
    minor_start_from: int = 0,
    micro_start_from: int = 0,
):
    """
    Bump a semantic version. The current version has to be in x.y.z format,
    where x, y, z are integers.

    :param current_version: current version string.
    :param major: bump major version.
    :param minor: bump minor version.
    :param patch: bump patch version.
    :param minor_start_from: if bumping major version, minor start from this number.
    :param micro_start_from: if bumping minor version, micro start from this number.
    """
    if sum([patch, minor, major]) != 1:
        raise ValueError(
            "Only one and exact one of 'patch', 'minor', 'major' can be True"
        )

    # get the current version
    major_ver, minor_ver, micro_ver = current_version.split(".")
    major_ver, minor_ver, micro_ver = int(major_ver), int(minor_ver), int(micro_ver)

    # update version
    if major:
        major_ver += 1
        minor_ver, micro_ver = minor_start_from, micro_start_from
    elif minor:
        minor_ver += 1
        micro_ver = micro_start_from
    elif patch:
        micro_ver += 1
    else:  # pragma: no cover
        raise NotImplementedError

    return f"{major_ver}.{minor_ver}.{micro_ver}"


def print_command(args: T.List[str]):
    cmd = " ".join(args)
    logger.info(f"run command: {cmd}")
