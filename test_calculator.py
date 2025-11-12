import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
     def test_add(self):
         assert Calculator.add(5,3)==8
         assert Calculator.add(5,-2)==3
         assert Calculator.add(-3,-2)==-5
    #     fill in code

    def test_subtract(self): # 3 assertions
        assert Calculator.sub(8,5)==3
        assert Calculator.sub(8,-3)==11
        assert Calculator.sub(-8,-3)==-5
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion

        try:
            Calculator.div (8,0)
        except ZeroDivisionError:
            print("Can't Divide by Zero")


    def test_logarithm(self): # 3 assertions
        assert Calculator.log (1,10)==0
        assert Calculator.log(8, 2) == 3

    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()