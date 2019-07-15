from setuptools import setup
setup(
    name='ybr',
    version='0.1',
    entry_points={
        'console_scripts': [
            'ybr=ybr:main'
        ]
    }
)
