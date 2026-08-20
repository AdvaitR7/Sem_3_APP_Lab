# Memoization Method
def fib_memo(num, cache=None):
    if cache is None:
        cache = {}

    if num in cache:
        return cache[num]

    if num <= 1:
        return num

    cache[num] = fib_memo(num - 1, cache) + fib_memo(num - 2, cache)
    return cache[num]


def fib_tab(num):
    if num <= 1:
        return num

    table = [0] * (num + 1)
    table[1] = 1

    for i in range(2, num + 1):
        table[i] = table[i - 1] + table[i - 2]

    print("Fibonacci Sequence (Tabulation):", table)
    return table[num]


def fib_optimized(num):
    if num <= 1:
        return num

    prev, curr = 0, 1
    for _ in range(2, num + 1):
        prev, curr = curr, prev + curr
    return curr


n = int(input("Enter Fibonacci Position: "))

memo_result = fib_memo(n)
tab_result = fib_tab(n)
opt_result = fib_optimized(n)

print("\nResult using Memoization :", memo_result)
print("Result using Tabulation  :", tab_result)
print("Result using Optimized DP:", opt_result)




# #OUTPUT

# Enter Fibonacci Position: 10
# Fibonacci Sequence (Tabulation): [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Result using Memoization : 55
# Result using Tabulation  : 55
# Result using Optimized DP: 55