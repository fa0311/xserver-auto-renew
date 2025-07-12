FROM python:3.9 AS builder

WORKDIR /app
COPY requirements.txt .
COPY xserver-auto-renew/ xserver-auto-renew/
COPY cookies.json .

FROM python:3.9

WORKDIR /app
COPY --from=builder /app /app

RUN pip install --no-cache-dir -r requirements.txt

ENV TZ=Asia/Tokyo

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    cron \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libc6 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

RUN echo "0 0 * * * python -m xserver-auto-renew.login && python -m xserver-auto-renew.main" > /etc/cron.d/xserver-auto-renew

RUN chmod 0644 /etc/cron.d/xserver-auto-renew

RUN crontab /etc/cron.d/xserver-auto-renew

RUN chmod 777 /app/cookies.json

CMD ["cron", "-f"]