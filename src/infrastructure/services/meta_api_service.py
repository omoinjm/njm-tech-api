import asyncio
from metaapi_cloud_sdk import MetaApi
from datetime import datetime, timedelta

class MyClass:
    def __init__(self, token, accountId):
        self.api = MetaApi(token)
        self.accountId = accountId
        asyncio.run(self.test_meta_api_synchronization(accountId))
    
    async def test_meta_api_synchronization(self):
        try:
            account = await self.api.metatrader_account_api.get_account(self.accountId)
            initial_state = account.state
            deployed_states = ['DEPLOYING', 'DEPLOYED']

            if initial_state not in deployed_states:
                #  wait until account is deployed and connected to broker
                print('Deploying account')
                await account.deploy()
            
            print('Waiting for API server to connect to broker (may take couple of minutes)')
            await account.wait_connected()

            # connect to MetaApi API
            connection = account.get_rpc_connection()
            await connection.connect()

            # wait until terminal state synchronized to the local state
            print('Waiting for SDK to synchronize to terminal state (may take some time depending on your history size)')
            await connection.wait_synchronized()
        


        except Exception as err:
            print(api.format_error(err))
    