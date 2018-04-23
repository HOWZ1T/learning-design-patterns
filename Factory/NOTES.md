![factory uml](https://www.tutorialspoint.com/design_pattern/images/factory_pattern_uml_diagram.jpg)
###### Image sourced from (https://www.tutorialspoint.com/)
# Factory
### The Factory method lets a class defer instantiation it uses to subclasses.
- ## Why
  - The Factory Method design pattern solves problems like:

    - How can an object be created so that subclasses can redefine which class to instantiate?
    - How can a class defer instantiation to subclasses?

- ## Some Use Cases
  - In the case of: we know when to create an object but the type of object remains undecided or it will be decided by dynamic parameters.
  - [Project Zomboid](https://github.com/gzhernov/project-zomboid/blob/master/src/zombie/characters/traits/TraitFactory.java) uses factories to create items etc.