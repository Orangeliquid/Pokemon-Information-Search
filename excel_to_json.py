import pandas as pd


def excel_to_json(file_path, output_path=None):
    # Read the Excel file
    df = pd.read_excel(file_path, sheet_name=None)  # Read all sheets into a dictionary of DataFrames

    # Convert to JSON
    excel_json = {sheet: data.to_dict(orient='records') for sheet, data in df.items()}

    # Save to file if output_path is provided
    if output_path:
        with open(output_path, 'w') as json_file:
            import json
            json.dump(excel_json, json_file, indent=4)
        print(f"JSON saved to {output_path}")

    return excel_json


# Usage example
file_path = "excel_wb/National_Pokedex_Gen_9.xlsx"
output_path = "excel_wb/National_Pokedex_Gen_9.json"

json_data = excel_to_json(file_path, output_path)
