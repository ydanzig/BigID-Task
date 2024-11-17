#Importing Modules
from faker import Faker
import random

#Internal Functions
#Function generates a random n-digits number
def randomDigits(n):
    lower = 10**(n-1)  #Lower number with n digits
    upper = 10**n - 1  #highest number with n digits
    return random.randint(lower, upper)

#Function returns list with fake fields [email, firstname, lastname, city, country, 9-digit personal ID number].
def mockPerson():
    faker = Faker()
    email = random.choice([faker.email(),faker.safe_email(),faker.free_email(),faker.company_email()])
    firstName = faker.first_name()
    lastName = faker.last_name()
    city = faker.city()
    country = faker.country()
    idNumber = randomDigits(9)
    L = [email,firstName,lastName,city,country,idNumber]
    return L

#Function prints n fake personal data: email, firstname, lastname, city, country, ID
def mockPersons(n):
    for i in range(n):
        L = mockPerson()
        print(*L, sep=", ")


#Main function
def main():
    num = input("How many mock personal data would you like to print?")
    mockPersons(int(num))

#Main
if __name__ == '__main__':
    main()