"""
Bruce zhu 2018/04/28
"""
import unittest
from src.MyObservatory import MyObservatory


class BaseCase(unittest.TestCase):

    def setUp(self):
        MyObservatory.close_and_launch_app()

    def tearDown(self):
        MyObservatory.close()


