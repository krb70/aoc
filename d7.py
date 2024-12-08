import pathlib as P, sys as S, operator as O

txt = P.Path((S.argv + ['d7.txt'])[1]).read_text().strip().split('\n')
tests = [x.split(':') for x in txt]
tests = [(int(x[0]), [int(_) for _ in x[1].strip().split()]) for x in tests]
def check(res, nums, acc):
    if not nums: return acc == res
    return any(check(res, nums[1:], op(acc, nums[0])) for op in ops)

ops = (O.add, O.mul)
print(sum(res for res, nums in tests if check(res, nums[1:], nums[0]))) 

ops += (lambda a, b: int(str(a)+str(b)),)
print(sum(res for res, nums in tests if check(res, nums[1:], nums[0]))) 

