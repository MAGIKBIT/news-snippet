FROM python:3.6.5-alpine3.7

# 1. Install build tools including git
:contentReference[oaicite:2]{index=2} \
      gcc \
      libc-dev \
      libxml2-dev \
      libxslt-dev \
      python3-dev \
      git

# 2. Install runtime dependencies
:contentReference[oaicite:3]{index=3} \
      libxml2 \
      libxslt \
      jpeg-dev \
      zlib-dev

# 3. Upgrade pip & setuptools
:contentReference[oaicite:4]{index=4}

# 4. Clone project
:contentReference[oaicite:5]{index=5}

# 5. Install Python dependencies
:contentReference[oaicite:6]{index=6} \
    :contentReference[oaicite:7]{index=7}

# 6. Clean up build dependencies
:contentReference[oaicite:8]{index=8}

# 7. Copy startup script
:contentReference[oaicite:9]{index=9}
:contentReference[oaicite:10]{index=10}

# Optional: set entrypoint
# ENTRYPOINT ["/docker.sh"]
