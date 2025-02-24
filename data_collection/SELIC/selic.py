import requests
import datetime
import webbrowser
import logging

"""
This script is designed to fetch and display SELIC (Sistema Especial de Liquidação e de Custódia) data from the Central Bank of Brazil's API. 
It provides functionalities to validate dates, fetch the full time series data, fetch data within a specified date range, 
fetch the last N values, and create an HTML file to display the data in a tabular format. 

The script also includes a main function that allows user interaction through the command line, 
enabling users to choose different options for fetching and displaying the SELIC data. 
Logging is configured to capture and display errors for better debugging and user feedback.
"""

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Base URL for the Central Bank of Brazil API (SELIC)
BASE_URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs'
SERIES_CODE = '11'  # Code for the SELIC time series
FORMAT = 'json'  # Data format

# Function to validate and format dates in the Brazilian format (dd/mm/yyyy)
def validate_date(date):
    """
    Validate and format a date string in the Brazilian format (dd/mm/yyyy).

    Args:
        date (str): The date string to validate.

    Returns:
        str: The validated and formatted date.

    Raises:
        ValueError: If the date format is invalid.
    """
    try:
        return datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%d/%m/%Y')
    except ValueError:
        raise ValueError('Invalid date format! Use dd/mm/yyyy.')

# Function to fetch the full time series data in JSON format
def fetch_full_data():
    """
    Fetch the full SELIC time series data in JSON format.

    Returns:
        list: A list of dictionaries containing the SELIC data.
        None: If an error occurs during the request.
    """
    api_url = f'{BASE_URL}.{SERIES_CODE}/dados?formato={FORMAT}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return None

# Function to fetch data by date range
def fetch_data_by_range(start_date, end_date):
    """
    Fetch SELIC data for a specified date range.

    Args:
        start_date (str): The start date in the format dd/mm/yyyy.
        end_date (str): The end date in the format dd/mm/yyyy.

    Returns:
        list: A list of dictionaries containing the SELIC data.
        None: If an error occurs during the request.
    """
    start_date = validate_date(start_date)
    end_date = validate_date(end_date)
    
    api_url = f'{BASE_URL}.{SERIES_CODE}/dados?formato={FORMAT}&dataInicial={start_date}&dataFinal={end_date}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return None

# Function to fetch the last N values
def fetch_last_n_values(n):
    """
    Fetch the last N values of the SELIC time series.

    Args:
        n (int): The number of values to retrieve (between 1 and 20).

    Returns:
        list: A list of dictionaries containing the SELIC data.
        None: If an error occurs during the request or if n is out of range.
    """
    if n <= 0 or n > 20:
        logging.error("The number of values must be between 1 and 20!")
        return None
       
    api_url = f'{BASE_URL}.{SERIES_CODE}/dados/ultimos/{n}?formato={FORMAT}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return None

# Function to create an HTML file from the data
def create_html_file(data, filename='selic.html'):
    """
    Create an HTML file from the SELIC data.

    Args:
        data (list): A list of dictionaries containing the SELIC data.
        filename (str): The name of the HTML file to create.
    """
    html_content = '<!DOCTYPE html>\n'
    html_content += '<html lang="en">\n'
    html_content += '<head>\n'
    html_content += '<meta charset="UTF-8">\n'
    html_content += '<meta http-equiv="X-UA-Compatible" content="IE=edge">\n'
    html_content += '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    html_content += '<title>SELIC Data</title>\n'
    html_content += '</head>\n'
    html_content += '<body>\n'
    html_content += '<h1>SELIC Data</h1>\n'
    html_content += '<table border="1">\n'
    html_content += '<tr>\n'
    html_content += '<th>Date</th>\n'
    html_content += '<th>Value</th>\n'
    html_content += '</tr>\n'
    
    for record in data:
        html_content += '<tr>\n'
        html_content += f'<td>{record["data"]}</td>\n'
        html_content += f'<td>{record["valor"]}</td>\n'
        html_content += '</tr>\n'
    html_content += '</table>\n'
    html_content += '</body>\n'
    html_content += '</html>\n'
    with open(filename, 'w') as file:
        file.write(html_content)

# Main function for user interaction
def main():
    """
    Main function for user interaction to fetch SELIC data and create an HTML file.
    """
    print('SELIC Data Collection')
    print('Choose an option:')
    option = input('1: Fetch full data\n2: Fetch data by date range\n3: Fetch last N values\nChoose an option: ')
    
    if option == '1':
        data = fetch_full_data()
        if data:
            create_html_file(data)
            print('HTML file created successfully!')
        else:
            logging.error('Error fetching the data!')
    
    elif option == '2':
        try:
            start_date = input('Enter the start date (dd/mm/yyyy): ')
            end_date = input('Enter the end date (dd/mm/yyyy): ')
            data = fetch_data_by_range(start_date, end_date)
            if data:
                create_html_file(data)
                print('HTML file created successfully!')
            else:
                logging.error('Error fetching the data!')
        except ValueError as e:
            logging.error(f"Invalid date format: {e}")
    
    elif option == '3':
        try:
            n = int(input('Enter the number of values to retrieve (1-20): '))
            if n < 1 or n > 20:
                raise ValueError("The number of values must be between 1 and 20!")
            data = fetch_last_n_values(n)
            if data:
                create_html_file(data)
                print('HTML file created successfully!')
            else:
                logging.error('Error fetching the data!')
        except ValueError as e:
            logging.error(f"Invalid input: {e}")
    
    else:
        logging.error('Invalid option!')
    
    # Open the HTML file in the browser
    webbrowser.open('selic.html')

if __name__ == "__main__":
    main()