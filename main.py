from openpyxl import load_workbook


def load_workbook_and_sheet(file_path, sheet_name):
    try:
        workbook = load_workbook(file_path)
        sheet = workbook[sheet_name]
        return workbook, sheet
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit()


def find_pokemon(sheet, inquiry_column, pokemon_name):
    pokemon_name_column = inquiry_column

    for row in sheet.iter_rows(min_row=2, max_col=sheet.max_column, max_row=sheet.max_row, values_only=True):
        if row[1] == pokemon_name:  # Adjust the index to 1
            header_row = sheet[1]
            min_length = min(len(header_row), len(row))
            pokemon_dict = {header_row[i].value: row[i] for i in range(min_length)}
            return pokemon_dict

    print(f'Pokemon "{pokemon_name}" is not found in column {pokemon_name_column} - please check spelling!')
    return None


def print_pokemon_data(pokemon_data):
    if pokemon_data is not None:
        print("Pokemon Data:")
        for key, value in pokemon_data.items():
            if value is not None and key != "Total":
                print(f'{key}: {value}')


def main():
    active_wb = "excel_wb/National_Pokedex_Gen_9.xlsx"
    sheet_name = "Pokedex"
    inquiry_column = 2

    pokemon_inquiry = input("Enter Pokemon name: ").title()
    if not pokemon_inquiry.isalnum():
        print("Invalid input. Please enter a valid Pokemon name.")
        exit()

    workbook, sheet = load_workbook_and_sheet(active_wb, sheet_name)
    pokemon_data = find_pokemon(sheet, inquiry_column, pokemon_inquiry)
    print_pokemon_data(pokemon_data)


if __name__ == "__main__":
    main()
