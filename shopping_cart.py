# shopping_cart.py

import datetime as dt

TAX_RATE = 0.06 # Washington, DC sales tax rate (constant)




import csv

products = [] # TODO: read from csv file

csv_file_path = "products.csv" # a relative filepath

with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    for row in reader:
        #d = dict(row)
        d = {"id": row["id"], "name": row["name"], "price": float(row["price"])}
        #print(type(d), d["name"], d["price"])
        products.append(d)






















#
# INFO CAPTURE / INPUT
#

checkout_start_at = dt.datetime.now() # current date and time, see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/datetime.md
subtotal_price = 0
selected_ids = []

while True:
    selected_id = input("Please input a product identifier: ") #> "9" (string)
    if selected_id == "DONE":
        break
    else:
        selected_ids.append(selected_id)

#
# INFO DISPLAY / OUTPUT
#

print("---------------------------------")
print("GREEN FOODS GROCERY")
print("WWW.GREEN-FOODS-GROCERY.COM")
print("---------------------------------")
print("CHECKOUT AT: " + checkout_start_at.strftime("%Y-%m-%d %I:%M %p")) # datetime formatting, see: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print("---------------------------------")

# utility function to convert float or integer to usd-formatted string (for printing)
# see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/datatypes/numbers.md
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

print("SELECTED PRODUCTS:")

for selected_id in selected_ids:
      matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
      matching_product = matching_products[0]
      subtotal_price = subtotal_price + matching_product["price"]
      print(" ... " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")

tax = subtotal_price * TAX_RATE

total_price = subtotal_price + tax

print("---------------------------------")
print("SUBTOTAL: " + to_usd(subtotal_price))
print("TAX: " + to_usd(tax))
print("TOTAL: " + to_usd(total_price))
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")
