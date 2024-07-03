# My FastAPI Project

This is a project that utilizes FastAPI to build a web scraper.

## Prerequisites

Before running this project, make sure you have the following installed:

- docker and docker-compose

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory: `cd my_fastapi_project/app/`.
3. Install the required dependencies: `docker-compose up --build`.

## Usage

To run the project, follow these steps:

1. Open your web browser and go to `http://localhost:8000/docs` to access the OpenAPI docs to trigger the scraper. 


## Features Covered
1. Queue using celery and redis
2. Cache using redis
3. Params to the endpoint
4. Notification using the console after task complete
5. Downloading image files to local

## Features missing
1. Auth token for the endpoint
2. Use of parse_string - `The secod one will provide a proxy string that tool can use for scraping` - not too familiar with this
3. Retry mechanism - Fairly simple to add using flower with celery



