# Xserver Auto Renew

An automated tool for renewing Xserver's free VPS service to prevent expiration.

## Overview

This Python application automatically renews your Xserver free VPS service by simulating the manual renewal process through web scraping. It uses session cookies to authenticate and perform the renewal operation, helping you maintain your free VPS without manual intervention.

## Features

- **Automated Renewal**: Automatically renews your Xserver free VPS service
- **Session Management**: Uses browser cookies for authentication
- **Error Handling**: Validates renewal success and provides clear error messages
- **Environment Configuration**: Secure configuration through environment variables
- **User Agent Spoofing**: Uses realistic browser headers to avoid detection

## Installation

1. Clone the repository:

```bash
git clone https://github.com/fa0311/xserver-auto-renew.git
cd xserver-auto-renew
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   Create a `.env` file in the root directory:

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

- `ID_VPS`: Your VPS ID from Xserver (required)

```env
ID_VPS=your_vps_id_here
```

<img src="image/README/1752250288684.png" alt="image" style="width: 50%;">

### Cookie Setup

1. Log in to your Xserver account in your browser
2. Navigate to the VPS management page
3. Export cookies for the `secure.xserver.ne.jp` domain
4. Save the cookies as `cookies.json` in JSON format

Example `cookies.json` structure:

```json
[
  {
    "domain": "secure.xserver.ne.jp",
    "name": "X2SESSID",
    "path": "/",
    "value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  },
  {
    "domain": "secure.xserver.ne.jp",
    "name": "XSERVER_DEVICEKEY",
    "path": "/",
    "value": "xxxxxxx"
  }
]
```

### File Structure

```filetree
xserver-auto-renew/
├── xserver-auto-renew/
│   └── ...
├── .env                 # Environment variables
├── cookies.json        # Browser cookies
└── ...
```

## Usage

Run the renewal script:

```bash
python -m xserver-auto-renew.main
```
