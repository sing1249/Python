from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
print(soup.title)
span_tag = soup.find_all(name="span", class_="titleline") #To find the first a tag
article_text = []
article_link = []
for span in span_tag:
    a_tag = span.find(name="a")
    text = a_tag.getText()
    article_text.append(text)
    link =a_tag.get("href") #Will get the Href attribute value
    article_link.append(link)


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#List comprehension, that is called on the list as find_all returns a list. score will be used to loop through it and the new object is
#score.getText() on each list item. Same as running through each list.
#since the list for upvote give result as 30 points, we will use the split method. By default, it splits by the space between them.
# print(int(article_upvote[0].split()[0])) #Getting hold of the split number from the upvote

#print(article_text)
#print(article_link)
#print(article_upvote)
highest_upvote = max(article_upvote)
#print(highest_upvote)
highest_index = article_upvote.index(highest_upvote)
#print(highest_index)

#Getting hold of the corresponding article
popular_article = article_text[highest_index]
popular_link = article_link[highest_index]
print(f"The most popular article is {popular_article} - {popular_link} with {highest_upvote} upvotes.")
