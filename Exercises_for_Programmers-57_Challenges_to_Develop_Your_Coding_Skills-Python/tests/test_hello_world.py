import unittest
from unittest.mock import patch
from hello_world import HelloWorld

class TestHelloWorld(unittest.TestCase):

    @patch('builtins.input', side_effect=['Mary Joe'])
    def test_prompt_user(self, mock_input):
        hello_world_instance = HelloWorld()
        result = hello_world_instance.prompt_user()
        self.assertEqual(result, 'Mary Joe')

if __name__ == '__main__':
    unittest.main
