from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_chkEmpty(self):
        assert checkout_solution.checkout("") == 0
    def test_chk3As(self):
        assert checkout_solution.checkout("AAA") == 130
    def test_chk2Bs(self):
        assert checkout_solution.checkout("BB") == 45
    def test_chkNormal(self):
        assert checkout_solution.checkout("ABCD") == 115
    def test_dealsGalore(self):
        assert checkout_solution.checkout("AAAAAABBBB") == 350
class TestSum():
    def test_chkEmpty(self):
        assert checkout_solution.checkout("") == 0
    def test_chk3As(self):
        assert checkout_solution.checkout("AAA") == 130
    def test_chk2Bs(self):
        assert checkout_solution.checkout("BB") == 45
    def test_chkNormal(self):
        assert checkout_solution.checkout("ABCD") == 115
    def test_dealsGalore(self):
        assert checkout_solution.checkout("AAAAAABBBB") == 350

TestSum().test_chkEmpty()
TestSum().test_chk3As()
TestSum().test_chk2Bs()
TestSum().test_chkNormal()
TestSum().test_dealsGalore()
