def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    result_with_dupes = []
    hash_result = {}

    for num in a:
        hash_table[num] = True

    for key in hash_table.keys():
        if (key * -1) in hash_table:
            result_with_dupes.append(abs(key))

    for num in result_with_dupes:
        if num != 0:
            if not num in hash_result:
                hash_result[num] = 0
            hash_result[num] += 1

    result = list(hash_result.keys())

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
