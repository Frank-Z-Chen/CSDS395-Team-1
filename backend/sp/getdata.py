import os
import sys
from shutil import copyfile
import util

pwd = util.sp_address_extension(os.getcwd()) 
name = sys.argv[1]
cat = sys.argv[2]
target = pwd + '/temp/' + cat + '_' + name
source = pwd + '/figure/' + name
temp = target + '/' + cat + '_' + name
modi = pwd +'/temp/' + cat + '_' + name.split(".")[0] + '_temp.png'
rd = pwd + '/roughdata/' + cat + '_' + name.split(".")[0] + '_rough.csv'
copyfile(source,target)
process = pwd + '/' + 'process.py'
ocr = pwd + '/' + 'ocr.py'
read = pwd + '/' + 'read.py'
learn = pwd + '/' + 'learn.py'

os.system("python %s" %(ocr + ' ' +  target))
os.system("python %s" %(process + ' ' +  target))
os.system("python %s" %(ocr + ' ' +  modi))
if (os.path.isfile(pwd + '/model/' + cat + '.pkl')):
    os.system("python %s" %(learn + ' ' + modi + ' ' + cat))

# wait til the user alter the roughdata


if (os.path.isfile(pwd + '/data/' + cat + '_' + name.split("/")[-1].split(".")[0] + '_temp_learn.csv')): # wait until learn.csv return， if 方便调试
        os.system("python %s" %(read + ' ' +  modi + ' ' + cat))


# store final attributes

