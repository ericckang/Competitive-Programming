import heapq
from heapq import heappop, heappush


def lastStoneWeight(stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i, s in enumerate(stones):
            stones[i] = -s
        while (stones):
            if (len(stones) == 1):
                return abs(stones[0])
            heapq.heapify(stones)
            y = abs(heapq.heappop(stones))
            x = abs(heapq.heappop(stones))
            print(y)
            print(x)
            if (not (y == x)):
                z = y - x
                heappush(stones, -z)
        return 0
def main():
	print(lastStoneWeight([9,3,2,10]))


if __name__ == "__main__":
    main()