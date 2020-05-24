import glob
import os
import shutil

SRC_DIR = "./src/"
DST_DIR = "./dst/"

for f in glob.glob(SRC_DIR + "*.txt"):
    src_fn = f[len(SRC_DIR):]
    ini = src_fn[:4]
    num = src_fn[-8:-4]
    ext = src_fn[-4:]
    
    if num[0] == "_":
        num = "0" + num[1:]
    num = str(int(num)+1).zfill(4)
    
    dst_fn = ini + num + ext
    print(SRC_DIR + src_fn + " -> " + DST_DIR + dst_fn)
    shutil.copy(SRC_DIR + src_fn, DST_DIR + dst_fn)
    
    # rename method delete original file
    # os.rename(SRC_DIR + src_fn, DST_DIR + dst_fn)
    