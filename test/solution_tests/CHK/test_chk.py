from lib.solutions.CHK import checkout_solution


class TestChk():
    def test_chkEmpty(self):
        assert checkout_solution.checkout("") == 0
    def test_chkInvalid(self):
        assert checkout_solution.checkout("1") == -1
    def test_chk3As(self):
        assert checkout_solution.checkout("AAA") == 130
    def test_chk2Bs(self):
        assert checkout_solution.checkout("BB") == 45
    def test_chkNormal(self):
        assert checkout_solution.checkout("ABCD") == 115
    def test_chkDealsGalore(self):
        assert checkout_solution.checkout("AAAAAABBBB") == 340
    def test_chk2Es1BFree(self):
        assert checkout_solution.checkout("EEEEBB") == 160
    def test_chk9As(self):
        assert checkout_solution.checkout("AAAAAAAAA") == 380
    def test_chk2Fs(self):
        assert checkout_solution.checkout("FF") == 20
    def test_chk3Fs(self):
        assert checkout_solution.checkout("FFF") == 20
    def test_chk5Fs(self):
        assert checkout_solution.checkout("FFFFF") == 40
    def test_chkGroupDiscount(self):
        assert checkout_solution.checkout("STS") == 45
    def test_chkGroupDiscountMultiple(self):
        assert checkout_solution.checkout("STXYZS") == 90
    def test_chkNotGroupDiscount(self):
        print(checkout_solution.checkout("SS"))
        assert checkout_solution.checkout("SS") == 40


TestChk().test_chkEmpty()
TestChk().test_chkInvalid()
TestChk().test_chk3As()
TestChk().test_chk2Bs()
TestChk().test_chkNormal()
TestChk().test_chkDealsGalore()
TestChk().test_chk2Es1BFree()
TestChk().test_chk9As()
TestChk().test_chk2Fs()
TestChk().test_chk3Fs()
TestChk().test_chk5Fs()
TestChk().test_chkGroupDiscount()
TestChk().test_chkGroupDiscountMultiple()
TestChk().test_chkNotGroupDiscount()
