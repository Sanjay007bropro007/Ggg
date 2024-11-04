import random
import string
import time
import names
import requests
import logging
import discord
from discord.ext import commands

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# List of proxies for rotation
proxies_list = [
    {'http': 'http://43.153.207.93:3128'},
    {'http': 'http://3.70.244.223:8090'},
    {'http': 'http://54.93.97.30:8090'},
    {'http': 'http://165.22.77.86:8080'},
    {'http': 'http://180.180.213.237:8080'},
    {'http': 'http://38.156.72.86:8080'},
    {'http': 'http://170.78.144.41:8080'},
    {'http': 'http://119.252.167.130:41890'},
    {'http': 'http://119.76.142.133:8080'},
    {'http': 'http://41.204.53.30:80'},
    {'http': 'http://72.10.164.178:29847'},
    {'http': 'http://178.130.125.66:8080'},
    {'http': 'socks4://45.94.135.23:4500'},
    {'http': 'http://185.200.38.140:8080'},
    {'http': 'http://72.10.160.174:5337'},
    {'http': 'http://191.243.46.30:43241'},
    {'http': 'http://72.10.160.170:6511'},
    {'http': 'socks4://117.74.65.207:443'},
    {'http': 'http://72.10.160.172:1577'},
    {'http': 'http://15.235.12.19:3128'},
    {'http': 'http://103.169.133.42:8080'},
    {'http': 'http://109.61.42.223:80'},
    {'http': 'http://45.202.198.17:3128'},
    {'http': 'http://139.255.41.118:8080'},
    {'http': 'http://147.75.34.103:10001'},
    {'http': 'http://150.136.170.150:8090'},
    {'http': 'http://67.43.228.254:7271'},
    {'http': 'http://147.75.34.103:80'},
    {'http': 'http://109.195.113.65:8080'},
    {'http': 'http://103.180.123.93:8080'},
    {'http': 'http://103.191.218.255:8087'},
    {'http': 'http://217.112.80.252:80'},
    {'http': 'http://196.251.222.109:8104'},
    {'http': 'http://147.75.34.103:443'},
    {'http': 'http://51.159.159.73:80'},
    {'http': 'http://177.234.223.29:999'},
    {'http': 'http://150.136.4.250:3128'},
    {'http': 'http://144.126.216.57:80'},
    {'http': 'http://210.79.30.157:8080'},
    {'http': 'http://72.128.133.154:16099'},
    {'http': 'http://162.240.154.26:3128'},
    {'http': 'http://62.33.53.248:3128'},
    {'http': 'socks4://66.29.128.242:14330'},
    {'http': 'http://103.176.97.72:8090'},
    {'http': 'http://67.43.228.254:10439'},
    {'http': 'socks4://213.218.232.214:1344'},
    {'http': 'http://111.1.61.47:3128'},
    {'http': 'http://103.155.198.166:8082'},
    {'http': 'http://38.252.82.11:9090'},
    {'http': 'http://8.209.255.13:3128'},
    {'http': 'http://146.56.154.83:21000'},
    {'http': 'http://14.103.21.34:8081'},
    {'http': 'http://103.187.86.10:8182'},
    {'http': 'http://45.202.198.120:3128'},
    {'http': 'http://27.67.54.178:8080'},
    {'http': 'http://200.94.96.174:999'},
    {'http': 'http://103.48.70.57:83'},
    {'http': 'http://103.188.168.3:32650'},
    {'http': 'http://154.64.219.4:8888'},
    {'http': 'http://47.74.152.29:8888'},
    {'http': 'http://103.228.246.151:7070'},
    {'http': 'socks4://190.198.69.97:9064'},
    {'http': 'http://47.251.43.115:33333'},
    {'http': 'http://47.242.47.64:8888'},
    {'http': 'http://103.153.62.155:8080'},
    {'http': 'http://72.10.160.171:1811'},
    {'http': 'http://46.36.123.53:81'},
    {'http': 'http://67.43.236.20:25667'},
    {'http': 'socks4://47.89.159.212:80'},
    {'http': 'http://138.59.151.162:8080'},
    {'http': 'http://72.10.160.90:28753'},
    {'http': 'http://38.156.74.171:8080'},
    {'http': 'http://49.7.11.187:80'},
    {'http': 'http://91.235.75.57:8282'},
    {'http': 'http://178.128.113.118:23128'},
    {'http': 'http://221.219.99.76:9000'},
    {'http': 'http://193.233.84.99:1080'},
    {'http': 'http://72.10.160.90:11729'},
    {'http': 'http://38.41.0.60:11201'},
    {'http': 'http://177.43.72.250:3128'},
    {'http': 'http://182.93.85.225:8080'},
    {'http': 'http://23.88.51.178:8888'},
    {'http': 'http://198.49.68.80:80'},
    {'http': 'http://115.77.20.123:2024'},
    {'http': 'socks4://98.175.31.195:4145'},
    {'http': 'http://175.100.91.212:8080'},
    {'http': 'http://77.119.240.209:8080'},
    {'http': 'http://72.10.160.92:27555'},
    {'http': 'http://67.43.228.253:21117'},
    {'http': 'http://201.91.82.155:3128'},
    {'http': 'http://187.94.100.254:8080'},
    {'http': 'http://86.101.159.145:18080'},
    {'http': 'socks4://47.238.134.126:9080'},
    {'http': 'http://122.52.109.184:8080'},
    {'http': 'http://197.248.86.237:32650'},
    {'http': 'http://187.249.20.153:8081'},
    {'http': 'http://154.236.168.176:1981'},
    {'http': 'http://103.87.148.40:1111'},
    {'http': 'http://103.156.17.83:8181'},
    {'http': 'http://86.101.159.147:18080'},
    {'http': 'http://5.166.47.95:8080'},
    {'http': 'http://212.252.73.29:8080'}
]

