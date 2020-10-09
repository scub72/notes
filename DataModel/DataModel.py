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
            'User-defined functions': "",
            'Instance methods': "",
            'Generator functions': "",
            'Coroutine functions': "",
            'Asynchronous generator functions': "",
            'Built-in functions': "",
            'Built-in methods': "",
            'Classes': "",
            'Classes Instances': ""
        },
        'Modules': "",
        'Custom classes': "",
        'Custom instances': "",
        'I/O objects': "",
        'Internal types': "",
    }

    def python_types(self):
        print(self.python_types_array.keys())
