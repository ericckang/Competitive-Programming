
def main():
    n,h = map(int, input().split())
    obstacles_bottom = []
    obstacles_top = []
    for i in range(n):
        obstacle = int (input())
        if i % 2 == 1:
            obstacles_bottom.append(obstacle)
        else:
            obstacles_top.append(obstacle)

    min_obstacles = n
    levels = 0
    numberofobsticles = 0
    totalobsticlesateachlevel = []
    for i in range(h):
        for o in obstacles_bottom:
            if o >= i:
                numberofobsticles += 1
        for d in obstacles_top:
            if h-d < i:
                numberofobsticles += 1
        totalobsticlesateachlevel.append(numberofobsticles)
        numberofobsticles = 0

    print(totalobsticlesateachlevel)

    for i in totalobsticlesateachlevel:
        if i < min_obstacles:
            min_obstacles = i
            levels = 1
        elif i == min_obstacles:
            levels += 1

    print(min_obstacles,levels)


if __name__ == "__main__":
    main()