from setuptools import setup
from setuptools import find_packages

desc = """\
SMS-cli
==============

Command line interface for sending AT (ATtention) commands via serial port to GSM shield module.
"""

setup(name="sms-cli",
      version="1.0.0",
      author="luka",
      author_email="lukamatosevic5@gmail.com",
      packages=find_packages(),
      install_requires=["pyserial", "argparse"],
      entry_points={
          'console_scripts': [
              'sms-cli = cli.main:main'
          ]
      },
      description="SMS command line interface tool",
      long_description=desc)
