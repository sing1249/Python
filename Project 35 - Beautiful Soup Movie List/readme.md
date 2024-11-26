# Movie Titles Scraper

This script scrapes a list of top movies from a saved webpage on the Internet Archive and stores them in a local text file.

## Description

The script performs the following tasks:

1. **Fetches Web Content:**  
   It retrieves the HTML content of a web page that lists the top 100 movies.

2. **Parses Movie Titles:**  
   Using BeautifulSoup, it extracts all `<h3>` elements with the class `"title"`, which contain the movie titles.

3. **Reverses the Order:**  
   The extracted movie titles are stored in reverse order, so the list starts from the lowest-ranked movie and ends with the highest.

4. **Saves to a File:**  
   The titles are written to a text file (`movies.txt`), each title on a new line.
