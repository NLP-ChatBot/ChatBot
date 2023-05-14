# imports
import matplotlib
import nltk
import pandas
import PySide6
import sklearn
import wordcloud


def test_package_version() -> None:
    
    # looping through each
    # package
    for pack, version in (
            (matplotlib, '3.7.1'),
            (nltk, '3.8.1'),
            (pandas, '2.0.1'),
            (PySide6, '6.5.0'),
            (sklearn, '1.2.2'),
            (wordcloud, '1.9.1.1')
        ):
        assert pack.__version__ == version
