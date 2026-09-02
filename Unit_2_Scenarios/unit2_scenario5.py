
def minimum_coins(denominations, target):
    # dp[i] stores the minimum coins required for amount i
    dp = [target + 1] * (target + 1)
    dp[0] = 0

    # Calculate minimum coins for each possible amount
    for value in range(1, target + 1):
        for coin in denominations:
            if coin <= value:
                dp[value] = min(dp[value], 1 + dp[value - coin])

    # Return -1 when the target cannot be formed
    if dp[target] > target:
        return -1
    return dp[target]


coins = list(map(int, input("Enter the coin values: ").split()))
amount = int(input("Enter the required amount: "))

answer = minimum_coins(coins, amount)

if answer == -1:
    print("The given amount cannot be formed using these coins.")
else:
    print("Minimum coins needed:", answer)