class ProxyManager:
    def __init__(self, proxies):
        self.proxies = proxies

    def get_random_proxy(self):
        return random.choice(self.proxies)

    def get_proxy(self):
        proxy = self.get_random_proxy()
        logger.info(f"Using proxy: {proxy}")
        return proxy

proxy_manager = ProxyManager(proxies_list)

def get_headers(country, language):
    session = requests.Session()
    while True:
        try:
            # Generate a random user-agent
            user_agent = f'Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; ' \
                         f'{"".join(random.choices(string.ascii_uppercase, k=3))}{random.randint(111, 999)}) ' \
                         f'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'

            # Fetch a random proxy from the manager
            proxy = proxy_manager.get_proxy()

            # Initial request to Facebook for js_datr token
            res = session.get("https://www.facebook.com/", headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                              'Chrome/81.0.4044.138 Safari/537.36'
            }, proxies=proxy, timeout=10)
            js_datr = res.text.split('["_js_datr","')[1].split('",')[0]

            # Fetch Instagram cookies (csrftoken, mid, ig_did)
            insta_cookies = session.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers={
                'User-Agent': user_agent
            }, proxies=proxy, timeout=10).cookies

            # Initial headers
            headers1 = {
                'authority': 'www.instagram.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': f'{language}-{country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'cookie': f'dpr=3; csrftoken={insta_cookies["csrftoken"]}; mid={insta_cookies["mid"]}; ig_nrcb=1; ig_did={insta_cookies["ig_did"]}; datr={js_datr}',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': user_agent,
                'viewport-width': '980',
            }

            # Request Instagram main page to extract app_id and rollout_hash
            response1 = session.get('https://www.instagram.com/', headers=headers1, proxies=proxy, timeout=10)
            app_id = response1.text.split('APP_ID":"')[1].split('"')[0]
            rollout_hash = response1.text.split('rollout_hash":"')[1].split('"')[0]

            # Final headers with additional fields
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': f'{language}-{country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'dpr=3; csrftoken={insta_cookies["csrftoken"]}; mid={insta_cookies["mid"]}; ig_nrcb=1; ig_did={insta_cookies["ig_did"]}; datr={js_datr}',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/signup/email/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'sec-ch-ua-mobile': '?1',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-asbd-id': '198387',
                'x-csrftoken': insta_cookies["csrftoken"],
                'x-ig-app-id': app_id,
                'x-ig-www-claim': '0',
                'x-instagram-ajax': rollout_hash,
                'x-requested-with': 'XMLHttpRequest',
                'user-agent': user_agent
            }

            return headers  # Successfully generated headers, exit loop
        except (IndexError, KeyError, requests.RequestException) as e:
            logger.warning(f"Error generating headers: {e}. Retrying with a new proxy...")
            time.sleep(2)  # Wait briefly before retrying with a new proxy

