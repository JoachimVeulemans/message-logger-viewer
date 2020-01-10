#!/bin/bash

docker build -t joachimveulemans/message-logger-viewer:frontend ./frontend/

docker build -t joachimveulemans/message-logger-viewer:backend ./backend/
