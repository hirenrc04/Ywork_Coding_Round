def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    # Pass left to right
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 2

    # Pass right to left
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 2)

    return sum(candies)   

#Test cases
print(candy([1,0,0]))    # Expected 3 → [1,1,1]
print(candy([1,2,2]))    # Expected 4 → [1,2,1]
print(candy([3,2,1]))    # Expected 7 → [3,2,2]
print(candy([0,0,0]))    # Expected 3 → [1,1,1]
print(candy([1,3,4,5,2]))# Expected 17 → [1,3,5,7,1]
