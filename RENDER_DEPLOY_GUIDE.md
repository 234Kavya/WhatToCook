# Complete Guide: Deploy on Render.com

## Step-by-Step Instructions

### Step 1: Sign Up / Login to Render
1. Go to **https://render.com**
2. Click **"Get Started for Free"** or **"Sign In"**
3. Sign up using your **GitHub account** (recommended - easier to connect repos)

---

### Step 2: Create a New Web Service
1. Once logged in, you'll see the Render Dashboard
2. Click the **"New +"** button (top right)
3. Select **"Web Service"** from the dropdown menu

---

### Step 3: Connect Your GitHub Repository
1. You'll see options to connect a repository
2. If you haven't connected GitHub yet:
   - Click **"Connect GitHub"** or **"Configure account"**
   - Authorize Render to access your repositories
   - Select the repositories you want to give access to (or select "All repositories")
3. After connecting, you'll see a list of your repositories
4. Find and click on **"WhatToCook"** repository

---

### Step 4: Configure Your Web Service

Fill in the following settings:

#### Basic Settings:
- **Name:** `whattocook` (or any name you prefer)
  - This will be your app URL: `https://whattocook.onrender.com`

#### Environment:
- **Environment:** Select **"Python 3"** (it should auto-detect)

#### Build & Deploy Settings:
- **Region:** Choose closest to you (e.g., "Oregon (US West)" or "Frankfurt (EU Central)")

- **Branch:** `main` (should be selected by default)

- **Root Directory:** Leave empty (or set to `WhatToCook` if your files are in a subdirectory)

- **Build Command:** 
  ```
  pip install -r requirements-minimal.txt
  ```
  ⚠️ **Important:** Use `requirements-minimal.txt` not `requirements.txt` (to avoid installing unnecessary packages)

- **Start Command:**
  ```
  gunicorn wsgi:app
  ```

#### Plan:
- Select **"Free"** plan (for now)
  - Free tier includes:
    - 750 hours/month (enough for 24/7 operation)
    - Automatic SSL/HTTPS
    - Auto-deploy on git push

---

### Step 5: Advanced Settings (Optional)

Click **"Advanced"** to configure:

#### Environment Variables (if needed):
If you have API keys or secrets, add them here:
- **Key:** `API_ID`
- **Value:** `7aa516a5` (or use a secret)

But for now, you can skip this since your API keys are in the code.

#### Health Check Path (Optional):
Leave empty or set to `/` (default)

---

### Step 6: Create and Deploy
1. Review all your settings
2. Click **"Create Web Service"** button at the bottom
3. Render will start building your application

---

### Step 7: Monitor the Deployment

You'll see a deployment log showing:
1. **Building** - Installing dependencies
2. **Deploying** - Starting your application
3. **Live** - Your app is running! ✅

**Expected build time:** 2-5 minutes

---

### Step 8: Access Your App

Once deployment is complete:
- Your app will be available at: `https://whattocook.onrender.com`
- The URL will be shown in the Render dashboard
- Click the URL to open your app in a browser

---

## Troubleshooting

### Build Fails with "Module not found"
**Solution:** Make sure you're using `requirements-minimal.txt` in the build command.

### Build Fails with "File not found"
**Solution:** 
- Check if `IndianFoodDatasetCSV.csv` is in your repository
- Make sure the file path in `app.py` is correct

### App Crashes on Start
**Common causes:**
1. Missing CSV file - Make sure `IndianFoodDatasetCSV.csv` is committed to Git
2. Wrong start command - Should be `gunicorn wsgi:app`
3. Port issues - Render handles this automatically, but check logs

### View Logs:
- Click on your service in Render dashboard
- Go to **"Logs"** tab
- Check for error messages

---

## Important Notes

### Free Tier Limitations:
- ⚠️ **Spins down after 15 minutes of inactivity**
  - First request after spin-down takes ~30 seconds (cold start)
  - Subsequent requests are fast
- ✅ **750 hours/month** - Enough for 24/7 if you keep it active
- ✅ **Automatic HTTPS** - SSL certificate included
- ✅ **Auto-deploy** - Updates automatically on git push

### To Keep Free Tier Active:
- Use a service like **UptimeRobot** (free) to ping your app every 5 minutes
- Or upgrade to paid plan ($7/month) for always-on service

---

## Updating Your App

After making changes:
1. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your changes"
   git push origin main
   ```
2. Render will **automatically detect** the push
3. It will **automatically rebuild and redeploy** your app
4. Check the "Events" tab in Render to see deployment progress

---

## Quick Reference

**Your Render Dashboard:**
- View logs: Click service → "Logs" tab
- View metrics: Click service → "Metrics" tab
- Manual deploy: Click service → "Manual Deploy" → "Deploy latest commit"
- Settings: Click service → "Settings" tab

**Your App URL:**
- Format: `https://[your-service-name].onrender.com`
- Example: `https://whattocook.onrender.com`

---

## Next Steps After Deployment

1. ✅ Test all your routes:
   - `/` - Home page
   - `/pantry-mode` - Pantry mode
   - `/cook-mode` - Cook mode
   - `/order-mode` - Order mode
   - `/recipefinder` - Recipe finder

2. ✅ Check if CSV file loads correctly
3. ✅ Test recipe search functionality
4. ✅ Verify static files (CSS, images) load properly

---

## Need Help?

If you encounter issues:
1. Check the **Logs** tab in Render dashboard
2. Verify all files are in GitHub repository
3. Make sure `requirements-minimal.txt` has correct packages
4. Check that `wsgi.py` is properly configured

**Common Error Messages:**
- `ModuleNotFoundError` → Check requirements-minimal.txt
- `FileNotFoundError` → Check CSV file is in repo
- `Port already in use` → Render handles this, ignore if app works
- `Application failed to respond` → Check start command is `gunicorn wsgi:app`

---

## Success Checklist

- [ ] Signed up on Render.com
- [ ] Connected GitHub account
- [ ] Created new Web Service
- [ ] Selected WhatToCook repository
- [ ] Set build command: `pip install -r requirements-minimal.txt`
- [ ] Set start command: `gunicorn wsgi:app`
- [ ] Selected Free plan
- [ ] Clicked "Create Web Service"
- [ ] Waited for build to complete
- [ ] Opened your app URL
- [ ] Tested the application

**Congratulations! Your app is now live! 🎉**

