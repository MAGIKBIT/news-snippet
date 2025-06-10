FROM python:3.6.5-alpine3.7

# 1. Install build dependencies
RUN apk add --no-cache --virtual .build-deps \
      gcc \
      libc-dev \
      libxml2-dev \
      libxslt-dev \
      python3-dev

# 2. Install runtime dependencies
RUN apk add --no-cache \
      libxml2 \
      libxslt \
      jpeg-dev \
      zlib-dev

# 3. Upgrade pip and setuptools
RUN pip3 install --no-cache-dir --upgrade pip setuptools

# 4. Clone your project repo
RUN git clone https://github.com/MAGIKBIT/news-snippet.git /news-snippet

# 5. Install Python dependencies
RUN cd /news-snippet/src && \
    pip3 install --no-cache-dir -r requirements.txt

# 6. Remove build dependencies to slim image
RUN apk del .build-deps

# 7. Copy your startup script
COPY docker.sh /docker.sh

# 8. (Optional) Make script executable
RUN chmod +x /docker.sh

# 9. (Optional) Set default CMD or ENTRYPOINT
# ENTRYPOINT ["/docker.sh"]
