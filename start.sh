#!/bin/bash
# Exit immediately if a command fails
set -e

# echo "==> 1. Updating Linux system packages..."
apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    git \
    curl \
    wget \
    ffmpeg \
    libsm6 \
    libxext6

# echo "==> 2. Upgrading Pip..."
python3 -m pip install --upgrade pip setuptools wheel

# echo "==> 3. Installing Python dependencies..."
if [ -f "requirements.txt" ]; then
    pip install --no-cache-dir -r requirements.txt
else
    echo "No requirements.txt found, installing default Gradio..."
    pip install --no-cache-dir gradio
fi

# echo "==> 4. Setting ownership permissions for Hugging Face non-root user..."
chown -R user:user /app

# echo "==> Build complete successfully!"
#!/bin/bash

# echo "==> Launching app.py..."

