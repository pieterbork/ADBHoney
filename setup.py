from setuptools import setup

setup(name='adbhoney',
        version='1.0.0',
        packages=['adbhoney', 'adbhoney.outputs'],
        entry_points={
        'console_scripts': [
            'adbhoney = adbhoney:main'
            ]
        },
)
