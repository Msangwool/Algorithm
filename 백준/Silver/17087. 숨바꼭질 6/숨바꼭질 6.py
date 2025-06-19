import sys
import math
from functools import reduce

n, s = map(int, input().split())
a = list(map(int, input().split()))

diffs = [abs(ai - s) for ai in a]

def gcd_list(nums):
    return reduce(math.gcd, nums)

print(gcd_list(diffs))