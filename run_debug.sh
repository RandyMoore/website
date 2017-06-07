#!/usr/bin/env bash
export FLASK_APP=app # assumes running 'pip install --editable .' from app in virtualenv
export FLASK_DEBUG=true
flask run