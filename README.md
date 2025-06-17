# News-Snippet

This project uses [news-please](https://github.com/fhamborg/news-please) (with custom updates) and [boilerpipe](https://github.com/kohlschutter/boilerpipe) to crawl news and generate XML files.  
It fetches news content and automatically classifies it into different categories using machine learning.

**Now supports crawling news websites in any language!**

---

## How It Works

- **Configuration:**  
  Base URLs of news websites are provided in a configuration file located at `src/config/configuration.ini`.
- **Crawling:**  
  The crawler picks each URL and fetches news articles posted within a configurable time limit (default: last 48 hours).
- **Extraction:**  
  - Posted Time (customized date extractor for Urdu and other sites)
  - News Image
  - Title
  - Content (via Boilerpipe)
  - Category (via ML classifier)
- **Output:**  
  - Downloads images to the directory specified in the config file.
  - Saves generated XML files to the directory specified in the config file.

---

## Requirements

- **Python 3.7+**
- **Configuration file:**  
  Ensure `src/config/configuration.ini` exists and contains the following sections:
  - `[news_sources]`
  - `[general]`
  - `[source_urdu_names]`
  - `[solr_info]`

  Example:
  ```ini
  [general]
  RETRY_LIMIT = 1
  SRV_THUMBNAIL_DIR = _i/thmb/nws/
  IMAGE_DIR = images/current/
  XML_DIR = XMLs/current/
  IMAGE_TOLERANCE = False
  ARTICLE_DAYS_LIMIT = 30
  LOGGING = True
  ```

- **Run the script from the correct directory:**  
  The script expects the config file at `src/config/configuration.ini`.  
  If you run from another directory, update the config path in your script as shown below:

  ```python
  import os
  import configparser

  config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'configuration.ini')
  parser = configparser.ConfigParser()
  parser.read(os.path.abspath(config_path))
  ```

---

## Common Errors & Fixes

- **Missing section in configuration file:**  
  Ensure all required sections (`[general]`, `[news_sources]`, `[source_urdu_names]`, `[solr_info]`) are present in `src/config/configuration.ini`.

- **File not found:**  
  Make sure the config file is at `src/config/configuration.ini` relative to your script.

- **Permissions:**  
  Ensure the config file is readable:  
  `chmod 644 src/config/configuration.ini`

---

## Solr Guide

**Start Solr:**
```sh
solr start -e dih
```

**Delete Solr index:**
```sh
curl http://localhost:8983/solr/newsy/update?commit=true -H "Content-Type: text/xml" --data-binary '<delete><query>*:*</query></delete>'
```

**Index XML news extractions in Solr:**
```sh
./bin/post -c newsy /path/to/your/NEWSY3/src/NewExtraction/XMLs/current/nazret/*.xml
```
---

## Solr Commands and Resources

**Useful Solr Commands:**

- Query Solr for documents containing "foundation":
	```sh
	curl "http://localhost:8983/solr/mycore/select?wt=json&indent=true&q=foundation"
	```

- Query all documents and get facet pivot on `cat` and `inStock`:
	```sh
	curl 'http://localhost:8983/solr/mycore/select?q=*:*&rows=0&wt=json&indent=on&facet=on&facet.pivot=cat,inStock'
	```

**Resources:**

- [Solr Quick Start Guide](http://lucene.apache.org/solr/quickstart.html)
---

## Docker Build and Run

```sh
docker build -t news-snippet:latest .
docker run -d --name enewsygridcrawlernextractor \
  -v ~/volumes/news-snippet/news-please/config/:/news-snippet/src/newsplease/config/ \
  news-snippet:latest
```
---

## Running Locally

1. **Install dependencies:**
	```sh
	pip install -r requirements.txt
	```

2. **Ensure configuration file exists:**
	- Verify `src/config/configuration.ini` is present and properly configured.

3. **Run the main script:**
	```sh
	python src/main.py
	```

4. **Check output:**
	- Extracted XML files and images will be saved to the directories specified in your config file.

--- 
---

## Troubleshooting

- If you see errors about missing config sections, double-check your `configuration.ini` for typos and correct section headers.
- If you see file not found errors, check your working directory and config file path.
- For further issues, print the resolved config path in your script for debugging.

---

## License