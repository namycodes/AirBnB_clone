#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import uuid
from datetime import datetime
import time
class BaseModelTests(unittest.TestCase):
    """Test Cases for Base Model Class"""
    def setUp(self) -> None:
        """Setup function To handle global initialisation"""
        self.my_model = BaseModel()
        self.uuid = str(uuid.uuid4())
        self.my_model_2 = BaseModel('namycodes',self.uuid)

    def test_initialisation_positive(self):
       """Test passing cases `BaseModel` initialization."""
       self.assertIsInstance(self.uuid,str)
       self.assertIsInstance(self.uuid,str)
       self.assertEqual(self.uuid,self.my_model_2.id,msg="They are not equal")
       self.assertEqual(self.my_model_2.name,'namycodes')
       self.assertEqual(str(type(self.my_model)),"<class 'models.base_model.BaseModel'>")
       self.assertIsInstance(self.my_model.created_at,datetime)
       self.assertIsInstance(self.my_model.updated_at,datetime)
    def test_dict(self):
        """Test cases for dictionary of the basemodel"""
        my_model_json = self.my_model.to_dict()
        self.assertIsInstance(my_model_json,dict)
        self.assertIn('id',my_model_json.keys())
        self.assertIn('updated_at',my_model_json.keys())
        self.assertIn('created_at',my_model_json.keys())
        self.assertEqual(my_model_json['__class__'], type(self.my_model).__name__)
    def test_save(self):
        """Test cases for the save function method"""
        time.sleep(0.5)
        date_now = datetime.now()
        self.my_model.save()
        difference = self.my_model.updated_at - date_now
        self.assertTrue(abs(difference.total_seconds()) < 0.01)

if __name__ == "__main__":
    unittest.main()