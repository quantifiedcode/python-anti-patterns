Working with json correctly
===================================================

When reading or writing json from/to a file-like object, don't use json.loads/json.dumps. The json module has respective methods to work with json from a file.

Anti-pattern
------------

.. code:: python

	# read from file-like
	with open("json_file.json") as json_file:
	  json_string = json_file.read()
	  dictionary = json.loads(json_string)

	# write to file-like
	dictionary = {"key": "value"}
	with open("json_file.json", "w") as json_file:
	  json_string = json.dumps(dictionary)
	  json.file.write(json_string)

Best practice
-------------
  When read/write to file-like objects use the json respective method load/dump instead of using loads/dumps.

  .. code:: python

  	# read from file-like
  	with open("json_file") as json_file:
  	  dictionary = json.load(json_file)

  	# write to file-like
  	dictionary = {"key": "value"}
  	with open("json_file.json", "w") as json_file:
  	  json.dump(dictionary, json_file)

References
----------

- `http://chimera.labs.oreilly.com/books/1230000000393/ch06.html#_solution_95`
