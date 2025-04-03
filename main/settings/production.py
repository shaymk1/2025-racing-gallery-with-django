
from .base import *
from .base import *

# Enable secure cookies for sessions and CSRF
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Redirect all HTTP traffic to HTTPS
SECURE_SSL_REDIRECT = True

# Enable HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Prevent the browser from guessing content types
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable XSS protection
SECURE_BROWSER_XSS_FILTER = True