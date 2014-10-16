:fa:`puzzle-piece` Maintainability
==================================

A program is **maintainable** if it is easy to understand and modify the code even for someone
that is unfamiliar with the code base. Maintainability is intertwined, but more than readability.

Use the following patterns to increase maintainability and avoid creating `spaghetti code`.

.. toctree::
    :maxdepth: 1

    duplicate_key_in_dictionary
    from_module_import_all_used
    Loop var shadows import <import_module_shadowed_by_loop_variable>
    Name assigned but never used <local_variable_name_is_assigned_to_but_never_used>
    module_imported_but_not_used
    Not enough format string args <not_enough_arguments_for_format_string>
    not_using_with_to_open_files
    redefining_built-in
    redefinition_of_unused_name
    Multiple function return types <returning_more_than_one_variable_type_from_function_call>
    single_responsibility_principle
    the_loop_may_never_terminate
    Too many format string args <too_many_arguments_for_format_string>
    undefined_name_in_all
    unused_import
    Unused wildcard import <unused_import_from_wildcard_import>
    unused_variable
    Possible undefined loop var <using_possible_undefined_loop_variable>
    using_the_global_statement
    very_complex_function
    wildcard_import
