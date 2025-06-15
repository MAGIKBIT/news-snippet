from newsplease import NewsPlease

class ArticleDataExtractor:
    def __init__(self, retry_limit):
        self.article_date = None
        self.article_image = None
        self.article_title = None
        self.date_download = None
        self.date_modify = None
        self.description = None
        self.filename = None  
        self.language = None
        self.localpath = None
        self.title_page = None
        self.title_rss = None
        self.source_domain = None
        self.text = None
        self.url = None 
        self.authors = None       
        self.Retry_Limit = retry_limit

    def news_article_date_extractor(self, url):
        error = True
        counter = 0
        while error and counter < self.Retry_Limit:
            try:
                article = NewsPlease.from_url(url)
                self.article_date = article.date_publish
                self.article_image = article.image_url
                self.article_title = article.title
                self.date_download = article.date_download
                self.date_modify = article.date_modify
                self.description = article.description
                self.filename = article.filename  
                self.language = article.language
                self.localpath = article.localpath
                self.title_page = article.title_page
                self.title_rss = article.title_rss
                self.source_domain = article.source_domain
                self.text = article.text
                self.authors = article.authors
                self.url = article.url
                print("Article desc: " + article.description)
                print("Article filename: " + article.filename)
                print("Article lang: " + article.language)
#                 print("Article Authors: " + article.authors)
                print("Article source_domain: " + article.source_domain)
                        
                error = False
            except Exception as e:
                counter = counter + 1
                self.article_date = None
                print(e)
                print(url + " ---> Retrying...")
                error = True


        return self.article_date

    def get_article_image(self):
        return self.article_image

    def get_article_title(self):
        return self.article_title
    
    def get_date_download(self):
        return self.date_download

    def get_date_modify(self):
        return self.date_modify
    
    def get_description(self):
        return self.description

    def get_filenamee(self):
        return self.filename
    
    def get_language(self):
        return self.language

    def get_localpath(self):
        return self.localpath
    
    def get_title_page(self):
        return self.title_page

    def get_title_rss(self):
        return self.title_rss
    
    def get_source_domain(self):
        return self.source_domain

    def get_text(self):
        return self.text
    
    def get_url(self):
        return self.url
    