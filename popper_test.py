import popper
import unittest
 
PORT_NUMBER = 8089
HOSTNAME = 'Arjuns-MacBook-Pro.local'
class TestUM(unittest.TestCase):

    def test_port_number(self):
        self.assertTrue(popper.find_port_number()==PORT_NUMBER)

    def test_user_host(self):
        self.assertTrue(popper.find_user_host('arjun')==HOSTNAME)
 
 
if __name__ == '__main__':
    unittest.main()