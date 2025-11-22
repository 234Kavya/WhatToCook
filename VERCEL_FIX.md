# Fix Vercel Build Error

## Problem
Vercel is trying to install from `requirements.txt` which has incompatible packages for Python 3.12.

## Solution: Update Vercel Project Settings

### Step 1: Go to Vercel Dashboard
1. Open your project in Vercel: https://vercel.com/dashboard
2. Click on your **WhatToCook** project
3. Go to **Settings** tab
4. Scroll down to **Build & Development Settings**

### Step 2: Update Install Command
1. Find **"Install Command"** field
2. Replace it with:
   ```
   pip install -r requirements-vercel.txt
   ```
3. Leave **"Build Command"** empty
4. Click **"Save"**

### Step 3: Redeploy
1. Go to **"Deployments"** tab
2. Click the **"..."** menu on the latest deployment
3. Click **"Redeploy"**
4. Or push a new commit to trigger auto-deploy

---

## Alternative: Quick Fix (Temporary)

If you want a quick fix without changing settings:

1. **Backup your current requirements.txt:**
   ```bash
   git mv requirements.txt requirements-full.txt
   ```

2. **Copy the Vercel requirements:**
   ```bash
   cp requirements-vercel.txt requirements.txt
   ```

3. **Commit and push:**
   ```bash
   git add .
   git commit -m "Use minimal requirements for Vercel"
   git push origin main
   ```

4. **After deployment, restore for local development:**
   ```bash
   git mv requirements.txt requirements-vercel.txt
   git mv requirements-full.txt requirements.txt
   ```

---

## What I Fixed

✅ Updated `requirements-vercel.txt` with Python 3.12 compatible versions:
- pandas==2.1.4 (compatible with Python 3.12)
- numpy==1.26.4 (compatible with Python 3.12)
- Added required dependencies (python-dateutil, pytz, tzdata)

✅ Updated `vercel.json` with build command (may not work, so use Solution 1)

---

## Recommended: Use Solution 1
Setting the Install Command in Vercel dashboard is the cleanest solution and won't affect your local development.

