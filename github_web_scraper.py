import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter a Github Username: ")
url = "https://github.com/"+github_user
r = requests.get(url)
soup = bs(r.content, "html.parser")
profile_image = soup.find("img", {'alt' : 'Avatar'})['src']
repoCount = soup.find("span", {'class' : 'Counter'})['title']

print("You entered "+github_user+" as the Github username.\n")
print("Here's the link to "+github_user+"'s profile picture: "+profile_image+"\n")
print(github_user+" has "+repoCount+" public repositiories!\n")


