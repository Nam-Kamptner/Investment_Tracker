# Import functions from other files
from fetch_data import fetch_stock_data
from process_data import process_data
from plot_data import plot_data


def main():

    # Prompt user to enter polygon.io API key
    api_key = input("Enter polygon.io API key: ")

    # Prompt user to enter stock symbols separated by commas
    symbols = input(
        "Enter stock symbols separated by commas (e.g. AAPL, NVDA): "
    ).split(",")

    # Looping through each stock symbol
    for symbol in symbols:
        # Remove whitespaces and convert to uppercase
        symbol = symbol.strip().upper()

        # Fetch stock data for current symbol
        data = fetch_stock_data(symbol, api_key)

        # Check if data is successfully fetched. Then process and plot data.
        if data is not None:
            data = process_data(data)
            plot_data(data, symbol)
        else:
            print(f"Failed to retrieve data for {symbol}.")


if __name__ == "__main__":
    main()
