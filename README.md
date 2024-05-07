# Data-Structures-And-Object-Oriented-Design

This repo includes most homework and lab assignments from the data structures & object-oriented design class

# Mod 1 Lab - Basic Python

## Part 1 – Solo – hello.py
3)	Click the `mod_1_lab` subdirectory on the left-hand sidebar to expand it. You should see 4 files:
    * `hello.py` - a file you will modify shortly
    * `Mod1Lab.md` - the markdown version of these instructions (viewable in Mimir)
    * `Mod1Lab.pdf` - the pdf version of these instructions (not viewable in Mimir)
    * `stats.py` - a file you will modify shortly

    Click `hello.py` to open it in a text editor.

4) Add the following to hello.py :
```python
print("Hello World!")
```
 
## Part 2 – Group – stats.py

### stats.py
Implement 4 functions:
* `compute_mean(collection, n)`
   * Returns the mean of all items `collection` rounded to `n` decimal points (hint - look up "rounding in Python") 

* `compute_median(collection)`
   * Returns the median of all items in `collection`
   * When there are an even number of items, return the lower of the two middle numbers. This is how we will define the median in algorithms throughout this course.

* `compute_mode(collection)` 
   * Returns the mode of all items in `collection`
   * When there are multiple potential modes, return the lowest 

* `compute_stats(collection)`
   * Returns a three-tuple of the mean, median, and mode of a collection
## External Modules
**Do not use any imported modules (`math`, `collections`, ...) when implementing functionality.** It is okay to use imported modules for testing.

It is okay to import modules you write yourself; e.g. any data structures you write yourself.
