import os
import time

start = time.time()
os.system("cd deep-high-resolution-net.pytorch && python demo/demo.py --image /mnt/Media/Programming/Python/ML/data/test2017")
end = time.time()
print(end - start)