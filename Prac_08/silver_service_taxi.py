from taxi import Taxi


class Silver_service_taxi(Taxi):

    price_per_km = 1.23
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        return "${} plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        fare = round(self.price_per_km * self.current_fare_distance +self.flagfall, 1)
        return fare

