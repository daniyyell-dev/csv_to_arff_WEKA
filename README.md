# csv_to_arff_WEKA

## Introduction

This Python script converts a CSV file to the ARFF format. The conversion is intended for use with the Weka machine learning toolkit, which commonly uses ARFF files.

## Prerequisites

Make sure you have the required libraries installed. You can install them using:

```bash
pip install pandas scipy

Usage
1. Clone the Repository

Clone the repository to your local machine:

bash

git clone https://github.com/your-username/csv-to-arff-converter.git
cd csv-to-arff-converter

2. Prepare your CSV file

Place your CSV file in the same directory as the script. Ensure that the CSV file follows the required format.
3. Run the Script

Execute the script by running:

bash

python csv_to_arff_converter.py

4. Output

The script will generate an ARFF file named "Dataset-me-WEKA.arff" in the same directory as the CSV file.
Configuration

You can customize the script by modifying the following variables:

    csv_file_path: Path to your CSV file.
    arff_file_path: Desired path for the output ARFF file.

Customization

If you need to customize the attribute names or data types, you can modify the script accordingly. Ensure that your changes are compatible with the Weka ARFF format.
