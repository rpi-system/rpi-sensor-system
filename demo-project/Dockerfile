# temp stage
FROM python:3.12.2-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /src

RUN apt-get update && \
    apt-get install -y build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /src/requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
        pip install -r /src/requirements.txt
# RUN pip wheel --no-cache-dir --no-deps --wheel-dir /src/wheels -r requirements.txt

COPY ./app.py /src/app.py
RUN chmod +x /src/app.py

RUN addgroup --gid 1001 --system app && \
    adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group app

USER app

# final stage
FROM python:3.12.2-slim

WORKDIR /src

COPY --from=builder /src/requirements.txt .
COPY --from=builder /src/app.py .

USER app

ENTRYPOINT ["python", "/src/app.py"]