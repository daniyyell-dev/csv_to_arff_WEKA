import pandas as pd

# Load the binary dataset
file_path = 'DATASET.csv'
df_binary = pd.read_csv(file_path)

# Map 1 to 'MALWARE' and 0 to 'BENIGN' in the LABEL column
df_binary['LABEL'] = df_binary['LABEL'].map({1: 'MALWARE', 0: 'BENIGN'})

# Save the updated dataset
output_file_path = 'OUTPUT.csv'
df_binary.to_csv(output_file_path, index=False)
