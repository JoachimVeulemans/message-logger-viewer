[![Frontend CI Build](https://img.shields.io/azure-devops/build/joachimveulemans/3fbff01b-aee2-4a9f-9e6c-c18be3511772/13?label=Frontend%20CI%20Build)](https://dev.azure.com/JoachimVeulemans/message-logger-viewer/_build?definitionId=13)
[![Backend CI Build](https://img.shields.io/azure-devops/build/joachimveulemans/3fbff01b-aee2-4a9f-9e6c-c18be3511772/11?label=Backend%20CI%20Build)](https://dev.azure.com/JoachimVeulemans/message-logger-viewer/_build?definitionId=11)

# Message Logger Viewer

## Introduction

This repository contains 2 dockers (frontend & backend) to post en view log messages.

## Running the project locally

If you want to run the project locally on your own computer, you can do so in two ways. You can run it like in production and start the Docker containers or run it like you would when developing.

### Production-like

Here is assumed that you have [Docker](https://www.docker.com/get-started) installed correctly.

Start of by building the images: `.\00_build_images.cmd` or `./00_build_images.sh`. Alternatively, you can also pull the images that are already build by: `.\00b_pull_images.cmd` or `./00b_pull_images.sh`.

#### Frontend

Start frontend by: `.\01_start_frontend.cmd` or `./01_start_frontend.sh`. You can now go to this address in your browser: [localhost:4200](http://localhost:4200).

#### Backend

Start backend by: `.\02_start_backend.cmd` or `./02_start_backend.sh`. You can now go to this address in your browser: [localhost:5000](http://localhost:5000).

### Development

There is assumed that you have [NPM](https://www.npmjs.com/) and [Python 3](https://www.python.org/downloads/) installed correctly.

#### Frontend

1. Go the the frontend directory by: `cd frontend`.
2. Install dependencies by: `npm install`.
3. Run the project by: `npm run start`.
4. You can now go to this address in your browser: [localhost:4200](http://localhost:4200).

#### Backend

1. Go the the backend directory by: `cd backend`.
2. Install dependencies by: `pip install -r requirements.txt`.
3. Run the project by: `python3 application.py`.
4. You can now go to this address in your browser: [localhost:5000](http://localhost:5000).
