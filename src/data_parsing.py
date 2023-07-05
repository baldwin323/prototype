```python
import json
from marshmallow import Schema, fields, ValidationError

class UserSchema(Schema):
    id = fields.Str(required=True)
    username = fields.Str(required=True)
    follower_count = fields.Int(required=True)
    engagement_metrics = fields.Dict(required=True)
    content_uploads = fields.List(fields.Str(), required=True)

class ChatHistorySchema(Schema):
    id = fields.Str(required=True)
    messages = fields.List(fields.Str(), required=True)

class ResponseSchema(Schema):
    id = fields.Str(required=True)
    response = fields.Str(required=True)

class PaymentSchema(Schema):
    id = fields.Str(required=True)
    status = fields.Str(required=True)

def parse_data(schema, data):
    try:
        result = schema().load(json.loads(data))
        return result
    except ValidationError as e:
        print(f"Error occurred while parsing data: {e}")
        return None

def parse_user_data(data):
    return parse_data(UserSchema, data)

def parse_chat_history(data):
    return parse_data(ChatHistorySchema, data)

def parse_response_data(data):
    return parse_data(ResponseSchema, data)

def parse_payment_data(data):
    return parse_data(PaymentSchema, data)
```