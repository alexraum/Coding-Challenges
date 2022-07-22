def number(bus_stops):
    
    # initialize a counter
    count = 0
    
    # for each sub array in the array
    for stop in bus_stops:
    
        # add element 0 to the count
        count += stop[0]
        # subtract element 1 from the count
        count -= stop[1]
        
    # return the count
    return count
