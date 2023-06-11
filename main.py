# # # This is a sample Python script.
# #
# # # Press Shift+F10 to execute it or replace it with your code.
# # # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# #
# #
# # def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
# #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# #
# #
# # # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
# #     print_hi('PyCharm')
# #
# # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
#
# import requests
# import pandas as pd
#
#
# def collect_data(symbol, interval):
#     base_url = "https://api.binance.com/api/v3/klines"
#     params = {
#         "symbol": symbol,
#         "interval": interval,
#         "limit": 1000  # Maximum limit per request
#     }
#
#     response = requests.get(base_url, params=params)
#     data = response.json()
#
#     df = pd.DataFrame(data, columns=["Open time", "Open", "High", "Low", "Close", "Volume", "Close time",
#                                      "Quote asset volume", "Number of trades", "Taker buy base asset volume",
#                                      "Taker buy quote asset volume", "Ignore"])
#
#     # Convert timestamp to datetime
#     df["Open time"] = pd.to_datetime(df["Open time"], unit="ms")
#     df["Close time"] = pd.to_datetime(df["Close time"], unit="ms")
#
#     # Save data to CSV
#     filename = f"{symbol}_{interval}.csv"
#     df.to_csv(filename, index=False)
#     print(f"Data saved to {filename}")
#
#
# # Example usage
# symbol = "ETHUSDT"
# interval = "4d"
# collect_data(symbol, interval)