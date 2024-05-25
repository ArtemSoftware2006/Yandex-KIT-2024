#2001:0db8:285c:d98f:5535:69c1:3d59:d056 [15/03/2024:19:41:25 +0300] "GET /whales-are-amazing HTTP/1.0" 200 870773 0.2008 "Mozilla/5.0 (Windows NT 10.0;

import re
import sys
import math

def percentile(arr, n):
    k = (len(arr)-1) * n
    f = math.floor(k)
    c = math.ceil(k)
    if f==c:
        return arr[int(k)]
    d0 = arr[int(f)] * (c-k)
    d1 = arr[int(c)] * (k-f)
    return d0+d1

def find_first_greater(arr, n):
    for num in arr:
        if num > n:
            return num
    return None

input_lines = sys.stdin.readlines()

latencies = []
for line in input_lines:
    match = re.search(r'"\S+ .+?" (\d+) \d+ ([0-9.]+)', line)
    if match:
        latency = float(match.group(2))
        status_code = int(match.group(1))
        if status_code < 500:
            latencies.append(latency)


average_latency = percentile(latencies, 0.75)
latencies.sort()
procentel = find_first_greater(latencies, average_latency)
print(procentel)

