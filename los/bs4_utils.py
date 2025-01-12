from bs4 import BeautifulSoup


def print_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # 불필요한 CSS 제거
    for tag in soup(["style", "link", "code"]):  # style 태그와 link 태그 제거
        tag.decompose()

    pretty_hhtml = soup.prettify()
    print(pretty_hhtml)
    return pretty_hhtml
