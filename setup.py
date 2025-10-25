#!/usr/bin/env python3
"""
Setup script for GitHub Analyzer
Helps users configure their GitHub token
"""

import os
from pathlib import Path

def setup_github_token():
    print("🚀 GitHub Analyzer Setup")
    print("=" * 40)
    print()
    print("To use the GitHub API effectively, you need a Personal Access Token.")
    print("This increases the rate limit from 60 to 5,000 requests per hour.")
    print()
    print("📋 Steps to get your token:")
    print("1. Go to: https://github.com/settings/tokens")
    print("2. Click 'Generate new token' → 'Generate new token (classic)'")
    print("3. Give it a name like 'GitHub Analyzer'")
    print("4. Select scopes: ✅ public_repo (or ✅ repo for private repos)")
    print("5. Click 'Generate token'")
    print("6. Copy the token (it starts with 'ghp_' or 'github_pat_')")
    print()
    
    # Check if .env already exists
    env_file = Path("backend/.env")
    if env_file.exists():
        with open(env_file, "r") as f:
            content = f.read()
            if "GITHUB_TOKEN=" in content and not "your_github_token_here" in content:
                print("✅ GitHub token is already configured!")
                return
    
    token = input("🔑 Paste your GitHub token here: ").strip()
    
    if not token:
        print("❌ No token provided. You can set it manually in backend/.env")
        return
    
    if not (token.startswith('ghp_') or token.startswith('github_pat_')):
        print("⚠️  Warning: Token doesn't look like a GitHub token (should start with 'ghp_' or 'github_pat_')")
        proceed = input("Continue anyway? (y/N): ").strip().lower()
        if proceed != 'y':
            return
    
    # Create backend directory if it doesn't exist
    Path("backend").mkdir(exist_ok=True)
    
    # Write .env file
    env_content = f"""# GitHub API Configuration
# Get your token from: https://github.com/settings/tokens
# Permissions needed: public_repo (or repo for private repos)
GITHUB_TOKEN={token}

# Flask Configuration
PORT=5000
"""
    
    with open("backend/.env", "w") as f:
        f.write(env_content)
    
    print("✅ GitHub token saved to backend/.env")
    print("🎉 Setup complete! You can now run the application.")
    print()
    print("To start the application:")
    print("Backend:  cd backend && python app.py")
    print("Frontend: cd frontend && npm start")

if __name__ == "__main__":
    setup_github_token()