cpp-examples
============

Intro C++ examples


### Exercise 1.

Write a command line program that will:
* Take a filename of an ascii file as an argument (you can use the Holmes.txt example provided)
* Load that ascii file.
* Count the number of occurrences of unique words (this should be case and punctuation insensitive. Limit punctuation to following characters appear somewhere in a word = <code>.,?'"!():</code> (hint: you will need a backslash escape character for the double-quote)
* Write out a results file containing the unique words and the number of uses in descending order of usage, e.g.
 Word    Usage
 
 which           55
 holmes          48
 there           32
 could           25
 photograph      21
 ...

### Exercise 2.
Write a command line program that:
* Has classes to allow number of shapes to be defined: square (side1), rectangle(side1, side2), circle(radius), triangle(height, width).
  * Each shape class should know it's type ("Square"), how many sides it has.
  * Each shape needs to be able to calculate it's perimeter and area.
* Within the Main method create a variety of the shapes and put them in a std::vector
* Create a class ShapeSorter which should contain five methods
  * Print out the Shapes that match a chosen type
  * Print out the Shapes that match a chosen number of sides
  * Print out the Shapes in order of volume descending
  * Print out the Shapes in order of perimeter descending
