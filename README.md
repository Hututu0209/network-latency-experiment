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

## Requirements

- Python 3
- Matplotlib

Install Matplotlib with:

```bash
pip install matplotlib

## Usage

Run the HTTP latency experiment:

```bash
python latency_experiment.py
```

Run the ping RTT experiment:

```bash
python ping_latency.py
```

## What I Learned

Through this project, I practiced:

- Measuring elapsed time in Python
- Running system commands from Python
- Extracting values from command output
- Calculating basic statistics
- Visualizing measurement results
- Using Git and GitHub for version control

## Future Improvements

Possible extensions include:

- Saving measurement results to CSV files
- Comparing latency to different servers
- Calculating standard deviation
- Creating latency histograms
- Investigating network jitter and packet loss