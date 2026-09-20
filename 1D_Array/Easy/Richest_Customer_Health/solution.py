m = int(input("Enter number of customers: "))
n = int(input("Enter number of banks: "))

accounts = []

print("Enter the wealth of each customer:")

for i in range(m):
    row = list(map(int, input().split()))
    accounts.append(row)

max_wealth = 0

for i in range(m):
    current_wealth = 0

    for j in range(n):
        current_wealth += accounts[i][j]

    if current_wealth > max_wealth:
        max_wealth = current_wealth

print("Richest customer wealth:", max_wealth)