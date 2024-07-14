import os
import pandas as pd

# Define the directory
data_dir = r'C:\\Users\\bolts\\TennisShots\\data\\'

# Initialize an empty list to store the data
data = []

# Loop through each folder in the data directory
for label in ['serve', 'forehand', 'backhand']:
    folder_path = os.path.join(data_dir, label)
    
    # Ensure the folder exists
    if os.path.exists(folder_path):
        # Loop through each file in the folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.jpg'):
                # Add the image name and label to the data list
                data.append([file_name, label])

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['id', 'label'])

# Export the DataFrame to a CSV file
csv_path = os.path.join(data_dir, 'tennis_shots.csv')
df.to_csv(csv_path, index=False)

print(f"CSV file has been created at: {csv_path}")
