def pack_bag_perfectly(item_sizes, item_prices, max_bag_space):
    total_items = len(item_sizes)
    decision_notebook = []

    for _ in range(total_items + 1):
        blank_page = [0] * (max_bag_space + 1)
        decision_notebook.append(blank_page)

    for item_number in range(1, total_items + 1):
        current_size = item_sizes[item_number - 1]
        current_price = item_prices[item_number - 1]
        
        for space_we_have in range(1, max_bag_space + 1):
            value_if_we_leave_it = decision_notebook[item_number - 1][space_we_have]
            value_if_we_take_it = 0
            if current_size <= space_we_have:
                space_left_over = space_we_have - current_size
                value_of_remaining_space = decision_notebook[item_number - 1][space_left_over]
                
                value_if_we_take_it = current_price + value_of_remaining_space
            if value_if_we_take_it > value_if_we_leave_it:
                decision_notebook[item_number][space_we_have] = value_if_we_take_it
            else:
                decision_notebook[item_number][space_we_have] = value_if_we_leave_it
    best_possible_value = decision_notebook[total_items][max_bag_space]
    items_we_packed = []
    space_tracker = max_bag_space
    
    for item_number in range(total_items, 0, -1):
        if decision_notebook[item_number][space_tracker] != decision_notebook[item_number - 1][space_tracker]:
            actual_index = item_number - 1
            items_we_packed.append({
                "size": item_sizes[actual_index], 
                "price": item_prices[actual_index]
            })
            space_tracker -= item_sizes[actual_index]
    return best_possible_value, items_we_packed

item_sizes = [3, 8, 7, 2, 4]

item_prices = [24, 56, 49, 10, 16]

max_space = 15

final_value, packed_items = pack_bag_perfectly(item_sizes, item_prices, max_space)

print(f"🏆 Absolute Perfect Value: {final_value}")
print(f"📦 Items packd:")

for item in packed_items:
    print(f"  -> Size: {item['size']}, Prize: {item['price']}")

# Output received after runnin on terminal:
# 🏆 Absolute Perfect Value: 105
# 📦 Items packd:
#   -> Size: 7, Prize: 49
#   -> Size: 8, Prize: 56