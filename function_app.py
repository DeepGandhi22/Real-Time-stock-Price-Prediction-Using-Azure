import logging
import asyncio
import yfinance as yf
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
from dotenv import load_dotenv
import os
import json
import azure.functions as func
 
# Load environment variables from .env file
load_dotenv()
 
# Azure Event Hub connection string and event hub name
EVENT_HUB_CONNECTION_STR = os.getenv("EVENT_HUB_CONNECTION_STR")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")
 
# Function to fetch stock data using yfinance
def fetch_stock_data(tickers):
    stock_data = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period='1d')
            if not data.empty:
                stock_data.append({
                    'Stock': ticker,
                    'Open': data.iloc[0]['Open'],
                    'High': data.iloc[0]['High'],
                    'Low': data.iloc[0]['Low'],
                    'Close': data.iloc[0]['Close'],
                    'Volume': data.iloc[0]['Volume'],
                    'Dividends': data.iloc[0]['Dividends'],
                    'Stock Splits': data.iloc[0]['Stock Splits']
                })
            else:
                logging.info(f"No data available for {ticker}")
        except Exception as e:
            logging.error(f"Error fetching data for {ticker}: {str(e)}")
    
    return stock_data
 
# Function to send stock data to Azure Event Hub
async def send_stock_data_to_eventhub(stock_data):
    try:
        producer = EventHubProducerClient.from_connection_string(
            conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME
        )
        async with producer:
            for data in stock_data:
                try:
                    event_data_batch = await producer.create_batch()
                    event_data_batch.add(EventData(json.dumps(data)))  # Serialize data to JSON
                    await producer.send_batch(event_data_batch)
                    logging.info(f"Stock data sent successfully for {data['Stock']} to Event Hub!")
                except Exception as e:
                    logging.error(f"Error sending data for {data['Stock']}: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

app = func.FunctionApp()

@app.function_name(name="stock_trigger")
@app.timer_trigger(schedule="* */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False) 
async def stock_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')
 
    logging.info('Python timer trigger function executed.')
    
    tickers = ['NVDA', 'TSLA', 'MSFT', 'AAPL', 'GOOGL', 'AMZN', 'META', 'LLY', 'TSM', 
               'AVGO', 'JNJ', 'V', 'XOM', 'PG', 'KO', 'MCD', 'INTC', 'CSCO', 'UNH', 'T']
    
    stock_data = fetch_stock_data(tickers)
    
    # Run the async function
    await send_stock_data_to_eventhub(stock_data)