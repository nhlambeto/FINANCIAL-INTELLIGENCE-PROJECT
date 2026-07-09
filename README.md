# Financial Intelligence Engine (Project 2)

Welcome to our advanced stock forecasting and portfolio optimisation system. This repository documents our strategic plan and development roadmap for building a machine learning-driven investment engine.

**For first-time visitors:** This repository is currently in the pre-implementation planning phase. Our team has reviewed financial research papers, machine learning studies, and deep learning architectures to form our hypotheses and select specific models. This README serves as our system design guide.

Once the coding phase is complete, final performance results, interactive charts, and live trading simulations will be connected to a **Streamlit dashboard**.

---

## System Design: Four-Stage Pipeline

Our end-to-end strategy transforms research into an operational machine learning pipeline:

```
Stage 1: Data Audit & EDA
├─ Clean data and verify prices across daily, weekly, and monthly timelines
└─ Group data by individual stock ticker in strict historical order

           ↓

Stage 2: Feature Pipeline Generation
├─ Build market features: Trends (EMA), Momentum (RSI), Volatility Bands
└─ Filter redundant features using Random Forest and PCA (keep 10-20 best)

           ↓

Stage 3: Machine Learning Engine Design
├─ Baselines: Regularized Random Forest and fine-tuned XGBoost
└─ Advanced Layer: Custom Hybrid LSTM-GRU Neural Network

           ↓

Stage 4: Validation & Portfolio Allocation
├─ Testing: Move forward chronologically (no shuffling to prevent cheating)
└─ Allocation: Shift investments to maximize Sharpe Ratio
```

---

## Phase 1: Financial Systems, Datasets & Exploratory Data Analysis

**Objective:** Audit baseline data quality, check stock behaviors, and format clean historical timelines before passing data to our deep learning models.

### Operational Process
Based on QuantRocket and ResearchGate reviews, we implement:

- **Strict Pre-Modeling Checks:** Deep data validation audits on raw OHLCV (Open, High, Low, Close, Volume) inputs to fix missing or incorrect data before models train
- **Multi-Timeline Sweeps:** Analyze stock price behavior across daily, weekly, and monthly intervals to understand wider market trends
- **Ticker Segmentation:** Separate the dataset by individual stock tickers to keep data continuous and in perfect date order

### Methodologies Explicitly Rejected

- **Macro Climate Tracking & Sector Exposure:** Our dataset contains only basic price and volume data. It lacks company financial statements (operating margins, revenues) and macro economics data (GDP, inflation, US Dollar Index). Guessing these values would introduce dangerous noise, so they are excluded.

---

## Phase 2: Preprocessing, Feature Engineering & Financial Indicators

**Objective:** Turn raw price histories into highly accurate predictive features while keeping overall data clean and simple.

### Candidate Feature Generation (20-30 Attributes)

- **Trend Indicators:** Simple Moving Averages (SMA), Exponential Moving Averages (EMA), Rate of Change (ROC)
- **Momentum Indicators:** Relative Strength Index (RSI), Stochastic Oscillators, speed metrics
- **Volatility Indicators:** Bollinger Bands, Average True Range (ATR), Rolling Standard Deviations
- **Volume Indicators:** On-Balance Volume (OBV), Volume Moving Averages, volume changes

### Feature Selection Strategy

Feeding highly correlated or overlapping features into machine learning models hurts performance. We'll address this by applying:

- Random Forest Feature Importance analysis
- Mutual Information (MI) scoring
- Principal Component Analysis (PCA)
---

## Phase 3: Traditional ML Baseline Models & Optimization

**Objective:** Build high-performing baseline tree models to give us a clear accuracy benchmark to beat.

### Core Benchmarking Insights
Based on Qian and Wu research:

- **Random Forest (RF):** Highly stable with low error rates and reliable out-of-the-box performance on historical corporate stock data
- **XGBoost:** Incredibly powerful at finding complex patterns, but easily overfits (memorizes data too closely) on noisy stock data if settings aren't carefully restricted

