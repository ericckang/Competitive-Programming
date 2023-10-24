def combinationSum(candidates, target):
    res = []

    def dfs (i, curr, total):
        if i >= len(candidates) or total > target:
            return
        if total == target:
            res.append(curr.copy())
            return

        curr.append(candidates[i])
        dfs(i, curr, total + candidates[i])
        curr.pop()
        dfs(i + 1, curr, total)

    dfs(0, [], 0)
    return res

def main():
    x = combinationSum([2,3,6,7],7)
    print(x)


if __name__ == "__main__":
    main()