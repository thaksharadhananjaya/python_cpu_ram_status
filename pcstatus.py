import psutil

print("---PC Status---")

print("CPU Usage: ", psutil.cpu_percent(1), "%")
print("Total RAM: ", round(psutil.virtual_memory()[0]/2**30, 2), "GB") # 2**30 --> 2^30 for convert byte to Giga Byte
print("RAM Usage: ", round(psutil.virtual_memory()[3]/2**30, 2), "GB")
print("Available RAM: ", psutil.virtual_memory()[1])
print("RAM Usage Percent: ", psutil.virtual_memory()[2], "%\n")