"""
Avril Mauro, Katelyn Donn, Monisha Kapadia, Alyssa Benjamin, & Jaclyn Xu
DS 3500 Final Project
S&P 500 Stock Analysis
April 19th, 2023

This file deploys a dashboard for the analysis of stocks in the S&P 500
"""

from dash import Dash, dcc, html, Input, Output
from utils import num_filter
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import charts

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# S&P Industries by Ticker and Company
industry_df = pd.read_csv('sp500_Industries.csv').rename(columns={'Symbol': 'Ticker'})
sector_list = list(set(industry_df['Sector'].values)) + ['All']

# S&P Individual Stock Prices
price_df = pd.read_csv('sp500_Price.csv').drop('Unnamed: 0', axis=1)

# S&P Individual Stock Prices and their industry (sector)
close_df = pd.merge(price_df, industry_df, on='Ticker')

# S&P 500 Index Price (2010 to 2020)
index_df = pd.read_csv('spIndex_Price.csv')
index_df = num_filter(index_df, 'Date', ['2010-01-01', '2022-12-31'])

# LAYOUT
app.layout = dbc.Container([
    # GRAPH: LINE CHART
    dbc.Row([
        html.H1('S&P 500 Stock Analysis', style={'text-align': 'center', 'marginTop': 25}),
        html.Br(),
    ]),
    dbc.Row([
        dbc.Col(html.Div([
            dcc.Graph(id='BubbleSectors',
                      figure=charts.display_bubble_chart(),
                      style={"marginTop": 25}),
        ]), width=9),
        dbc.Col(html.Div([
            html.H4('Bubble Chart'),
            html.P('The S&P500 is a collection of stocks divided among 11 industry sectors'),
            html.P('bubble size: number of stocks which are in a specific industry sector'),
            html.P('y-axis: aggregated average closing price of all stocks in one sector during 2020'),
            html.P('x-axis: percent growth in closing price (aggregated average of 2020 vs. 2010)'),
        ], style={"marginTop": 50}, ), width=3),
    ]),
    dbc.Row([
        html.H3('Your Turn to Explore!', style={'text-align': 'center'}),
        html.H4('Select Specific Years and Industries', style={'text-align': 'center'}),
        html.Br(),
        html.Br(),
    ]),
    dbc.Row([
        dbc.Col([html.P('Start & End Year', style={'text-align': 'right', 'marginLeft': '150px'})]),
        dbc.Col([
            dcc.Input(id='Year0', type='number', placeholder=2010, min=2010, max=2022,
                      style={'width': 110}),
            dcc.Input(id='Year1', type='number', placeholder=2020, min=2010, max=2022,
                      style={'width': 110, 'marginLeft': '10px'}, debounce=True)
        ], width=3),
        dbc.Col([
            html.P('Industry', style={'text-align': 'left'}),
        ], width=1),
        dbc.Col([
            dcc.Dropdown(sector_list, id='IndustryPicker', placeholder='All',
                         style={'width': 300, 'marginRight': '100px'})
        ], width=5)
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Bullet', style={'marginTop': '10px'}),
            width=4),
        dbc.Col(html.Div([
            dcc.Graph(id='Table'),
        ]), width=8),
    ]),
    dbc.Row([
        dcc.Graph(id='Top_6')
    ]),
    dbc.Row([
        dbc.Col([html.Div([
            html.H3('Visualizing Industry Performance Over Time', style={'text-align': 'center'}),
            html.P('Click and drag anywhere below to zoom in on a specific timeframe',
                   style={'text-align': 'center'}),
            dcc.Graph(id='Candlestick', style={'marginTop': '20px'}),
        ])
        ]),
        dbc.Col(html.Div([
            html.H3('Market Sector Breakdown', style={'text-align': 'center'}),
            html.P('The Global Industry Classification Standard defines 11 Industry Sectors',
                   style={'text-align': 'center'}),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        [
                            html.P("All sectors make up the S&P 500 which stands for "
                                   "The Standard and Poor's 500. The S&P 500 is a stock market"
                                   " index tracking the performance of 500 of the largest "
                                   "companies listed on stock exchanges in "
                                   "the United States. It is one of the most commonly followed equity indices"),
                        ],
                        title="All Sectors",
                    ),
                    dbc.AccordionItem(
                        [
                            html.P(
                                "The energy sector covers companies that do business in the oil "
                                "and natural gas industry. "
                                "It includes oil and gas exploration and production companies, "
                                "as well as producers of other "
                                "consumable fuels like coal and ethanol. "
                                "The energy sector also includes the related businesses that "
                                "provide equipment, materials, and services to oil and gas producers."),
                        ],
                        title="Energy",
                    ),
                    dbc.AccordionItem(
                        [
                            html.P(
                                "The materials sector includes companies that provide "
                                "various goods for use in manufacturing and other applications."
                                " You'll find makers of chemicals, construction materials, "
                                "and containers and packaging within the "
                                "materials sector, along with mining stocks and companies "
                                "specializing in making paper and forest products."),

                        ],
                        title="Materials",
                    ),
                    dbc.AccordionItem(
                        ["The industrials sector encompasses a wide range of different businesses "
                         "that generally involve the use of heavy equipment. "
                         "Transportation stocks such as airlines, railroads, and "
                         "logistics companies are found within the industrials sector, "
                         "as are companies in the aerospace, defense, construction, and engineering industries. "
                         "Companies making building products, electrical equipment, "
                         "and machinery also fall into this sector, as do many conglomerates."],
                        title="Industrials",
                    ),

                    dbc.AccordionItem(
                        ["The utilities sector encompasses just about "
                         "every different type of utility company you can "
                         "think of. Within the sector, you'll find utilities "
                         "specializing in making electrical power available to residential and "
                         "commercial customers, as well as specialists in natural "
                         "gas transmission and distribution. "
                         "Other utilities are responsible for delivering water to customers."],
                        title="Utilities",
                    ),

                    dbc.AccordionItem(
                        ["The healthcare sector has two primary components. "
                         "One component includes companies that develop pharmaceuticals and treatments based on "
                         "biotechnology, as well as the analytical tools "
                         "and supplies needed for the clinical trials that test those treatments. "
                         "The other encompasses healthcare equipment and services, including surgical supplies,"
                         " medical diagnostic tools, and health insurance."],
                        title="Health Care",
                    ),

                    dbc.AccordionItem(
                        ["The financials sector includes businesses that are "
                         "primarily related to handling money. "
                         "Banks are a key industry group within the sector,"
                         " but you'll also find insurance companies, "
                         "brokerage houses, consumer finance providers, and mortgage-related "
                         "real estate investment trusts among financials."],
                        title="Financials",
                    ),

                    dbc.AccordionItem(
                        "The consumer discretionary sector covers goods and services for which "
                        "consumer demand depends upon consumer financial status. For example, "
                        "if you make $25,000 per year, you probably buy a different car than someone"
                        " who makes $25 million per year. The sector includes companies that sell "
                        "higher-priced items like automobiles and luxury goods, as well as leisure products. "
                        "You'll find both brick-and-mortar and e-commerce-based retail companies in this category, "
                        "along with hotel and restaurant stocks.",
                        title="Consumer Discretionary",
                    ),

                    dbc.AccordionItem(
                        ["The consumer staples sector includes goods and services that consumers need,"
                         " regardless of their current financial condition."
                         " The category includes companies in the food, beverage, and "
                         "tobacco industries, as well as household and personal care products. "
                         "You'll also find retail companies that specialize in selling staples, "
                         "such as supermarkets, in this group."],
                        title="Consumer Staples",
                    ),

                    dbc.AccordionItem(
                        ["The information technology sector covers companies involved in the "
                         "different categories of technological innovation. "
                         "Some companies in information technology "
                         "focus on creating software or providing services related to "
                         "implementing technological solutions, "
                         "while others are more involved in building the equipment, components, "
                         "and hardware that make tech possible."],
                        title="Information Technology",
                    ),

                    dbc.AccordionItem(
                        [" The communication services sector is the newest of the GICS "
                         "sectors and includes a couple of major areas that used to be part "
                         "of other sectors. Telecommunication services providers, including "
                         "both wireless telecom networks and providers of old-style landline "
                         "services, make up one wing of the sector. At the other end are media "
                         "and entertainment companies, including both older media like television "
                         "and radio and interactive media "
                         "via the internet and newer forms of communication."],
                        title="Communication Sevices",
                    ),

                    dbc.AccordionItem(
                        ["The real estate sector generally includes two different types of investments "
                         "related to real estate. "
                         "Some stocks in the sector are responsible for developing "
                         "new real estate projects and "
                         "then managing them by obtaining tenants "
                         "for various spaces within the project property. "],
                        title="Real Estate",
                    ),

                ], start_collapsed=True)])),
        dbc.Row([
            html.Br(),
            html.Br()
        ])
    ])])


