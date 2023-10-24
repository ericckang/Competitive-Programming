#Author: Eric Kang
#It is not ok to share my code anonymously for educational purposes

def main():
    while True:
        n = int(input())

        #break the loop when n is 0
        if n == 0:
            break

        #read the first and the second lists
        list1 = [int(input()) for _ in range(n)]
        list2 = [int(input()) for _ in range(n)]

        #make 2 sorted lists to check for index
        sorted1 = sorted(list1)
        sorted2 = sorted(list2)

        #initialize hashmaps to store value and index
        map1 = {}
        map2 = {}

        #set val as key and map it to index for first list
        for i, val in enumerate(sorted1):
            map1[val] = i

        #set index as key and map it to val for second list
        for d, val in enumerate(sorted2):
            map2[d] = val

        res = []

        #find the index of each element in the first list in sorted order and map it to the corresponding value in the second list
        for val in list1:
            index = map1[val]
            res.append(map2[index])

        #print each value in the resultant list
        for val in res:
            print(val)
        print()

if __name__ == "__main__":
    main()
