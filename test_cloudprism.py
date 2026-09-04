# test_cloudprism.py
"""
Tests for CloudPrism module.
"""

import unittest
from cloudprism import CloudPrism

class TestCloudPrism(unittest.TestCase):
    """Test cases for CloudPrism class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CloudPrism()
        self.assertIsInstance(instance, CloudPrism)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CloudPrism()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
