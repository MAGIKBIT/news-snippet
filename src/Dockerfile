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

# Copy the workspace source code into the image
COPY . /news-snippet
# RUN git clone https://github.com/MAGIKBIT/news-snippet.git /news-snippet

# Install Python dependencies
COPY requirements.txt /news-snippet/requirements.txt
WORKDIR /news-snippet
RUN pip3 install --no-cache-dir -r requirements.txt

# Clean up build-time dependencies
RUN apk del .build-deps

# Copy the startup script and make it executable
COPY docker.sh /docker.sh
RUN dos2unix /docker.sh && chmod +x /docker.sh
# Copy __main__.py and make it executable
COPY __main__.py /__main__.py
RUN chmod +x /__main__.py


# Set the working directory
# WORKDIR /news-snippet/src
# Set default entrypoint
# ENTRYPOINT ["/docker.sh"]
CMD ["python3", "__main__.py"]
