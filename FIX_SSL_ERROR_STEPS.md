# 🔧 FIX SSL ERROR - Step by Step Guide

## ⚠️ IMPORTANT: You MUST clear your browser's HSTS cache!

The error `ERR_SSL_PROTOCOL_ERROR` happens because your browser is trying to use HTTPS, but Django's development server only supports HTTP.

---

## ✅ SOLUTION: Clear Browser HSTS Cache

### For Chrome/Edge (Most Common):

1. **Open Chrome/Edge**
2. **Type in address bar:** `chrome://net-internals/#hsts`
   - (For Edge, use: `edge://net-internals/#hsts`)
3. **Scroll down to "Delete domain security policies"**
4. **Enter:** `127.0.0.1`
5. **Click "Delete"**
6. **Enter:** `localhost`
7. **Click "Delete"**
8. **Close ALL browser windows completely**
9. **Reopen browser**
10. **Type in address bar:** `http://127.0.0.1:8000` (use `http://` NOT `https://`)

### For Firefox:

1. **Type in address bar:** `about:config`
2. **Click "Accept the Risk" if prompted**
3. **Search for:** `security.tls.insecure_fallback_hosts`
4. **Double-click it** and add: `127.0.0.1,localhost`
5. **Restart Firefox**
6. **Type in address bar:** `http://127.0.0.1:8000`

### Quick Alternative - Use Incognito/Private Mode:

**This bypasses HSTS cache immediately:**

- **Chrome/Edge:** Press `Ctrl+Shift+N` (Windows) or `Cmd+Shift+N` (Mac)
- **Firefox:** Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
- **Then go to:** `http://127.0.0.1:8000`

---

## ✅ Verify Your Server is Running

1. **Open terminal/PowerShell**
2. **Navigate to project:** `cd D:\kemet\KEMET-CONSULTING-UAE`
3. **Activate virtual environment:** `.\venv\Scripts\Activate.ps1`
4. **Start server:** `python manage.py runserver`
5. **You should see:** `Starting development server at http://127.0.0.1:8000/`

---

## ✅ Access the Site

**After clearing HSTS cache, use HTTP (NOT HTTPS):**

- ✅ **Correct:** `http://127.0.0.1:8000`
- ✅ **Correct:** `http://localhost:8000`
- ❌ **Wrong:** `https://127.0.0.1:8000` (will cause SSL error)
- ❌ **Wrong:** `https://localhost:8000` (will cause SSL error)

---

## 🔍 Still Not Working?

### Check 1: Is the server running?
- Look at your terminal - do you see "Starting development server"?
- If not, start it: `python manage.py runserver`

### Check 2: Are you using the correct URL?
- Make sure you type `http://` (not `https://`)
- Make sure you include the port: `:8000`

### Check 3: Try a different browser
- If Chrome doesn't work, try Firefox or Edge
- Or use Incognito/Private mode

### Check 4: Clear all browser data
1. Press `Ctrl+Shift+Delete` (Windows) or `Cmd+Shift+Delete` (Mac)
2. Select "All time"
3. Check "Cached images and files" and "Cookies and other site data"
4. Click "Clear data"
5. Restart browser

---

## 📝 What Changed in Settings

✅ **SECURE_SSL_REDIRECT = False** (completely disabled)  
✅ **HSTS disabled** for localhost  
✅ **DEBUG = True** by default  
✅ **ALLOWED_HOSTS** includes localhost and 127.0.0.1  

The Django server is correctly configured. The issue is your browser's cached HSTS policy.

---

## 🎯 Quick Test

1. Open **Incognito/Private window** (`Ctrl+Shift+N`)
2. Go to: `http://127.0.0.1:8000`
3. If it works in incognito, you need to clear HSTS cache in your regular browser

---

## 💡 Why This Happens

Browsers cache HSTS (HTTP Strict Transport Security) policies. If you previously visited a site with HTTPS, the browser remembers to always use HTTPS for that domain - even for localhost!

The solution is to clear this cache so the browser will accept HTTP connections again.

