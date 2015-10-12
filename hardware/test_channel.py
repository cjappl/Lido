from pydub import AudioSegment

import pytest
import numpy as np
import os
from hardware.channel import Channel 

BEATS_PER_PHRASE = 64
BEATS_PER_BAR = 4
BARS_PER_PHRASE = 16

I_AM_ONE_BPM = 120
I_AM_ONE_BPS = 120 / 60
IAO_START_TIME = .065 * 1000  # exact time of first beat in ms
IAO_PATH = os.path.join(os.getcwd(), "Lido", "test_songs", "easy_names", "I Am One.mp3")

@pytest.fixture
def setup_channel_A():
    return Channel("A")


@pytest.fixture
def setup_CDJ_A():
    return dumb_CDJ()

def test_channel_id(setup_channel_A):
    channel_A = setup_channel_A
    assert channel_A.id_string == "A"

