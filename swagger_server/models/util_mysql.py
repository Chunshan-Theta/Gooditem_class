# Connect MySQL
import mysql.connector
from mysql.connector import pooling
from swagger_server.models.secret import password,user,database,host
from swagger_server.models.comment import Comment



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
      print("[SQL]:\t{}".format(cursor.statement))
      try:
          result = cursor.fetchall()
          cursor.close()
          return result
      except mysql.connector.errors.InterfaceError as e:
          print("[Row]:\t{}".format(cursor.lastrowid))
          self.connection_objt.commit()
          cursor.close()
          return str(cursor.lastrowid)

  def close(self):
      del self.connection_objt

class comment_operation(MysqlObj_pool):
  def select_comment_byid(self,comment_id = 1) -> Comment:
      sql = "SELECT * FROM `comment` WHERE `comment_id` < %s"
      agrs= [comment_id]
      result = self.exe(sql=sql,agrs=tuple(agrs))
      Commentobj = Comment(comment_id=result[0], object_type="normal", class_name=result[1], teacher_name=result[2],
                           user_memo=result[6])

      return Commentobj

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