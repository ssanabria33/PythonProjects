"""
Challenge: Ensure that the function works correctly with tuples of different lengths.
=============================================
Description: Create a function called
concat_tuples that takes two tuples as input and returns a
new tuple containing all elements from both input tuples.

"""

def concat_tuples(tuple1, turple2):
    try:
        set1 = set(tuple1)
        set2 = set(tuple2)

        common = set1.intersection(set2)

        return list(common)

    except TypeError as e:
        print(f"TypeError: One or both tuples are not iterable: {e} ")
        return []

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

    print(concat_tuples([1,2,3,4,5], [3,4,5,6,7]))
