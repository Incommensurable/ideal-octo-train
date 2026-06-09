# :)

you're going to make a program that

- makes HTTP requests to a public website (wikipedia) and parse the data you get in response to make additional requests
- make the program accessible through a web page
- display clickable links on the web page


## project setup

- make sure python is installed
- set up poetry as a dependency manager [documentation](https://python-poetry.org/docs/basic-usage/#initialising-a-pre-existing-project)
    - `pip install poetry` to install the tool
    - `poetry init` to set up the files that it's going to use
    - add this to pyproject.toml to tell poetry that it won't be packaged and published
        ```
        [tool.poetry]
        package-mode = false
        ```

    - `poetry add requests` to add a dependency

    - now make sure it works. either [activate a virtual environment](https://python-poetry.org/docs/managing-environments/#activating-the-environment) or do `poetry run python` to open an interpreter? this might take a bit of massaging
- commit your work so far
