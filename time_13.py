import os
import time

start = time.time()
os.system("OmniPose &&  python inference.py --cfg experiments/coco/omnipose_w48_384x288.yaml")
end = time.time()
print(end - start)