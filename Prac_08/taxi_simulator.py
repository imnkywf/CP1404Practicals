from taxi import Taxi
from silver_service_taxi import Silver_service_taxi

def main():
    bill = 0.00
    Menu = "q)uit, c)hoose taxi, d)rive"
    print("Let's drive!")
    print(Menu)
    print("Bill to date: ${}".format(bill))




    choice = str(input(">>>"))
    choice.lower()

    while choice != "q":
        if choice.lower() == "c":
            print("Taxis available: ")
            print("0 - Prius, fuel=100, odometer=0, 0km on current fare, $1.23/km"
                  "\n""1 - Limo, fuel=100, odometer=0, 0km on current fare, $2.46/km plus flagfall of $4.50"
                  "\n""2 - Hummer, fuel=200, odometer=0, 0km on current fare, $4.92/km plus flagfall of $4.50")
            car_choose = int(input("Choose car:"))
            if car_choose == 0:
                distance = int(input("Drive how far?"))
                taxi0 = Taxi("Prius 1", 100)
                taxi0.drive(distance)
                print("Bill to date: ${}".format(taxi0.get_fare()))
                bill += taxi0.get_fare()
                print(Menu)
                print("Bill to date: ${}".format(bill))
                choice = str(input(">>>"))
                choice.lower()

            elif car_choose == 1:
                distance = int(input("Drive how far?"))
                taxi1 = Silver_service_taxi("Limo", 100, 2)
                taxi1.drive(distance)
                print("Bill to date: ${}".format(taxi1.get_fare()))
                print(Menu)
                print("Bill to date: ${}".format(bill))
                choice = str(input(">>>"))
                choice.lower()

            elif car_choose == 2:
                distance = int(input("Drive how far?"))
                taxi2 = Silver_service_taxi("Limo", 100, 2)
                taxi2.drive(distance)
                print("Bill to date: ${}".format(taxi2.get_fare()))
                print(Menu)
                print("Bill to date: ${}".format(bill))
                choice = str(input(">>>"))
                choice.lower()

            else:
                print("Invalid option")
                print("Bill to date: ${})".format(bill))


main()