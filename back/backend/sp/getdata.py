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
ori = pwd +'/temp/' + cat + '_' + name
modi = pwd +'/temp/' + cat + '_' + name.split(".")[0] + '_temp.png'
rd = '/roughdata/' + cat + '_' + name.split(".")[0] + '_rough.csv'
copyfile(source,target)
process = pwd + '/' + 'process.py'
ocr = pwd + '/' + 'ocr.py'
read = pwd + '/' + 'read.py'
learn = pwd + '/' + 'learn.py'
rect = pwd + '/' + 'rect.py'

os.system("python %s" %(ocr + ' ' +  target))
os.system("python %s" %(process + ' ' +  target))
os.system("python %s" %(ocr + ' ' +  modi))
if (os.path.isfile(pwd + '/model/' + cat + '.pkl')):
    os.system("python %s" %(learn + ' ' + modi + ' ' + cat))

os.system("python %s" %(rect + ' ' +  ori + ' ' + '/' + rd))

# wait til the user alter the roughdata


# store final attributes

