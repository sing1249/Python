import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
titles = [title.get_text() for title in soup.find_all(name="h3", class_="title")]
ordered_list = titles[::-1]


with open("movies.txt", "w") as file:
    for item in ordered_list:
        file.write(f"{item}\n")

