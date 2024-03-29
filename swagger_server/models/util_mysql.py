# Connect MySQL
import mysql.connector
from mysql.connector import pooling
from swagger_server.models.secret import password,user,database,host
from swagger_server.models.comment import Comment
from swagger_server.models.reply import Reply
from swagger_server.models.util_logging import records



class MysqlObj(object):
    def __init__(self):
        self.maxdb = mysql.connector.connect(
          host = host,
          user = user,
          password = password,
          database = database
          )
    def test(self):
        cursor=self.maxdb.cursor()

        #
        cursor.execute("SELECT * FROM `comment` LIMIT 30")
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()

#a =MysqlObj()
#a.test()

connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="pynative_pool",
                                                              pool_size=8,
                                                              pool_reset_session=True,
                                                              host=host,
                                                              database=database,
                                                              user=user,
                                                              password=password)
class MysqlObj_pool(MysqlObj):
  def __init__(self):
      global connection_pool
      self.connection_objt = connection_pool.get_connection()

  def test(self):
      cursor=self.connection_objt.cursor()
      #
      cursor.execute("SELECT * FROM `comment` LIMIT 30")
      result = cursor.fetchall()
      for row in result:
          print(row)
      cursor.close()

  def exe(self,sql="SELECT * FROM `comment` WHERE `comment_id` < %s", agrs:list=[10]):
      cursor=self.connection_objt.cursor()
      cursor.execute(sql, agrs)
      #print("[SQL]:\t{}".format(cursor.statement))
      records("SQL","MySql_util","{}".format(cursor.statement))
      try:
          result = cursor.fetchall()

          return result
      except mysql.connector.errors.InterfaceError as e:
          #print("[Row]:\t{}".format(cursor.lastrowid))
          records("SQL", "MySql_util", "{}".format(cursor.lastrowid),"error")
          self.connection_objt.commit()
          cursor.close()
          return str(cursor.lastrowid)
      finally:
          cursor.close()
          self.connection_objt.close()
          del self.connection_objt

  def close(self):
      self.connection_objt.close()
      del self.connection_objt

class comment_operation(MysqlObj_pool):
  def select_comment_byid(self,comment_id = 1) -> Comment:
      sql = "SELECT * FROM `comment` WHERE `comment_id` = %s"
      agrs= [comment_id]
      result = self.exe(sql=sql,agrs=tuple(agrs))[0]
      Commentobj = Comment(comment_id=result[0], object_type=result[13], class_name=result[1],
                               teacher_name=result[2],
                               user_memo=result[6],major=result[3],midexam=result[4],endexam=result[5],
                               value=result[7],cost=result[8],classcall=result[9],homework=result[10],classexam=result[11])

      return Commentobj
  def delete_comment_byid(self,comment_id) -> Comment:
      sql = "DELETE FROM `comment` WHERE `comment`.`comment_id` = %s"
      agrs= [comment_id]
      result = self.exe(sql=sql,agrs=tuple(agrs))

      return result
  def new_comment_byid(self, classN, teacherN, major, midexam, endexam, say, value, cost,classcall,homework,classexam):

      sql = "INSERT INTO `comment` (`comment_id`, `classN`, `teacherN`, `major`, `midexam`, `endexam`, `say`, `value`, `cost`, `classcall`, `homework`, `classexam`, `posttime`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP);"
      agrs = [classN, teacherN, major, midexam, endexam, say, value, cost,classcall,homework,classexam]
      result = self.exe(sql=sql, agrs=tuple(agrs))
      return result

  def update_comment_byid(self,comment_id:int, classN = None, teacherN= None, major= None, midexam= None, endexam= None, say= None, value= None, cost= None,classcall= None,homework= None,classexam= None):
      sql = "UPDATE `comment` SET "
      agrs = []
      field = {
          "classN": classN,
          "teacherN": teacherN,
          "major": major,
          "midexam": midexam,
          "endexam": endexam,
          "say": say,
          "value": value,
          "cost": cost,
          "classcall": classcall,
          "homework": homework,
          "classexam": None
      }

      for key, val in field.items():
          if val is None: continue
          if len(agrs) !=0:
              sql += ", `{}` = %s ".format(key)
          else:
              sql += " `{}` = %s ".format(key)

          agrs.append(val)
      if len(agrs) == 0: #args empty
          raise IOError("args empty")

      sql += " WHERE `comment`.`comment_id` = {};".format(comment_id)
      #print(sql % tuple(agrs))
      _ = self.exe(sql=sql, agrs=tuple(agrs))
      return comment_id
  # INSERT INTO `comment` (`comment_id`, `classN`, `teacherN`, `major`, `midexam`, `endexam`, `say`, `value`, `cost`, `classcall`, `homework`, `classexam`, `posttime`) VALUES (NULL, '奇幻中文課', '鍾老師', '資訊管理系', '沒有', '沒有', '好課程', '價值連城', '浪費生命', '0', '0', '0', CURRENT_TIMESTAMP);
  # DELETE FROM `comment` WHERE `comment`.`comment_id` = 195
  # UPDATE `comment` SET `classN` = '版主回饋' WHERE `comment`.`comment_id` = 194;

