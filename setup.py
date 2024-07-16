from setuptools import setup, find_packages

setup(
    name='imagic',
    version='0.1.2',
    py_modules=['imagic'],
    install_requires=[
        'rich',
        'google',
        'pillow'
    ],
    entry_points='''
        [console_scripts]
        imagic=imagic:main
    ''',
)
