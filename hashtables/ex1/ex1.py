def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    hash_table = {}
    solution = None

    if len(weights) <= 1:
        return None

    if len(weights) == 2:
        if limit - weights[0] - weights[1] == 0:
            return (1, 0)

    for i in range(0, len(weights)):
        if not i in hash_table.values():
            hash_table[weights[i]] = i

    for weight in weights:
        if (limit - weight) in hash_table:
            if hash_table[(limit-weight)] > hash_table[weight]:
                solution = (hash_table[(limit-weight)], hash_table[weight])
            else:
                solution = (hash_table[weight], hash_table[(limit-weight)])
    return solution
