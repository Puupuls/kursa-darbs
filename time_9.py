import os
import time

start = time.time()
os.system("cd ViTPose &&  python demo/top_down_img_demo_with_mmdet.py --img-root ../../data/test2017/ demo/mmdetection_cfg/ssdlite_mobilenetv2_scratch_600e_coco.py https://download.openmmlab.com/mmdetection/v2.0/ssd/ssdlite_mobilenetv2_scratch_600e_coco/ssdlite_mobilenetv2_scratch_600e_coco_20210629_110627-974d9307.pth configs/wholebody/2d_kpt_sview_rgb_img/topdown_heatmap/coco-wholebody/vipnas_res50_coco_wholebody_256x192_dark.py https://download.openmmlab.com/mmpose/top_down/vipnas/vipnas_res50_wholebody_256x192_dark-67c0ce35_20211112.pth")
end = time.time()
print(end - start)