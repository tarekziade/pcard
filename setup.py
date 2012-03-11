import os
from setuptools import setup, find_packages


requires = ['bottle']


setup(name='pcard',
      version='0.1',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      [console_scripts]
    pcard = pcard.gen:main
    """,
)
