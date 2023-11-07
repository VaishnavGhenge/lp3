def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    for item in items:
        item['value_to_weight'] = item['value'] / item['weight']

    # Sort items in descending order of value-to-weight ratio
    items.sort(key=lambda x: x['value_to_weight'], reverse=True)

    total_value = 0.0  # Initialize the total value in the knapsack
    knapsack = []  # Initialize the knapsack as an empty list

    for item in items:
        if capacity >= item['weight']:
            # If the entire item can fit, add it to the knapsack
            knapsack.append(item)
            total_value += item['value']
            capacity -= item['weight']
        else:
            # If only a fraction of the item can fit, add a fraction to the knapsack
            fraction = capacity / item['weight']
            knapsack.append({'item': item['item'], 'weight': capacity, 'value': item['value'] * fraction})
            total_value += item['value'] * fraction
            break  # The knapsack is now full

    return total_value, knapsack

if __name__ == '__main__':
    # Example usage:
    items = [
        {'item': 'item1', 'weight': 10, 'value': 60},
        {'item': 'item2', 'weight': 20, 'value': 100},
        {'item': 'item3', 'weight': 30, 'value': 120},
    ]
    knapsack_capacity = 50

    max_value, selected_items = fractional_knapsack(items, knapsack_capacity)

    print("Maximum value:", max_value)
    print("Selected items:")
    for item in selected_items:
        print(f"Item: {item['item']}, Weight: {item['weight']}, Value: {item['value']}")
