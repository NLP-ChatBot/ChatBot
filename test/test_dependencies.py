# imports
import ipykernel
import matplotlib
import nltk
import pandas
import PySide6


def test_package_version() -> None:
    
    # looping through each
    # package
    for pack, version in zip(
        (ipykernel, matplotlib, nltk, pandas, PySide6),
        ('6.23.0', '3.7.1', '3.8.1', '2.0.1', '6.5.0')
        ):
        assert pack.__version__ == version
