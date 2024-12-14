def powerset_recursive(lst):
    # Base case: if list is empty, return list containing empty list
    if not lst:
        return [[]]
    
    # Take first element
    first = lst[0]
    # Get powerset of rest of the list
    rest_powerset = powerset_recursive(lst[1:])
    
    # Create new subsets by adding first element to existing subsets
    return rest_powerset + [subset + [first] for subset in rest_powerset]

# Example usage
arr = [1, 2, 3]
result = powerset_recursive(arr)
print(result)