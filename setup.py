from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'PyWaMG - WhatsApp Automator Bot'
LONG_DESCRIPTION = 'PyWaMG is a simple python library to automate sending messages and files on WhatsApp'

setup(
        name="PyWaMG", 
        version=VERSION,
        author="Meghraj Goswami",
        author_email="meghgoswami835@gmail.com",
        url="https://github.com/megz15/PyWaMG",
        license='MIT',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
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
            'pillow==8.0.1'
        ]
)