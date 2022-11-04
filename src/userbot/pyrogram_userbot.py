import asyncio
from pyrogram.errors import ApiIdInvalid, PhoneCodeExpired, PhoneCodeInvalid, PhoneNumberInvalid
from pyrogram import Client
import pdb

class Pyrogram:
    def __init__(self, api_id, api_hash, phone):
        self.app = ''
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone = phone

        while True:
            try:
                self.app = self.log_in(self.api_id, self.api_hash)
                self.app.connect()
            except RuntimeError as e:
                if "There is no current event loop in thread" in str(e):
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    continue
            break

    def exit(self, *args):
        self.app.disconnect()

    def log_in(self, api_id, api_hash):
        return Client(':memory:', in_memory=True, api_id=api_id, api_hash=api_hash, test_mode=True) # TODO: remove test_mode

    def get_hash(self):
        try:
            phone_hash = self.app.send_code(self.phone)
            return phone_hash.phone_code_hash
        except (ApiIdInvalid, PhoneNumberInvalid) as e:
            return e

    def send_confirmation(self, phone_hash, confirmation_code):
        try:
            result = self.app.sign_in(self.phone, phone_hash, confirmation_code)
            print(result)
            pdb.set_trace()
            return True
        except (PhoneCodeExpired, PhoneCodeInvalid) as e:
            return e

    def get_session_string(self):
        return self.app.export_session_string()
