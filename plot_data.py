import matplotlib.pyplot as plt


def plot_data(data, symbol):
    """
    Plot stock performance with closing prices and cumulative returns.

    Parameters:
    data (pd.Dataframe): DataFrame containing processed stock data.
    symbol (str): Stock symbol.
    """

    # New figure with specified size
    plt.figure(figsize=(10, 5))

    # Plot close prices
    plt.plot(data.index, data["close"], label="Closing Price")

    # Plot cumulative returns
    plt.plot(data.index, data["cumulative_return"], label="Cumulative Return")

    # Add title and labels
    plt.title(f"Stock Performance for {symbol}")
    plt.xlabel("Date")
    plt.ylabel("Price/Return")

    # Add legend to plot
    plt.legend()

    # Show plot
    plt.show()
