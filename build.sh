#!/bin/bash
echo "Forcing clean Python build"
rm -rf /tmp/oryx-*
rm -rf /tmp/build-*
pip install --no-cache-dir -r requirements.txt