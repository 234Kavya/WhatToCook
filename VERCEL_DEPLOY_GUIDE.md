# Complete Guide: Deploy on Vercel

## ⚠️ Important Notes About Vercel

### Limitations:
- ✅ **Works with Flask** but optimized for serverless
- ⚠️ **50MB function size limit** - Must use minimal dependencies
- ⚠️ **Cold starts** - First request after inactivity takes 5-10 seconds
- ⚠️ **CSV file** - Must be small (< 10MB recommended)
- ⚠️ **10-second timeout** on free tier (can extend to 30s with config)

### Advantages:
- ✅ **Free tier** with generous limits
- ✅ **Automatic HTTPS**
- ✅ **Global CDN**
- ✅ **Auto-deploy** on git push
- ✅ **No spin-down** (always available)

---

## Step-by-Step Deployment

### Step 1: Sign Up / Login to Vercel
1. Go to **https://vercel.com**
2. Click **"Sign Up"** or **"Log In"**
3. Sign up using your **GitHub account** (recommended)

---

### Step 2: Import Your Project
1. Once logged in, click **"Add New..."** → **"Project"**
2. You'll see a list of your GitHub repositories
3. Find and click **"WhatToCook"** repository
4. Click **"Import"**

---

### Step 3: Configure Project Settings

Vercel will auto-detect your `vercel.json` file, but verify these settings:

#### Framework Preset:
- Should auto-detect as **"Other"** or **"Python"**
- If not, select **"Other"**

#### Root Directory:
- Leave empty (if your files are in root)
- Or set to `WhatToCook` if files are in subdirectory

#### Build and Output Settings:
- **Build Command:** Leave empty (Vercel handles this automatically)
- **Output Directory:** Leave empty
- **Install Command:** 
  ```
  pip install -r requirements-vercel.txt
  ```
  ⚠️ **Important:** Use `requirements-vercel.txt` (minimal dependencies)

#### Environment Variables (Optional):
- Add any API keys or secrets here if needed
- For now, you can skip this

---

### Step 4: Deploy
1. Review all settings
2. Click **"Deploy"** button
3. Vercel will start building your application

---

### Step 5: Monitor Deployment

You'll see a deployment log showing:
1. **Building** - Installing dependencies
2. **Deploying** - Creating serverless functions
3. **Ready** - Your app is live! ✅

**Expected build time:** 1-3 minutes

---

### Step 6: Access Your App

Once deployment is complete:
- Your app will be available at: `https://whattocook.vercel.app`
- Or a custom domain if you set one up
- The URL will be shown in the Vercel dashboard

---

## Troubleshooting

### ❌ Build Fails: "Function size exceeds 50MB"
**Solution:**
1. Make sure you're using `requirements-vercel.txt`
2. Remove unnecessary packages
3. Check CSV file size (should be < 10MB)

### ❌ Build Fails: "Module not found"
**Solution:**
- Verify `requirements-vercel.txt` has all needed packages
- Check that install command uses `requirements-vercel.txt`

### ❌ App Returns 500 Error
**Common causes:**
1. **CSV file not found:**
   - Make sure `IndianFoodDatasetCSV.csv` is in your repository
   - Check the file path in `app.py` is correct

2. **Timeout issues:**
   - First request after cold start may timeout
   - Try again (subsequent requests are faster)

3. **Import errors:**
   - Check Vercel logs for specific error messages

### ❌ Slow First Request
**This is normal!**
- Cold starts take 5-10 seconds on free tier
- Subsequent requests are fast (< 1 second)
- Consider using Vercel Pro for faster cold starts

### View Logs:
1. Go to your project in Vercel dashboard
2. Click on the deployment
3. Go to **"Functions"** tab to see logs
4. Or check **"Runtime Logs"** for errors

---

## Optimizing for Vercel

### 1. Lazy Load CSV (Recommended)
Instead of loading CSV at module level, load it on first request:

```python
# In app.py, replace:
df = pd.read_csv('IndianFoodDatasetCSV.csv')

# With:
df = None

def get_df():
    global df
    if df is None:
        df = pd.read_csv('IndianFoodDatasetCSV.csv')
    return df
```

Then use `get_df()` instead of `df` in your routes.

### 2. Use Minimal Dependencies
- Always use `requirements-vercel.txt`
- Don't include TensorFlow, Jupyter, or other heavy packages

### 3. Optimize CSV File
- If CSV is large, consider:
  - Compressing it
  - Using a database instead
  - Loading only needed columns

---

## Important Notes

### Free Tier Limits:
- ✅ **100GB bandwidth/month**
- ✅ **100 serverless function executions/day** (then pay-per-use)
- ✅ **10-second function timeout** (extendable to 30s with config)
- ✅ **No spin-down** - Always available
- ⚠️ **Cold starts** - First request after inactivity is slow

### Function Timeout:
- Free tier: 10 seconds (default)
- With `vercel.json` config: Up to 30 seconds
- Pro tier: Up to 60 seconds

### Auto-Deploy:
- ✅ Automatically deploys on every git push to `main` branch
- ✅ Creates preview deployments for pull requests
- ✅ Can rollback to previous deployments

---

## Updating Your App

After making changes:
1. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your changes"
   git push origin main
   ```
2. Vercel will **automatically detect** the push
3. It will **automatically build and deploy** your app
4. Check the "Deployments" tab in Vercel to see progress

---

## Quick Reference

**Your Vercel Dashboard:**
- View deployments: Project → "Deployments" tab
- View logs: Deployment → "Functions" tab → Click function → "Logs"
- View metrics: Project → "Analytics" tab
- Settings: Project → "Settings" tab

**Your App URL:**
- Format: `https://[your-project-name].vercel.app`
- Example: `https://whattocook.vercel.app`
- Custom domain: Can be added in Settings → Domains

---

## Comparison: Vercel vs Render

| Feature | Vercel | Render |
|---------|--------|--------|
| **Free Tier** | ✅ Yes | ✅ Yes |
| **Cold Starts** | ⚠️ 5-10s | ⚠️ 30s |
| **Always On** | ✅ Yes | ❌ Spins down after 15min |
| **Function Size** | ⚠️ 50MB limit | ✅ No limit |
| **Best For** | Serverless apps | Traditional Flask apps |
| **CSV/Data Processing** | ⚠️ Limited | ✅ Better |

**Recommendation:**
- Use **Vercel** if you want always-on, fast subsequent requests
- Use **Render** if you have large files or need more processing power

---

## Success Checklist

- [ ] Signed up on Vercel.com
- [ ] Connected GitHub account
- [ ] Imported WhatToCook repository
- [ ] Verified install command uses `requirements-vercel.txt`
- [ ] Clicked "Deploy"
- [ ] Waited for build to complete
- [ ] Opened your app URL
- [ ] Tested the application (first request may be slow)
- [ ] Verified CSV file loads correctly

**Congratulations! Your app is now live on Vercel! 🎉**

---

## Need Help?

If you encounter issues:
1. Check **Function Logs** in Vercel dashboard
2. Verify CSV file is in repository and < 10MB
3. Make sure `requirements-vercel.txt` has correct packages
4. Check that `vercel.json` is properly configured
5. Try lazy loading CSV (see optimization section above)

