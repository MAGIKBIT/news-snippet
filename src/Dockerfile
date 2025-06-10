FROM python:3.6.5-alpine3.7

# 1. Install build dependencies (including git for cloning)
RUN apk add --no-cache --virtual .build-deps \
      gcc \
      libc-dev \
      libxml2-dev \
      libxslt-dev \
      python3-dev \
      git

# 2. Install runtime libraries needed by lxml and image handling
RUN apk add --no-cache \
      libxml2 \
      libxslt \
      jpeg-dev \
      zlib-dev

# 3. Upgrade pip and setuptools before installing Python libs
RUN pip3 install --upgrade pip setuptools

# 4. Clone the repository
RUN git clone https://github.com/MAGIKBIT/news-snippet.git /news-snippet

# 5. Install Python dependencies (including lxml, etc.)
RUN cd /news-snippet/src && \
    pip3 install --no-cache-dir -r requirements.txt

# 6. Cleanup build dependencies to shrink final image
RUN apk del .build-deps

# 7. Copy the startup script and make it executable
COPY docker.sh /docker.sh
RUN chmod +x /docker.sh

# 8. (Optional) Set an entrypoint
# ENTRYPOINT ["/docker.sh"]
