import pandas as pd
import json


def clean_column_names(columns):
    # Ensure all column names are strings, then clean them
    return [str(col).replace('\n', ' ').strip() for col in columns]


def excel_to_json_cleaned(file_path, output_path=None):
    # Read the Excel file
    df = pd.read_excel(file_path, sheet_name=None)  # Read all sheets into a dictionary of DataFrames

    # Clean column names and convert to JSON
    cleaned_data = {}
    for sheet_name, sheet_data in df.items():
        # Ensure all column names are cleaned
        sheet_data.columns = clean_column_names(sheet_data.columns)
        cleaned_data[sheet_name] = sheet_data.to_dict(orient='records')

    # Save to JSON file if output_path is provided
    if output_path:
        with open(output_path, 'w') as json_file:
            json.dump(cleaned_data, json_file, indent=4)
        print(f"Cleaned JSON saved to {output_path}")

    return cleaned_data


if __name__ == '__main__':
    file_path = "excel_wb/National_Pokedex_Gen_9.xlsx"
    output_path = "excel_wb/National_Pokedex_Gen_9_cleaned.json"
    json_data = excel_to_json_cleaned(file_path, output_path)
