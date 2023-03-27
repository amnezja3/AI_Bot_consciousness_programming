from bs4 import BeautifulSoup
from requests import get


def search(term, num_results=10, lang="en", proxy=None):
    print(term)
    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36'}

    def fetch_results(search_term, number_results, language_code):
        escaped_search_term = search_term.replace(' ', '+')
        number_results = number_results + 1
        google_url = f'https://www.google.com/search?q={escaped_search_term}&num={number_results}&hl={language_code}'
        proxies = None
        if proxy:
            if proxy[:5]=="https":
                proxies = {"https":proxy} 
            else:
                proxies = {"http":proxy}
        
        response = get(google_url, headers=usr_agent, proxies=proxies)
        response.raise_for_status()
        return response.text

    def parse_results(raw_html):
        soup = BeautifulSoup(raw_html, 'html.parser')
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            link = result.find('a', href=True)
            title = result.find('h3')
            if link and title:
                yield link['href']

    html = fetch_results(term, num_results, lang)
    return list(parse_results(html))
