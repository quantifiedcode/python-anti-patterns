Very high complexity
^^^^^^^^^^^^^^^^^^^^

Functions and classes with high complexity are empirically correlated with higher error
rates and bugs. In addition, they are often hard to understand, maintain and extend.
Avoid them whenever possible.

How to measure complexity?
""""""""""""""""""""""""""

While perceived complexity is highly subjective, several standard metrics have been proposed to
measure it. **Cyclomatic complexity** (or `cc`) is probably the most widely used metrict today:
It measures the number of possible code execution paths that a function call might take at runtime.

How complex is too complex?
"""""""""""""""""""""""""""


Solution Strategies 
"""""""""""""""""""

To reduce function complexity, apply the following strategies:

* Reduce the number of tasks per function: Each function should be responsible for one single,
  well-specific task only. This is often called the **single-responsibility-principle**.
* Keep the number of arguments low. If possible, avoid functions with more than two mandatory
  arguments.
* Factor out a well-defined task within the function to an external function. 
  If the given task is only used by the original function, you may define the helper function
  within the body of the original function: This increases readability while keeping related
  functionality together.
* Use existing function libraries to reduce complexity: Python provides excellent
  libraries for many common container types as well as tasks such as sorting and searching. 
  Familiarise yourself with these libraries and make use of them.
  For example, `collections` and `itertools` provide algorithms and data types for a large range
  of common problems encountered in programming.

