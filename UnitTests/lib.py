from django.test.client import Client
import unittest
import sys

__author__ = 'tdd'

class ControllerTestCase(unittest.TestCase):
    controller_modules = None
    __captured_modules = None

    @classmethod
    def setUpClass(cls):
        cls.client = Client()
        cls.client.get("/test/")
        
    def _clean_modules(self):
        for k,v in self.__captured_modules.iteritems():
            reload(v)
            globals()[k] = v
        
    def _capture_controller_modules(self):
        for k,v in sys.modules.iteritems():
            for module in self.controller_modules:
                if module in k:
                   self.__captured_modules[k] = v
                   setattr(self, module, v)

    def setUp(self):
        self.client = Client()
        self.__captured_modules = {}
        self._capture_controller_modules()
        
    def tearDown(self):
        self._clean_modules()

        