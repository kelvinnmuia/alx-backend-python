#!/usr/bin/env python3
'''
Task 6 module
'''
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Computes the sum of a list integers and floating-point numbers.
    '''
    return float(sum(mxd_lst))