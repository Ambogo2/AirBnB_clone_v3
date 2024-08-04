#!/usr/bin/python3
"""test for file_storage"""

import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for test cases"""
        cls.user = User(email="test@test.com", password="password")
        cls.user.save()

    def test_get(self):
        """Test get method"""
        user = storage.get(User, self.user.id)
        self.assertEqual(user, self.user)
        self.assertIsNone(storage.get(User, "invalid_id"))

    def test_count(self):
        """Test count method"""
        self.assertEqual(storage.count(User), 1)
        self.assertEqual(storage.count(), 1)

if __name__ == '__main__':
    unittest.main()
