# TIP-AND-TAX-BILL-CALCULATOR
Program where you input your subtotal and it will automatically calculate your total bill with 15% tip rate and 12% tax rate

## Overview

This is a beginner Python project I built while learning programming through my own practice

The program calculates the total cost of a bill by automatically applying a **12% tax** and a **15% tip** to a user-provided subtotal. It also accepts subtotal values with or without a dollar sign by automatically removing the currency symbol before performing the calculations.

The goal of this project was to practice using functions, mathematical calculations, user input, and formatting numerical output.

---

## Features

* Accepts a bill subtotal from the user.
* Automatically removes a leading dollar sign (`$`) if included.
* Calculates a **12% tax**.
* Calculates a **15% tip**.
* Computes the final bill total.
* Displays the tax, tip, and total bill in a clean currency format.

---

## Concepts Practiced

* User-defined functions
* Function decomposition
* Returning values with `return`
* User input (`input()`)
* String methods

  * `.lstrip()`
* Type conversion (`float()`)
* Percentage calculations
* Floating-point arithmetic
* Formatted output using f-strings

---

## Purpose

This project was created as a learning exercise to practice organizing a program into smaller, reusable functions while performing real-world calculations.

Rather than writing everything in a single block of code, the program separates calculations, formatting, and output into individual functions to improve readability and organization.

---

## Current Limitations

This is an introductory learning project and has several intentional limitations:

* Does not validate whether the user enters a valid numeric value.
* Does not display a custom error message for invalid input.
* Uses fixed tax and tip percentages.
* Supports only a single bill calculation per program execution.

---

## Possible Future Improvements

* Add user-friendly error handling for invalid input.
* Allow users to customize the tax and tip percentages.
* Split the bill among multiple people.
* Support multiple currencies.
* Generate an itemized receipt.
* Allow repeated calculations without restarting the program.
* Create a graphical user interface or web version.

---

## Learning Notes

This project is part of my programming learning journey. The objective was to strengthen my understanding of Python functions, percentage calculations, user input processing, and organizing code into smaller, reusable components while building a practical utility.
