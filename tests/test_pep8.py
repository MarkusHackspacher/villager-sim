# -*- coding: utf-8 -*-

import unittest
import pep8
import os


class TestCodeFormat(unittest.TestCase):
    """Some code format tests
    """

    def test_pep8_os_walk(self):
        """Test that code conform to PEP8. all .py files"""
        check_files = []
        for root, dirs, files in os.walk(os.path.join(
                os.path.dirname(__file__), '..', )):
            for file in files:
                if file.endswith(".py"):
                    check_files.append(os.path.join(root, file))
        pep8style = pep8.StyleGuide(quiet=False, )  #config_file='setup.cfg')
        result = pep8style.check_files(check_files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
