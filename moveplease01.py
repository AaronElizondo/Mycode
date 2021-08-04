#!usr/bin/env python3

import shutil
import os

#change to directory of Mycode
os.chdir('/home/student/Mycode')

#move file to destination of choice
shutil.move('raynor.obj', 'ceph_storage/')
#prompting for a new file name
xname=input ('What is the new name for kerrigan.obj?')
shutil.move('ceph_storage/kerrigan.obj','ceph_storage/' + xname)

