"""
Writing a reuseable function to handle adding the two integers will help cancel reptition when calculating the sum of numerous pairs of integers
"""

def get_sum(a:int, b:int) -> int:
    result = a + b
    print(result)

get_sum(2, 3)
get_sum(4, 2)
get_sum(4, 7)
get_sum(1, 3)

