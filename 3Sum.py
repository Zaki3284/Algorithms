nums = [-1,0,1,2,-1,-4]

def tree(numbs):
    n = len(numbs)
    for _ in range(n):
        for i in range(n-1):
            if numbs[i] > numbs[i+1]:
                temp = numbs[i]
                numbs[i] = numbs[i+1]
                numbs[i+1] = temp
    return numbs

output = tree(nums)
    
print(output)



from itertools import combinations, permutations

def all_possibilities(nums):
    result = []

    for comb in combinations(nums, 3):
        for perm in permutations(comb):
            if sum(comb)==0:
             result.append(perm)
    
    return result


nums = [-1,0,1,2,-1,-4]

r = all_possibilities(nums)

print(len(r))
print(r[:10])