.. Python Code Patterns documentation master file, created by
   sphinx-quickstart on Fri Jul 25 15:49:10 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive. 

***************************************
The Little Book of Python Anti-Patterns
***************************************

|
|

.. image:: snake_warning.png
  :width: 200pt
  :align: center

|
|


:github_badge:`quantifiedcode/python-code-patterns`

Welcome, fellow Pythoneer! This is a small book of Python  **anti-patterns** and **bad practices**.

Learning about these anti-patterns will help you to avoid them in your own code and make you
a better programmer (hopefully). Each pattern comes with a small description, examples and
possible solutions.

Why did we write this?
----------------------

**Short answer**: We think that you can learn as much from reading bad code as you can from reading good one.


**Long answer**: There is an overwhelming amount of Python books that show you how to do things by focusing on 
best practices and examples of good code. There are only very few books out there that show you how **not** to do things. We wanted to change that by providing you with an **anti-book** that
teaches you things which you should **never** do in practice. 

Who are we?
-----------

We're `QuantifiedCode`_, a Berlin-based startup. Our mission
is to help everyone to write better code, faster! Our first product is an `online tool`_ for
automated, data-driven code review. When building this tool, we learned a lot about code quality
in Python and decided to compile our knowledge into this book.

.. _QuantifiedCode: https://www.quantifiedcode.com/
.. _online tool: https://www.quantifiedcode.com/

References
----------

Whenever we cite an anti-pattern from another source we tried including the link to the original
article on the bottom of the page. If you should have missed one, please feel free to add it
and make a pull request on Github. Thanks!

Licensing
---------

This document is licensed under a creative-commons NC license, so you can use the text freely
for non-commercial purposes and adapt it to your needs. The only thing we ask in return is the
inclusion of a link to this page on the top of your website, so that your readers will be able to
find the content in its original form and possibly even contribute to it.

Contributing
------------

If you think this collection can be improved or extended, please contribute! You can do this by
simply forking our Github project and sending us a pull request once you're done adding your changes.
We will review and merge all pull requests as fast as possible and be happy to include your name on
the list of authors of this document.

Index Of Patterns
-----------------

.. toctree::
    :glob:
    :maxdepth: 2

    maintainability/index
    readability/index
    security/index
    performance/index
    correctness/index
