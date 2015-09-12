#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_project-time-tracker
----------------------------------

Tests for `projecttimetracker` module.
"""

import unittest

from projecttimetracker import projecttimetracker


class TestProjecttimetracker(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        self.assertEqual(projecttimetracker.value, 1);

    def tearDown(self):
        pass