@app.callback(
    Output('Bullet', 'figure'),
    Input('Year0', 'value'),
    Input('Year1', 'value'),
    Input('IndustryPicker', 'value'))
def update_bullet(year0, year1, industry):
    """ creates a bullet chart/card which shows the change in aggregated closing price
        between two user-inputter years and/or a user-inputted industry """

    if year0 is None:
        year0 = 2010

    if year1 is None:
        year1 = 2020

    if industry is None:
        industry = 'All'

    if industry == 'All':
        # filter on years for the entire S&P index
        t0 = num_filter(index_df, 'Date', [f'{year0}-01-01', f'{year0}-12-31'])
        t1 = num_filter(index_df, 'Date', [f'{year1}-01-01', f'{year1}-12-31'])

        # retrieve closing price of year0 and year1 for entire S&P Index
        p0 = ((t0['Close']).mean())
        p1 = ((t1['Close']).mean())

    else:
        # filter on years for the stock specific data
        t0 = num_filter(close_df, 'Date', [f'{year0}-01-01', f'{year0}-12-31'])
        t1 = num_filter(close_df, 'Date', [f'{year1}-01-01', f'{year1}-12-31'])

        # retrieve avg adjusted closing price per industry for year0
        c0 = pd.DataFrame(t0.groupby('Sector').mean(numeric_only=True)['Adj Close']).reset_index()
        c0.columns = ['Sector', 'Adj Close']

        # retrieve avg adjusted closing price per industry for year1
        c1 = pd.DataFrame(t1.groupby('Sector').mean(numeric_only=True)['Adj Close']).reset_index()
        c1.columns = ['Sector', 'Adj Close']

        # retrieve closing price of year0 and year1 for specific industry
        p0 = (c0[c0.Sector == industry]['Adj Close']).iloc[0]
        p1 = (c1[c1.Sector == industry]['Adj Close']).iloc[0]

    # plot the bullet chart
    fig = go.Figure(go.Indicator(
        mode="number+delta",
        value=p1,
        title={"text": f"{industry} Sector<br><span style='font-size:0.6em; \
                              color:gray'>Change in Avg. Closing Price</span><br><span \
                              style='font-size:0.6em;color:gray'>{year0} to {year1}</span>"},
        number={'prefix': "$"},
        delta={'position': "top", 'reference': p0},
        domain={'x': [0, 1], 'y': [0, 1]})
    )

    fig.update_layout(
        margin=dict(l=100, r=100, t=50, b=50))

    return fig


