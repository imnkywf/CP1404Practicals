print("Electricity bill estimator 2.0")

tariff = int(input("Which tariff? 11 or 31:"))
daily_use_in_kWh = float(input("Enter daily use in kWh:"))
billing_days = int(input("Enter number of billing days:"))

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

if tariff == 11:
    bill_11 = TARIFF_11 * daily_use_in_kWh * billing_days
    print("Estimated bill: ${:.2f}".format(bill_11))
elif tariff == 31:
    bill_31 = TARIFF_31 * daily_use_in_kWh * billing_days
    print("Estimated bill:${:.2f}".format(bill_31))










