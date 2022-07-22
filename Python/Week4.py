def mxdiflg(a1, a2):
    
    # handle edge cases
    if (len(a1) == 0 or len(a2) == 0):
        return -1
    
    # find extrema in each list to avoid pairwise checks (quadratic time)
    
    """
    # define a1 extrema to be the first element
    min_a1 = max_a1 = len(a1[0])
    # define a2 extrema to be the first element
    min_a2 = max_a2 = len(a2[0])
    
    # check remaining elements of a1
    for i in range(1, len(a1)):
        # redefine max based on comparisons to current max
        max_a1 = len(a1[i]) if len(a1[i]) > max_a1 else max_a1
        # redefine min based on comparisons to current min
        min_a1 = len(a1[i]) if len(a1[i]) < min_a1 else min_a1
    
    # check remaining elements of a2
    for i in range(1, len(a2)):
        # redefine max based on comparisons to current max
        max_a2 = len(a2[i]) if len(a2[i]) > max_a2 else max_a2
        # redefine min based on comparisons to current min 
        min_a2 = len(a2[i]) if len(a2[i]) < min_a2 else min_a2
        
    # return the maximum of the two differences
    return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1))
    """
    
    # create lists of string lengths for both input lists
    str_len_a1 = [len(string) for string in a1]
    str_len_a2 = [len(string) for string in a2]
    
    # calculate both possible absolute differences in extrema between lists
    abs_diff1 = abs(max(str_len_a1) - min(str_len_a2))
    abs_diff2 = abs(max(str_len_a2) - min(str_len_a1))

    # return the large of these two differences
    return max(abs_diff1, abs_diff2)
