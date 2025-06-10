FROM python:3.6.5-alpine3.7

# 1. Install build dependencies safely in a virtual package
:contentReference[oaicite:1]{index=1} \
      gcc \
      libc-dev \
      libxml2-dev \
      libxslt-dev \
      python3-dev

# 2. Install runtime dependencies for lxml
:contentReference[oaicite:2]{index=2} \
      libxml2 \
      libxslt

# 3. Upgrade pip and setuptools
:contentReference[oaicite:3]{index=3}

# 4. Clone project
:contentReference[oaicite:4]{index=4}

# 5. Install Python dependencies (including lxml) from source
:contentReference[oaicite:5]{index=5} \
    :contentReference[oaicite:6]{index=6}

# 6. Remove build dependencies to shrink image size
:contentReference[oaicite:7]{index=7}

# 7. Copy startup script
:contentReference[oaicite:8]{index=8}

# 8. Define entrypoint or cmd (optional)
# e.g., ENTRYPOINT ["sh", "/docker.sh"]
