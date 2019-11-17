from swagger_server.models.reply import Reply

a = Reply(comment_id=1,object_type="normal",user_memo="超過100分",replay_id=-1)
print(a.to_dict())