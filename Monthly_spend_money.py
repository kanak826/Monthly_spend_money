#Inputs we need from user->
#Total rent
#Total travelling  charge daily
#Total food charge
#Total clg fee
#Total persons living in flat
#total water can charge
person=int(input("enter number of person"))
rent=int(input("enter rent of hostel per month of each person"))
total_rent=person*rent
Travelling_charge=int(input("enter your daily travelling charge"))
num_days=int(input("enter number of days you gone"))
total_Travelling_charge=Travelling_charge*num_days*person
food=int(input("enter your daily food charge"))

# clg_fee=int(input("enter your semester fee"))
water_cane=int(input("enter no. of water cane  used per month="))
charge_water_cane=int(input("enter charge of per water cane is="))
total_watercane_charge=water_cane*charge_water_cane
output=(food+total_rent+total_Travelling_charge+total_watercane_charge)//person
print("Each person Bill pay = ",output)
