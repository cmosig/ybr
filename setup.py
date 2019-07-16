from setuptools import setup
setup(
    name='ybr',
    version='0.3',
    entry_points={
        'console_scripts': [
            'ybr=ybr:main'
        ]
    }
)
