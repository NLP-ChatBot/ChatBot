# imports
import matplotlib
import nltk
import pandas
import PySide6
import pymongo
import sklearn
import torch
import wordcloud


def test_package_version() -> None:
    
    # looping through each
    # package
    for pack, version in (
            (matplotlib, '3.7.1'),
            (nltk, '3.8.1'),
            (pandas, '2.0.1'),
            (PySide6, '6.5.0'),
            (pymongo, '4.3.3'),
            (sklearn, '1.2.2'),
            (torch, '1.13.1+cu117'),
            (wordcloud, '1.9.1.1')
        ):
        assert pack.__version__ == version
