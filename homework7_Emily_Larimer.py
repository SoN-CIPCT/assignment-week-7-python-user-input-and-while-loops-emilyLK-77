# You are in charge of making sure all pizza orders are made on time at your restaurant. Perform the following to check that all orders have been fulfilled.

# Make a list called pizza_orders and populate it with names of pizzas that have been ordered.
pizza_orders = ['hawiian', 'cheese', 'pesto', 'mushroom']
# Make an empty list called finished_pizzas.
finished_pizzas = []
# Loop through the list of pizza orders and print a message for each order, saying “Your pizza pie is finished!”.
# After the pizza is made and a message has been printed for a pizza order, move that pizza to the list finished_pizzas.
# After all of the pizzas have been made, print a message “The pizza {name} was made.” for each finished pizza, replacing {name} with the pizza’s name.
while  pizza_orders:
    pizza = pizza_orders.pop()
    print(f"{pizza}: Your pizza pie is finished!")
    finished_pizzas.append(pizza) 
for pizza in finished_pizzas:
      print(f"Your {pizza} pizza was made.")
