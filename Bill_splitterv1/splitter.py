#SIMPLE BILL SPLITTER FOR TAX AND TIP AND TOTAL AMOUNT CALCULATOR

#Ask the user for the subtotal of a meal, calculate a 12% tax
#and a 15% tip, and output the total bill.
def total():

    subtotal = subtotal_float(input("Enter Subtotal of bill "))
    tip_rate = subtotal * 0.15 #15% in decimals is 0.15
    tax_rate = subtotal * 0.12 #12% in decimals is 0.12
    tip_amount = tip_rate #tip rate results
    tax_amount = tax_rate #tax rate results
    total_bill = subtotal + tip_amount + tax_amount #add them all together for the total

#printing the output
    print_tax(tax_amount)
    print_tip(tip_amount)
    print_total(total_bill)


######### PRINT FUNCTIONS ##########
def print_tax(tax_amount):
    print(f"Tax: ${tax_amount:.2f}")

def print_tip(tip_amount):
    print(f"Tip: ${tip_amount:.2f}")

def print_total(total_bill):
    print(f"The total bill amount is ${total_bill:.2f}")

######### PRINT FUNCTIONS ##########

####### REMOVING THE DOLLAR SIGN AUTOMATICALLY IF INPUTED ####
def subtotal_float(s):
    s = float(s.lstrip("$"))
    return s

total()
