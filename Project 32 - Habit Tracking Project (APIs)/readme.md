# Habit Tracking Project with Pixela API

This project demonstrates how to use the Pixela API to track daily habits, specifically focused on meditation time. The project involves creating a user, setting up a graph to track meditation minutes, posting data to the graph, updating the data, and deleting data when needed.

## Project Overview

The script uses Python's `requests` library to interact with the Pixela API. Here's what the script does:

1. **User Creation**: The script creates a new user on Pixela using the provided token and username.
2. **Graph Creation**: It sets up a graph to track the number of minutes spent meditating. The graph is configured to record floating-point numbers with a unit of "minutes".
3. **Posting Data**: It posts daily data (meditation time) to the graph.
4. **Updating Data**: The script demonstrates how to update previously posted data.
5. **Deleting Data**: It deletes the data for the current day.

### Features

- **User Creation**: The script creates a user on Pixela for habit tracking.
- **Graph Setup**: A custom graph is created for tracking meditation time.
- **Data Tracking**: The script allows you to track your meditation minutes and update or delete data as needed.
  
