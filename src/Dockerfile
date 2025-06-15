FROM python:3.6.5-alpine3.7

# Install build-time dependencies and git
RUN apk add --no-cache --virtual .build-deps \
    build-base \
    python3-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    jpeg-dev \
    zlib-dev \
    pkgconfig \
    git

# Install runtime dependencies
RUN apk add --no-cache \
    libffi \
    libxml2 \
    libxslt \
    jpeg \
    zlib

# Upgrade pip and setuptools
RUN pip3 install --no-cache-dir --upgrade pip setuptools

# Clone the news-snippet repo
RUN git clone https://github.com/MAGIKBIT/news-snippet.git /news-snippet

# Install Python dependencies
RUN cd /news-snippet/src && \
    pip3 install --no-cache-dir -r requirements.txt

# Clean up build-time dependencies
RUN apk del .build-deps

# Copy the startup script and make it executable
COPY docker.sh /docker.sh
RUN chmod +x /docker.sh

# Set the working directory
WORKDIR /news-snippet/src

# Set default entrypoint
ENTRYPOINT ["/docker.sh"]