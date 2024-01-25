import unittest
import psutil
from unittest.mock import patch
from menu_selection import SystemMonitor
 
class Unittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # This method is executed once before all the test methods in this class
        cls.monitor = SystemMonitor()
 
    @patch('psutil.disk_usage')
    def test_check_disk_usage_normal(self, mock_disk_usage):
        # Test the normal case where disk usage is below the threshold
        mock_disk_usage.return_value.percent = 25
        self.assertTrue(self.monitor.check_disk_usage())
 
    @patch('psutil.disk_usage')
    def test_check_disk_usage_high(self, mock_disk_usage):
        # Test the case where disk usage is above the threshold
        mock_disk_usage.return_value.percent = 80
        self.assertFalse(self.monitor.check_disk_usage())
 
    # Add more test cases as needed
 
if __name__ == '__main__':
    unittest.main()
