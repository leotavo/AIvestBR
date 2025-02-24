
# Investment Recommendation System

## 📄 Description
This tool helps investors make informed investment decisions using machine learning algorithms to analyze market data and provide personalized recommendations.

## ⚙️ Installation
To install the system, follow the steps below:

1. 🛠️ Clone the repository:
```bash
git clone https://github.com/leotavo/investment_recommendation_system.git
```
2. 📂 Navigate to the project directory:
```bash
cd investment_recommendation_system
```
3. 📦 Install the dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage
To use the system, follow the steps below:

1. 🌐 Navigate to the SELIC data collection directory:
```bash
cd data_collection/SELIC
```
2. ⚡ Run the SELIC data collection script:
```bash
python selic.py
```
3. 📊 Follow the on-screen instructions to fetch SELIC data and create an HTML file with the results.

## 🌟 Upcoming Features

### 🔍 Data Management and Integration
- 📡 **Extended Data Sources:** Incorporate CDI, IPCA, inflation indices, and sector-specific indicators.
- ⏰ **Temporal Consistency Checks:** Ensure synchronized time-series data with aligned reference dates.
- 🗃️ **Advanced Data Formats:** Standardize storage in CSV, JSON, and SQL for integration with dashboards.

### 📈 Machine Learning and Analysis
- 🧮 **Feature Engineering:** Creation of predictive variables such as moving averages and technical indicators.
- 🤖 **Model Selection:** Implementation of ARIMA, LSTM, and Prophet algorithms for time series forecasting.
- 🔄 **Validation and Backtesting:** Automated backtesting with adjustable parameters to validate generated signals.

### 🚀 System Performance and Automation
- 🔄 **Automated Updates:** Continuous data fetching and processing pipelines.
- 🌐 **API Integration:** Seamless data import/export for external systems.
- 📊 **Real-time Dashboards:** Interactive dashboards for visualization of predictions and insights.

### 💡 Risk Management and Decision Support
- 💳 **Credit and Market Spread Analysis:** Monitoring of spreads for dynamic risk assessment.
- 📈 **Portfolio Optimization:** Analysis of asset allocation, liquidity, and credit ratings.
- 🏦 **Decision Support Tools:** Automated alerts for buy/sell opportunities with risk-adjusted insights.

### 🔒 Metadata and Documentation
- 📝 **Comprehensive Metadata:** Documentation of data sources, update frequencies, and calculation methodologies.
- 🔎 **Traceability and Transparency:** Clear records of model decisions and data transformations.

## 🤝 Contribution
If you wish to contribute to the project, please fork the repository and submit a pull request with your changes.

## 📝 License
This project is licensed under the Apache License 2.0. See the LICENSE file for more details.
