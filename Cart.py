clothes = {}
Price ={}
total ={}

while True:
    clothes = input("enter the item to buy(q to quit): ")
    if clothes.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {clothes}: R"))
        clothes.append(clothes)
        price.append(price)
print("---My Cart---")
for clothes in clothes:
    print (clothes, end=" ")
    
for price in price:
    total += price
print()  
print("Total: R", total)
        