@app.callback(
    Output('Table', 'figure'),
    Input('Year0', 'value'),
    Input('Year1', 'value'),
    Input('IndustryPicker', 'value'))
def update_table(year0, year1, industry):
    """ creates a table showing the change in stock prices between two user-inputted years
        and/or a user inputted industry, also displaying each stock's ticker and industry """

    if year0 is None:
        year0 = 2010

    if year1 is None:
        year1 = 2020

    if industry is None:
        industry = 'All'

    # initialize empty dataframe
    df = pd.DataFrame()

    # retrieve data from year0 and year1 using stock specific dataframe
    t0 = num_filter(price_df, 'Date', [f'{year0}-01-01', f'{year0}-12-31'])
    t1 = num_filter(price_df, 'Date', [f'{year1}-01-01', f'{year1}-12-31'])

    # retrieve avg adjusted closing price for each ticker in year 1
    year0_close = pd.DataFrame(t0.groupby('Ticker').mean(numeric_only=True)['Adj Close']).reset_index()
    year0_close.columns = ['Ticker', f'{year0} Adj Close']

    # retrieve avg adjusted closing price for each ticker in year 2
    year1_close = pd.DataFrame(t1.groupby('Ticker').mean(numeric_only=True)['Adj Close']).reset_index()
    year1_close.columns = ['Ticker', f'{year1} Adj Close']

    # merge year0 and year1 dataframes and calculate change in closing prices
    df = pd.merge(year0_close, year1_close, how='outer')
    df['Change'] = df[f'{year1} Adj Close'] - df[f'{year0} Adj Close']
    df = df.round(2)

    # add sector label to the tickers
    df = pd.merge(df, industry_df, on='Ticker')
    df = df.iloc[:, [-1, 0, -2, 1, 2, 3]]

    if industry != 'All':
        # filter by sector and display table (positive change = green, negative change = red)
        df = df[df.Sector == industry]

    fill_color = ['#E6F2FD' for _ in range(len(df.columns) - 1)]
    change_color = ['#D0FDC1' if change >= 0 else '#FFC2C2' for change in df['Change']]
    fill_color.append(change_color)

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    font=dict(color='rgb(45,45,45)'),
                    ),
        cells=dict(values=list(df.to_dict('list').values()),
                   font=dict(color='black'),
                   align=['left'] * len(df),
                   fill=dict(color=fill_color)))])

    fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=50))

    return fig


