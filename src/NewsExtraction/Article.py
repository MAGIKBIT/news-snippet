
class Article:

    def __init__(self):
        self.title = None
        self.content = None
        self.published_date = None
        self.tag = None
        self.group = None
        self.url = None
        self.img_url = None
        self.adpath = None
        self.authors = []
        self.date_download = None
        self.date_modify = None
        self.description = None
        self.filename = None
        self.image_url = None
        self.language = None
        self.localpath = None
        self.source_domain = None
        self.title_page = None
        self.title_rss = None

    def set_title(self, title):
        self.title = title

    def set_content(self, content):
        self.content = content

    def set_published_date(self, pubDate):
        self.published_date = pubDate

    def set_tag(self, tag):
        self.tag = tag

    def set_group(self, group):
        self.group = group

    def set_url(self, url):
        self.url = url

    def set_img_url(self, img_url):
        self.img_url = img_url

    def set_adpath(self, adpath):
        self.adpath = adpath

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_published_date(self):
        return self.published_date

    def get_tag(self):
        return self.tag

    def get_group(self):
        return self.group

    def get_url(self):
        return self.url

    def get_img_url(self):
        return self.img_url

    def get_adpath(self):
        return self.adpath
    
    def get_date_download(self):
        return self.date_download
    
    def get_date_modify(self):
        return self.date_modify
    
    def get_description(self):
        return self.description
    
    def get_filename(self):
        return self.filename

    def get_image_url(self):
        return self.image_url
    
    def get_language(self):
        return self.language

    def get_localpath(self):
        return self.localpath

    def get_source_domain(self):
        return self.source_domain
    
    def get_title_page(self):
        return self.title_page
    
    def get_title_rss(self):
        return self.title_rss  
    
    def set_date_download(self, date_download):
        self.date_download = date_download
    
    def set_date_modify(self, date_modify):
        self.date_modify = date_modify
    
    def set_authors(self, authors):
        self.authors = authors    
    
    def set_description(self, description):
        self.description = description
    
    def set_filename(self, filename):
        self.filename = filename

    def set_image_url(self, image_url):
        self.image_url = image_url
    
    def set_language(self, language):
        self.language = language

    def set_localpath(self, localpath):
        self.localpath = localpath

    def set_source_domain(self, source_domain):
        self.source_domain = source_domain
    
    def set_title_page(self, title_page):
        self.title_page = title_page
    
    def set_title_rss(self, title_rss):
        self.title_rss = title_rss                