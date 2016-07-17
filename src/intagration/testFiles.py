import unittest
import os
import subprocess
import tempfile
import shutil

class Test_testFiles(unittest.TestCase):

    def setUp(self):
        """Compiles the test files"""
        self.testSource = os.path.join(os.path.dirname(__file__), 'testFiles/')
        self.testOutput = os.path.join(os.path.dirname(__file__), 'compiledTestFiles/')
        status = subprocess.call(['coconut','--target','35',self.testSource,self.testOutput])
        self.assertEqual(status,0)


    def tearDown(self):
        pass
        #shutil.rmtree(self.testOutput)

    def test_testFiles_runner(self):
        process = subprocess.Popen(['python','runner.py'],cwd=self.testOutput)
        process.wait()
        self.assertEqual(process.returncode,0)

        

    

if __name__ == '__main__':
    unittest.main()
