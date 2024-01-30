from hello_world.formater import plain_text_upper_case
import unittest

class TestFormater(unittest.TestCase):
    def test_plain_text_upper_case(self):
        r = plain_text_upper_case('wwww', "ESMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())
