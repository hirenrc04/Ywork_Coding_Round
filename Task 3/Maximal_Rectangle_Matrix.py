# Maximal Rectangle in a Binary Matrix

def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    max_area = 0
    cols = len(matrix[0])
    heights = [0] * (cols + 1)  # Add an extra zero for easier calculation

    for row in matrix:
        for i in range(cols):
            # Update the running count of consecutive '1's in column i
            heights[i] = heights[i] + 1 if row[i] == '1' else 0

        # Calculate the largest rectangle in the histogram for this row
        stack = []
        for i in range(cols + 1):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

    return max_area

# Example usage:
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
print(maximalRectangle(matrix)) 