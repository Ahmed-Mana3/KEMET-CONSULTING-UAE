# Fixing SSL Error on Localhost

## The Problem
You're seeing `ERR_SSL_PROTOCOL_ERROR` because your browser is trying to access the site via HTTPS (`https://127.0.0.1:8000`), but Django's development server only serves HTTP.

## Solutions

### Solution 1: Use HTTP (Not HTTPS) ✅ **RECOMMENDED**

**Always use `http://` (not `https://`) for localhost:**

- ✅ **Correct**: `http://127.0.0.1:8000`
- ✅ **Correct**: `http://localhost:8000`
- ❌ **Wrong**: `https://127.0.0.1:8000` (causes SSL error)
- ❌ **Wrong**: `https://localhost:8000` (causes SSL error)

### Solution 2: Clear Browser HSTS Cache

If your browser keeps redirecting to HTTPS, clear the HSTS cache:

#### Chrome/Edge:
1. Go to: `chrome://net-internals/#hsts`
2. Under "Delete domain security policies", enter: `127.0.0.1`
3. Click "Delete"
4. Also delete: `localhost`
5. Close and reopen your browser

#### Firefox:
1. Go to: `about:config`
2. Search for: `security.tls.insecure_fallback_hosts`
3. Add: `127.0.0.1,localhost`
4. Restart Firefox

#### Safari:
1. Close Safari
2. Delete: `~/Library/Cookies/HSTS.plist`
3. Restart Safari

### Solution 3: Use Incognito/Private Mode

Temporarily use incognito/private browsing mode to bypass HSTS cache:
- Chrome: `Ctrl+Shift+N` (Windows) or `Cmd+Shift+N` (Mac)
- Firefox: `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
- Edge: `Ctrl+Shift+N` (Windows) or `Cmd+Shift+N` (Mac)

### Solution 4: Verify DEBUG Mode

Make sure `DEBUG=True` in your `.env` file:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
```

Then restart the server:
```bash
python manage.py runserver
```

## Quick Test

1. **Start the server:**
   ```bash
   python manage.py runserver
   ```

2. **Open your browser and go to:**
   ```
   http://127.0.0.1:8000
   ```
   (Notice: `http://` NOT `https://`)

3. **You should see your site!**

## Current Configuration

✅ **SSL Redirects**: Disabled when `DEBUG=True`  
✅ **HSTS**: Disabled when `DEBUG=True`  
✅ **CSRF**: Allows localhost when `DEBUG=True`  
✅ **ALLOWED_HOSTS**: Includes localhost and 127.0.0.1  

## Still Having Issues?

If you're still getting SSL errors:

1. **Check your `.env` file** - Make sure `DEBUG=True`
2. **Clear browser cache** - Clear all browsing data
3. **Try a different browser** - Test in a browser you haven't used before
4. **Check the URL** - Make absolutely sure you're using `http://` not `https://`
5. **Restart the server** - Stop and restart `python manage.py runserver`

## Production vs Development

- **Development (localhost)**: Uses `http://` - No SSL needed
- **Production (kemetvision.com)**: Uses `https://` - SSL required

The settings automatically handle this based on the `DEBUG` setting.

