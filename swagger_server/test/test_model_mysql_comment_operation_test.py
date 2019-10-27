from swagger_server.models.util_mysql import comment_operation

c = comment_operation()
obj = c.select_comment_byid(comment_id= 10)
print(f"result obj type: {type(obj)}")
print(f"result obj: {obj.to_dict()}")


c = comment_operation()
id = c.new_comment_byid("classN_C", "teacherN_C", "major_C", "midexam_C", "endexam_C", "say_C", "value_C", "cost_C",1,0,0)
c.update_comment_byid(comment_id=int(id),classN="HIHI",teacherN="QQ")