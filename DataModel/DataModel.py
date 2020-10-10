import numpy


class DataModel:
    python_types_array = {
        'None': "type with single value for signing the absence of value; its value is false",
        'NotImplemented': "type with single value; numeric and comparison methods should return "
                          "this value if do not implement operation",
        'Ellipsis': "'...' is used to omit the words ",
        'numbers.Number': {
            "numbers.Integral": " Integers(int) and Booleans(bool)",
            "numbers.Real": "double precision floating point numbers",
            "Complex": "a pair of floating point numbers with z.real and z.imag parts"
        },
        'Sequences': {
            'Immutable': {
                'Strings': "sequence of Unicode points; "
                           "all points are in range U+0000 - U+10FFFF can be represented by string"
                           "python doesnt have char type"
                           "every code point is represented by string object with length 1"
                           "Built in functions:"
                           "ord() - converts code point from string form to integer in range 0-10FFFF"
                           "chr() converts integer in range 0-10FFFF to string object with length 1"
                           "str.encode() converts a str to bytes using given text encoding"
                           "bytes.decode() converts bytes to str",
                'Tuples': "python object inside parentheses '()' ",
                'Bytes': "immutable array 8 bit bytes represented by integers in range 0<=x<256"
                         "bytes literals (like b'abc') and the built-in bytes() constructor can be used"
                         "to create bytes objects"
                         "bytes objects can be decoded to strings via decode()"
            },  # unchangeable after creation
            'Mutable': {
                'Lists': "the items of list are python objects"
                         "list is formed by objects comma-separated inside square brackets",
                'Byte Arrays': "mutable array"
                               "created by bytearray()"
                               "mutable and unhashable"
                               "provide same interface and funcionality as immutable bytes objects"
            }  # changeable after creation
        },
        'Set types': {

            """ 
                Represents unordered finite set of unique, immutable objects. 
                Cannot be indexed by any subscript.
                Can be iterated over, 
                The built-in function len() returns the number of items
                
                Set types usage: 
                    fast membership testing, 
                    removing duplicates from sequence, 
                    computing mathematical operations as intersection, union, difference, symmetric difference
            """

            'Sets': "Represent a mutable set"
                    "created by the built-in set() constructor"
                    "can be modified afterwards by several methods, such as add()",
            'Frozen set': "Represent an immutable set"
                          "created by the built-in frozenset() constructor"
                          "is immutable and hashable"
                          "can be used again as an element of another set, or as a dictionary key."
        },
        'Mappings': {
            """
                Represent finite sets of objects indexed by arbitrary index sets
                The subscript notation a[k] selects the item indexed by k from the mapping a;
                this can be used in expressions and as the target of assignments or del statements
                len() returns the number of items in a mapping.
            """
            'Dictionaries': "Represent finite sets of objects indexed by nearly arbitrary values"
                            "The only types of values not acceptable as keys are values containing lists or "
                            "dictionaries or other mutable types that are compared by value rather "
                            "than by object identity,"
                            "Dictionaries requires a key’s hash value to remain constant"
                            "If two numbers compare equal (e.g., 1 and 1.0) then they can be used interchangeably "
                            "to index the same dictionary entry."
                            "Dictionaries:"
                            " preserve insertion order,"
                            " Replacing an existing key does not change the order"
                            " removing a key and re-inserting it will add it to the end "
                            ""
                            "Dictionaries are mutable; they can be created by the {...} notation "
                            "The extension modules dbm.ndbm and dbm.gnu provide additional examples of mapping types, "
                            "as does the collections module."
        },
        'Callable types': {
            'User-defined functions': "Functions defined by user eg. function()"
                                      "you can check following attributes of the function"
                                      "__doc__ - documentation written under function name"
                                      "__name__ - function name"
                                      "__qualname__ - function qualified name"
                                      "__module__ - function module name"
                                      "__defaults__ - tuple of default values of arguments"
                                      "__code__ - code object representing compiled function body"
                                      "__globals__ - the global namespace of the module in which the function "
                                      "             was defined."
                                      "__dict__ - The namespace supporting arbitrary function attributes."
                                      "__closure__"
                                      "__annotations__"
                                      "__kwdefaults__",
            'Instance methods': "methods called with the class object eg. Class.instance_method()"
                                "you can check the function attributes like with user-defined functions"
                                "eg. Class.instance_method.__doc__ etc.",
            'Generator functions': "Function or method which uses the yield statement"
                                   "Such a function, when called, always returns an iterator object"
                                   "When the function executes a return statement or falls off the end, "
                                   "a StopIteration exception is raised and the iterator will have reached "
                                   "the end of the set of values to be returned.",
            'Coroutine functions': "Function or method which is defined using async def is called a coroutine function. "
                                   "Such a function, when called, returns a coroutine object. "
                                   "It may contain await expressions, as well as async with and async for statements.",
            'Asynchronous generator functions': "Function or method which is defined using async def and which uses the "
                                                "yield statement "
                                                "Such a function, when called, returns an asynchronous iterator object "
                                                "which can be used in an async for statement to execute the body of "
                                                "the function"
                                                "Calling the asynchronous iterator’s aiterator.__anext__() method will "
                                                "return an awaitable which when awaited will execute until it provides "
                                                "a value using the yield expression. When the function executes an "
                                                "empty return statement or falls off the end, a StopAsyncIteration "
                                                "exception is raised and the asynchronous iterator will have reached "
                                                "the end of the set of values to be yielded.",
            'Built-in functions': " Examples of built-in functions are len() and math.sin() "
                                  "(math is a standard built-in module)",
            'Built-in methods': "This is really a different disguise of a built-in function, this time containing an "
                                "object passed to the C function as an implicit extra argument. An example of a "
                                "built-in method is alist.append(), assuming alist is a list object. In this case, the "
                                "special read-only attribute __self__ is set to the object denoted by alist.",
            'Classes': "Classes are callable. These objects normally act as factories for new instances of themselves, "
                       "but variations are possible for class types that override __new__(). The arguments of "
                       "the call are passed to __new__() and, in the typical case, to __init__() to initialize "
                       "the new instance.",
            'Classes Instances': "Instances of arbitrary classes can be made callable by defining a __call__() "
                                 "method in their class."
        },
        'Modules': "Modules are a basic organizational unit of Python code, and are created by the import system as "
                   "invoked either by the import statement, or by calling functions such as importlib.import_module() "
                   "and built-in __import__(). A module object has a namespace implemented by a dictionary object "
                   "(this is the dictionary referenced by the __globals__ attribute"
                   "Special read-only attribute: __dict__ is the module’s namespace as a dictionary object."
                   "Custom class types are typically created by class definitions ",
        'Custom classes': "A class object can be called "
                          "to yield a class instance",
        'Custom instances': "A class instance is created by calling a class object (see above). A class instance has "
                            "a namespace implemented as a dictionary which is the first place in which attribute "
                            "references are searched. When an attribute is not found there, and the instance’s class "
                            "has an attribute by that name, the search continues with the class attributes. If a class "
                            "attribute is found that is a user-defined function object, it is transformed into an "
                            "instance method object whose __self__ attribute is the instance.",
        'I/O objects': "A file object represents an open file. "
                       "Various shortcuts are available to create file objects: "
                       "open() built-in function, "
                       "os.popen(), "
                       "os.fdopen(), "
                       "makefile() method of socket objects (and perhaps by other functions or methods provided "
                       "by extension modules). "
                       ""
                       "The objects sys.stdin, sys.stdout and sys.stderr are initialized to file objects corresponding "
                       "to the interpreter’s standard input, output and error streams; they are all open in text mode "
                       "and therefore follow the interface defined by the io.TextIOBase abstract class.",
        'Internal types': {
            'Code objects': "Code objects represent byte-compiled executable Python code, or bytecode. "
                            "The difference between a code object and a function object is that the function "
                            "object contains an explicit reference to the function’s globals "
                            "(the module in which it was defined), while a code object contains no context; "
                            "also the default argument values are stored in the function object, not in the code "
                            "object (because they represent values calculated at run-time). Unlike function objects, "
                            "code objects are immutable and contain no references (directly or indirectly) to mutable "
                            "objects.",
            'Frame objects': "Frame objects represent execution frames. They may occur in traceback objects , "
                             "and are also passed to registered trace functions.",
            'Traceback objects': "Traceback objects represent a stack trace of an exception. A traceback object is "
                                 "implicitly created when an exception occurs, and may also be explicitly created by "
                                 "calling types.TracebackType.",
            'Slice objects': "Slice objects are used to represent slices for __getitem__() methods. "
                             "They are also created by the built-in slice() function.",
            'Static method objects': "Static method objects provide a way of defeating the transformation of function "
                                     "objects to method objects described above. A static method object is a wrapper "
                                     "around any other object, usually a user-defined method object. When a static "
                                     "method object is retrieved from a class or a class instance, the object actually "
                                     "returned is the wrapped object, which is not subject to any further "
                                     "transformation. Static method objects are not themselves callable, although the "
                                     "objects they wrap usually are. Static method objects are created by the built-in "
                                     "staticmethod() constructor.",
            'Class method objects': "A class method object, like a static method object, is a wrapper around another "
                                    "object that alters the way in which that object is retrieved from classes and "
                                    "class instances. The behaviour of class method objects upon such retrieval is "
                                    "described above, under “User-defined methods”. Class method objects are created "
                                    "by the built-in classmethod() constructor"
        },
    }


    def python_types(self):
        print(self.python_types_array.keys().__len__())


dm = DataModel().python_types()
print(dm)



