#!usr/bin/env python3
#importing additional code to complete our task
import shutil
import os
#this will call operating system change directory 
os.chdir("/home/student/Mycode/")
#shutil.copy copys a single file 
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#shuntil.copytree copys folder, subfolders and files inside them as well
shutil.copytree("5g_research/", "5g_research_backup/")

