# Pokemon Information Search

[GitHub Repository](https://github.com/Orangeliquid/pokemon-information-search)


## Overview
This Python script utilizes the openpyxl library to load data from an Excel workbook containing a Pokemon Pokedex. The user can input a Pokemon name, and the script will retrieve and display the corresponding data from the workbook.

## Features
- Loads an Excel workbook and selects a specified sheet.
- Finds a Pokemon's data in the sheet based on user input.
- Prints the fetched Pokemon data excluding the "Total" column.

## Prerequisites
- Python 3.x
- openpyxl library (install using pip install openpyxl)

## Usage
1. Clone the repository to your local machine.
  ```bash
  git clone https://github.com/Orangeliquid/pokemon-information-search.git
  ```
2. Ensure you have Python installed.
3. Install the required library using pip install openpyxl.
  ```bash
    pip install openpyxl
  ```
4. Run the script: python pokemon_data_fetcher.py.
  ```bash
    python pokemon_data_fetcher.py
  ```
5. Enter a valid Pokemon name when prompted.

## Structure
- `pokemon_data_fetcher.py`: The main script containing the Pokemon data fetching functionality.
- `excel_wb/National_Pokedex_Gen_9.xlsx`: Excel workbook with Pokemon data.

## Contributing
Feel free to contribute to the project by opening issues or pull requests.

## Pokemon Work Book Source
Shout out to Andrew Berrodin for the in-depth Google Sheet!
Link to sheet: https://docs.google.com/spreadsheets/d/19Me94k6YLz1_3EO_PwTPsAI9KmdFTh07/edit#gid=353590428

## License
This project is licensed under the [MIT License](LICENSE.txt).
