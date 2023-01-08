import requests 
import json

class Node:
	def __init__(self,api_key,wallet_pw,node_address,node_ip):
		
		self.wallet_pw = wallet_pw 
		self.node_address = node_address
		self.req_url = f'http://{node_ip}/'
		self.header = {
						'api_key':api_key,
						'Accept': 'application/json',
						'Content-Type': 'application/json'
						}
	def send_payment_tx(self,address,erg_value = 0.001,assets = []):
		erg_value = erg_value*10**9
		send_payment_header = [
						{
							'address' : address,
	 						'value' : erg_value,
	 						'assets': assets

						}	
					]
		send_payment = requests.post(f"{self.req_url}wallet/payment/send",headers = self.header,data = json.dumps(send_payment_header)).json()
		return send_payment

	def unlock_wallet(self):
		unlock_wallet_header = {"pass" : self.wallet_pw}
		unlock_wallet = requests.post(f"{self.req_url}wallet/unlock",headers = self.header,data = json.dumps(unlock_wallet_header)).json()
		return unlock_wallet

	def get_tokens(self):
		get_tokens = requests.get(f'{self.req_url}wallet/balances',headers = self.header).json()['assets']
		return get_tokens

	def get_erg_balance(self):
		get_erg_balance = requests.get(f'{self.req_url}wallet/balances',headers = self.header).json()['balance']*10**-9
		return get_erg_balance

	def get_transactions(self):
		get_transactions = requests.get(f'{self.req_url}wallet/transactions',headers = self.header).json()
		return get_transactions 

	def get_boxId_byIdBinary(self,boxId):
		get_boxId_byIdBinary = requests.get(f'{self.req_url}utxo/withPool/byIdBinary/{boxId}',headers = self.header).json()
		return get_boxId_byIdBinary 

	def get_transaction_byId(self,txId):
		get_transaction_byId = requests.get(f'{self.req_url}wallet/transactionById?id={txId}',headers = self.header).json()
		return get_transaction_byId

	def get_address_ergotree(self):
		get_address_ergotree = requests.get(f'{self.req_url}utils/addressToRaw/{self.node_address}',headers = self.header).json()['raw']  
		return '0008cd'+ get_address_ergotree





