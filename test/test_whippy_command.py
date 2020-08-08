from whippy.whippy_command import WhippyCommand
from whippy.exception.whippy_exception import CircuitOpenException
from whippy.whippy_factory import WhippyFactory
import unittest
import time
import concurrent.futures

class TestWhippyCommand(unittest.TestCase):

    def test_whippy_execute(self):
        def test_method(name):
            return name*2
        test_command = WhippyCommand()
        tes_method = test_command.execute(test_method)
        self.assertEqual(tes_method('this'), 'thisthis')

    def test_whippy_execute_raise_timeout(self):
        def test_method(name):
            time.sleep(20)
            print('exiting now')
            return name*2
        test_command_timeout = WhippyCommand()
        test_method = test_command_timeout.execute(test_method)
        self.assertRaises(concurrent.futures.TimeoutError, test_method, 'test_timeout')

