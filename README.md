# cs362_hw2
White Box tests

Description
For this assignment you will have to achieve 100% Branch and Condition Coverage. For this assignment, this means that for each 
conditional statement, you need to have a test case for each combination of conditions. So if your conditional statement was a 
or b you would need to have a test case for each row of the following truth table:

a	b	outcome
T	T	T
T	F	T
F	T	T
F	F	F
If you recall what I said in the exploration, Branch and Condition coverage is usually not done due to the number of tests 
required. The reason we are doing it here, is we are only testing a single function, not an entire program. The function under
test is defined below.

Behold! The Source!

def contrived_func(val):
    # This function serves no logical purpose
    # DO NOT try to make sense of it!
    # Just make sure your tests cover everything requested
    # val is a numerical value
    if val < 150 and val > 100:
        return True
    elif val * 5 < 361 and val / 2 < 24:
        if val == 6:
            return False
        else:
            return True
    elif (val > 75 or val / 8 < 10) and val**val % 5 == 0:
        return True
    else:
        return False
Again, this function's only purpose is as a learning aid, it doesn't do anything. DO NOT try to rationalize its behavior! This function
is contained within contrived_func.py, so make sure you are importing the correct file.

You need to write a series of unit tests that attempt to meet 100% Branch and Condition Coverage. Once submitted to Gradescope, the 
autograder will run the tests against a modified version of the above code. The contrived_func on Gradescope is functionally equivalent
but includes print statements when each condition combination is triggered. There are 12 such triggers, labled C1-C12. You will only
receive full credit for the autograded portion if your test suite triggers all 12 print statements.

Outside of the autograded portion, your test suite will also be graded based on how many tests were required to uncover all 12 triggers. 
Full points will only be rewarded if you can do it with 7 or fewer test cases. Please note, that if your tests do not pass the autograder
with full marks, you will not be eligible for these Efficient Testing points. Also, for the purposes of the efficiency points, each assert/call
to contrived_func counts as a single test, so no putting in multiple asserts in each test case.

Finally, as was the case last week, your test suite needs to be free of linting errors.

