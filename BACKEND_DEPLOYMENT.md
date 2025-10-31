# Backend Deployment Guide

Your EMOS website is live at https://aprilaihub.github.io/EMOS, but the Flask backend needs separate hosting since GitHub Pages only serves static files.

## 🚀 Deploy Backend to Render (Recommended)

### Step 1: Prepare Your Repository
✅ **Already done** - I've added these files:
- `Procfile` - Tells Render how to start your app
- `requirements.txt` - Python dependencies
- Updated `backend/app.py` for production

### Step 2: Deploy on Render

1. **Go to [render.com](https://render.com)** and sign up/login
2. **Click "New +"** → **"Web Service"**
3. **Connect GitHub** → Select your `aprilaihub/EMOS` repository
4. **Configure the service**:
   ```
   Name: emos-backend
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: python backend/app.py
   ```
5. **Click "Create Web Service"**

### Step 3: Get Your Backend URL
After deployment, Render will give you a URL like:
```
https://emos-backend-xyz.onrender.com
```

### Step 4: Update Frontend Configuration
Add this script tag to your GitHub Pages site to connect to the backend:

```html
<script>
window.EMOS_BACKEND_BASE_URL = 'https://your-render-url.onrender.com';
</script>
```

## 🔧 Alternative Options

### Railway.app
1. Go to [railway.app](https://railway.app)
2. Import your GitHub repo
3. Railway auto-detects Python and deploys
4. Get your URL and update the frontend

### Fly.io
1. Install flyctl CLI
2. Run `fly launch` in your repo
3. Deploy with `fly deploy`

## 📝 Frontend Update

Once your backend is deployed, update the main site by adding this to `index.html`:

```html
<!-- Add this in the <head> section -->
<script>
// Set your deployed backend URL here
window.EMOS_BACKEND_BASE_URL = 'https://your-backend-url.onrender.com';
</script>
```

The frontend is already configured to use this URL automatically!

## 🧪 Testing

1. Deploy backend to Render/Railway
2. Update frontend with backend URL
3. Test features on https://aprilaihub.github.io/EMOS
4. Check browser console for any connection errors

## 💡 Free Tier Limits

- **Render**: 750 hours/month (goes to sleep after 15min inactivity)
- **Railway**: $5 credit monthly
- **Fly.io**: Good for small apps

For production use, consider upgrading to paid plans for better performance.