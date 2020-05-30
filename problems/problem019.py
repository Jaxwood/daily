def minimum_cost(costs: [[(int,str)]]) -> int:
    """A builder is looking to build a row of N houses that can be of K
    different colors. He has a goal of minimizing cost while ensuring that no
    two neighboring houses are of the same color. Given an N by K matrix
    where the nth row and kth column represents the cost to build the nth
    house with kth color, return the minimum cost which achieves this goal."""
    total = 0
    previous_color = None
    for house in costs:
        best = float('inf')
        last_color = None
        for (cost, color) in house:
            if min(best, cost) < best and color != previous_color:
                last_color = color
                best = cost
        previous_color = last_color
        total += best
    return total