from flask import Flask, redirect, request,url_for,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
# from acthelper import *

# pymysql.install_as_MySQLdb() 
# from db import db
# from demo import selectDemo,test,cursor,conn
# from db import cursor,conn
# from werkzeug import secure_filename

app = Flask(__name__)
# 初始化App配置 这个app配置就厉害了,专门针对 SQLAlchemy 进行配置
# SQLALCHEMY_DATABASE_URI 配置 SQLAlchemy 的链接字符串儿
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://camore:camore@rm-2zeu8n6l02168zxwe4o.mysql.rds.aliyuncs.com/medstore'
# # "mysql+pymysql://root:DragonFire@127.0.0.1:3306/dragon?charset=utf8"
# # SQLALCHEMY_POOL_SIZE 配置 SQLAlchemy 的连接池大小
# app.config["SQLALCHEMY_POOL_SIZE"] = 5
# # SQLALCHEMY_POOL_TIMEOUT 配置 SQLAlchemy 的连接超时时间
# app.config["SQLALCHEMY_POOL_TIMEOUT"] = 15
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# # 初始化SQLAlchemy , 本质就是将以上的配置读取出来
# # db.init_app(app)
# db = SQLAlchemy(app)
# # db.cursor(cursor=pymysql.cursors.DictCursor)
# conn = pymysql.connect('rm-2zeu8n6l02168zxwe4o.mysql.rds.aliyuncs.com',user = "camore",passwd = "camore",db = "medstore")
# cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)



@app.route('/')
def initMainPage():
   return render_template('hello.html')

@app.route('/test')
def hello_world():
   return render_template('hello.html')

@app.route('/act')
def actPage():
   return render_template('act.html')

@app.route('/act/comb')
def createComb():
   prodId = request.args.get('prodId')
   fee = request.args.get('fee')
   price = request.args.get('price')
   count = request.args.get('count')

   huohaos = request.args.get('huohaos')
   drugstoreIds = request.args.get('drugstoreIds')
   logging.info('------------- createComb: %s %s',huohaos,drugstoreIds)
   hlist = huohaos.split(',')
   dlist = drugstoreIds.split(',')
   for huohao in hlist:
      for drugstoreId in dlist:
         createCombByHuohao(huohao,drugstoreId,prodId,fee,price,count=count)
         buildSkuBaseByHuohao(huohao,drugstoreId)
   return jsonify({'code':'200'})

@app.route('/act/label')
def createLabel():
   huohaos = request.args.get('huohaos')
   drugstoreIds = request.args.get('drugstoreIds')
   logging.info('------------- createComb: %s %s',huohaos,drugstoreIds)
   hlist = huohaos.split(',')
   dlist = drugstoreIds.split(',')
   for huohao in hlist:
      for drugstoreId in dlist:
         buildSkuBaseByHuohao(huohao,drugstoreId)
   return jsonify({'code':'200'})

# 药店的按钮 轮播 九宫格
# @app.route('/showViews')
# def showViews():
#    # request.form['name'] post
#    drugstoreIds = request.args.get("drugstoreIds")
#    type = request.args.get("type")
#    typesql = ''
#    if type=='web':
#       typesql = ' and link_view is null '
#    else:
#       typesql = ' and link_view  in ("'+ type +'") '
#    print(drugstoreIds)
#    sql = '''SELECT `link_id`, `drugstore_id`, `seq_num` 排序, `image_url`, `link_url`,  `link_name`
#             , `link_status`, `link_view`,`link_type`, `link_param`, `link_remark`, `link_start_time`, `link_end_time`
#             from sm_image_link
#             WHERE  
#              link_version =1
#             {0}
#             and drugstore_id in ({1})
#             ORDER BY link_id DESC;
#    '''.format(typesql,drugstoreIds)
#    print(sql)
#    try:
#       # 执行SQL语句
#       cursor.execute(sql)
#       results = cursor.fetchall()
#       print('添加语句受影响的行数2：',results)
#       # for result in results:
#       #    pid = result['prod_id']
#       #    # pid = result[0]
#       #    print('添加语句受影响的行数2：',pid)
#       # 提交修改
#       # conn.commit()
#    except:
#       # 发生错误时回滚
#       conn.rollback()
#    return jsonify(results)

# # 药店的按钮 轮播 九宫格 替换 图片
# @app.route('/updateMainImage')
# def updateMainImage():
#    # return jsonify({'a':'b'})
#    # request.form['name'] post
#    type = request.args.get("type")
#    img = request.args.get("img")
#    sql = '''UPDATE sm_image_link set image_url = {0}
#             WHERE 
#             link_name = '分类找药'
#             and link_version =1
#             and drugstore_id in {1} ;
#    '''.format(img,type)

#    # sql = "INSERT INTO `medstore`.`sm_image_link` ( link_id, `drugstore_id` ) VALUES (  '1000', '1000' );"
#    print(sql)
#    try:
#       # 执行SQL语句
#       cursor.execute(sql)
#       print('添加语句受影响的行数2：',cursor.rowcount,cursor.lastrowid )

#       conn.commit()
#    except Exception:
#       #如果发生异常，则回滚  
#       print("发生异常",Exception)
#       #输出异常信息  
#       # traceback.print_exc() 
#       # 发生错误时回滚
#       conn.rollback()
#       return jsonify({'code':'500','message':'数据执行失败啦','lastId':cursor.lastrowid})
   
#    return jsonify({'code':'200','message':'数据执行成功啦','lastId':cursor.lastrowid})

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      f.save('./uploads/'+f.filename)
      # f.save(secure_filename(f.filename))
   return 'file uploaded successfully'

# def test(self,name):
#    print('testestest===========')
#    return 'testestest==========='

if __name__ == '__main__':
   
   # # 初始化App配置 这个app配置就厉害了,专门针对 SQLAlchemy 进行配置
   # # SQLALCHEMY_DATABASE_URI 配置 SQLAlchemy 的链接字符串儿
   # app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://camore:camore:rm-2zeu8n6l02168zxwe4o.mysql.rds.aliyuncs.com/medstore'
   # # "mysql+pymysql://root:DragonFire@127.0.0.1:3306/dragon?charset=utf8"
   # # SQLALCHEMY_POOL_SIZE 配置 SQLAlchemy 的连接池大小
   # app.config["SQLALCHEMY_POOL_SIZE"] = 5
   # # SQLALCHEMY_POOL_TIMEOUT 配置 SQLAlchemy 的连接超时时间
   # app.config["SQLALCHEMY_POOL_TIMEOUT"] = 15
   # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

   # # 初始化SQLAlchemy , 本质就是将以上的配置读取出来
   # db.init_app(app)
   app.debug = True
   app.run()