nums = list(map(int, input().split()))

n = len(nums)

i = n - 2
while i >= 0:
    if nums[i] < nums[i + 1]:
        break
    i -= 1

if i >= 0:
    j = n - 1
    while j >= 0:
        if nums[j] > nums[i]:
            break
        j -= 1

    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

left = i + 1
right = n - 1

while left < right:
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp

    left += 1
    right -= 1

for x in nums:
    print(x, end=" ")