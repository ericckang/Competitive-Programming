import heapq
from heapq import heappop, heappush


def permute(nums):
    res = []
    if len(nums) == 1:
        return([nums.copy()])
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        print(perms)
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res


def main():
    print(permute([1,2,3]))


if __name__ == "__main__":
    main()