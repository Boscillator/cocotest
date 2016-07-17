import unittest
from coconut import convenience

exec(convenience.parse(""))

class Test_convenience(unittest.TestCase):
    
    def test_convenience_version(self):
        version = convenience.version()
        self.assertIsInstance(version,str)

if __name__ == '__main__':
    unittest.main()
