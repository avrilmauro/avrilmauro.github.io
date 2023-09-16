import pandas as pd
from utils import num_filter


def main():
    # S&P Industries by Ticker and Company
    industry_df = pd.read_csv('sp500_Industries.csv')
    industry_df = industry_df.rename(columns={'Symbol': 'Ticker'})

    # S&P Individual Stock Prices
    price_df = pd.read_csv('sp500_Price.csv').drop('Unnamed: 0', axis=1)
    price_df = num_filter(price_df, 'Date', ['2010-01-01', '2022-12-31'])
    price_df = price_df[['Ticker', 'Date', 'Volume', 'Adj Close']]

    # SIZE = # of stocks
    count_df = pd.DataFrame(industry_df.groupby('Sector').count().drop('Name', axis=1)).reset_index()
    count_df.columns = ['Sector', 'Count']

    # Y AXIS = close
    price2020_df = num_filter(price_df, 'Date', ['2022-01-01', '2022-12-31'])
    cdf = pd.merge(industry_df, price2020_df, on=['Ticker'])
    close_df = pd.DataFrame(cdf.groupby('Sector').mean(numeric_only=True)['Adj Close']).reset_index()
    close_df.columns = ['Sector', 'Close']

    rows = []
    for stock in list(set(price_df.Ticker.values)):
        df = price_df[price_df.Ticker == stock]['Adj Close']
        growth = ((df.iloc[-1] - df.iloc[0]) / df.iloc[0]) * 100
        row = stock, round(growth, 2)
        rows.append(row)

    growth_df = pd.DataFrame(rows, columns=['Ticker', 'Growth (%)'])
    growth_df = pd.merge(industry_df, growth_df, on=['Ticker'])
    growth_df = growth_df.groupby('Sector').mean(numeric_only=True)

    df = pd.merge(pd.merge(growth_df, close_df, on='Sector'), count_df, on='Sector')

    df.to_csv('sp500_growth.csv')


if __name__ == '__main__':
    main()
