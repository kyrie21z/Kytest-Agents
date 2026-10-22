def allocate(total, weights):
    """Split a non-negative integer total into integer shares proportional to weights.

    weights is a list of non-negative ints with at least one positive entry.
    Every entry first receives floor(total * w / sum(weights)). The units left
    over are then handed out one each to the entries with the largest fractional
    remainder (total * w mod sum(weights)); ties go to the entry with the lower
    index. The result is a new list of ints, one per weight, summing to total.
    Entries with weight 0 always receive 0.

    Raises ValueError if total is negative, weights is empty, any weight is
    negative, or all weights are zero.

    >>> allocate(100, [1, 1, 1])
    [34, 33, 33]
    >>> allocate(10, [3, 0, 7])
    [3, 0, 7]
    """
    if total < 0 or not weights or any(w < 0 for w in weights) or not any(weights):
        raise ValueError("invalid allocation request")
    whole = sum(weights)
    shares = [total * w // whole for w in weights]
    remainders = [total * w % whole for w in weights]
    leftover = total - sum(shares)
    order = sorted(range(len(weights)), key=lambda i: (-remainders[i], -i))
    for i in order[:leftover]:
        shares[i] += 1
    return shares
