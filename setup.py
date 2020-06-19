from setuptools import setup

setup(name='adbhoney',
        version='1.0.1',
        description='A low interaction honeypot for ADB Connections',
        url='https://github.com/huuck/ADBHoney',
        packages=['adbhoney', 'adbhoney.outputs'],
        entry_points={
        'console_scripts': [
            'adbhoney = adbhoney:main'
            ]
        },
        python_requires='>=3.6'
)
