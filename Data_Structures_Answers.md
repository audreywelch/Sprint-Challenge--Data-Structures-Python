Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

2. What is the space complexity of your ring buffer's `append` function?

3. What is the runtime complexity of your ring buffer's `get` method?

4. What is the space complexity of your ring buffer's `get` method?


5. What is the runtime complexity of the provided code in `names.py`?
    > The runtime is O(n * m), (but I think we would just say, O(n^2)), with `n` referring to the elements in `names_1` and `m` referring to the elements in `names_2`. The worst case scenario would be iterating through all of the elements in `n` AND all of the elements in `m`.

6. What is the space complexity of the provided code in `names.py`?
    >  Because I am creating a new array with the duplicates, the worst case is that every name in `names_1` is also in `names_2`, and the space that would be taken up is the space of whichever is smallest, `n` or `m`. So the space complexity would be O(n).

7. What is the runtime complexity of your optimized code in `names.py`?
    > The optimized code has two for-loops, but they aren't nested, so the runtime would be O(2 * n), but the number of inputs becomes insignificant, so we ignore the constant and it becomes O(n).

8. What is the space complexity of your optimized code in `names.py`?
    > The space complexity for my optimized code is worse than the original code. In addition to allocating an array to hold the duplicates, it also allocates the storage for a dictionary to hold key, value pairs for one of the dictionaries. So the Space complexity would be O(n + n)
