#!/usr/bin/env python
from commands import getoutput
import os
import string
import sys

valid_extensions = ['.mkv','.avi','.mpg','.ts','.wmv']
valid_chars = '-_.' + string.ascii_letters + string.digits
options = '-e x264 -f mp4 -Z "High Profile"'

try:
  path = os.sys.argv[1]
  filename = ''
  for file in os.listdir(path):
    if (os.path.splitext(file)[1] in valid_extensions) and file.lower().find('sample') == -1 and file.lower().find('SAMPLE') == -1 and file.find('.mp4') == -1 and file.find('.m4v') == -1:
      filename = ''.join(c for c in file.replace(' ','.') if c in valid_chars)
      #getoutput('mv "' + path + '/' + file + '" ' + path + '/' + filename)
      cmd= r'cd "' + path + '" && HandBrakeCLI -i ' + filename + ' -o ' + '.'.join(filename.split('.')[:-1]) + '.mp4 ' + options + ' > ' + '.'.join(filename.split('.')[:-1]) + '.log && rm ' + filename
      print(cmd)
      #getoutput(cmd)
except Exception, e:
  open(path + '/root/errors.txt','w').write(str(e))
