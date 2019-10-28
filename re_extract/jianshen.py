import requests

def get_pg_src(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        resp.encoding = resp.apparent_encoding
        return resp.text
    return ''

def parse(src):
    from lxml import etree
    html = etree.HTML(src)
    # article = html.xpath('//article[@class="article"]/p/text()')[0]
    title = html.xpath('//article[@class="article"]/p[@data-role="original-title"]/text()')
    content_list = html.xpath('//article[@class="article"]//p/text()')
    return title, content_list
    # return article


def _parse_with_bs(src):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(src,features='lxml')
    # print(soup.title)
    print(soup.get_text())
    pass


if __name__ == "__main__":
    src = get_pg_src('https://www.sohu.com/a/308488304_120132390')
    # # print(src)
    # # article = parse(src)
    # title, content = parse(src)
    # print('title is ', title[0])
    # print('content is ', ''.join(content))
    # # print('article is ', article)

    _parse_with_bs(src)
