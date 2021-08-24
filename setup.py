from setuptools import setup

setup(
    name='rr',
    version='1.0.0',
    packages=['rr'],
    url='',
    license='',
    author='thedjaney',
    author_email='thedjaney@gmail.com',
    description='Measure respiratory rate',
    entry_points={
        'console_scripts': [
            'rr=rr.command:main'
        ]
    }
)
