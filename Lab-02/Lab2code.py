#Course Marks with a List
programming_ds = float(input("Enter your Programming for DS Marks:"))
data_visualization = float(input("Enter your Data Visualization Marks:"))
data_processing = float(input("Enter your Data Processing Marks:"))
intro_to_ds = float(input("Enter your Introduction to DS Marks:"))

marks = [programming_ds, data_visualization, data_processing, intro_to_ds]


total_grade = 0
for mark in marks:
    total_grade += mark

avg_grade = total_grade / len(marks)
print("Average Grade:", avg_grade)
high_grade = max(marks)
print("Highest Grade:", high_grade)
low_grade = min(marks)
print("Lowest Grade:", low_grade)

if marks[0] >= 50 and marks[1] >= 50 and marks[2] >= 50 and marks[3] >= 50:
    print("You have passed the course.")
else:
    print("You have failed the course.")

    count = 0
    for mark in marks:
        if mark < 50:
            count += 1
    print("You have failed in", count, "subjects.")

    '''Weekend Temperature with a Tuple:Create a tuple containing the temperatures recorded on Saturday and Sunday for three different times of the day. 
    Use a for loop to display each temperature. Then calculate the highest and lowest temperature in the tuple.'''
    weekend_temperatures = (25, 28, 30, 22, 26, 29)  # Example temperatures for Saturday and Sunday at three times each
    print("Weekend Temperatures:")
    for temp in weekend_temperatures:
        print(temp)
    print("Highest Temperature:", max(weekend_temperatures))
    print("Lowest Temperature:", min(weekend_temperatures))

    '''Word Analyzer :Ask the user to enter a word or short sentence. 
    Display the number of characters, the number of vowels (a, e, i, o, u), and the number of spaces. Use a for loop to examine each character.'''
    word = input("Enter a word or short sentence: ")
    char_count = len(word)
    vowel_count = 0
    space_count = 0
    vowels = "aeiouAEIOU"
    for char in word:
        if char in vowels:
            vowel_count += 1
        if char == " ":
            space_count += 1
    print("Number of characters:", char_count)
    print("Number of vowels:", vowel_count)
    print("Number of spaces:", space_count)

    '''Grade Calculator Function : Write a function called calculate_grade(marks) that receives a list of marks. The function should calculate the average and return a grade using these rules: 
    A for average ≥ 80, B for ≥ 70, C for ≥ 60, D for ≥ 50, and F for below 50. Call the function using a list of 5 marks.'''
    def calculate_grade(marks):
        average = sum(marks) / len(marks)
        if average >= 80:
            return 'A'
        elif average >= 70:
            return 'B'
        elif average >= 60:
            return 'C'
        elif average >= 50:
            return 'D'
        else:
            return 'F'
    '''Shopping Cart Processor: Create a list of dictionaries representing 4 products. Each dictionary should contain product name, price, and quantity. 
    Use a for loop to calculate the total cost of the cart. Then write a function called apply_discount(total) that returns the final price after a 10% discount when the total is greater than or equal to 2,000; otherwise, no discount is applied.'''
    shopping_cart = [
        {"name": "Laptop", "price": 1000, "quantity": 1},
        {"name": "Smartphone", "price": 800, "quantity": 2},
        {"name": "Headphones", "price": 150, "quantity": 3},
        {"name": "Keyboard", "price": 100, "quantity": 1}
    ]
    total_cost = 0
    for item in shopping_cart:
        total_cost += item["price"] * item["quantity"]
    print("Total cost of the cart:", total_cost)

    def apply_discount(total):
        if total >= 2000:
            return total - (total * 0.1)
        else:
            return total
        
    '''Countdown: Write a program using a while loop that asks the user for a number and prints a countdown from that number to zero'''
    number = int(input("Enter a number: "))
    while number >= 0:
        print(number)
        number -= 1

    #Problem 08
    # Sample inventory data: list of dictionaries containing product details
inventory = [
    {"name": "Laptop", "price": 1200.00, "quantity": 5},
    {"name": "Mouse", "price": 25.00, "quantity": 40},
    {"name": "Monitor", "price": 300.00, "quantity": 12},
    {"name": "Keyboard", "price": 75.00, "quantity": 15},
    {"name": "Headphones", "price": 150.00, "quantity": 8},
]

total_inventory_value = 0
highest_product = None
highest_line_total = 0

print("=" * 45)
print(f"{'Product':<15} {'Price':<10} {'Qty':<6} {'Line Total'}")
print("=" * 45)


for item in inventory:
    line_total = item["price"] * item["quantity"]
    item["line_total"] = line_total
    
    total_inventory_value += line_total
    
   
    if line_total > highest_line_total:
        highest_line_total = line_total
        highest_product = item["name"]
        
    print(f"{item['name']:<15} ${item['price']:<9.2f} {item['quantity']:<6} ${line_total:,.2f}")


print("=" * 45)
print(f"Total Inventory Value : ${total_inventory_value:,.2f}")
print(f"Highest Value Item    : {highest_product} (${highest_line_total:,.2f})")
print("=" * 45)