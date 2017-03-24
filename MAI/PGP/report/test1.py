import unittest

def inc(a):
    return a + 1

class Test(unittest.TestCase):
    def test_inc(self):
        self.assertEqual(inc(7), 8)
        self.assertEqual(inc(-10), -9)


if __name__ == "__main__":
    unittest.main()
