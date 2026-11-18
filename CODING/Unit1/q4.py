#Write a program to calculate the total bill after applying GST and a discount.
amount = float(input("Enter the amount: "))
gst = float(input("Enter the GST percentage: "))
discount = float(input("Enter the discount percentage: "))

gst_amount = amount * gst / 100
discount_amount = amount * discount / 100
total_bill = amount + gst_amount - discount_amount

print("Total bill:", total_bill)