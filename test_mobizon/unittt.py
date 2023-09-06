import unittest
from test4 import rarara


class OurTestClass(unittest.TestCase):
    def test_method_1(self):
        res = rarara(5, 7, 10)
        self.assertEqual(res, 2)



#test1 = OurTestClass('test_method_1')

#print(test1.run())

if __name__ == '__main__':
    unittest.main()


