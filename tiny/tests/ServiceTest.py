from unittest import TestCase
from ..serviceTinyUrl import *


class ServiceTest(TestCase):


    def test_enconde(self):

        self.assertEqual(encode(1), 2251799813685248)
        self.assertEqual(encode(3), 3377699720527872)
        self.assertEqual(encode(10), 1407374883553280)
        self.assertEqual(encode(100), 668503069687808)
        self.assertEqual(encode(987654321), 2482043174780928)
        self.assertEqual(encode(123456789), 2967846795608064)
        self.assertEqual(encode(145678977787), 3928771094134784)


    def test_enbase(self):
        self.assertEqual(enbase(1), "W")
        self.assertEqual(enbase(3), "n")
        self.assertEqual(enbase(10), "C")
        self.assertEqual(enbase(100), "WF")
        self.assertEqual(enbase(987654321), "W9jkSp")
        self.assertEqual(enbase(123456789), "YvSaf")
        self.assertEqual(enbase(145678977787), "1XSmY3n")