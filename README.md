# Network Latency Experiment

A simple Python project for learning basic network latency measurement and data analysis.

## Overview

This project explores two basic methods for measuring network latency:

1. HTTP request latency
2. Ping round-trip time (RTT)

The goal is to practice Python programming, network measurement, basic statistics, and data visualization.

## Files

### `latency_experiment.py`

Measures the time required to send an HTTP request and receive a response.

The script performs multiple measurements and reports:

- Minimum latency
- Maximum latency
- Average latency

### `ping_latency.py`

Measures network round-trip time (RTT) using the system `ping` command.

The script performs multiple measurements, calculates basic statistics, and visualizes the RTT measurements using Matplotlib.

### `analyze_latency.py`

Analyzes the RTT measurements stored in `latency_data.csv`.

The script calculates descriptive statistics, detects outliers using 3-sigma and IQR methods, analyzes jitter, calculates outlier rates, and visualizes the results.

### `latency_data.csv`

Stores the RTT measurements collected by `ping_latency.py` for further analysis.

## Requirements

- Python 3
- Matplotlib

Install Matplotlib with:

```bash
pip install matplotlib
```

## Usage

Run the HTTP latency experiment:

```bash
python latency_experiment.py
```

Run the ping RTT experiment:

```bash
python ping_latency.py
```

Analyze the collected RTT data:

```bash
python analyze_latency.py
```

## Data Analysis

The RTT measurements were analyzed using several statistical methods:

- Mean and median latency
- Standard deviation
- 3-sigma outlier detection
- IQR-based outlier detection
- Jitter analysis
- Outlier rate calculation

## Results

For 100 RTT measurements:

- Mean RTT: 31.40 ms
- Median RTT: 31.00 ms
- Standard deviation: 4.82 ms
- Maximum RTT: 76.00 ms
- 3-sigma outlier rate: 1.00%
- IQR outlier rate: 11.00%
- Mean jitter: 2.33 ms
- Median jitter: 1.00 ms
- Jitter outlier rate: 4.04%

Most RTT measurements were concentrated around 30–32 ms, indicating relatively stable network latency. Two noticeable latency spikes were observed, including a maximum RTT of 76 ms. More measurements are needed to determine whether these spikes represent occasional network fluctuations or a recurring pattern.

## What I Learned

Through this project, I practiced:

- Measuring network latency with Python
- Running system commands from Python
- Extracting values from command output
- Reading and writing CSV files
- Calculating descriptive statistics
- Detecting outliers using 3-sigma and IQR methods
- Calculating network jitter
- Visualizing RTT and jitter measurements
- Using Git and GitHub for version control
