from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio
from telethon.errors.rpcerrorlist import SessionPasswordNeededError, PhoneNumberUnoccupiedError, ApiIdInvalidError, PhoneNumberInvalidError, FloodWaitError

class Telethon:
    def __init__(self, api_id, api_hash, phone):
        self.phone = phone
        while True:
            try:
                self.app = TelegramClient(StringSession(), api_id=api_id, api_hash=api_hash)
                self.app.loop.run_until_complete(self.app.connect())
            except RuntimeError as e:
                if "There is no current event loop in thread" in str(e):
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    continue
            break

    def exit(self, *args):
        self.app.disconnect()

    def send_code_request(self):
        try:
            phone_hash = self.app.loop.run_until_complete(self.app.send_code_request(self.phone))
            self.phone_hash = phone_hash.phone_code_hash
            return self.phone_hash
        except (ApiIdInvalidError, PhoneNumberInvalidError, FloodWaitError) as e:
            return e

    def sign_in(self, confirmation_code, password=None):
        try:
            result = self.app.loop.run_until_complete(self.app.sign_in(phone=self.phone, code=confirmation_code, phone_code_hash=self.phone_hash))
            return True
        except (SessionPasswordNeededError, PhoneNumberUnoccupiedError) as e:
            if isinstance(e, SessionPasswordNeededError) and password:
                result = self.app.loop.run_until_complete(self.app.sign_in(password=password))
                return True
            return e

    def get_session_string(self):
        return self.app.session.save()
