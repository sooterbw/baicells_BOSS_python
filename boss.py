import requests
from datetime import datetime
from base64 import b64encode
from typing import List

class Subscriber:
    def __init__(self, sub_id:str, sub_name:str, imsi:int=0, id_num:int=0, phone_number:int=0, email:str="", address:str="") -> None:
        self.sub_id = sub_id
        self.sub_name = sub_name
        self.imsi = imsi
        self.id_num = id_num
        self.phone_number = phone_number
        self.email = email
        self.address = address

class BOSS:
    def __init__(self, username:str, password:str, cloud_key:str) -> None:
        self.headers = {
            "cloud_key": cloud_key,
            "Authorization": b64encode(f"{username}:{password}".encode()).decode()
        }
        self.session_id = datetime.now().strftime('%Y%m%d%H')
        self.url = 'http://baiboss.cloudapp.net:47081/baicellsapi/'

    def query_by_imsi(self, imsi:int) -> dict:
        '''
        Query subscriber by IMSI
        '''
        r = requests.post(
            self.url + 'customers/query',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "imsi": imsi
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def query_by_sub_id(self, sub_id:str) -> dict:
        '''
        Query subscriber by their id
        '''
        r = requests.post(
            self.url + 'customers/querybyid',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "sub_id": sub_id
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def create_sub(self, sub:Subscriber) -> dict:
        '''
        Create new subscriber in BOSS
        sub_id: the ID string used by BOSS (must be unique)
        id_num: the ID number you wish to use externally (should be unique)
        '''
        r = requests.post(
            self.url + 'customers/create',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "sub_id": sub.sub_id,
                "sub_name": sub.sub_name,
                "id_num": sub.id_num,
                "phone_number": sub.phone_number,
                "email": sub.email,
                "address": sub.address
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def bulk_create_subs(self, service_plan_id:str, subs:List[Subscriber]) -> dict:
        '''
        Creates multiple subscriber accounts at once
        '''
        r = requests.post(
            self.url + 'customers/bulkcreate',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "service_plan_id": service_plan_id,
                "sub_list": [{
                    "sub_id": i.sub_id,
                    "sub_name": i.sub_name,
                    "imsi": i.imsi,
                    "id_num": i.id_num,
                    "phone_number": i.phone_number,
                    "email": i.email,
                    "address": i.address
                } for i in subs]
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def bind_service_plan(self, service_plan_id:str, sub_id:str=0, imsi:int=0) -> dict:
        '''
        Bind service plan to subscriber's account
        '''

        r = requests.post(
            self.url + 'customers/bindservice',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "sub_id": sub_id if sub_id else self.query_by_imsi(imsi)['data']['sub_id'],
                "service_plan_id": service_plan_id
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def update_service_plan(self, service_plan_id:str, sub_id:str="", imsi:int=0) -> dict:
        '''
        Update service plan attached to subscriber's account
        '''

        r = requests.post(
            self.url + 'customers/update',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "sub_id": sub_id if sub_id else self.query_by_imsi(imsi)['data']['sub_id'],
                "new_service_plan_id": service_plan_id
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def bind_imsi(self, sub_id:str, imsi:int) -> dict:
        '''
        Bind SIM from subscriber's account
        '''

        r = requests.post(
            self.url + 'customers/bindimsi',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "sub_id": sub_id,
                "imsi": imsi
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def unbind_imsi(self, sub_id:str="", imsi:int=0) -> dict:
        '''
        Unbind SIM from Subscriber's account
        '''

        r = requests.post(
            self.url + 'customers/unbindimsi',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "sub_id": sub_id if sub_id else self.query_by_imsi(imsi)['data']['sub_id']
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def activate(self, sub_id:str="", imsi:int=0) -> dict:
        '''
        Activate subsriber's SIM
        '''

        r = requests.post(
            self.url + 'customers/activate',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "sub_id": sub_id if sub_id else self.query_by_imsi(imsi)['data']['sub_id']
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def bulk_activate(self, sub_id_list:List[str]) -> dict:
        '''
        Activate multiple subscribers at once
        '''
        r = requests.post(
            self.url + 'customers/bulkactivate',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "data": sub_id_list
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def deactivate(self, sub_id:int=0, imsi:int=0) -> dict:
        '''
        Deactivate subscriber's SIM
        '''

        r = requests.post(
            self.url + 'customers/deactivate',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "sub_id": sub_id if sub_id else self.query_by_imsi(imsi)['data']['sub_id']
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def bulk_deactivate(self, sub_id_list:List[str]) -> dict:
        '''
        Deactivate multiple subscribers at once
        '''

        r = requests.post(
            self.url + 'customers/bulkdeactivate',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "data": sub_id_list
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def update_sub(self, sub:Subscriber) -> dict:
        '''
        Update subscriber information
        '''

        r = requests.post(
            self.url + 'customers/modify',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "sub_id": sub.sub_id if sub.sub_id else self.query_by_imsi(sub.imsi)['data']['sub_id'],
                "sub_name": sub.sub_name,
                "id_num": sub.id_num,
                "phone_number": sub.phone_number,
                "email": sub.email,
                "address": sub.address
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def delete(self, sub_id:str="", imsi:int=0) -> dict:
        '''
        Delete subscriber from CloudCore
        '''
        r = requests.post(
            self.url + 'customers/delete',
            headers = self.headers,
            json = {
                "session_id": self.session_id,
                "sub_id": sub_id if sub_id else self.query_by_imsi(imsi)['data']['sub_id']
            }
        )
        data = {
            "data": r.json(),
            "status": r.status_code
        }
        return data

    def get_service_plans(self) -> dict:
        '''
        Get list of service plans available
        '''
        r = requests.get(
            self.url + 'products/queryallplans',
            headers = self.headers,
        )
        return {
            "data": r.json(),
            "status": r.status_code
        }

    def modify_service_plan(self, service_id:str, service_plan_name:str, uplink:int, downlink:int) -> dict:
        '''
        Updates service plan for all subscribers
        '''
        r = requests.post(
            self.url + 'products/modify',
            headers = self.headers,
            json = {
                'session_id': self.session_id,
                'service_plan_id': service_id,
                'service_plan_name': service_plan_name,
                'uplink': uplink,
                'downlink': downlink
            }
        )
        return {
            "data": r.json(),
            "status": r.status_code
        }