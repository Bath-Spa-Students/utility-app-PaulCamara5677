print("Welcome to Sneaky_Snacks Co. vending machine!")
print("It is an honor to provide service for our customers.")
#In terms of stocks, I have decided to categorize each Snack, Drink & Meal in order to have a more
# show a  variety of products for the customers to choose from.
#The snacks will hold candies, chips, crackers and easily consumable food
#for the customer to enjoy.
items = [{"ProductID": 0,
        "ProductName": "Malteser's Candy pack",
        "ProductPrice": 1.25   
     },{
      "ProductID": 1,
      "ProductName": "SNICKERS bar",
      'ProductPrice': 3.00,
     },{"ProductId": 2,
        "ProductName": "Kit-Kat Bar 150g",
        'ProductPrice': 2.25
     },{"ProductID": 3,
        "ProductName": "Haribo Goldbears fruit juice gummies 160g",
        'ProductPrice': 9.75 
     },{"ProductID": 4,
        "ProductName": "Skittles candy pack 14x38g",
        'ProductPrice': 2.00,
     },{"ProductID": 5,
        "ProductName": "MARS bar",
        'ProductPrice': 3.25
     },{"ProductID": 6,
        "ProfuctName": "M&M's candy bag 82g",
        "ProductPrice": 2.50
     },{"ProductID": 7,
        "ProfuctName": "TWIX bar 25g",
        "ProductPrice": 2.50,
     },{"ProductID": 8,
        "ProfuctName": "Reese's Cups 46g",
        "ProductPrice": 4.00,
     },{"ProductID": 9,
        "ProfuctName": "Starburst FRUIT CHEWS 165g",
        "ProductPrice": 10.75
     },
#Unfortunately, the first attempt to full categorize each food group would prevent the code from running and result in INVALID.
# so to give a more neat presentation, i will use the comments as borderlines and seperate each food group.
     {"ProductID": 10,
        "ProfuctName": "Tiffany FINN's Creamy Cheddar chips",
        "ProductPrice": 5.00
     },{"ProductID": 11,
        "ProfuctName": "Tiffany FINN's Salt & Vinegar chips",
        "ProductPrice": 5.00
     },{"ProductID": 12,
        "ProfuctName": "Tiffany FINN's Louisiana Chili chips",
        "ProductPrice": 5.00
     },{"ProductID": 13,
        "ProfuctName": "Tiffany FINN's SCORCHIN' HOT chips",
        "ProductPrice": 5.00
     },{"ProductID": 14,
        "ProfuctName": "Doritos Cool Ranch flavor",
        "ProductPrice": 8.50
     },{"ProductID": 15,
        "ProfuctName": "Doritos Cheddar Cheese flavor",
        "ProductPrice": 8.50
     },{"ProductID": 16,
        "ProfuctName": "Doritos Spicy Nacho flavor",
        "ProductPrice": 8.50
     },{"ProductID": 17,
        "ProfuctName": "POPCORNERS White Cheddar 198.4g bag",
        "ProductPrice": 12.50
     },{"ProductID": 18,
        "ProfuctName": "POPCORNERS SWEET CHILI 198.4g bag",
        "ProductPrice": 12.50
     },{"ProductID": 19,
        "ProfuctName": "POPCORNERS Cinema Style Butter 198.4g bag",
        "ProductPrice": 12.50
     },
#The food group above is categorize as Chips, and the items below are best served with the help of an employee inside the store.
      {"ProductID": 20,
        "ProfuctName": "Chicken Leg + Thigh BBQ",
        "ProductPrice": 14.25
     },{"ProductID": 21,
        "ProfuctName": "Chicksilog breakfast meal",
        "ProductPrice": 12.50
     },{"ProductID": 22,
        "ProductName": "Chicken Skewer BBQ",
        "ProductPrice": 13.50
     },{"ProductID": 23,
        "ProductName": "Chicken Curry Rice bowl",
        "ProductPrice": 15.25,
     },{"ProductID": 24,
        "ProductName": "Turkey Bacon & Rice meal",
        "ProductPrice": 11.25
     },{"ProductID": 25,
        "ProductName": "Turkey bacon & hotdog sandwich",
        "ProductPrice": 12.25
     },{"ProductID": 26,
        "ProductName": "Sweetened Lamb slices with fried rice",
        "ProductPrice": 22.00
     },{"ProductID": 27,
        "ProductName": "Egg fried rice",
        "ProductPrice": 13.50
     },{"ProductID": 28,
        "ProductName": "Veggie fried rice",
        "ProductPrice": 12.25
     },{"ProductID": 29,
        "ProductName": "white rice(solo)",
        "ProductPrice": 6.50
     },
      
     
#For drinks, this will show the customer the varied items fit for drinking needs
#be it as necessity as Drinking Water to preferred flavored bottled soda and juice drinks.
{"ProductID": 30,
       "ProductName": "Mai Dubai bottled water 300ml",
       "ProductPrice": 1.50,
    },{"ProductID": 31,
       "ProductName": "Bottled Pepsi 500ml",
       "ProductPrice": 4.25,
    },{"ProductID": 32,
       "ProductName": "Bottled Coca-Cola 500ml",
       "ProductPrice": 4.25
    },{"ProductID": 33,
       "ProductName": "Bottle Lipton Lemon Ice Tea 800ml",
       "ProductPrice": 8.50
    },{"ProductID": 34,
       "ProductName": "Bottled Lipton Apple Ice Tea 800ml",
       "ProductPrice": 8.50
    },{"ProductID": 35,
       "ProductName": "Bottled Fanta Orange flavored drink 500ml",
       "ProductPrice": 4.25
    },{"ProducttID": 36,
       "ProductName": "Bottled Apple flavor Nestea drink 800ml",
       "ProductPrice": 8.50
    },{"ProductID": 37,
       "ProductName": "Bottled Sprite 500ml",
       "ProductPrice": 4.25
    },{"ProductID": 38,
       "ProductName": "Coca-Cola can 330ml",
        "ProductPrice": 3.75
    },{"ProductID": 39,
       "ProductName": "Pepsi can 330ml",
       "ProductPrice": 3.75
    },{"ProductID": 40,
       "ProductName": "Tissue pack x18",
       "ProductPrice": 0.00
    }]
