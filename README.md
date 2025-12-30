# Digital Library – Mini Project (Part 4 & 5)

## Objective
This project implements a simple digital library system using Object-Oriented Programming in Python.

## Features
- Add and manage books
- Register users
- Borrow and return books
- Display library state

## Project Structure
library_project
│
├── src/
│   ├── book.py
│   ├── user.py
│   ├── loan.py
│   ├── library.py
│   └── main.py
│
├── uml/
│   └── library_diagram.puml
│
├── README.md
└── git_commands.txt
The system is designed using Object-Oriented Programming principles.
The Book class represents a library resource and stores its identity and availability.
The User class represents a library member and only contains identification information, respecting the single responsibility principle.
The Loan class models the borrowing process by linking a book to a user. A loan remains active until the book is returned, which allows representing both borrowing and returning operations within the same object.
The Library class acts as the central controller of the system. It manages all collections (books, users, loans) and enforces business rules such as availability checks and borrowing constraints.
This design ensures clear responsibility separation, modularity, and coherence between the UML diagram and the Python implementation


## Technologies
- Python
- Object-Oriented Programming
- PlantUML

## How to Run
```bash
cd src
python main.py