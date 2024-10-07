def three_sum(nums):
    # Sort the array to make it easier to avoid duplicates
    nums.sort()
    triplets = []
    n = len(nums)

    for i in range(n - 2):
        # Avoid duplicate triplets for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Set up two pointers
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                triplets.append((nums[i], nums[left], nums[right]))
                
                # Move the left pointer to the right, avoiding duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Move the right pointer to the left, avoiding duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers after finding a valid triplet
                left += 1
                right -= 1
            
            elif current_sum < 0:
                left += 1  # We need a larger sum
            else:
                right -= 1  # We need a smaller sum

    return triplets

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print(result)
