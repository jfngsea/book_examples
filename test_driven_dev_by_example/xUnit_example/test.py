import abc


class TestCase:
    def __init__(self, name) -> None:
        self.name=name
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
    

class WasRun(TestCase):
    def testMethod(self):
        self.log= self.log + "testMethod "
    
    def setUp(self):
        self.log= "setUp "
    
    def tearDown(self):
        self.log= self.log + "tearDown "

class TestCaseTest(TestCase):
    def setUp(self):
        pass

    def testTemplateMethod(self):
        self.test= WasRun("testMethod")
        self.test.run()
        assert("setUp testMethod tearDown " == self.test.log)

TestCaseTest("testTemplateMethod").run()