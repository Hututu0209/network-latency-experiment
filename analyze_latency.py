import csv
import statistics
import matplotlib.pyplot as plt

latencies = []

with open("latency_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        latencies.append(float(row["latency_ms"]))

print("===== RTT 数据分析 =====")
print(f"数据量: {len(latencies)}")
print(f"平均值: {statistics.mean(latencies):.2f} ms")
print(f"中位数: {statistics.median(latencies):.2f} ms")
print(f"标准差: {statistics.stdev(latencies):.2f} ms")
print(f"最小值: {min(latencies):.2f} ms")
print(f"最大值: {max(latencies):.2f} ms")

sorted_latencies = sorted(latencies)

q1 = statistics.median(sorted_latencies[:50])
q3 = statistics.median(sorted_latencies[50:])

iqr = q3 - q1

lower_iqr = q1 - 1.5 * iqr
upper_iqr = q3 + 1.5 * iqr

iqr_outliers = []
for latency in latencies:
    if latency < lower_iqr or latency > upper_iqr:
        iqr_outliers.append(latency)

print(f"Q1: {q1:.2f} ms")
print(f"Q3: {q3:.2f} ms")
print(f"IQR: {iqr:.2f} ms")
print(f"Lower IQR threshold: {lower_iqr:.2f} ms")
print(f"Upper IQR threshold: {upper_iqr:.2f} ms")
print(f"IQR Outliers: {iqr_outliers}")

mean_latency = statistics.mean(latencies)
std_latency = statistics.stdev(latencies)

lower_threshold = mean_latency - 3 * std_latency
upper_threshold = mean_latency + 3 * std_latency

outliers = []

for latency in latencies:
    if latency < lower_threshold or latency > upper_threshold:
        outliers.append(latency)

print(f"Lower threshold: {lower_threshold:.2f} ms")
print(f"Upper threshold: {upper_threshold:.2f} ms")
print(f"Outliers: {outliers}")

measurement_numbers = range(1, len(latencies) + 1)

jitter_values = []

for i in range(1, len(latencies)):
    difference = abs(latencies[i] - latencies[i - 1])
    jitter_values.append(difference)

print(f"Jitter values: {jitter_values}")

mean_jitter = statistics.mean(jitter_values)
print(f"Mean jitter: {mean_jitter:.2f} ms")

median_jitter = statistics.median(jitter_values)
print(f"Median jitter: {median_jitter:.2f} ms")

plt.figure()

plt.plot(
    measurement_numbers,
    latencies,
    marker="o"
)

plt.axhline(
    upper_threshold,
    color="red",
    linestyle="--",
    linewidth=2,
    label="3-sigma threshold"
)

plt.axhline(
    upper_iqr,
    color="orange",
    linestyle=":",
    linewidth=2,
    label="IQR threshold"
)


plt.xlabel("Measurement")
plt.ylabel("RTT (ms)")
plt.title("RTT Measurements with Outlier Thresholds")
plt.legend()
plt.grid(True)

plt.show()

plt.hist(latencies, bins=15, edgecolor="black")

plt.xlabel("RTT (ms)")
plt.ylabel("Frequency")
plt.title("RTT Latency Distribution")

plt.show()

plt.figure()

jitter_numbers = range(1, len(latencies))

plt.plot(
    jitter_numbers,
    jitter_values,
    marker="o"
)

plt.xlabel("Measurement")
plt.ylabel("Jitter (ms)")
plt.title("Jitter Measurements")
plt.grid(True)

plt.show()

jitter_outliers = []

for i in range(len(jitter_values)):
    if jitter_values[i] > 10:
        jitter_outliers.append(jitter_values[i])
        print(f"Measurement {i + 1} -> {i + 2}: {jitter_values[i]:.2f} ms")

sigma_outlier_rate = len(outliers) / len(latencies) * 100
iqr_outlier_rate = len(iqr_outliers) / len(latencies) * 100
jitter_outlier_rate = len(jitter_outliers) / len(jitter_values) * 100
print(f"Sigma outlier rate: {sigma_outlier_rate:.2f}%")
print(f"IQR outlier rate: {iqr_outlier_rate:.2f}%")
print(f"Jitter outlier rate: {jitter_outlier_rate:.2f}%")