# Задание: Напишите программу или однострочник, который покажет, сколько памяти и сколько
# физических ядер есть в системе, на которой запущен тест. Информацию следует доставать из
# /proc, потому что каких-то специфичных приложений может не оказаться.
# Для памяти ответ дайте в килобайтах, для процессоров - в штуках. Считаем, что килобайт
# 1024 байта (== кибибайт).
# -
# Например, для 1-гигабайтного сервера с 8 ядрами ответ должен выглядеть так:
# 1048576
# 8
# Задача может быть решена частично (например, можно посчитать только память или только
# количество ядер), тогда вы получите за решение часть баллов. В этом случае достаточно
# просто вернуть одно полученное число.
# Максимальный балл за эту задачу - 40.

def get_memory_info():
    with open('/proc/meminfo') as f:
        for line in f:
            if line.startswith('MemTotal'):
                total_memory_kb = int(line.split()[1])
                break
    return total_memory_kb

def get_cpu_cores():
    with open('/proc/cpuinfo') as f:
        cpu_cores = 0
        for line in f:
            if line.startswith('processor'):
                cpu_cores += 1
    return cpu_cores

memory_kb = get_memory_info()
cpu_cores = get_cpu_cores()

print(memory_kb)
print(cpu_cores)