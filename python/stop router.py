import requests

ROUTER_IP = '192.168.10.1'
USERNAME = 'admin'
PASSWORD = 'fariamaria123'
WEBSITE_URL = 'www.youtube.com'

# Session object for persistent connection
session = requests.Session()

# Login to router
login_url = f'http://{ROUTER_IP}/login'
login_data = {'username': USERNAME, 'password': PASSWORD}
response = session.post(login_url, data=login_data)

if response.status_code == 200:
    print('Login successful')
else:
    print('Login failed')
    exit()

# Pause router
pause_url = f'http://{ROUTER_IP}/pause'
response = session.post(pause_url)

if response.status_code == 200:
    print('Router paused')
else:
    print('Failed to pause router')
    exit()

# Add website to blocklist
block_url = f'http://{ROUTER_IP}/block'
block_data = {'website': WEBSITE_URL}
response = session.post(block_url, data=block_data)

if response.status_code == 200:
    print(f'{WEBSITE_URL} blocked successfully')
else:
    print(f'Failed to block {WEBSITE_URL}')
    exit()

# Unpause router
unpause_url = f'http://{ROUTER_IP}/unpause'
response = session.post(unpause_url)

if response.status_code == 200:
    print('Router unpaused')
else:
    print('Failed to unpause router')
    exit()

# Close session
session.close()
