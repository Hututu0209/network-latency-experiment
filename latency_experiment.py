import time
import urllib.request

url = "https://www.baidu.com"

results = []

for i in range(30):
    start = time.perf_counter()

    try:
        urllib.request.urlopen(url, timeout=5)

        end = time.perf_counter()
        latency = (end - start) * 1000

        results.append(latency)

        print(f"第 {i+1:02d} 次：{latency:.2f} ms")

    except Exception as e:
        print(f"第 {i+1:02d} 次：请求失败")


print("\n===== 实验结果 =====")

if results:
    print(f"测量次数：{len(results)}")
    print(f"最小值：{min(results):.2f} ms")
    print(f"最大值：{max(results):.2f} ms")
    print(f"平均值：{sum(results) / len(results):.2f} ms")