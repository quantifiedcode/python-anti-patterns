# The Little Book of Python Anti-Patterns

This is an open-source book of **Python anti-patterns and worst practices**. Check out `docs/index.rst` for more information.

**Notice**: This is still (and will always be) a work-in-progress, feel free to contribute by suggesting improvements, adding new articles, improving existing ones, or translating this into other languages.

## PDF Version

You can find a PDF version of the book [here](./docs/The-Little-Book-Of-Python-Anti-Patterns.pdf).

## New articles
If you add new articles, please use the provided templates. Depending on the pattern you are creating, use either the [anti-pattern](templates/anti_pattern.rst) or the [migration-pattern](templates/migration_pattern.rst) template.

## Building the Documentation

To build the documentation, first install the required packages:

    pip install -r requirements.txt

Then, go to the `src` directory and run `make`:

    # HTML pages
    make html
    # PDF version
    make latexpdf

For the PDF version, you will need a working LaTeX installation (e.g. texlive).

You will find the updated documentation in the `docs` folder afterwards. You can clean the folder by running `make clean`.

## License

The book is made available under a Creative Commons Attribution-Non-Commercial-ShareAlike 4.0 license. This allows you to use and distribute it freely for your own non-commercial projects (e.g. for teaching) if you make your contributions available under the same license.

When using content from the book on your website or elsewhere, please add a visible link to [our website](http://docs.quantifiedcode.com/python-anti-patterns) or this Github project, so that your readers can easily find the original articles and make contributions.

Enjoy :)

![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png) This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
