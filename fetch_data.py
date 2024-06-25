import requests
import pandas as pd


def fetch_stock_data(symbol, api_key):
    """
    Fetch stock data for a given symbol polygon.io API.

    Parameters:
    symbol (str): The stock ticker symbol (e.g. 'NVDA' for NVIDIA).
    api_key (str): The polygon.io API Key.

    Returns:
    pd.dataFrame: DataFrame containing stock data or None if an error occurs.
    """
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/2022-01-10/2023-01-09?adjusted=true&sort=asc&limit=120&apiKey={api_key}"

    try:
        # Send request to polygon.io API
        response = requests.get(url)
        response.raise_for_status()  # raise error for bad status codes

        # parse the JSON response into a dictionary
        data = response.json()

        # check if 'results' key is in data
        if "results" not in data:
            print(f"No results found for: {symbol}")
            return None

        # Convert the 'results' list into a DataFrame (rows and columns)
        df = pd.DataFrame(data["results"])

        # rename columns for readability
        df = df.rename(
            columns={
                "v": "volume",
                "vw": "volume_weighted",
                "o": "open",
                "c": "close",
                "h": "high",
                "l": "low",
                "t": "timestamp",
                "n": "number_transactions",
            }
        )

        # Convert timestamp from milliseconds to datetime format
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

        # return relevant columns
        return df[["volume", "open", "close", "high", "low", "timestamp"]]

    except requests.exceptions.HTTPError as http_error:
        print(f"HTTP Error: {http_error}")
    except Exception as error:
        print(f"Other error: {error}")

    return None
