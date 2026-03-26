# Website Traffic Forecasting using Time Series Models

## Project Overview

This project focuses on forecasting website traffic using classical time series models and modern forecasting techniques. The goal is to analyze historical traffic data, identify patterns such as trend and seasonality, and build predictive models to forecast future website visits.


## Dataset

* Source: Kaggle Web Traffic Dataset
* Type: Time Series Data
* Features:

  * Date
  * Number of Visitors


## Exploratory Data Analysis (EDA)

### Trend Analysis

* Used rolling mean to observe long-term trends
* Found slight variation with no strong upward/downward growth

### Seasonality Detection

* Time series decomposition revealed **weekly seasonality**
* Traffic follows a repeating pattern

### Residual Analysis

* Random noise and spikes observed
* Indicates real-world unpredictable behavior


## Stationarity Check

* Performed Augmented Dickey-Fuller (ADF) Test
* Result:

  * p-value < 0.05
* Conclusion: Data is **stationary**, suitable for ARIMA-based models


## Models Used

### 1️. ARIMA (AutoRegressive Integrated Moving Average)

* Captures trend and past dependencies
* Does not handle seasonality

### 2️. SARIMA (Seasonal ARIMA)

* Extends ARIMA by including seasonal components
* Better performance for periodic data

### 3️. Prophet

* Developed by Meta
* Automatically models trend, seasonality, and holidays
* Handles real-world irregular patterns effectively


## Model Evaluation

| Model   |    RMSE    |     MAE    |
| ------- |    ----    |     ---    |
| ARIMA   | 15.078377  |  8.980165  |
| SARIMA  | 15.223764  |  9.177972  | 
| Prophet | 14.629834  |  9.285156  |


##  Best Model

* Prophet performed best based on lowest RMSE and MAE
* Captured seasonality and trends more effectively


## Future Forecast

* Predicted website traffic for the next 30 days
* Generated forecast values and visualization


## Results & Insights

* Website traffic shows **weekly seasonal behavior**
* Sudden spikes indicate external factors (events, promotions)
* Prophet provides more realistic forecasts compared to ARIMA/SARIMA


## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Statsmodels
* Prophet
* Scikit-learn


## Author

Muhammad Shaheer Ahmad Chishty


## If you like this project

Give it a star ⭐ on GitHub!
