import heapq


def fractional_knapsack(capacity, values_and_weights):
    order = [(-v / w, w) for v, w in values_and_weights]
    heapq.heapify(order)

    acc = 0
    while order and capacity:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w, capacity)
        acc -= v_per_w * can_take
        capacity -= can_take

    return acc


def main():
    n, capacity = map(int, input().split())
    values_and_weights = list(tuple(map(int, input().split())) for _ in range(n))
    assert len(values_and_weights) == n
    cost = fractional_knapsack(capacity, values_and_weights)
    print("{:.3f}".format(cost))


def test():
    assert fractional_knapsack(0, [(60, 20)]) == 0.0
    assert fractional_knapsack(25, [(60, 20)]) == 60.0
    assert fractional_knapsack(25, [(60, 20), (0, 100)]) == 60.0
    assert fractional_knapsack(25, [(60, 20), (50, 50)]) == 60.0 + 5.0

    assert fractional_knapsack(50, [(60,20), (100, 50), (120, 30)]) == 180.0

if __name__ == "__main__":
    main()
    # test()