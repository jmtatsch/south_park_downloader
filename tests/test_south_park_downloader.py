#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `south_park_downloader` package."""


import unittest
from click.testing import CliRunner

from south_park_downloader import south_park_downloader
from south_park_downloader import cli


class TestSouth_park_downloader(unittest.TestCase):
    """Tests for `south_park_downloader` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'south_park_downloader.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
