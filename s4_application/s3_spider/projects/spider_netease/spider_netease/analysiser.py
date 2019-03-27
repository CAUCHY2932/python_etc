from lxml import etree

class Analysister:
    def __init__(self):
        pass
        
    @staticmethod
    def htmlish(text):
        if text:
            text=etree.HTML(text)
            return htmlish_text
        return ''

    @staticmethod
    def analysis_by_lxml(htmlish_text,xpath_path):
        if xpath_path:
            xpath_list=htmlish_text.xpath(xpath_path)
            return xpath_list
        return []
