import logging
import sys
import webbrowser


def make_logger():
    logger = logging.getLogger('log')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt='%(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def main():
    """Construct URL for Python documentation web page.

    URL examples:

    pandas:
    - root: https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html

    numpy:
    - root: https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html
    - module: https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html
    """

    log = make_logger()

    text: str = sys.argv[1]
    log.info(f'{text=}')

    libraries: dict[str, str] = {
        'np': 'numpy',
        'pd': 'pandas',
    }

    # Function from an imported library
    if '.' in text:

        library_alias: str
        submodules: list[str]
        function: str

        library_alias, *submodules, function = text.split('.')
        try:
            library_name = libraries[library_alias]
        except KeyError:
            library_name = library_alias

        if library_name == 'pandas':
            url = f'https://pandas.pydata.org/docs/reference/api/pandas.{function}.html'
        elif library_name == 'numpy':
            url = f'https://numpy.org/doc/stable/reference/generated/numpy.{".".join(submodules + [function])}.html'
        else:
            return

    # Built-in function
    # TODO add built-in libraries
    else:
        library_name = 'built-in'
        submodules = ['']
        function = text
        url = f'https://docs.python.org/3/library/functions.html#{function}'

    log.debug(f'{library_name=}')
    log.debug(f'{submodules=}')
    log.debug(f'{function=}')

    webbrowser.open(url)
