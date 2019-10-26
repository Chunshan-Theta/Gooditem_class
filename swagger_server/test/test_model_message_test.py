from swagger_server.models.message import Message

a = Message(request_status="success",msg="hi")
print(a.to_dict())