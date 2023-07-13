# Test case 1
optimal_change(62.13, 100)
# Output: "The optimal change for an item that costs $62.13 with an amount paid of $100.00 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

# Test case 2
optimal_change(31.51, 50)
# Output: "The optimal change for an item that costs $31.51 with an amount paid of $50.00 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."

# Test case 3: No change
optimal_change(10, 10)
# Output: "The optimal change for an item that costs $10.00 with an amount paid of $10.00 is no change."

# Test case 4: Large amount paid
optimal_change(5.25, 1000)
# Output: "The optimal change for an item that costs $5.25 with an amount paid of $1000.00 is 49 $20 bills, 1 $10 bill, 2 $1 bills, 2 quarters, and 3 dimes."

# Test case 5: Large item cost
optimal_change(1000, 2000)
# Output: "The optimal change for an item that costs $1000.00 with an amount paid of $2000.00 is 10 $100 bills."

# Test case 6: Item cost equal to the amount paid
optimal_change(25.0, 25.0)
# Output: "The optimal change for an item that costs $25.00 with an amount paid of $25.00 is no change."