class reply_operation(MysqlObj_pool):

  def select_reply_byid(self,reply_id = 1) -> Reply:
      sql = "SELECT * FROM `comment_reply` WHERE `reply_id` = %s;"
      agrs= [reply_id]
      result = self.exe(sql=sql,agrs=tuple(agrs))[0]
      reply_obj = Reply(replay_id=result[0],comment_id=result[2],user_memo=result[1],object_type=result[3])
      return reply_obj

  def delete_reply_byid(self,reply_id):
      sql = "DELETE FROM `comment_reply` WHERE `comment_reply`.`reply_id` = %s"
      agrs= [reply_id]
      result = self.exe(sql=sql,agrs=tuple(agrs))

      return result
  def new_reply_byid(self, comment_id, user_memo, object_type="normal"):

      sql = "INSERT INTO `comment_reply` (`reply_id`, `content`, `comment_id`, `object_type`) VALUES (NULL, %s, %s, %s);"
      agrs = [user_memo, comment_id, object_type]
      result = self.exe(sql=sql, agrs=tuple(agrs))
      return result

  def update_reply_byid(self):
      return NotImplementedError


class search_operation(MysqlObj_pool):

  def select_reply_byNewest(self,num = 30) -> list:
      responds = list()
      sql = "SELECT * FROM `comment_reply` ORDER BY `reply_id` DESC limit %s";
      agrs= [num]
      result = self.exe(sql=sql,agrs=tuple(agrs))
      for r in result:
          reply_id = r[0]
          reply_content = r[1]
          reply_comment_id = r[2]
          reply_type = r[3]
          reply_obj = Reply(replay_id=reply_id,comment_id=reply_comment_id,user_memo=reply_content,object_type=reply_type)
          responds.append(reply_obj.to_dict())
      return responds
  def select_reply_under_comment(self,comment_id,num = 30) -> list:
      responds = list()
      sql = "SELECT * FROM `comment_reply` WHERE `comment_id`=%s ORDER BY `reply_id` DESC limit %s";
      agrs= [comment_id,num]
      result = self.exe(sql=sql,agrs=tuple(agrs))
      for r in result:
          reply_id = r[0]
          reply_content = r[1]
          reply_comment_id = r[2]
          reply_type = r[3]
          reply_obj = Reply(replay_id=reply_id,comment_id=reply_comment_id,user_memo=reply_content,object_type=reply_type)
          responds.append(reply_obj.to_dict())
      return responds

  def select_comment_byNewest(self,start_num=0,num = 30) -> list:
      responds = list()
      sql = "SELECT * FROM `comment` ORDER BY `comment_id` DESC limit %s,%s";
      agrs= [start_num,start_num+num]
      results = self.exe(sql=sql,agrs=tuple(agrs))
      for result in results:
          Commentobj = Comment(comment_id=result[0], object_type=result[13], class_name=result[1],
                               teacher_name=result[2],
                               user_memo=result[6],major=result[3],midexam=result[4],endexam=result[5],
                               value=result[7],cost=result[8],classcall=result[9],homework=result[10],classexam=result[11])
          responds.append(Commentobj.to_dict())
      return responds


  def select_comment_byKeyword(self,keyword:str) -> list:
      responds = list()
      sql = "SELECT *  FROM `comment` WHERE"
      agrs = list()
      for idx,k in enumerate(keyword.split(" ")):
          if idx != 0:
              sql += " OR "
          sql+=" `classN` LIKE %s OR `teacherN` LIKE %s OR `major` LIKE %s OR `say` LIKE %s ";
          agrs.extend(["%"+k+"%"] * 4)
      sql+= "ORDER BY `comment_id`  DESC"
      results = self.exe(sql=sql,agrs=tuple(agrs))
      for result in results:
          Commentobj = Comment(comment_id=result[0], object_type=result[13], class_name=result[1],
                               teacher_name=result[2],
                               user_memo=result[6], major=result[3], midexam=result[4], endexam=result[5],
                               value=result[7], cost=result[8], classcall=result[9], homework=result[10],
                               classexam=result[11])
          responds.append(Commentobj.to_dict())
      return responds