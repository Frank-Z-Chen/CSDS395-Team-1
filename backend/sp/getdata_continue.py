import os
import sys
from shutil import copyfile
import util

pwd = util.sp_address_extension(os.getcwd()) 
name = sys.argv[1]
cat = sys.argv[2]
modi = pwd +'/temp/' + cat + '_' + name.split(".")[0] + '_temp.png'
read = pwd + '/' + 'read.py'

if (os.path.isfile(pwd + '/data/' + cat + '_' + name.split("/")[-1].split(".")[0] + '_temp_learn.csv')): # wait until learn.csv return， if 方便调试
        os.system("python %s" %(read + ' ' +  modi + ' ' + cat))