# :)

you're going to make a program that

- makes HTTP requests to a public website (wikipedia) and parse the data you get in response to make additional requests
- make the program accessible through a web page
- display clickable links on the web page


## project setup

- make sure python and git are installed
- set up poetry as a dependency manager [documentation](https://python-poetry.org/docs/basic-usage/#initialising-a-pre-existing-project)
    - `pip install poetry` to install the tool
    - `poetry init` to set up the files that it's going to use
    - add this to pyproject.toml to tell poetry that it won't be packaged and published
        ```
        [tool.poetry]
        package-mode = false
        ```
    - `poetry add requests` to add a dependency
    - now make sure it works. either [activate a virtual environment](https://python-poetry.org/docs/managing-environments/#activating-the-environment) or do `poetry run python` to open an interpreter I think. this might take a bit of massaging
    - this might be a good time to talk about shells? just to sortof explain what the virtual environment is doing
    - if this doesn't work we can do it manually with the virtualenv package
- commit your work so far

## project start

- write a function that accepts the name of an article as an argument and returns the contents
    - https://www.mediawiki.org/wiki/API:Get_the_contents_of_a_page
    - https://docs.python-requests.org/en/latest/index.html
- commit
- update the function to search for links in the wiki article and return them
    - you probably want to use regular expressions for this. regular expressions are a format for expressing text patterns. python has a library for loading these patterns and using them to parse text
    - https://docs.python.org/3/howto/regex.html
        - the basics:
        - `() [] + ^ . * \` are special characters that have syntactical meaning
            - `()` is a capturing group
            - `[]` is to indicate one of several characters. e.g `[a-z]` means any character from a-z
            - `.` means any character
            - `+` means 1 or more of something. e.g `.+` means one or more character
            - `*` means 0 or more of something
            - `\` is an escape character. `\\` means one literal `\`, `\n` means a newline
            - `^` is the start of a line/string
        - `\w \s \d` are common shorthands for characters
            - `\w` means any uppercase or lowercase letter (not including accented chracters)
            - `\s` means any whitespace (tab, space, newline)
            - `\d` means a digit (0-9)
        - `\w+\-\d\d*` matches a bunch of letters, a hyphen, and then 1 or 2 digits. `blahblah-1`
    - https://regex101.com/ this is what I use to test regular expressions
- commit
