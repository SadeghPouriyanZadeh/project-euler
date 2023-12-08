"""
Project Euler Problem Module
"""

import requests
from bs4 import BeautifulSoup


def get_euler_problem_text(
    problem_number: int,
    html_out: bool = False,
    timeout: float = 1000.0,
):
    """get the problem text by quering the number of the problem

    Args:
        problem_number (int): the number of the problem
        html_out (bool, optional): whether you want the html written out. Defaults to False.
        timeout (float, optional): the seconds for timeout in get request. Defaults to 1000.0.

    Returns:
        _type_: _description_
    """
    url = f"https://projecteuler.net/problem={problem_number}"
    headers = {"User-Agent": """Mozilla/5.0"""}
    response = requests.get(url=url, headers=headers, timeout=timeout)
    if response.status_code != 200:
        print(response)
    if html_out:
        with open("soup.html", "wb") as file:
            file.write(response.content)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find("div", class_="problem_content")
    problem_str = result.text
    return url, problem_str
