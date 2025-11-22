# Git Commands to Deploy on GitHub

## Step-by-Step Commands

### 1. Navigate to your project directory
```bash
cd "C:\Users\DELL\programming\2025\Project\WhatToCook\WhatToCook"
```

### 2. Initialize Git (if not already initialized)
```bash
git init
```

### 3. Add all files to staging
```bash
git add .
```

### 4. Create your first commit
```bash
git commit -m "Initial commit: WhatToCook Flask application"
```

### 5. Create a new repository on GitHub
**Option A: Using GitHub CLI (if installed)**
```bash
gh repo create WhatToCook --public --source=. --remote=origin --push
```

**Option B: Manual method (recommended)**
1. Go to https://github.com/new
2. Repository name: `WhatToCook` (or any name you prefer)
3. Choose Public or Private
4. **DO NOT** initialize with README, .gitignore, or license (you already have files)
5. Click "Create repository"

### 6. Add remote and push (if using manual method)
```bash
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/WhatToCook.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## Complete Command Sequence (Copy & Paste)

```bash
# Navigate to project
cd "C:\Users\DELL\programming\2025\Project\WhatToCook\WhatToCook"

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: WhatToCook Flask application"

# Add remote (REPLACE YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/WhatToCook.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## If you get authentication errors:

### For HTTPS (recommended):
1. Use a Personal Access Token instead of password
2. Go to: https://github.com/settings/tokens
3. Generate new token (classic) with `repo` permissions
4. Use token as password when prompted

### For SSH (alternative):
```bash
# Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add SSH key to GitHub (copy the public key)
cat ~/.ssh/id_ed25519.pub

# Then use SSH URL instead:
git remote set-url origin git@github.com:YOUR_USERNAME/WhatToCook.git
```

---

## After Pushing to GitHub:

### Deploy on Render.com:
1. Go to https://render.com
2. Sign up/Login
3. Click "New +" → "Web Service"
4. Connect GitHub account
5. Select your `WhatToCook` repository
6. Configure:
   - **Name:** whattocook
   - **Build Command:** `pip install -r requirements-minimal.txt`
   - **Start Command:** `gunicorn wsgi:app`
   - **Plan:** Free
7. Click "Create Web Service"

### Deploy on Railway:
1. Go to https://railway.app
2. Sign up/Login with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your `WhatToCook` repository
6. Railway will auto-detect and deploy!

---

## Quick Reference:

```bash
# Check status
git status

# See what files will be committed
git status --short

# View commit history
git log --oneline

# Update remote URL (if needed)
git remote set-url origin https://github.com/YOUR_USERNAME/WhatToCook.git

# Push future changes
git add .
git commit -m "Your commit message"
git push
```

---

## Troubleshooting:

**Error: "remote origin already exists"**
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/WhatToCook.git
```

**Error: "failed to push some refs"**
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

**Error: Authentication failed**
- Use Personal Access Token (see above)
- Or set up SSH keys

