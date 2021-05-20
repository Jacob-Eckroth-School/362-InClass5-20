import unittest
import leapyear


class TestCase(unittest.TestCase):
    def test_odd_year(self):
        self.assertEqual(leapyear.isLeapYear(123),False)
    def test_odd_year_two(self):
        self.assertEqual(leapyear.isLeapYear(1231232121),False)
    def test_divis_by_400(self):
        self.assertEqual(leapyear.isLeapYear(400),True)
    def test_divis_by_400_2(self):
        self.assertEqual(leapyear.isLeapYear(1200),True)
    def test_divis_by_100(self):
        self.assertEqual(leapyear.isLeapYear(100),False)    #Shoudl be false, because divisible by 100
    def test_divis_by_300(self):
        self.assertEqual(leapyear.isLeapYear(900),False)
    def test_divis_by_4(self):
        self.assertEqual(leapyear.isLeapYear(4),True)
    def test_divis_by_4(self):
        self.assertEqual(leapyear.isLeapYear(20),True)
    def test_divis_by_3(self):
        self.asserTEqual(leapyear.isLeapYear(9),False)

