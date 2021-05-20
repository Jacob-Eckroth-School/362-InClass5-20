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
        self.assertEqual(leapyear.isLeapYear(9),False)


if __name__ == "__main__":
    unittest.main()


#pytest code:
def test_odd_year():
        assert(not leapyear.isLeapYear(123))
def test_odd_year_two():
    assert( not leapyear.isLeapYear(1231232121))
def test_divis_by_400():
    assert(leapyear.isLeapYear(400))
def test_divis_by_400_2():
    assert(leapyear.isLeapYear(1200))
def test_divis_by_100():
    assert(not leapyear.isLeapYear(100))    #Shoudl be false, because divisible by 100
def test_divis_by_300():
    assert(not leapyear.isLeapYear(900))
def test_divis_by_4():
    assert(leapyear.isLeapYear(4))
def test_divis_by_4():
    assert(leapyear.isLeapYear(20))
def test_divis_by_3():
    assert(not leapyear.isLeapYear(9))