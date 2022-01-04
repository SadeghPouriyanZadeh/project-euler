import requests
from bs4 import BeautifulSoup

def euler_problem(problem_number, html_out=False):
    url = f"https://projecteuler.net/problem={problem_number}"
    headers = {"User-Agent": """Mozilla/5.0"""}
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        print(response)
    if html_out:
        with open("soup.html", "wb") as file:
            file.write(response.content)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find("div", class_="problem_content")
    problem_str = result.text
    print(problem_str)
    return url

