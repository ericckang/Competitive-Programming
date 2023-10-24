def main():
    def llcs(pat, alph):
        m = len(pat)
        n = len(alph)
        lcs = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    lcs[i][j] = 0
                elif pat[i - 1] == alph[j - 1]:
                    lcs[i][j] = 1 + lcs[i - 1][j - 1]
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

        return lcs[m][n]

    pat = input().strip()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lcs = llcs(pat, alphabet)
    print(26 - lcs)

if __name__ == "__main__":
    main()