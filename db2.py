import pymysql
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# from werkzeug import secure_filename
import logging

logger = logging.getLogger()
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my-611.log', level=logging.DEBUG, format=LOG_FORMAT)
#  创建一个handler，用于将日志输出到控制台
# log = logging.StreamHandler()
# log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)
# 基于pymysql 

isDeve = False
if isDeve: # 准生产
   host = 'rm-2ze7fnv9ydw78u07a7o.mysql.rds.aliyuncs.com'
   logging.info('deve准生产数据库连接--------'+host)
else:# 生产
   host = 'rdsb7rqeyb7rqeyyo.mysql.rds.aliyuncs.com'
   logging.info('store生产数据库连接--------'+host)
db = pymysql.connect(host,user = "camore",passwd = "camore",db = "medstore")

# db = pymysql.connect('rm-2zeu8n6l02168zxwe4o.mysql.rds.aliyuncs.com',user = "camore",passwd = "camore",db = "medstore")
# 准生产
# db = pymysql.connect('rm-2ze7fnv9ydw78u07a7o.mysql.rds.aliyuncs.com',user = "camore",passwd = "camore",db = "medstore")

# 生产只读
# db = pymysql.connect('rr-2zepi5ii881yk8fug5o.mysql.rds.aliyuncs.com',user = "camore",passwd = "camore",db = "medstore")
# 生产
# host ='rdsb7rqeyb7rqeyyo.mysql.rds.aliyuncs.com'
# db = pymysql.connect(host,user = "camore",passwd = "camore",db = "medstore")

# db = pymysql.connect('rdsb7rqeyb7rqey434.mysql.rds.aliyuncs.com',user = "camore",passwd = "camore",db = "medstore") # 生产
cursor=db.cursor(cursor=pymysql.cursors.DictCursor)

# 基于 SQLAlchemy
# conn = create_engine('mysql://camore:camore:rm-2zeu8n6l02168zxwe4o.mysql.rds.aliyuncs.com/medstore', echo=True)
# cursor = engine.connect()

#创建pythonBD数据库
# reult=cursor.execute('select * from pm_prod_info limit 100;')
# print('添加语句受影响的行数：',reult)
# results = cursor.fetchall()
# print('添加语句受影响的行数2：',results)
# cursor.close()#先关闭游标
# conn.close()#再关闭数据库连接
 
# app = Flask(__name__)

# db = SQLAlchemy()
# # 初始化App配置 这个app配置就厉害了,专门针对 SQLAlchemy 进行配置
# # SQLALCHEMY_DATABASE_URI 配置 SQLAlchemy 的链接字符串儿
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:DragonFire@127.0.0.1:3306/dragon?charset=utf8"
# # SQLALCHEMY_POOL_SIZE 配置 SQLAlchemy 的连接池大小
# app.config["SQLALCHEMY_POOL_SIZE"] = 5
# # SQLALCHEMY_POOL_TIMEOUT 配置 SQLAlchemy 的连接超时时间
# app.config["SQLALCHEMY_POOL_TIMEOUT"] = 15
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# # 初始化SQLAlchemy , 本质就是将以上的配置读取出来
# db.init_app(app)

def querySQL(sql):
   logging.debug(sql)
   try:
      cursor.execute(sql)
      # db.commit()
      # logging.debug('querySQL语句受影响的行数：：',cursor.rowcount,'最后一个id',cursor.lastrowid )
      # print('querySQL语句受影响的行数：',cursor.rowcount,cursor.lastrowid )
      logging.debug('querySQL语句受影响的行数：：%s  %s',cursor.rowcount,cursor.lastrowid )
      return {
         'code':200,
         'count':cursor.rowcount,
         'lastId':cursor.lastrowid,
         'data':cursor.fetchall()
      }
      #  cursor.fetchall()
   # except Exception:
   except Exception as err:
      db.rollback()
      logging.error("Error %s for execute sql: %s" % (err, sql))
      logging.debug('新建商品的品牌墙，insert语句失败！！！')
      return {
         'code':404,
         'count':0,
         'lastId':0,
         'data':[]
      }



def updateSQL(sql):
   logging.debug(sql)
   # try:
   cursor.execute(sql)
   # db.commit()
   logging.debug('insert语句受影响的行数：%s  %s',cursor.rowcount,cursor.lastrowid )
   return {
      'code':200,
      'count':cursor.rowcount,
      'lastId':cursor.lastrowid,
      'data':cursor.fetchall()
   }
   # except Exception:
   # except Exception as err:
   #    logging.error("Error %s for execute sql: %s" % (err, sql))
   #    logging.debug('语句失败！！！')
   #    db.rollback()
   #    return {
   #       'code':404,
   #       'count':0,
   #       'lastId':0,
   #       'data':[]
   #    }
def insertSQL(sql):
   # print(sql)
   return updateSQL(sql)
def selectDemo():
   # SQL 删除语句
   sql = '''select * from pm_prod_info 
   limit 10;
   '''
   try:
      # 执行SQL语句
      cursor.execute(sql)
      results = cursor.fetchall()
      print('添加语句受影响的行数2：',results)
      for result in results:
         pid = result['prod_id']
         # pid = result[0]
         print('添加语句受影响的行数2：',pid)
      # 提交修改
      db.commit()
   except:
      # 发生错误时回滚
      db.rollback()


def selectBy(sql):
   '''只返回结果'''
   logging.debug(sql)
   try:
      cursor.execute(sql)
      # db.commit()
      # logging.debug('querySQL语句受影响的行数：：',cursor.rowcount,'最后一个id',cursor.lastrowid )
      # print('querySQL语句受影响的行数：',cursor.rowcount,cursor.lastrowid )
      logging.debug('querySQL语句受影响的行数：：%s  %s',cursor.rowcount,cursor.lastrowid )
      return cursor.fetchall()
      #  cursor.fetchall()
   # except Exception:
   except Exception as err:
      db.rollback()
      logging.error("Error %s for execute sql: %s" % (err, sql))
      logging.debug('新建商品的品牌墙，insert语句失败！！！')
      return []

def selectOneBy(sql):
   '''只返回结果'''
   logging.debug(sql)
   try:
      cursor.execute(sql)
      # db.commit()
      # logging.debug('querySQL语句受影响的行数：：',cursor.rowcount,'最后一个id',cursor.lastrowid )
      # print('querySQL语句受影响的行数：',cursor.rowcount,cursor.lastrowid )
      res = cursor.fetchone()
      logging.debug('querySQL语句受影响的行数：：%s  %s',cursor.rowcount,res)
      return res
      #  cursor.fetchall()
   # except Exception:
   except Exception as err:
      # db.rollback()
      logging.error("Error %s for execute sql: %s" % (err, sql))
      logging.debug('selectOneBy语句失败！！！')
      return ''
def test():
    print('test=============')
# selectDemo() 