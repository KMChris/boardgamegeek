from setuptools import setup, find_packages

setup(
    name="boardgames",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "pandas",
        "numpy",
        "matplotlib",
        "selenium",
        "python-dotenv",
        "scikit-learn"
    ],
)
