"""Config Module for fmpdy."""
import os
import configparser


def load():
    """Loader of config (.ini) files for fmdpy."""
    config = configparser.ConfigParser()

    config['DEFAULT'] = {}

    config['UI'] = {
            'max_result_count': "10",
    }

    config['DL_OPTIONS'] = {
            'fmt': "native",
            'lyrics': "False",
            'bitrate': '250',
            'default_directory': "./",
            'multiple': '1',
    }

    config['API_KEYS'] = {
            'spotify_client_id': " bc18f68df9a64865bb34dbb381cd0faahi",
            'spotify_client_secret': "9b84af20ae3c48cebf64c7127f6f0933",
            'lyricsgenius'"",
    }

    config['STREAM'] = {
            'player_cmd': ['setsid', '-f', 'mpv', '$audio',
                '--cover-art-file=$cover',
                '--force-media-title=$title',
                '--really-quiet',
                '--oset-metadata-set=comment="a"', '--no-terminal'],
    }

    file_path = os.getenv('FMDPY_CONFIG_FILE') or \
        os.path.expanduser('~/.fmdpy.ini')

    if os.path.isfile(file_path):
        config.read(file_path)

    return config
