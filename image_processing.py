from  PIL import Image
import glob

INPUT_FILE = "input.png"
SRC_DIR = "./src/"

TMP_SIZE = (890, 185)
TMP_PASTE = (1, 0)
TMP_FNAME = "tmp.png"
TMP_DIR = "./tmp/"

ENL_SIZE = (1068, 222)
ENL_FNAME = "enl.png"
ENL_DIR = "./enl/"

NINE_SIZE = (666, 222)
NINE_CROP = (201, 0, 867, 222)
NINE_FNAME = "nine.png"
NINE_DIR = "./nine/"

SEVEN_SIZE = (518, 222)
SEVEN_CROP = (275, 0, 793, 222)
SEVEN_FNAME = "seven.png"
SEVEN_DIR = "./seven/"

for f in glob.glob(SRC_DIR + "*.png"):
    fn = f[len(SRC_DIR):]
    img_org = Image.open(SRC_DIR + fn)
    print("read : " + SRC_DIR + fn)
    
    img_tmp = Image.new("RGB", TMP_SIZE, (0, 0, 0))
    img_tmp.paste(img_org, TMP_PASTE)
    img_tmp.save(TMP_DIR + fn)
    print("write : " + TMP_DIR + fn)
    
    img_enl = img_tmp.resize(ENL_SIZE, Image.LANCZOS)
    img_enl.save(ENL_DIR + fn)
    print("write : " + ENL_DIR + fn)
    
    img_nine = img_enl.crop(NINE_CROP)
    img_nine.save(NINE_DIR + fn)
    print("write : " + NINE_DIR + fn)
    
    img_seven = img_enl.crop(SEVEN_CROP)
    img_seven.save(SEVEN_DIR + fn)
    print("write : " + SEVEN_DIR + fn)
    