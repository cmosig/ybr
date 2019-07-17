from setuptools import setup
setup(
    name='ybr',
    version='0.3',
    install_requires=[
        'bs4',
        'pandas',
        'tabulate'
        ],
    entry_points={
        'console_scripts': [
            'ybr=ybr:main'
        ],
    }
)
