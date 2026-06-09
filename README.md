# :)

you're going to write a program that

- makes HTTP requests to a public website (wikipedia) and parse the data you get in response to make additional requests
- makes the program accessible through a web page
- displays clickable links on the web page


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

## python start

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
        - ex. `\w+\-\d\d*` matches a bunch of letters, a hyphen, and then 1 or 2 digits. like `blahblah-1`
    - https://regex101.com/ this is what I use to test regular expressions
- commit

## webapp start

at this point it's important to understand the basics of http

- https://medium.com/@secshubhamsharma/the-http-basics-to-advanced-beginner-friendly-guide-to-how-the-web-works-816ed26017e8
- https://www.tomshardware.com/how-to/use-wget-download-files-command-line for testing http requests in your terminal
    - on linux I would use curl most of the time, it's a bit simpler

some links that might be helpful in setting up the flask app

- [set up a flask app](https://www.geeksforgeeks.org/python/flask-creating-first-simple-application/)
- [render some data in html with a common templating format](https://enkledesigns.com/how-to-get-a-table-to-display-in-flask/)
- [more templating documentation](https://jinja.palletsprojects.com/en/stable/templates/)
