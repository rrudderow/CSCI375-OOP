# CSCI375-Final

| Basic Info | --- |
| --- | ---|
| Course: | CSCI375 - OOP and Design Patterns |
| Semester: | Fall 2024 |
| Instructor: | Dr. Ram Basnet |
| Students: | Aidan Meens, Renee Rudderow, Cody Stoffel |
| Repository | https://github.com/rrudderow/CSCI375-OOP |
| How to Run | ```python3 main.py``` |
| How to Test | ```make all``` |

# Final Project
| Name | Value |
| --- | --- |
| Name: | Warehouses System |
| Description: | Creates a system of warehouses for user organization |
| Due Date: | 12/03/24 |
| Status: | Complete |
| Location: | https://github.com/rrudderow/CSCI375-OOP |
| Self Grade | 110/100 |
| Judges Grade | 50/45 |
| Notes: | Completed all the requirements, passed tests with ~99% coverage, went above and beyond with a CLI |

# Group Objectives

## Aidan Meens
Adian worked on the Warehouse class and printing out things in the CLI. He created the Iterator patterns used throughout the code.

## Renee Rudderow
Renee worked on the Item class, as well as the Subject and Observer classes, which were used to create the Observer pattern. She added functions to the Warehouse and CLI classes in order to facilitate the Observer pattern.

## Cody Stoffel
Cody wrote the CLI class and created the Command Line Interface that the user interacts with, as well as the Warehouses class. He also set up the Singleton Pattern for both the Warehouses and CLI classes.

## Design Patterns
The three OOP design patterns we chose are the Singleton, the Iterator, and the Observer patterns. Together these design patterns have allowed us to create an efficient inventory management system with an intuitive user interface through the command line.

The Singleton pattern is used in both the CLI and Warehouses classes. This ensures that both classes only have one instance, so that the user will only be interacting with one CLI and so that all individual warehouses are routed through the same place. This allows for the individual warehouses to be a part of a greater system, which facilitates communication between them. This means that an item can be moved from one warehouse to another easily and efficiently.

The Iterator pattern allows sequential access to the elements of a collection without exposing its underlying structure. We are using the Iterator to dynamically count the number of items in each warehouse and to count anye duplicates of items. We also use the Iterator to iterate through a list of a given warehouse's items and to iterate through the list of individual warehouses.

The Observer pattern is being used to automatically update the price of an item in all places where the item may reside. If an instance of an item is being watched by multiple different observers, then the all observers will be notified of the item's price change.
