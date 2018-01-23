import os
import shutil


os.system('python3 setup.py sdist')
shutil.rmtree('sms_cli.egg-info')
