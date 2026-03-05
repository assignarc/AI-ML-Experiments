#!/bin/bash
# Installs llama-cpp-python as a native arm64 binary with Metal GPU support.
# Run this script instead of pip install for llama-cpp-python.
# Usage: ./install_llama.sh

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$REPO_DIR/.venv-metal"

if [ ! -d "$VENV" ]; then
  echo "❌ Virtual environment not found at $VENV"
  exit 1
fi

echo "🔧 Uninstalling any existing llama-cpp-python..."
"$VENV/bin/pip" uninstall llama-cpp-python -y 2>/dev/null || true
rm -rf "$VENV/lib/python3.13/site-packages/llama_cpp"

echo "🏗️  Building llama-cpp-python for arm64 with Metal support..."
PATH="/opt/homebrew/bin:$PATH" \
  CMAKE_ARGS="-DGGML_METAL=on -DGGML_NATIVE=OFF" \
  FORCE_CMAKE=1 \
  arch -arm64 "$VENV/bin/pip" install llama-cpp-python \
    --no-cache-dir \
    --no-binary llama-cpp-python

echo ""
echo "✅ Done! Verifying..."
arch -arm64 "$VENV/bin/python" -c "from llama_cpp import Llama; print('✅ llama-cpp-python (arm64 + Metal) loaded successfully!')"
