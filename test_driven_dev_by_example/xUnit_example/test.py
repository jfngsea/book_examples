import abc


class TestCase:
    def __init__(self, name) -> None:
        self.name=name
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        result= TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result
    

class WasRun(TestCase):
    def testMethod(self):
        self.log= self.log + "testMethod "
    
    def setUp(self):
        self.log= "setUp "
    
    def tearDown(self):
        self.log= self.log + "tearDown "
    
    def testBrokenMethod(self):
        raise Exception

class TestCaseTest(TestCase):
    def setUp(self):
        pass

    def testTemplateMethod(self):
        self.test= WasRun("testMethod")
        self.test.run()
        assert("setUp testMethod tearDown " == self.test.log)

    def testResult(self):
        test= WasRun("testMethod")
        result= test.run()
        assert("1 run, 0 failed" == result.summary())
    
    def testFailedResult(self):
        test= WasRun("testBrokenMethod")
        result= test.run()
        assert("1 run, 1 failed", result.summary)

class TestResult:
    def __init__(self) -> None:
        self.runCount= 0

    def testStarted(self):
        self.runCount+=1

    def summary(self):
        return f'{self.runCount} run, 0 failed'

TestCaseTest("testFailedResult").run()