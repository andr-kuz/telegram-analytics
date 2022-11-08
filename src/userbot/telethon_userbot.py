from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio
from telethon.errors.rpcerrorlist import SessionPasswordNeededError, PhoneNumberUnoccupiedError, ApiIdInvalidError, PhoneNumberInvalidError, FloodWaitError
import pdb

class Telethon:
    def __init__(self, api_id, api_hash, phone):
        self.app = ''
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone = phone

        while True:
            try:
                self.app = self.log_in()
                self.app.loop.run_until_complete(self.app.connect())
            except RuntimeError as e:
                if "There is no current event loop in thread" in str(e):
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    continue
            break

    def exit(self, *args):
        self.app.disconnect()

    def log_in(self):
        return TelegramClient(StringSession(), api_id=self.api_id, api_hash=self.api_hash)

    def request_code(self):
        try:
            phone_hash = self.app.loop.run_until_complete(self.app.send_code_request(self.phone))
            self.phone_hash = phone_hash.phone_code_hash
            return self.phone_hash
        except (ApiIdInvalidError, PhoneNumberInvalidError, FloodWaitError) as e:
            return e

    def send_confirmation(self, confirmation_code, password=''):
        try:
            if not password:
                result = self.app.loop.run_until_complete(self.app.sign_in(phone=self.phone, code=confirmation_code, phone_code_hash=self.phone_hash))
            else:
                result = self.app.loop.run_until_complete(self.app.sign_in(password=password))
            return True
        except SessionPasswordNeededError as e:
            return e
        except PhoneNumberUnoccupiedError as e:
            return e

    def get_session_string(self):
        return self.app.session.save()
