return {"ERROR": "Unauthorized USER"}, 401_server.models.util_mysql import search_operation

c = search_operation()
#a = c.select_reply_byNewest()
#print(a)
#a = c.select_comment_byNewest()
#print(a)
a = c.select_comment_byKeyword(keyword="資訊")
print(a)
a = c.select_comment_byKeyword(keyword="資 訊")
print(a)
#a = c.select_reply_under_comment(comment_id=1)
#print(a)