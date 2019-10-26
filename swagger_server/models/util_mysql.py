# Connect MySQL
import mysql.connector
from mysql.connector import pooling
from swagger_server.models.secret import password,user,database,host



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

  def exe(self,sql="SELECT * FROM `comment` WHERE `comment_id` < %s", agrs:list=[10]) -> list:
      cursor=self.connection_objt.cursor()
      cursor.execute(sql, agrs)
      result = cursor.fetchall()
      cursor.close()
      return result

  def close(self):
      del self.connection_objt
