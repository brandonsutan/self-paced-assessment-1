def optimal_change(item_cost, amount_paid):
    denominations = {
        'bill': [100, 50, 20, 10, 5, 1],
        'quarter': 0.25,
        'dime': 0.1,
        'penny': 0.01
    }

    change = amount_paid - item_cost
    change_str = f"The optimal change for an item that costs ${item_cost:.2f} with an amount paid of ${amount_paid:.2f} is "

    for denom_name, denom_value in denominations.items():
        if denom_name == 'bill':
            for bill in denom_value:
                bill_count = int(change // bill)
                if bill_count > 0:
                    change_str += f"{bill_count} ${bill} bill{'s' if bill_count > 1 else ''}, "
                    change -= bill * bill_count
        else:
            if denom_value <= change:
                denom_count = int(change // denom_value)
                change_str += f"{denom_count} {denom_name}{'s' if denom_count > 1 else ''}, "
                change -= denom_value * denom_count

    change_str = change_str.rstrip(", ") + '.'
    print(change_str)
