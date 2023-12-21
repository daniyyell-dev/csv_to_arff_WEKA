
import pandas as pd
from scipy.io import arff
from tqdm import tqdm

# Load the CSV file
csv_file_path = 'YOUR_DATASET.csv'  # Replace with the actual path to your CSV file, please makes sure it has correct label e.g BENIGN,MALWARE
df = pd.read_csv(csv_file_path)

# Convert the DataFrame to an ARFF format
arff_file_path = 'OUTPUT_NAME.arff'  # Replace with the desired output name.

with open(arff_file_path, 'w') as arff_file:
    arff_file.write('@RELATION Dataset\n\n')
    for i, column in enumerate(df.columns):
        if column == 'label':
            arff_file.write('@ATTRIBUTE {} {}\n'.format(column.replace(' ', '_'), '{BENIGN,MALWARE}'))
        else:
            arff_file.write('@ATTRIBUTE {} {}\n'.format('_'.join(column.split()), 'REAL' if i != len(df.columns) - 1 else '{BENIGN,MALWARE}'))

    arff_file.write('\n@DATA\n')
    for index, row in df.iterrows():
        arff_file.write(','.join(map(str, row)) + '\n')

  # Add tqdm to show a progress bar
    for index, row in tqdm(df.iterrows(), total=len(df), desc="Converting to ARFF...", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'):
        arff_file.write(','.join(map(str, row)) + '\n')

