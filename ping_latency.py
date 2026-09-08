import subprocess
import re
import statistics
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

target = "www.baidu.com"
results = []

for i in range(30):
    command = ["ping", "-n", "1", target]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    match = re.search(r"时间[=<](\d+)ms", result.stdout)

    if match:
        latency = float(match.group(1))
        results.append(latency)
        print(f"第 {i+1:02d} 次：{latency:.0f} ms")
    else:
        print(f"第 {i+1:02d} 次：请求失败")


print("\n===== RTT 实验结果 =====")

if results:
    print(f"测量次数：{len(results)}")
    print(f"最小值：{min(results):.0f} ms")
    print(f"最大值：{max(results):.0f} ms")
    print(f"平均值：{statistics.mean(results):.2f} ms")
    import matplotlib.pyplot as plt

plt.plot(range(1, len(results) + 1), results, marker="o")
plt.xlabel("测量次数")
plt.ylabel("RTT (ms)")
plt.title("网络 RTT 测量结果")
plt.grid(True)

plt.show()
