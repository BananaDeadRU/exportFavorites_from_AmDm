import re
import requests
from bs4 import BeautifulSoup
import time
import random
import os

class AmDm:

    @staticmethod
    def get_chords_block(url):
        print(f"Fetching chords from: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()  # Проверка статуса ответа
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return None, None
        
        soup = BeautifulSoup(response.content, "html.parser")
        content_block = soup.find("div", class_="b-podbor__text")
        title = soup.find("title").get_text() if soup.find("title") else "song"
        
        if content_block:
            for link in content_block.find_all("link", href=True):
                if "/cs/app/5.2/css/app_old.css" in link["href"]:
                    link["href"] = "style/style.css"
            
            html_content = str(content_block)
            return html_content, title
        else:
            print(f"No content block found at {url}")
            return None, title

    def get_favorites_chords(self, favorites_url):
        print(f"Fetching favorites from: {favorites_url}")
        try:
            response = requests.get(favorites_url)
            response.raise_for_status()  # Проверка статуса ответа
        except requests.RequestException as e:
            print(f"Failed to fetch {favorites_url}: {e}")
            return []
        
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", class_="items")
        if not table:
            print("No table with class 'items' found.")
            return []
        
        artist_links = table.find_all("a", class_="artist")

        song_links = [link for link in artist_links if re.search(r'/\d+/', link['href'])]

        if not song_links:
            print(f"No song links found in the table.")
            return []

        chords_blocks = []
        errors = []

        for link in song_links:
            full_url = link['href']
            print(f"Full URL: {full_url}")  
            html_content, title = self.get_chords_block(full_url)
            if html_content:
                match = re.search(r'/akkordi/[^/]+/([^/]+)/', full_url)
                if match:
                    song_name = match.group(1)
                else:
                    song_name = title 
                
                chords_blocks.append({
                    'url': full_url,
                    'html': html_content,
                    'title': title,
                    'name': song_name
                })
            else:
                errors.append(full_url)
            time.sleep(random.uniform(0.5, 1.5))

        if errors:
            print("The following URLs failed to fetch:")
            for error_url in errors:
                print(error_url)

        return chords_blocks

def save_chords_to_files(chords_data, save_path):
    html_path = os.path.join(save_path, "html")
    if not os.path.exists(html_path):
        os.makedirs(html_path)
        print(f"Directory created: {html_path}")
    
    navigate_links = []

    for song in chords_data:
        sanitized_title = re.sub(r'[^\w\s]', '', song['title']).strip()
        readable_title = re.sub(r'\s+', ' ', sanitized_title).title()
        file_name = f"{song['name']}.html"
        file_path = os.path.join(html_path, file_name)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("<html><head><title>{}</title><link rel='stylesheet' href='style/style.css'></head><body>".format(song['title']))
            file.write(song['html'])
            file.write("</body></html>")
        print(f"Saved chords to {file_path}")

        navigate_links.append({
            'title': song['title'],
            'file': file_name
        })

    navigate_file_path = os.path.join(save_path, "navigate.html")
    with open(navigate_file_path, 'w', encoding='utf-8') as navigate_file:
        navigate_file.write("<html><head><title>Каталог</title></head><body>")
        navigate_file.write("<h1>Выгруженные песни:</h1>")
        navigate_file.write("<ul>")
        for link in navigate_links:
            navigate_file.write(f'<li><a href="html/{link["file"]}">{link["title"]}</a></li>')
        navigate_file.write("</ul>")
        navigate_file.write("</body></html>")
    
    print(f"Navigation file saved to {navigate_file_path}")

print('def succeeded')


amdm = AmDm()
username_site = input("Введите имя пользователя: ")
favorites_url = "https://amdm.j119.ru/users/" + username_site + "/favorites/"
chords_data = amdm.get_favorites_chords(favorites_url)

if chords_data:
    save_path = os.path.join(os.path.expanduser("~"), "Desktop", "amdm")
    save_chords_to_files(chords_data, save_path)
else:
    print("No chords data found.")
print('debug2')
