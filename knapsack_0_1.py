def knapsack_0_1(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            item = items[i - 1]
            if item['weight'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item['weight']] + item['value'])
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1]['weight']

    return max_value, selected_items

if __name__ == '__main__':
    # Example usage:
    items = [
        {'item': 'item1', 'weight': 10, 'value': 60},
        {'item': 'item2', 'weight': 20, 'value': 100},
        {'item': 'item3', 'weight': 30, 'value': 120},
    ]
    knapsack_capacity = 50

    max_value, selected_items = knapsack_0_1(items, knapsack_capacity)

    print("Maximum value:", max_value)
    print("Selected items:")
    for item in selected_items:
        print(f"Item: {item['item']}, Weight: {item['weight']}, Value: {item['value']}")
