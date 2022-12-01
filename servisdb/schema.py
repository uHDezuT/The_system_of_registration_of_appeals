# import db_models
import json
from base64 import b64encode, b64decode


class RabbitBody:
    appeal: dict

    def __init__(self, appeal):
        self.appeal = appeal

    def decode(self):
        dict_appeal = self.appeal
        return json.loads(b64decode(dict_appeal))

    # @staticmethod
    # def decode(encoded):
    #     dicc = json.loads(b64decode(encoded))
    #     fibo = dicc["fibo"]
    #     return RabbitBody(fibo)


#
# # Add File to DB
# def add_appeal_to_db(db, **kwargs):
#     new_appeal = db_models.Appeals(
#         last_name=kwargs['last_name'],
#         first_name=kwargs['first_name'],
#         second_name=kwargs['second_name'],
#         telephone=kwargs['telephone'],
#         body=kwargs['body']
#     )
#     db.add(new_appeal)
#     db.commit()
#     db.refresh(new_appeal)
#     return new_appeal



