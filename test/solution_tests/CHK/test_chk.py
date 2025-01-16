from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_chkEmpty(self):
        assert checkout_solution.checkout("") == 0
    def test_chk3As(self):
        assert checkout_solution.checkout("AAA") == 130
    def test_chk2Bs(self):
        assert checkout_solution.checkout("BBB") == 45
    def test_chkNormal(self):
        assert checkout_solution.checkout("ABCD") == 115
