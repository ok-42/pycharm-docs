import sys
import webbrowser


def main():
    """Construct URL for Python documentation web page.

    URL examples:

    pandas:
    - root: https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html

    numpy:
    - root: https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html
    - module: https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html
    """

    text: str = sys.argv[1]
    print(text)

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
        function = text
        url = f'https://docs.python.org/3/library/functions.html#{function}'

    webbrowser.open(url)
