'''Check yout routes on your website and checks if they return error'''
from os import listdir
import requests

#Get route from app.py file
def get_route_app():
    route = []
    try:
        with open("app.py") as app:
            route = [line[line.find("/")+1:].rstrip("')\n") for line in app.readlines() if "@app.get" in line]
        return route
    except FileNotFoundError:
        print("Python script is in wrong folder move it to /var/www/flaga/")


#Get route from templates/*.html files
def get_route_html():
    try:
        html_pages = [page.rstrip(".html") for page in listdir("templates")]
        return html_pages
    except FileNotFoundError:
        print("Python script is in wrong folder move it to /var/www/flaga/")

#Get information about your domain name from setting.ini file
def get_domain():
    try:
        with open("settings.ini") as settings:
            line = settings.readlines()[1]
            domain = line[line.find("=") + 2:]
        return domain
    except FileNotFoundError:
        print("Python script is in wrong folder move it to /var/www/flaga/")


if __name__ == "__main__":
    domain = get_domain()
    for route in set(get_route_app() + get_route_html()):
        address = f'http://{domain}/{route}'
        response = requests.get(address)
        print(f'{route} give {response}')
