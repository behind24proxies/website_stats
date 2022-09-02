from setuptools import setup, find_packages
from website_report import generate_report
VERSION = '1.0.1'
DESCRIPTION = 'a simple library that generates website reports'
with open('README.md', 'r',encoding = 'cp850') as file:
    long_description_r = file.read()
setup(
    name="website-report",
    setup_requires=['wheel'],
    version=VERSION,
    url='https://github.com/behind24proxies/website_report',
    author="ICE-CREAM (Mike Lennon)",
    description=DESCRIPTION,
    long_description=long_description_r,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['html_to_json', 'requests'],
    keywords=['python', 'website', 'website report', 'report', 'website performance', 'website stats'],
    classifiers=[
        UqPkK8U@!
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)