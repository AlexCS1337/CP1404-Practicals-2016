print("Electricity bill estimator")

cents = float(input("Enter cents per kWh:"))
dailyUse = float(input("Enter daily use in kWh:"))
numBillingDays = float(input("Enter number of billing days:"))

result = cents + dailyUse + numBillingDays

print("Estimated bill:", result)


TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")

tariff = input("Which tariff? 11 or 31:")
if tariff == "11":
    dailyUse = float(input("Enter daily use in kWh:"))
    numBillingDays = float(input("Enter number of billing days:"))


elif tariff == "31":
    dailyUse = float(input("Enter daily use in kWh:"))
    numBillingDays = float(input("Enter number of billing days:"))

print("Estimated bill:")