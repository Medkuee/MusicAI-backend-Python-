import numpy as np
import pandas as pd

# Load dataset
data = pd.read_csv('csv-classical/1759.csv')

# Get user input for first three notes
note1 = int(input("Enter first note (1-88): "))
note2 = int(input("Enter second note (1-88): "))
note3 = int(input("Enter third note (1-88): "))

# Filter dataset for notes matching user input
notes = data[data['note'].isin([note1, note2, note3])]

# Randomly select one row from filtered dataset
row = np.random.choice(notes.index)

# Get start_time, end_time, note, and note_value from selected row
start_time = data.at[row, 'start_time']
end_time = data.at[row, 'end_time']
note = data.at[row, 'note']
note_value = data.at[row, 'note_value']

# Print results
print(f"Generated music based on {note1}, {note2}, {note3}:")
print(f"Start time: {start_time}")
print(f"End time: {end_time}")
print(f"Note: {note}")
print(f"Note value: {note_value}")