# import db_models
import json
from base64 import b64decode

import pika


class RabbitBody:
    appeal: dict

    def __init__(self, appeal):
        self.appeal = appeal

    def decode(self):
        return json.loads(b64decode(self.appeal))