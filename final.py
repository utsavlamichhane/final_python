import yfinance as yf
tesla = yf.Ticker('TSLA')
tesla_data = tesla.history(period = 'max')
tesla_data.reset_index(inplace = True)
tesla_data.head()
tesla_data.tail()
tesla_data.reset_index(inplace=True)
print(tesla_data.head())
tesla_data.tail()
import plotly.graph_objs as go

# Define the figure layout
layout = go.Layout(title="Tesla Stock Data")

# Create the plot using the make_graph function
fig = make_graph(tesla_data, 'Date', 'Close', layout)

# Display the plot
fig.show()

import pandas as pd
import plotly.graph_objs as go
from datetime import datetime

def make_graph(x, y, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name="Stock Prices"))
    fig.update_layout(title=title, xaxis_title="Date", yaxis_title="Price")
    return fig


tesla = yf.Ticker("TSLA")


tesla_data = tesla.history(period="max")


tesla_data.reset_index(inplace=True)


graph = make_graph(tesla_data["Date"], tesla_data["Close"], "Tesla Stock Price")


graph.show()
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)

# Plot GameStop stock data
make_graph(gme_data, "GameStop Stock Data")
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go


def make_graph(x, y, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name='Stock Prices'))
    fig.update_layout(title=title, xaxis_title='Date', yaxis_title='Price')
    return fig


gme = yf.Ticker('GME')
gme_data = gme.history(period='max')
gme_data.reset_index(inplace=True)

title = "GameStop Stock Prices Over Time"
fig = make_graph(gme_data['Date'], gme_data['Close'], title)
fig.show()