def Get_UserName(Headers, Name, Email):
    try:
        proxy = proxy_manager.get_proxy()
        updict = {"referer": 'https://www.instagram.com/accounts/signup/birthday/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}
        
        while True:
            data = {
                'email': Email,
                'name': Name + str(random.randint(1, 99)),
            }

            response = requests.post(
                'https://www.instagram.com/api/v1/web/accounts/username_suggestions/',
                headers=Headers,
                data=data,
                proxies=proxy,
                timeout=30
            )
            if 'status":"fail' in response.text:
                logger.info(response.text)
            elif 'status":"ok' in response.text:
                logger.info(response.text)
                return random.choice(response.json()['suggestions'])
            else:
                logger.info(response.text)
    except Exception as e:
        logger.error(f"Error in Get_UserName: {e}")

def Send_SMS(Headers, Email):
    try:
        proxy = proxy_manager.get_proxy()
        data = {
            'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'email': Email,
        }

        response = requests.post(
            'https://www.instagram.com/api/v1/accounts/send_verify_email/',
            headers=Headers,
            data=data,
            proxies=proxy,
            timeout=30
        )
        return response.text
    except Exception as e:
        logger.error(f"Error in Send_SMS: {e}")

def Validate_Code(Headers, Email, Code):
    try:
        proxy = proxy_manager.get_proxy()
        updict = {"referer": 'https://www.instagram.com/accounts/signup/emailConfirmation/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}

        data = {
            'code': Code,
            'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'email': Email,
        }

        response = requests.post(
            'https://www.instagram.com/api/v1/accounts/check_confirmation_code/',
            headers=Headers,
            data=data,
            proxies=proxy,
            timeout=30
        )
        return response
    except Exception as e:
        logger.error(f"Error in Validate_Code: {e}")

def Create_Acc(Headers, Email, SignUpCode):
    try:
        proxy = proxy_manager.get_proxy()
        firstname = names.get_first_name()
        UserName = Get_UserName(Headers, firstname, Email)
        Password = firstname.strip() + '@' + str(random.randint(111, 999))

        updict = {"referer": 'https://www.instagram.com/accounts/signup/username/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}

        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{round(time.time())}:{Password}',
            'email': Email,
            'username': UserName,
            'first_name': firstname,
            'month': random.randint(1, 12),
            'day': random.randint(1, 28),
            'year': random.randint(1990, 2001),
            'client_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'seamless_login_enabled': '1',
            'tos_version': 'row',
            'force_sign_up_code': SignUpCode,
        }
        logger.info(f"Creating account with data: {data}")

        response = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
            headers=Headers,
            data=data,
            proxies=proxy,
            timeout=30
        )
        logger.info(response.text)
        if '"account_created":true' in response.text:
            logger.info(f'UserName: {UserName}')
            logger.info(f'PassWord: {Password}')
            return {"username": UserName, "password": Password}
        return False
    except Exception as e:
        logger.error(f"Error in Create_Acc: {e}")

# Set up the Discord bot with intents
intents = discord.Intents.default()
intents.messages = True  # Enable the message intent
bot = commands.Bot(command_prefix='1', intents=intents)

bot.remove_command('help')

@bot.command(name='1')
async def create_account(ctx, email: str):
    await ctx.send(f'Creating account for {email}...')
    headers = get_headers(country='US', language='en')

    ss = Send_SMS(headers, email)
    if 'email_sent":true' in ss:
        await ctx.send('Verification email sent! Please check your inbox for the code.')
        code_message = await bot.wait_for('message', check=lambda m: m.author == ctx.author)
        a = Validate_Code(headers, email, code_message.content)
        if 'status":"ok' in a.text:
            SignUpCode = a.json()['signup_code']
            success = Create_Acc(headers, email, SignUpCode)
            if success:
                embed = discord.Embed(title="Account created successfully!", color=discord.Color.green())
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1244903243663020083/1287296970393915453/IMG_20240804_163305_598.jpg?ex=66f259ba&is=66f1083a&hm=60cac0d5cd9e9329284b36bf7f537fae23f25adef305e108cde75ed4fa9781a6&")
                embed.add_field(name="Email", value=email, inline=False)
                embed.add_field(name="UserName", value=success['username'], inline=False)
                embed.add_field(name="Password", value=success['password'], inline=False)
                embed.set_footer(text="THIS BOT CREATED BY @BROPRO007")
                
                await ctx.send(embed=embed)
            else:
                await ctx.send('Failed to create account.')
        else:
            await ctx.send('Failed to validate the code.')
    else:
        await ctx.send('Failed to send SMS.')

# Run the bot with your token
TOKEN = ''
bot.run(TOKEN)

