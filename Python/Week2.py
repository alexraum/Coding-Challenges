### Python Challenge
### Week 2

def scale(strng, k, v):

    # catch and return the empty case
    if strng == '':
        return strng

    # create an empty string
    new_str = ''

    # for each character in strng
    for char in strng:
        # if the character is not new line
        if char != '\n':
            # horizontally scale the character by k and append
            new_str += char * k
        else:
            # otherwise, append new line character
            new_str += '\n'

    # create a list of each line in the string
    line_list = new_str.split('\n')
    # create an empty string
    new_str = ''

    # for each element in the line_list
    for i in range(len(line_list)):
        # for each level of vertical scaling
        for j in range(v):
            # if it's the last line
            if ((i == (len(line_list) - 1)) & (j == (v - 1))):
                # append just the element
                new_str += line_list[i]
            else:
                # append the element and a new line character
                new_str += line_list[i] + '\n'

    # return the string
    return(new_str)

print(scale("abcd\nefgh\nijkl\nmnop", 2, 3))
