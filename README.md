# Weather API

A simple Django REST Framework API that fetches real-time weather data from Visual Crossing and caches it using Redis. This project demonstrates working with third-party APIs, caching, and error handling in Python.

## Features

- Fetch weather data for any city via Visual Crossing API
- Redis caching with expiration (12 hours)
- Graceful error handling for:
  - Invalid city names
  - API timeouts
  - Network errors
  - Redis failures
- Easy configuration using `.env` environment variables

## Getting Started

### Prerequisites

- Python 3.10+
- Redis
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
