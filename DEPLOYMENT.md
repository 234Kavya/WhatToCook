# Deployment Guide for WhatToCook

## Recommended: Render.com (Best Option)

### Why Render.com?
- ✅ Free tier available
- ✅ Perfect for Flask applications
- ✅ Handles CSV files and pandas well
- ✅ Easy deployment from GitHub
- ✅ Automatic HTTPS
- ✅ Persistent storage

### Steps to Deploy on Render:

1. **Prepare your repository:**
   - Make sure all files are committed to GitHub
   - Ensure `requirements.txt` includes only necessary packages (see below)

2. **Create a minimal requirements.txt:**
   ```txt
   Flask==2.3.2
   pandas==2.0.3
   gunicorn==21.2.0
   Werkzeug==2.3.6
   ```

3. **Go to Render.com:**
   - Sign up at https://render.com
   - Connect your GitHub account
   - Click "New +" → "Web Service"
   - Select your repository

4. **Configure the service:**
   - **Name:** whattocook (or any name)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn wsgi:app`
   - **Plan:** Free

5. **Deploy:**
   - Click "Create Web Service"
   - Render will automatically deploy your app
   - Your app will be available at: `https://your-app-name.onrender.com`

---

## Alternative: Railway

### Steps to Deploy on Railway:

1. **Sign up at Railway:**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Create a new project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Railway will auto-detect:**
   - It will detect Python/Flask
   - Add a `Procfile` with: `web: gunicorn wsgi:app`

4. **Deploy:**
   - Railway will automatically build and deploy
   - Get your URL from the dashboard

---

## Alternative: PythonAnywhere

### Steps to Deploy on PythonAnywhere:

1. **Sign up:** https://www.pythonanywhere.com (free tier available)

2. **Upload files:**
   - Use the Files tab to upload your project
   - Or use Git: `git clone https://github.com/yourusername/WhatToCook.git`

3. **Configure Web App:**
   - Go to Web tab
   - Click "Add a new web app"
   - Choose Flask and Python 3.10
   - Set source code directory

4. **Update WSGI file:**
   - Edit the WSGI file to point to your app
   - Set: `from app import app as application`

5. **Reload:**
   - Click the green reload button
   - Your app will be live!

---

## If You Still Want to Use Vercel:

### Update vercel.json:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "wsgi.py"
    }
  ],
  "functions": {
    "wsgi.py": {
      "maxDuration": 30
    }
  }
}
```

### Create a minimal requirements.txt for Vercel:
Only include essential packages to reduce bundle size.

### Limitations:
- CSV file must be small (< 50MB)
- Cold starts may be slow
- Not ideal for data processing

---

## Important Notes:

1. **Optimize requirements.txt:**
   Your current requirements.txt has many unnecessary packages (TensorFlow, Jupyter, etc.). Create a minimal version:

   ```txt
   Flask==2.3.2
   pandas==2.0.3
   gunicorn==21.2.0
   Werkzeug==2.3.6
   ```

2. **Environment Variables:**
   If you need to hide API keys, use environment variables in your hosting platform.

3. **CSV File:**
   Make sure `IndianFoodDatasetCSV.csv` is in your repository and accessible.

4. **Static Files:**
   All static files should be in the `static/` folder (which you already have).

---

## Quick Comparison:

| Platform | Free Tier | Flask Support | CSV/Data | Ease of Use | Best For |
|----------|-----------|---------------|----------|-------------|----------|
| **Render** | ✅ Yes | ✅ Excellent | ✅ Great | ⭐⭐⭐⭐⭐ | **Recommended** |
| **Railway** | ✅ Yes | ✅ Excellent | ✅ Great | ⭐⭐⭐⭐ | Good alternative |
| **PythonAnywhere** | ✅ Yes | ✅ Excellent | ✅ Great | ⭐⭐⭐ | Traditional option |
| **Vercel** | ✅ Yes | ⚠️ Limited | ⚠️ Limited | ⭐⭐⭐ | Serverless only |
| **GitHub Pages** | ✅ Yes | ❌ No | ❌ No | - | Static sites only |

---

## Recommendation: **Use Render.com** 🚀

It's the best fit for your Flask application with CSV data processing.

