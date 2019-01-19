import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
source = ['"C:\\My Documents"', 'C:\\Code']
# Example on Mac OS X and Linux:
# source = ['/Users/swa/notes']
# Notice we had to use double quotes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
# target_dir = '/Users/swa/backup'
# Remember to change this to which folder you will be using

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)   # make directory

# 3. The files are backed up into a zip file
# 4. The current day is the name of the subdirectory
# in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')

