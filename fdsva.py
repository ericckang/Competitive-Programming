def main():
    def count2(n):
        count = 0
        for i in range(n):
            for j in range(i):
                for k in range(j,n):
                    count += 3
        return count

    print(count2(2))


if __name__ == "__main__":
    main()