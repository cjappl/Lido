# -----------------------------------------------------------------------------
# Author: Chris Apple
# Last Edited: 10/11/15
# Description: Song class, contains error checking for incorrect files
# TODO:
# -----------------------------------------------------------------------------

ACCEPTABLE_FILE_TYPES = ['.mp3', '.wav']


class Song:

    def __init__(self, file_path):
        self._file_path = self._init_file_path(file_path)

    @property
    def file_path(self):
        """ Getter method for file_path """
        return self._file_path

    def _init_file_path(self, file_path):
        """ Sets file path initially, checks if file extension is correct

        Params:
            file_path : str, file path of song to import

        Returns:
            file_path : str, if the string ends in ACCEPTABLE_FILE_TYPES

        Raises:
            TypeError : if song is not in ACCEPTABLE_FILE_TYPES
        """

        file_path_lower = file_path.lower()

        for file_type in ACCEPTABLE_FILE_TYPES:
            if file_path_lower.endswith(file_type):
                return file_path
        else:
            raise TypeError('Filetype not accepted: %s' % file_path)
