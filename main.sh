#!/bin/bash
set -e

echo "🚀 Building site..."
python3 src/main.py
cd public && python3 -m http.server 8000
echo "✅ Build finished. Check the public/ folder."
