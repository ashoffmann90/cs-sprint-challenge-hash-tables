

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    # return a list called result
    result = []
    # loop through array, and loop through each array
    for array in arrays:
        for number in array:
            # check if the number is in the cache
            if number in cache:
                # move through array
                cache[number] += 1
                # if the index is the same as len
                if cache[number] == len(arrays):
                    result.append(number)
                    # print(cache[number])
                    # print(len(arrays))
            else:
                cache[number] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
