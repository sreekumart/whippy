import unittest
from whippy.whippy_factory import WhippyFactory
from whippy.whippy_command import WhippyCommand
from unittest.mock import patch


class TestWhippyFactory(unittest.TestCase):

    def test_whippy_factory_new(self):
        self.assertIsInstance(WhippyFactory.get_command(group_name='testgroup'), WhippyCommand)

    def test_whippy_factory_existing(self):
        WhippyFactory._factory_objects['testgroup'] = WhippyCommand()
        self.assertIsInstance(WhippyFactory.get_command(group_name='testgroup'), WhippyCommand)

    def test_whippy_create_command(self):
        def test_method():
            return "hello"
        whippy_command = WhippyCommand()
        new_method = WhippyFactory.create_decorator(whippy_command, test_method)
        self.assertEqual(new_method(), "hello")


