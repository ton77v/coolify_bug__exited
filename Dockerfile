FROM ghcr.io/astral-sh/uv:python3.13-bookworm
ARG UV_CACHE_DIR="/root/.cache/uv"

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-dev libxml2-dev libxslt-dev apt-transport-https ca-certificates curl gnupg && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root
COPY pyproject.toml uv.lock ./
ENV UV_CACHE_DIR=$UV_CACHE_DIR
RUN uv sync

COPY src src
# ...

# ...

COPY scripts /bin
RUN chmod +x /bin/*.sh

# ...

RUN echo "ALL DONE..........🦁"
CMD ["start_service.sh"]
