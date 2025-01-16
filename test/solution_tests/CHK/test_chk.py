from lib.solutions.CHK import checkout_solution


class TestChk():
    def test_chkEmpty(self):
        assert checkout_solution.checkout("") == 0
    def test_chkInvalid(self):
        assert checkout_solution.checkout("Z") == -1
    def test_chk3As(self):
        assert checkout_solution.checkout("AAA") == 130
    def test_chk2Bs(self):
        assert checkout_solution.checkout("BB") == 45
    def test_chkNormal(self):
        assert checkout_solution.checkout("ABCD") == 115
    def test_dealsGalore(self):
        assert checkout_solution.checkout("AAAAAABBBB") == 350
    def test_2Es1BFree(self):
        assert checkout_solution.checkout("EEEEBB") == 160
    def test_2Es1BFree(self):
        assert checkout_solution.checkout("EEEEBB") == 160
    def test_9As(self):
        assert checkout_solution.checkout("AAAAAAAAA") == 160

TestChk().test_chkEmpty()
TestChk().test_chkInvalid()
TestChk().test_chk3As()
TestChk().test_chk2Bs()
TestChk().test_chkNormal()
TestChk().test_dealsGalore()
TestChk().test_dealsGalore()
TestChk().test_dealsGalore()
