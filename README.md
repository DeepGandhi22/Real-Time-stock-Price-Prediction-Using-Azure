# Real Time Stock Price Prediction Using Azure

## Project Overview

This project showcases the implementation of a **real-time data pipeline** that fetches financial data from the **Yahoo Finance API**, processes it using **Azure Functions**, stores and analyzes it through **Azure Data Lake** and **Stream Analytics**, and leverages **Azure Machine Learning Studio** for model inference and reporting.

---
## Architecture Diagram

  ![mlAI (1)](https://github.com/user-attachments/assets/2c920517-1b38-490a-8de5-b826dc96cf33)

---
## End-to-End Workflow

### Step-by-Step Process

1. **Data Ingestion with Azure Functions**  
   - Azure Functions are used to call the **Yahoo Finance API** at scheduled intervals.
   - The function is configured to fetch real-time stock or market data and pass it downstream.

2. **Data Routing via Azure Event Hub**  
   - The function sends the fetched data to **Azure Event Hub**, which acts as a real-time ingestion buffer.
  
   ![eventsHub](https://github.com/user-attachments/assets/4cd3c1a7-cd63-43da-835e-a433120bbd7f)

3. **Data Storage and ML Integration**  
   - The data is then stored in **Azure Data Lake** for persistent, scalable storage.
   - The stored data is used as input to a **machine learning model** hosted in **Azure ML Studio** to generate predictions or classifications.

![DataLake Container](https://github.com/user-attachments/assets/b6986e17-0795-43d7-840e-d0be0ee0bce1)

4. **Stream Analytics for Real-Time Processing**  
   - Simultaneously, **Azure Stream Analytics** processes the real-time data from Event Hub.
   - It performs filtering, aggregation, and transformation operations to create structured output suitable for reporting.

![StreamAnalytics](https://github.com/user-attachments/assets/b0bc2443-35c5-469f-b2ed-d4f439e5ca48)

---

## What I Did

- Set up **Azure Functions** with a timer trigger to periodically call Yahoo Finance API.
- Streamed the response to **Azure Event Hub** for real-time data flow.
- Created an **Azure Stream Analytics Job** to process and shape data for business reporting.
- Stored raw data in **Azure Data Lake** for machine learning and future batch processing.
- Built and deployed a **machine learning model** in Azure ML Studio, which reads from Data Lake.
- Connected processed data from Stream Analytics directly into **Power BI** for live dashboards.

---

## Tools & Technologies Used

- **Azure Functions**
- **Yahoo Finance API**
- **Azure Event Hub**
- **Azure Data Lake Storage**
- **Azure Stream Analytics**
- **Azure Machine Learning Studio**

---

## Outcome

This pipeline provides a real-time, scalable solution to collect, process, analyze, and visualize financial market data. It integrates modern Azure services to support both streaming analytics and machine learning applications.
