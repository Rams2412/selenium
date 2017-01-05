import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Report(unittest.TestCase):

    def setUp(self): #sample test
        #self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver = webdriver.Firefox()  
        self.driver.implicitly_wait(30)        
        self.verificationErrors = []        
        self.driver.maximize_window()        
        self.driver.delete_all_cookies() 
    
    def testPass(self):
        self.driver.get("http://www.google.com")
        
        print self.driver.title
        self.assertEqual("a", "a", "bothmatches")
    
    
    def testFail(self):
        self.driver.get("http://www.google.com")
        
        print self.driver.title
        self.assertEqual("a", "b", "bothmatches")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
