# IRCTC Website Automation

A Selenium-based automation project for the IRCTC (Indian Railway Catering and Tourism Corporation) website. This project demonstrates automated testing of train search functionality using Python and Selenium WebDriver.

## Features
- Automated train search
- Handling of dynamic elements and wait conditions
- Extraction of train details
- Results export to text file

## Prerequisites
- Python 3.x
- Chrome browser
- ChromeDriver (matching your Chrome version)

## Installation

1. Clone the repository
```bash
git clone git@github.com:RizwanGit01/irctc_selenium.git
```


## Usage

Run the tests using pytest:
```bash
pytest tests/irctc.py
```

## Test Flow
1. Launch IRCTC website
2. Handle notification popup
3. Enter source station ("from" location)
4. Enter destination station ("to" location)
5. Select travel date
6. Click search button
7. Extract train results
8. Save results to results.txt

## Project Structure
```
├── pages/
│   ├── tests.py
│   └── locators.py
├── tests/
│   └── irctc.py
└── results.txt
```

# Test case

1. Open the IRCTC website
2. Enter the "from" location
3. Select the first option for "from" location
4. Enter the "to" location
5. Select the first option for "to" location
6. Click on the date picker
7. Select the desired date
8. Click on the search button
9. Retrieve the search results
10. Print the results in a results.txt file



