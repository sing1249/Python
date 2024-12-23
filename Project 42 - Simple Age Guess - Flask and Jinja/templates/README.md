# Flask Age and Gender Predictor App

This is a simple web application built using Flask and Jinja templating. The app uses two external APIs to predict the age and gender of a user based on their name. The results are displayed on dynamic web pages rendered with Jinja.

## Features

- **Dynamic Homepage**: Displays the current year and a randomly generated number.
- **Age and Gender Prediction**: Users can enter their name in the URL to get an estimated age and predicted gender.
- **Jinja Templating**: Dynamically renders HTML pages with data passed from Flask.
- **API Integration**: Fetches data from the [Agify API](https://agify.io/) and [Genderize API](https://genderize.io/) for predictions.

---

## How It Works

1. **Homepage**:
   - Navigate to the root URL (`/`) to view the homepage.
   - Displays:
     - A random number between 1 and 10.
     - The current year.

2. **Name-Based Prediction**:
   - Visit `/guess/<name>` (replace `<name>` with a name of your choice).
   - The app calls the following APIs:
     - [Agify API](https://agify.io): Predicts the age based on the name.
     - [Genderize API](https://genderize.io): Predicts the gender based on the name.
   - The predictions are rendered on a separate page using Jinja templates.

