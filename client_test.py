import popper_client
import unittest
 
PORT_NUMBER = 8089
DATA_SIZE = 4096
class TestUM(unittest.TestCase):
 
    def test_config_file(self):
        self.assertTrue(type(popper_client.get_popper_config())==dict)

    def test_port_number(self):
        self.assertTrue(popper_client.find_port_number()==PORT_NUMBER)

    def test_data_size(self):
        self.assertTrue(popper_client.find_data_size()==DATA_SIZE)
 
 
if __name__ == '__main__':
    unittest.main()