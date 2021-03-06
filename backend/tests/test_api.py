#!/usr/bin/env python3

import sys, os
import json
import unittest
import hashlib
sys.path.append(os.path.join(sys.path[0],'..'))
from application import app
from parameterized import parameterized, parameterized_class

class TestApi(unittest.TestCase):
    def setUp(self):
        self.myapp = app.test_client()
        self.myapp.testing = True    
        self.headers = {
            'ContentType': 'application/json',
            'dataType': 'json'
        }
 
    def test_dummy(self):
        test = 'ok'
        self.assertEqual(test, 'ok')
    
        
if __name__ == '__main__':
    unittest.main()
