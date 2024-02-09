from setuptools import setup

setup(
    name='CLCTool',
    version='0.1',
    py_modules=['clctool'],
    install_requires=[
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'clctool = clctool:main',
        ],
    },
    long_description="""
    CLCTool - Custom Linux configuration tool
    ========================================

    Little but powerful.

    """,
    long_description_content_type='text/x-rst',
)