#After the 39 items are listed, the code that is required in order for the vending machine to actually run.
#This is where the fun begins ;v;
user_balance = int(input("Please insert bill:"))
items = []
receipt = """
\t \t ProductName -- COST
"""
sum = 0
run = True
print("Sneaky_Sanacks vending machine")
print("----------The Items currently available are----------\n\n")

for i in items:
   print(f"Item: {i['ProductName']} --- Price: {i['ProductPrice']} --- Item ID: {i['ProductID']} --- Stock: {i['ProductStock']}")

#def function will define the code that interprets the code written for the vending machine
   
def vendingMachine(user_balance, items_data, run, item):
   while run:
      """for i in items:
         if balance>=i["ProductPrice"]:
            balance-=i["ProductPrice"]"""
      

      buyItem = int(
         input("\n\nEnter the item code for the item you want to buy: "))
      if buyItem < len(items_data):
         item.append(items_data[buyItem])
      else:
         print("THE PRODUCT ID IS INCORRECT!")
      moreItems = str(
         input("type any key to add more products, and type X to stop:  "))
      if moreItems.upper() == "X":
         break
      receiptValue = int(
        input(("1. Print the receipt? 2. Only print the total sum: ")))
      if receiptValue == 1:
         print(createReceipt(item, receipt))
      elif receiptValue == 2:
         print(sumItems(item))
      else:
         print("INVALID")


def sumItem(item):
   sumItems = 0
   for i in item:
      sumItems += i["itemPrice"]
   return sumItems


def createReceipt(products, reciept):
   for i in products:
      reciept += f"""
      \t{i["ProductName"]} -- {i['ProductPrice']}
      """
   reciept += f"""
      \tTotal --- {sumItem(items)}
      """
   return reciept

def stock(products):
   for i in products:
      i[("ProductStock")]-=1
      return products

# Main Code flow...
vendingMachine(user_balance, ProductPrice, run, items)