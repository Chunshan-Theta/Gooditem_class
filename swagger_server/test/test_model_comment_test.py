from swagger_server.models.comment import Comment

a = Comment(comment_id=1,object_type="normal",class_name="中文課",teacher_name="鍾老師",user_memo="超過100分")
print(a.to_dict())