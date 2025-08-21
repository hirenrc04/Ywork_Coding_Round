
    n = len(ratings)
    candies = [1] * n

    # Left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 2
        elif ratings[i] == ratings[i - 1]:
            candies[i] = 1  # same rating = no forced rule

    # Right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 2)

    return sum(candies)


# 🔎 Test cases
print(candy([2,2, 2]))   # Expected 5 → [2,1,2]