### Operational Control Rules

- All features will be normalized using StandardScaler before training to protect tree models from market regime shifts
- We will use Grid Search and Random Search techniques to tune settings like tree depth and density, rather than relying on default presets

---

## Phase 4: Deep Learning Sequence Modeling & Portfolio Integration

**Objective:** Use advanced sequence models to convert historical price paths directly into optimal portfolio investment weights.

### The Core Model Choice: Hybrid LSTM-GRU Sequence Engine

**Why this approach?**

Stock market trends operate on two layers:
- Long-term broad trends
- Fast, short-term noise and spikes

**Individual limitations:**
- Standalone LSTM models excel at long-term patterns but react slowly to sudden market spikes
- Standalone GRU models are faster but tend to lose memory over very long horizons

**The hybrid advantage:** By combining LSTM (for long-term memory) with GRU (for short-term adjustments), we achieve 3% lower Mean Squared Error (MSE) than using either model alone.

### Connecting to a Portfolio Optimizer

Minimizing mathematical error doesn't automatically mean you make money in the real world. Our model's predictions feed directly into a Portfolio Optimizer that:

- Automatically calculates asset weights to maximize Sharpe Ratio
- Aims to beat a passive S&P 500 baseline by hunting for the best risk-adjusted returns

---

## Eliminating Systemic Risk: Preventing Lookahead Bias

Standard data science projects shuffle rows randomly before splitting data into 80% training and 20% testing sets. **In stock market modeling, this is a fatal flaw.**

### The Problem

Shuffling breaks your timeline, meaning the model accidentally uses future stock prices (like 2017) to predict past stock prices (like 2014). This creates **lookahead bias (data leakage)**, producing a model that looks perfect on paper but fails completely in live trading.

### The Solution: Walk-Forward Validation

We implement a strict Walk-Forward Validation framework that keeps data in chronological order and moves a testing window forward through time where the model can only use past data to predict the future:

```
Timeline Progression
├─ [Train Window 1] → [Test Window 1]
├─    [Train Window 2] → [Test Window 2]
└─         [Train Window 3] → [Test Window 3]
```

---

## Comprehensive Performance Matrix

The pipeline measures and reports data across three distinct areas to maintain total clarity:

### Performance Metrics by Category

| Category | Metrics | Purpose |
|----------|---------|---------|
| **Statistical Accuracy** | MSE, RMSE, MAE, ROC-AUC Scores | Measures how close our price forecasts are and how well we guess market direction |
| **Financial Risk** | Sharpe Ratio, Sortino Ratio, Max Drawdown | Evaluates our actual risk-adjusted returns and how well we protect capital from deep losses |
| **System Integrity** | Walk-Forward Chronological Splits | Proves our system is free from data leakage, cheating, and historical overfitting |

---

## Results Summary

[Our Streamlit dashboard link will be found here after completion]

---

## Project Structure

```
financial-intelligence-project/
├── README.md                 (You are here)
├── requirements.txt          (Python dependencies)
├── data/
│   ├── raw/                  (Original S&P 500 stock prices 2014-2017)
│   ├── clean_data/           (Validated, cleaned data)
│   └── preprocessed_and_feature_eng_data/  (Feature-engineered datasets)
├── src/                      (Source code by pair)
│   ├── pair 1/
│   ├── pair 2/
│   ├── pair 3/
│   └── pair 4/
├── outputs/                  (Generated files)
│   ├── figures/              (Charts and visualizations)
│   ├── models/               (Trained model files)
│   └── reports/              (Analysis reports)
└── streamlit/                (Dashboard application)
```

---

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Activate your virtual environment
3. Explore the data in `data/raw/`
4. Follow the pipeline from Phase 1 through Phase 4
5. Launch the Streamlit dashboard when complete

---

**Last Updated:** 2026-07-09 
