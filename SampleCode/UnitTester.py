from TestFile import MyClass
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):   
        p1 = MyClass()
        self.assertEqual(p1.myfunc(5), 6)


if __name__ == '__main__':
    unittest.main()