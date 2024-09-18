#6
#10 22 28 29 30 40
#54

number = int(input())
numbers = list(map(int, input().split()))
query = int(input())

# Initialize variables
possible_sums = set()  # Using a set to avoid duplicate sums
for i in range(number - 1):
    for j in range(i + 1, number):
        possible_sums.add(numbers[i] + numbers[j])  # Add all possible sums to the set

# Find the closest sum to the query
closest_sum = min(possible_sums, key=lambda x: abs(x - query))

print(closest_sum)