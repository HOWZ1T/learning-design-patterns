![builder uml](https://www.tutorialspoint.com/design_pattern/images/builder_pattern_uml_diagram.jpg)
###### Image sourced from (https://www.tutorialspoint.com/)
# Builder
### Builds a complex object using simple objects in a step by step approach
- ## Why
  - Separates construction of the complex object from its representation.
  - The Builder design pattern solves problems like:
    - How can a class (the same construction process) create different representations of a complex object?
    - How can a class that includes creating a complex object be simplified?
  - The intent of the Builder design pattern is to separate the construction of a complex object from its representation. <br> By doing so, the same construction process can create different representations.
- ## Some Use Cases
  - build meal orders for restaurants.
  - building complex objects like:
    - DOM
    - XML
    - HTML
    - etc.