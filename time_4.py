import os
import time

start = time.time()
os.system("cd AlphaPose && python scripts/demo_inference.py --cfg config.yaml --checkpoint fast_421_res152_256x192.pth --indir /mnt/Media/Programming/Python/ML/data/test2017 --detbatch 1 --posebatch 1 --sp --vis_fast")
end = time.time()
print(end - start)