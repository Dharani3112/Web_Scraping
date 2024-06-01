from bs4 import BeautifulSoup
import requests

x = input("Enter URL: ")
response = requests.get(x)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

title = soup.title.string
print(f"Title: {title}")
print()

para = soup.find_all('p')
print("First para: ")
print(para[1].get_text())
print()

links = soup.find_all(name = "a")
print("Link: ", )
for i in links:
    print(i.get("href"))
print()

images = soup.find_all(name = "img")
print("Images: ")
for i in images:
    print(i.get("src"))
print()