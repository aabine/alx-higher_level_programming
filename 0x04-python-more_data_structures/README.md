# 0x04. Python - More Data Structures: Set, Dictionary

In this lesson, we will learn about the set and dictionary data structures in Python.

## Set

A set is an unordered collection of unique elements. Sets are mutable, meaning that they can be changed after they are created.

To create a set, you can use the `set()` function. For example:


my_set = set([1, 2, 3, 4])
```

This creates a set called `my_set` that contains the numbers 1, 2, 3, and 4.

You can add elements to a set using the `add()` method. For example:

```
my_set.add(5)
```

This adds the number 5 to the set `my_set`.

You can remove elements from a set using the `remove()` method. For example:

```
my_set.remove(4)
```

This removes the number 4 from the set `my_set`.

You can check if an element is in a set using the `in` operator. For example:

```
if 5 in my_set:
    print("5 is in the set")
```

This will print the following output:

```
5 is in the set


## Dictionary

A dictionary is a collection of key-value pairs. Dictionaries are mutable, meaning that they can be changed after they are created.

To create a dictionary, you can use the `dict()` function. For example:


my_dict = dict()
```

This creates an empty dictionary called `my_dict`.

You can add key-value pairs to a dictionary using the `update()` method. For example:

```
my_dict.update({"name": "John Doe", "age": 30})
```

This adds the key-value pairs `"name": "John Doe"` and `"age": 30` to the dictionary `my_dict`.

You can get the value for a key in a dictionary using the `get()` method. For example:

```
name = my_dict.get("name")
```

This will assign the value of the key `"name"` to the variable `name`.

You can check if a key is in a dictionary using the `in` operator. For example:

```
if "name" in my_dict:
    print("The key 'name' is in the dictionary")
```

This will print the following output:

```
The key 'name' is in the dictionary
```