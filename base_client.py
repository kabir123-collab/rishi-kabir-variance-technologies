# Author - Karan Parmar

"""
Trade engine client
"""

import json
from datetime import datetime

import requests

class TradeEngineClient:

	ROOT_ENDPOINT = "http://localhost:80"

	def __init__(self):

		self.token = ''

	# Private methods
	def __request(self, method:str, endpoint:str, params:dict=None, data:dict=None) -> dict:
		"""
		Sends REST like request to the server\n
		"""
		url = self.ROOT_ENDPOINT + endpoint
		if data and (data.get('Content-Type') is None):
			data = json.dumps(data)
		return requests.request(method=method, url=url, params=params, data=data)

	def __request_with_token(self, method:str, endpoint:str, params:dict=None, data:dict=None) -> dict:
		"""
		Sends REST like authenticated request to the server\n
		"""
		url = self.ROOT_ENDPOINT + endpoint
		if data and data.get('Content-Type') is None:
			data = json.dumps(data)
		headers = {"Authorization" : f"Bearer {self.token}"}
		return requests.request(method=method, url=url, params=params, data=data, headers=headers)

	# Public methods
	
	## Auth
	def create_user(self, data:dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/auth/register"
		
		return self.__request(method=method, endpoint=endpoint, data=data)
	
	def request_verify_token(self, email: str) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/auth/request-verify-token"
		data = {
			"email": email,
		}
		return self.__request(method=method, endpoint=endpoint, data=data)
	
	def verify(self, token: str) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/auth/verify"
		data = {
			'token': token
		}
		return self.__request(method=method, endpoint=endpoint, data=data)

	def login(self, data:dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/auth/jwt/login"
		# data.update({"Content-Type":"application/x-www-form-urlencoded)"})
		data.update({"Content-Type":"multipart/form-data"})
		response = self.__request(method=method, endpoint=endpoint, data=data)
		if 'access_token' in response.json():
			self.token = response.json()['access_token']
		return response, response.json()
	
	def forgot_password(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/auth/forgot-password"
		return self.__request(method=method, endpoint=endpoint, data=data)
	
	def reset_password(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/auth/reset-password"
		return self.__request(method=method, endpoint=endpoint, data=data)

	def logout(self) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/auth/jwt/logout"
		return self.__request_with_token(method=method, endpoint=endpoint)

	def get_user(self) -> dict:
		"""
		"""
		method = "GET"
		endpoint = "/users/me"
		return self.__request_with_token(method=method, endpoint=endpoint)
	
	def get_user_info(self) -> dict:
		"""
		"""
		method = "GET"
		endpoint = "/user/get-user-info"
		return self.__request_with_token(method=method, endpoint=endpoint)
	
	def update_user_info(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/update-user-info"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	

	def add_broker_account(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/account"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def get_broker_accounts(self) -> dict:
		"""
		"""
		method = "GET"
		endpoint = "/user/account"
		data = {}
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def remove_broker_account(self, account_id: str) -> dict:
		"""
		"""
		method = "DELETE"
		endpoint = "/user/account"
		data = {
			"account_id": account_id
		}
		return self.__request_with_token(method=method, endpoint=endpoint, params=data)
	

	def create_base_strategy(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/strategy/"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def get_base_strategy(self, strategy_id: str) -> dict:
		"""
		"""
		method = "GET"
		endpoint = "/strategy/"
		data = {"strategy_id": strategy_id}
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def update_base_strategy(self, data: dict) -> dict:
		"""
		"""
		method = "PATCH"
		endpoint = "/strategy/"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def delete_base_strategy(self, strategy_id: str) -> dict:
		"""
		"""
		method = "DELETE"
		endpoint = "/strategy/"
		data = {"strategy_id": strategy_id}
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	
	def get_user_strategy(self, strategy_id: str) -> dict:
		"""
		"""
		method = "GET"
		endpoint = "/user/strategy"
		data = {"strategy_id": strategy_id}
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def get_user_all_strategies(self) -> dict:
		"""
		"""
		method = "GET"
		endpoint = "/user/strategy"
		data = {}
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def get_user_created_strategies(self) -> dict:
		"""
		"""
		method = "GET"
		endpoint = "/user/strategy/me"
		data = {}
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def get_user_subscribed_strategies(self) -> dict:
		"""
		"""
		method = "GET"
		endpoint = "/user/strategy/subscription"
		data = {}
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def update_user_strategy_info(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/strategy/info"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def update_user_strategy_settings(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/strategy/settings"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def delete_base_strategy(self, strategy_id: str) -> dict:
		"""
		"""
		method = "DELETE"
		endpoint = "/user/strategy"
		data = {"strategy_id": strategy_id}
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def get_marketplace_strategies(self) -> dict:
		"""
		"""
		method = "GET"
		endpoint = "/marketplace/"
		data = {}
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def subscribe_strategy(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/marketplace/subscribe"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)

	def clone_user_strategy(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/strategy/clone"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def activate_user_strategy(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/strategy/activate"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def deactivate_user_strategy(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/strategy/deactivate"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def connect_broker_to_strategy(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/strategy/account/connect"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def disconnect_broker_to_strategy(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/strategy/account/disconnect"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def activate_broker_to_strategy(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/strategy/account/activate"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def diactivate_broker_to_strategy(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/strategy/account/deactivate"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def emergency_exit(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/emergency-exit"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def emergency_exit_strategy(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/emergency-exit/strategy"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
	def emergency_exit_account(self, data: dict) -> dict:
		"""
		"""
		method = "POST"
		endpoint = "/user/emergency-exit/account"
		return self.__request_with_token(method=method, endpoint=endpoint, data=data)
	
if __name__ == "__main__":

	client = TradeEngineClient()
	with open("credentials.json", "r") as file:
		credentials = json.load(file)
		file.close()
	# NOTE Register user
	data = {
		"email" : credentials["admin_email"],
		"password" : credentials["admin_password"]
	}
	response = client.create_user(data=data)
	print(response)
	print(response.json())

	# NOTE Request verification
	# email = "dummy1@example.com"
	# response = client.request_verify_token(email=email)
	# print(response)
	# print(response.json())

	# NOTE Verify user
	# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NDlkNjRkMjE3MWUxMjNlNTc3ZjU4YTciLCJlbWFpbCI6ImR1bW15MUBleGFtcGxlLmNvbSIsImF1ZCI6ImZhc3RhcGktdXNlcnM6dmVyaWZ5IiwiZXhwIjoxNjg4MDQ0ODk5fQ.TYfltcgqwk4Sp1KxQOX9gIuYE_eVzVK-K9FaD_iBVb4"
	# response = client.verify(token=token)
	# print(response)
	# print(response.json())

	# NOTE Login
	
	data = {
		"username" : credentials["admin_email"],
		"password" : credentials["admin_password"]
	}
	response = client.login(data=data)
	print(response)

	# NOTE Get current user
	# response = client.get_user()
	# print(response)
	# print(response.json())

	# NOTE Logout
	# response = client.logout()
	# print(response)
	# print(response.json())

	# NOTE Forgot password / Change password token generation
	# data = {
	# 	"email": "dummy1@example.com"
	# }
	# response = client.forgot_password(data=data)
	# print(response)

	# NOTE Reset password
	# data = {
	# 	"token": "",
	# 	"password": ""
	# }
	# response = client.reset_password(data=data)
	# print(response)


	# NOTE Get user info
	# response = client.get_user_info()
	# print(response)
	# print(response.json())

	# NOTE Update user info
	# data = {
	# 	"name": "Dummy 1"
	# }
	# response = client.update_user_info(data=data)
	# print(response.json())

