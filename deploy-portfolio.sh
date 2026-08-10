#!/bin/bash
# Deploy Cherry's Portfolio to Vercel
# Usage: ./deploy-portfolio.sh

set -e

echo "=== Cherry Portfolio Deployment ==="
echo ""

# Check Vercel CLI
if ! command -v vercel &> /dev/null; then
    echo "Installing Vercel CLI..."
    npm install -g vercel
fi

# Deploy
echo "Deploying to Vercel..."
cd /root/cherry-portfolio
vercel --yes --prod

echo ""
echo "=== Deployment Complete ==="
echo "Your portfolio is live!"
