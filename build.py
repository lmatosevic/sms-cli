import os
import shutil

shutil.rmtree('dist', ignore_errors=True)
os.system('python3 setup.py sdist bdist_wheel')
shutil.rmtree('sms_cli.egg-info', ignore_errors=True)
