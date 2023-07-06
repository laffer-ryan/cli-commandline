from setuptools import setup, find_packages

setup(
    name="jformat",
    version="0.0.1",
    description="reformat file from stdout",
    install_requires = ["click", "colorama"],
    entry_points="""
    [console_scripts]
    jformat=jformat.main:main
    """,
    author="Ryan Lafferty",
    author_email="lafferty.ryan10@gmail.com",
    packages=find_packages(),
)