import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("electricity.csv")

df["period"] = pd.to_datetime(df["period"])

print("Loaded electricity dataset with", len(df), "rows")
print(df.columns)
print(df.head())

plt.figure(figsize=(8, 5))
plt.plot(df["period"], df["nswprice"], label="NSW Price")
plt.plot(df["period"], df["vicprice"], label="VIC Price")
plt.title("Electricity Prices in NSW vs Victoria")
plt.xlabel("Time Period")
plt.ylabel("Electricity Price")
plt.legend()
plt.grid(True)
plt.savefig("electricity_prices.png")
plt.show()
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(df["period"], df["nswdemand"], label="NSW Demand", s=10)
plt.scatter(df["period"], df["vicdemand"], label="VIC Demand", s=10)
plt.title("Electricity Demand Over Time")
plt.xlabel("Time Period")
plt.ylabel("Electricity Demand")
plt.legend()
plt.savefig("electricity_demand.png")
plt.show()
plt.close()