@app.callback(
    Output('Candlestick', 'figure'),
    Input('Year0', 'value'),
    Input('Year1', 'value'),
    Input('IndustryPicker', 'value')
)
def update_candlestick(year0, year1, industry):
    """ creates a candlestick chart of aggregated open/close/high/low prices
        for the entire S&P index or a user-inputted industry and time range """

    # set default years
    if year0 is None:
        year0 = 2010

    if year1 is None:
        year1 = 2020

    # set default industry
    if industry is None:
        industry = 'All'

    if industry == 'All':

        # retrieve data from year0 and year1 using stock specific dataframe
        t0 = num_filter(index_df, 'Date', [f'{year0}-01-01', f'{year1}-12-31'])

        # plot candlestick graph
        fig = go.Figure(data=[go.Candlestick(x=t0['Date'],
                                             open=t0['Open'],
                                             high=t0['High'],
                                             low=t0['Low'],
                                             close=t0['Close'])])

        fig.update_layout(
            title={'text': "S&P 500 Stock Price", 'xanchor': 'center', 'x': .5})

    else:
        # closing Prices per Industry
        sector_prices = pd.DataFrame(close_df.groupby(['Sector', 'Date']).mean(numeric_only=True)).reset_index()
        sector_prices = sector_prices[sector_prices['Sector'] == industry]

        # retrieve data from year0 and year1 using stock specific dataframe
        t0 = num_filter(sector_prices, 'Date', [f'{year0}-01-01', f'{year1}-12-31'])

        # plot candlestick graph
        fig = go.Figure(data=[go.Candlestick(x=t0['Date'],
                                             open=t0['Open'],
                                             high=t0['High'],
                                             low=t0['Low'],
                                             close=t0['Close'])])

        fig.update_layout(
            title={'text': f'{industry} Stock Price', 'xanchor': 'center', 'x': .5})

    # add y and x axes
    fig.update_xaxes(title_text='Time')
    fig.update_yaxes(title_text='Stock Price ($)')
    fig.update_layout(margin=dict(l=0, r=50, t=50, b=50), height=630)

    return fig


@app.callback(
    Output('Top_6', 'figure'),
    Input('Year0', 'value'),
    Input('Year1', 'value'),
    Input('IndustryPicker', 'value')
)
def update_top_6(year0, year1, industry):
    """ creates six subplots showing closing price over time for the top six
        performing stocks in the S&P 500 or a user-inputted industry/time range """

    # set default years
    if year0 is None:
        year0 = 2010

    if year1 is None:
        year1 = 2020

    # set default industry
    if industry is None:
        industry = 'All'

    if industry == 'All':

        # retrieve data from year0 and year1 using stock specific dataframe
        price_df1 = num_filter(price_df, 'Date', [f'{year0}-01-01', f'{year1}-12-31'])

        # group price data on ticker
        ticker_prices = pd.DataFrame(price_df1.groupby(['Ticker']).mean(numeric_only=True)).reset_index()

        # sort tickers based on adj closing price
        tickers = list(ticker_prices.sort_values(by=['Adj Close'], ascending=False).head(6)['Ticker'])
        top_6 = price_df1.loc[price_df1['Ticker'].isin(tickers), :]

        # plot subplot area graphs
        fig = px.area(top_6, x="Date", y="Close", color="Ticker", facet_col="Ticker", facet_col_wrap=3)
        fig.update_layout(title={
            'text': 'Top 6 Performing Stocks in S&P 500',
            'xanchor': 'center', 'x': .5})

    else:

        # filter data based on industry/date
        sector_df = close_df[close_df['Sector'] == industry]
        sector_df = num_filter(sector_df, 'Date', [f'{year0}-01-01', f'{year1}-12-31'])

        # group on ticker and sort for highest 6 mean adj close prices
        sector_prices = pd.DataFrame(sector_df.groupby(['Ticker']).mean(numeric_only=True)).reset_index()
        tickers = list(sector_prices.sort_values(by=['Adj Close'], ascending=False).head(6)['Ticker'])
        top_6 = sector_df.loc[sector_df['Ticker'].isin(tickers), :]

        # plot subplot area graphs
        fig = px.area(top_6, x="Date", y="Close", color="Ticker", facet_col="Ticker", facet_col_wrap=3)
        fig.update_layout(title={
            'text': f'Top 6 Performing Stocks in {industry} Sector',
            'xanchor': 'center', 'x': .5})

    return fig


def main():
    app.run_server(debug=True, port=8051)


if __name__ == '__main__':
    main()
