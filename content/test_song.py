# -----------------------------------------------------------------------------
# Author: Chris Apple
# Last Edited: 10/11/15
# Description: Tests for Song class
# Run from: Lido Folder, otherwise there may be path errors
# Run with: py.test
# TODO:
# -----------------------------------------------------------------------------


import pytest
import os
from content.song import Song


@pytest.fixture
def setup_IAO():
    """ Setup for the path to 'I Am One' song """
    return os.path.join('test_songs', 'easy_names', 'I Am One.mp3')


@pytest.fixture
def setup_txt():
    """ Setup for the path to 'bad_text.txt', TypeError """
    return os.path.join('test_songs', 'bad_files', 'bad_text.txt')


def test_song_init(setup_IAO):
    """ Tests normal song initializaiton """

    song_filepath = setup_IAO
    test_song = Song(song_filepath)

    assert test_song.file_path == song_filepath


def test_song_init_type_error(setup_txt):
    """ Tests that Song with throw TypeError with .txt input """
    txt_file_path = setup_txt

    with pytest.raises(TypeError):
        test_song = Song(txt_file_path)
