from openpyxl import load_workbook

active_wb = "excel_wb/National_Pokedex_Gen_9.xlsx"
sheet_name = "Pokedex"
inquiry_column = 2

# The goal is to take an input of a Pokemon and fetch the row data
# then take that data and place it into a dict


def find_pokemon(pokemon_name):
    # load workbook
    workbook = load_workbook(active_wb)

    # sheet selection
    sheet = workbook[sheet_name]

    # Pokemon name column
    pokemon_name_column = inquiry_column

    # Iterate through the rows in specific column
    for row in sheet.iter_rows(min_row=2, max_col=sheet.max_column, max_row=sheet.max_row, values_only=True):
        if row[1] == pokemon_name:  # Adjust the index to 1
            # If the Pokemon is found, create a dictionary with all column names and values
            header_row = sheet[1]

            # Ensure the range is within the length of both header_row and row
            min_length = min(len(header_row), len(row))

            # Create a dictionary with all column names and values
            pokemon_dict = {header_row[i].value: row[i] for i in range(min_length)}

            return pokemon_dict

    print(f'Pokemon "{pokemon_name}" is not found in column {pokemon_name_column} - please check spelling!')
    return None


pokemon_inquiry = input("Enter Pokemon name: ").title()

pokemon_data = find_pokemon(pokemon_inquiry)
if pokemon_data is not None:
    print("Pokemon Data: ")
    for key, value in pokemon_data.items():
        if value is not None and key != "Total":
            print(f'{key}: {value}')

