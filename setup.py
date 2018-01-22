from setuptools import setup
from setuptools import find_packages

desc = """\
SMS core
==============

Command line tool for sending AT (ATtention) commands via serial port to GSM shield module.
"""

setup(name="sms-core",
      version="1.0.0",
      author="luka",
      packages=find_packages(),
      install_requires=["pyserial", "argparse"],
      entry_points={
          'console_scripts': [
              'sms-core = core.main:main'
          ]
      },
      description="SMS core command line tool",
      long_description=desc)
