import matplotlib.pyplot as plt
import pandas as pd

# Example data
data = {
    'Date': ['2024-09-01', '2024-09-02', '2024-09-03', '2024-09-04'],
    'Temperature': [25, 26, 27, 28],
    'Humidity': [70, 72, 65, 68],
    'Fly_Density': [10, 15, 20, 30],
    'Damage': [5, 8, 10, 15]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot fly density and damage over time
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Fly_Density'], label='Fly Density', color='orange', marker='o')
plt.plot(df['Date'], df['Damage'], label='Damage to Olives', color='red', marker='o')
plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Fly Density and Damage to Olives Over Time')
plt.legend()
plt.grid(True)
plt.show()
