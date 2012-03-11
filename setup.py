import os
from setuptools import setup, find_packages


requires = ['bottle']


setup(name='pcard',
      version='0.1',
      author="Tarek Ziade",
      description="Generates a Password card",
      author_email="tarek@ziade.org",
      packages=find_packages(),
      include_package_data=True,
      licence='MIT',
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      [console_scripts]
    pcard = pcard.gen:main
    """,
)
