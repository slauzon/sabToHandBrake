#!/usr/bin/env python
from commands import getoutput
import os
import string
import sys

valid_extensions = ['.mkv','.avi','.mpg','.ts','.wmv']
valid_chars = '-_.' + string.ascii_letters + string.digits
options = '-e x264 -f mp4 -Z "High Profile"'

def parse(directory):
  filename = ''
  items = os.listdir(directory)
  for item in items:
    abspath = os.path.join(directory, item)
    if (os.path.isdir(abspath)):
      parse(abspath)
    else:
      if (os.path.splitext(item)[1] in valid_extensions) and item.lower().find('sample') == -1 and item.lower().find('SAMPLE') == -1 and item.find('.mp4') == -1 and item.find('.m4v') == -1:
        filename = ''.join(c for c in item.replace(' ','.') if c in valid_chars)
        renamecmd = r'mv "' + os.path.join(directory, item) + '" "' + os.path.join(directory, filename) + '"'
        getoutput(renamecmd)
        cmd = r'cd "' + directory + '" && HandBrakeCLI -i ' + filename + ' -o ' + '.'.join(filename.split('.')[:-1]) + '.mp4 ' + options + ' > ' + '.'.join(filename.split('.')[:-1]) + '.log && rm ' + filename
        print(cmd)
        getoutput(cmd)

try:
  parse(os.sys.argv[1])
except Exception, e:
  open('/root/errors.txt','w').write(str(e))
