Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
    > My runtime complexity is O(1) because I am simply replacing an item by the index and then resetting a variable.

2. What is the space complexity of your ring buffer's `append` function?
    > The space complexity is O(1) because the amount of memory that is being used is constant and does not depend on the data that is being processed. No matter how many elements are in the array, the memory for this function won't change depending on that number.

3. What is the runtime complexity of your ring buffer's `get` method?
    > The runtime is O(n) because I am iterating through each element in the storage array to check if it is None.

4. What is the space complexity of your ring buffer's `get` method?
    > I think the space complexity is O(n) because with the list comprehension I am creating an array/list with the `n` number of elements in my storage, if they are not equal to none. So worst case, none of them are equal to none, and it creates a list with `n` items.

5. What is the runtime complexity of the provided code in `names.py`?
    > The runtime is O(n * m), (but I think we would just say, O(n^2)), with `n` referring to the elements in `names_1` and `m` referring to the elements in `names_2`. The worst case scenario would be iterating through all of the elements in `n` AND all of the elements in `m`.

6. What is the space complexity of the provided code in `names.py`?
    >  O(1) b/c no additional space is allocated.

7. What is the runtime complexity of your optimized code in `names.py`?
    > The optimized code has two for-loops, but they aren't nested, so the runtime would be O(2 * n), but the number of inputs becomes insignificant, so we ignore the constant and it becomes O(n).

8. What is the space complexity of your optimized code in `names.py`?
    > The space complexity for my optimized code is worse than the original code. In addition to allocating an array to hold the duplicates, it also allocates the storage for a dictionary to hold key, value pairs for one of the dictionaries. So the Space complexity would be O(n + n)
