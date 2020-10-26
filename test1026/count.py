def real(a):
    f = 1

    for i in range(2, a + 1):
        f = f * i

    return f

def num(n, r):
    ans = 0
    ans = real(n) // real(n - r)

    return ans

def findPermutations(n):
    sum = 0
    for r in range(1, n + 1):
        P = num(n, r)
        sum = sum + P

    return sum


str = "1"
n = len(str)

# Function call
print(findPermutations(n))