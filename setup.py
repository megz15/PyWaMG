from setuptools import setup, find_packages
from pypandoc import convert_file

VERSION = '1.1.2' 
DESCRIPTION = 'PyWaMG - WhatsApp Automator Bot'
with open('README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
        name="PyWaMG", 
        version=VERSION,
        author="Meghraj Goswami",
        author_email="meghgoswami835@gmail.com",
        url="https://github.com/megz15/PyWaMG",
        license='MIT',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Programming Language :: Python :: 3.0',
            'Operating System :: Microsoft :: Windows :: Windows 10',
            'License :: OSI Approved :: MIT License',
            'Intended Audience :: Developers',
            'Topic :: Communications :: Chat'
        ],
        packages=find_packages(),
        install_requires=[
            'msedge-selenium-tools',
            'selenium==3.141',
            'pillow==8.0.1',
            'webdriver-manager==3.3.0'
        ]
)