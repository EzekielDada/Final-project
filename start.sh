#!/bin/bash
export MONGO_URI="YOUR_ATLAS_CONNECTION_STRING_HERE"
gunicorn --bind 0.0.0.0:5000 --workers 2 app:app
