from swagger_server.models.util_mysql import reply_operation

c = reply_operation()
obj = c.select_reply_byid(reply_id=10)
id = c.new_reply_byid(1, "balbalbal")
c.delete_reply_byid(reply_id=int(id))

#c = comment_operation()
#id = c.new_comment_byid("classN_C", "teacherN_C", "major_C", "midexam_C", "endexam_C", "say_C", "value_C", "cost_C",1,0,0)
#c.update_comment_byid(comment_id=int(id),classN="HIHI",teacherN="QQ")
#c.delete_comment_byid(comment_id=int(id))