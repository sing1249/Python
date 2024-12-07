# Cookie Clicker Automation with Selenium

This project automates the gameplay of the [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/) game using Python and Selenium. The script automatically clicks the cookie and buys upgrades based on the available money in the game.

## Project Overview

The goal of the project is to simulate the automatic clicking of cookies and purchasing of upgrades in the Cookie Clicker game. The script uses Selenium WebDriver to interact with the game by:

1. Continuously clicking the cookie to generate more money.
2. Monitoring the available money and buying upgrades when affordable.

## Features

- **Automated Cookie Clicking**: The script simulates repeated clicks on the cookie to accumulate cookies.
- **Upgrade Management**: It tracks available upgrades and purchases the most expensive upgrade affordable with the current cookies.
- **Dynamic Upgrade Selection**: The script evaluates all available upgrades and buys the most expensive one within the current budget.
- **Automatic Refresh of Upgrades**: Upgrades are checked and purchased every 5 seconds to optimize gameplay.
