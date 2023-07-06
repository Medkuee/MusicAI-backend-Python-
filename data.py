import numpy as np
import matplotlib.pyplot as plt
import csv

x = np.arange(0, 10*np.pi, 0.1)
y = np.cos(x)
y_n = list(y)
y_noise = np.array([])
for i in range(len(y_n)):
    y_rand = np.random.uniform(y_n[i]-0.2,y_n[i]+0.2, size=None)
    y_noise = np.append(y_noise, y_rand)

# print(len(y_))


# plt.plot(x, y_noise, color = "red")
# plt.plot(x, y, color = "green")
# plt.show()



data = [y_noise, y]
data = zip(*data)

csv_file = 'test.csv'

# Open the file in write mode and create a CSV writer object
with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)

    # Write the data to the CSV file
    writer.writerows(data)

print("Data has been written to", csv_file)