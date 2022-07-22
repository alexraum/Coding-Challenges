### Python Challenge
### Week 1

# positive sum accepts a list and returns the sum of all positive elements within the list
def positive_sum(arr):
    # use a list comprehension to create a list of positive elements
    # sum the list and return to the caller
    return(sum([num for num in arr if num >= 0]))