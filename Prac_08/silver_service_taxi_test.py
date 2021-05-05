from silver_service_taxi import Silver_service_taxi

def main():
    taxi = Silver_service_taxi("lambo", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())




main()