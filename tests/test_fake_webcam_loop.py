#!/usr/bin/env python

"""Tests for `fake_webcam_loop` package."""


import unittest
from click.testing import CliRunner

from fake_webcam_loop import fake_webcam_loop
from fake_webcam_loop import cli


class TestFake_webcam_loop(unittest.TestCase):
    """Tests for `fake_webcam_loop` package."""

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
        assert 'fake_webcam_loop.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
