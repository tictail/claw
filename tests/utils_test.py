# -*- coding: utf-8 -*-

from nose.tools import *

from claw import utils


def test_get_delimiter():
    eq_('\r\n', utils.get_delimiter('abc\r\n123'))
    eq_('\n', utils.get_delimiter('abc\n123'))
    eq_('\n', utils.get_delimiter('abc'))
