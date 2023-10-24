def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    length = len(s)
    for i in range(length):
        s.append(s[length - i - 1])
        print(s[length - i - 1])
        s.remove(s[length - i - 1])
        print(s[length - i - 1])
    return s

def main():
    print(reverseString(["H","a","n","n","a","h"]))

if __name__ == "__main__":
    main()