from bs4 import BeautifulSoup
import requests
import time

visited = []

def find_picture():
    html_text = requests.get("https://unsplash.com/collections/12276674/cat").text
    soup = BeautifulSoup(html_text, "lxml")
    imgs = soup.find_all('img', class_ = "YVj9w")
    for _, img in enumerate(imgs):
        source = img['src']
        if source not in visited:
            visited.append(source)
            with open(f'Projects\Web Scraping\posts\Cat Picture.txt', 'a+') as f:
                f.write(f'{source} \n')

if __name__ == '__main__':
    while True:
        find_picture()
        time_wait = 10
        print(f'Waiting {time_wait} seconds')
        time.sleep(time_wait)