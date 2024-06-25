def process_data(data):
    """
    Process the stock data to calculate daily and cumulative returns.

    Parameters:
    data (pd.DataFrame): DataFrame containing the stock data.

    Returns:
    pd.DataFrame: Processed DataFrame with additional colums for returns.
    """

    # timestamp in datetime format and set as index
    data["Date"] = data["timestamp"]
    data.set_index("Date", inplace=True)

    # calculate daily return as percentage change in close
    data["daily_return"] = data["close"].pct_change()

    # calculate cumulative return
    data["cumulative_return"] = (1 + data["daily_return"]).cumprod() - 1

    return data
