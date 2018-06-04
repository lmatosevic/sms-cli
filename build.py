import os
import shutil


os.system('python3 setup.py sdist bdist_wheel')
shutil.rmtree('sms_cli.egg-info')
