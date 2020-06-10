import wikipedia

class WikiScraper:
    def __init__(self, language):
        self.language = language
        self.page_list = None
        self.summaries = []
        self.contents = []
        wikipedia.set_lang(self.language)


    def _get_summary(self, page_name):
        return wikipedia.summary(page_name)

    def _get_content(self, page_name):
        return wikipedia.page(page_name).content

    def get_summaries(self, keyword):
        keyword = keyword
        page_list = wikipedia.search(keyword)
        summaries = []
        for page_name in page_list:
            try:
                summaries.append(self._get_summary(page_name))
            except:
                continue
        self.summaries = summaries

    def get_contents(self, keyword):
        keyword = keyword
        page_list = wikipedia.search(keyword)
        contents = []
        for page_name in page_list:
            try:
                contents.append(self._get_content(page_name))
            except:
                continue
        self.contents = contents
    