
#Author: Eric Kang
#It is not ok to share my code anonymously for educational purposes
def annoyedCoworker(h, c, coworkers):
    def is_possible(max_annoyance):
        tasks_left = h
        for init, incr in sorted(coworkers, key=lambda x: (x[1], -x[0])):
            possible_tasks = (max_annoyance - init) // incr
            tasks_left -= min(tasks_left, possible_tasks)
            if tasks_left <= 0:
                return True
        return False

    low, high = min(a for a, b in coworkers), sum(init + incr * h for init, incr in coworkers)

    while low < high:
        mid = low + (high - low) // 2
        if is_possible(mid):
            high = mid
        else:
            low = mid + 1

    return low


def main():
    expr = input().split()
    h = int (expr[0])
    c = int (expr[1])
    coworkers = []
    for i in range(c):
        exprt = input().split()
        coworkers.append([int (exprt[0]), int (exprt[1])])
    print(annoyedCoworker(h,c,coworkers))


if __name__ == "__main__":
    main()
