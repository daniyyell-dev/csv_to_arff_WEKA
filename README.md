# CSV to ARFF Converter

Let assuming your dataset look like the image bellow.


![Repository Logo](https://github.com/daniyyell-dev/csv_to_arff_WEKA/raw/main/logo1.png)

## Overview

This Python script converts a CSV (Comma-Separated Values) file to ARFF (Attribute-Relation File Format), a popular data format used in machine learning. The conversion process involves transforming column names and data from a CSV file into the required ARFF format. This was inspird by [IKUZ]( https://ikuz.eu/ikuz.eu/csv2arff/)
but the site is limited to 100MB upload file at a time (Date accessed: December 21, 2023) and unfortuanalty I have arround 369MB. 

## Requirements

- Python 3.x

  `pip install -r requirements.txt`

## Usage

1. **Clone Repository:**

    ```bash
    git clone https://github.com/daniyyell-dev/csv_to_arff_WEKA.git
    cd csv_to_arff_WEKA
    ```

2. **Run the Converter Script:**

    Replace `your_dataset.csv` with the path to your CSV file.

    ```bash
    python3 csv_to_arff.py your_dataset.csv output.arff
    ```

3. **Output:**

    The script will generate an ARFF file named `OUTPUT_NAME.arff` in the same directory.

43. **Alternative:**

    Open the code and edit
    `line 13` YOUR_DATASET.csv = your dataset name. \
    `line 17` OUTPUT_NAME.arff = your desire output name 
    
    Then just run
    
    `python3 csv_to_arff.py`
