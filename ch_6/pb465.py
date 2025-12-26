# Write a function cust_data() to ask user to enter their names and age to store data in customer.txt file.
def cust_data():
    name = input('Enter name -> ')
    age = int(input('enter age -> '))
    with open("hello.txt","w+") as f:
        f.write(name)
        f.write(str(age))
cust_data()