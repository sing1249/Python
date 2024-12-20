# Flask Number Guessing Game

This repository contains a simple Flask web application where users guess a number between 1 and 9. Based on their input, the app provides feedback, including whether the guess was too high, too low, or correct. The app also includes an exciting GIF-based user experience!

## Features
- A random number between 1 and 9 is generated at the start of each session.
- Users can guess the number by entering an integer in the URL.
- The app uses GIFs to visually show the result of the user's guess.
- The heading color changes randomly on each page load, creating a dynamic user interface.

## How It Works
1. When you visit the root URL (`/`), the page displays a prompt to guess a number between 1 and 9 along with a fun GIF.
2. When you visit a URL with an integer (e.g., `/5`), the app checks if the number matches the randomly generated number. It returns:
   - A success message with a celebratory GIF if the number is correct.
   - A message indicating that the guess is too high or too low along with an appropriate GIF.
3. The app uses a decorator to randomly change the color of the heading for each user request.

## Decorators in Use

In this app, a **decorator** is used to add dynamic styling to the page's heading. The decorator, `color_heading`, is applied to the `user_number` route to change the color of the `<h1>` heading each time a user visits the page.

### How the Decorator Works:
- The `color_heading` decorator function wraps around the `user_number` function.
- The decorator selects a random color from a predefined list of colors (Red, Blue, Green, Yellow, Purple, Orange, Pink, Black, Brown).
- The `user_number` function is executed, and the result is wrapped in an `<h1>` tag with a random color applied to it.
