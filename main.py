"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb

def longest_run(mylist, key):
    if len(mylist) == 0:
        return 0
    else:
        max_run = 0
        run = 0
        for i in range(len(mylist)):
            if mylist[i] == key:
                run += 1
                if run > max_run:
                    max_run = run
            else:
                run = 0
        return max_run


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
def longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    else:
        mid = len(mylist) // 2
        left = longest_run_recursive(mylist[:mid], key)
        right = longest_run_recursive(mylist[mid:], key)
        return combine_results(left, right)
        
def combine_results(left, right):
    if left.is_entire_range and right.is_entire_range:
        res = to_value(left) + to_value(right)
        return Result(res, res, res, True)

    left_res = left.left_size
    if left.is_entire_range:
        left_res += right.left_size

    right_res = right.right_size
    if right.is_entire_range:
        right_res += left.right_size
        
    both = left.right_size + right.left_size
    longest = max(to_value(left), to_value(right), both)
    return Result(left_res, right_res, longest, False)
