# Joker Poker
This project contains a simple version of the game Joker Poker. All information needed about the project can be found below.
## Project Documentation
#### [Functional Specification](https://github.com/JesseHantula/ot-harjoitustyo/blob/master/documentation/functionalspecification.md)
#### [Worktime Accounting](https://github.com/JesseHantula/ot-harjoitustyo/blob/master/documentation/worktimeaccounting.md)
#### [Architecture](https://github.com/JesseHantula/ot-harjoitustyo/blob/master/documentation/architecture.md)
#### [Changelog](https://github.com/JesseHantula/ot-harjoitustyo/blob/master/documentation/changelog.md)
#### [User Manual](https://github.com/JesseHantula/ot-harjoitustyo/blob/master/documentation/usermanual.md)
## Project Releases
#### [Week 5](https://github.com/JesseHantula/ot-harjoitustyo/releases/tag/Week5)
#### [Week 6](https://github.com/JesseHantula/ot-harjoitustyo/releases/tag/Week6)
## Set-up
Install dependencies with:

`poetry install`

To run the game, clone the repository and go to the poker directory. From there, run the following command: 

`poetry run invoke start`

## Testing
Run tests with:

`poetry run invoke test`

## Code Coverage
Run code coverage with:

`poetry run invoke coverage-report`

The coverage report will be available in the htmlcov directory, the file name being index.html.
## Pylint
Run pylint with:

`poetry run invoke lint`

This will show the quality of the code, and any errors or warnings.