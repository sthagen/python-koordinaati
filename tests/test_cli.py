# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import koordinaatit.cli as cli


def test_cli():
    assert cli.main(['argument']) == 0
