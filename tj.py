from db2 import db,cursor,querySQL,updateSQL,insertSQL,selectBy,selectOneBy
import time
import datetime
import json
import logging
import xlwt
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
# worksheet = workbook.add_sheet('检查一下56')
style = xlwt.XFStyle()

style.num_format_str = 'M/D/YY h:mm:ss'

def selectNewRegister(ydId,start,end):
    """新注册 并访问某药店的人数"""
    sql = f"""SELECT   DISTINCT u.`user_id` 
                FROM `um_user_info` AS u , st_user_visit AS v 
                WHERE  v.`user_id`= u.`user_id` 
                    and u.`regist_date` BETWEEN   '{start}'  and '{end}' 
                    and v.`pharmacy_id` IN ({ydId}) """
    res = insertSQL(sql)
    logging.info(f"新注册用户数：                   人数为： {res['count']} --- 从{start} 到 {end} 注册，并访问{ydId}药店的  ")
    return res['count']

def selectOrderUsers(ydId,start,end):
    """月下单用户数"""
    sql = f"""  SELECT `user_id` from `om_order_info` o 
                WHERE `pharmacy_id` IN ({ydId}) 
                    and o.order_create_time BETWEEN '{start}'  and '{end}'  AND o.`order_status`= 44 
                    GROUP BY o.`user_id` ; """
    res = insertSQL(sql)
    logging.info(f"月下单用户数：                   人数为： {res['count']} --- 从{start} 到 {end} 在{ydId}药店下单")
    return res['count']

def selectRepeatOrderUsersMoreThan2(ydId,start,end):
    """App累计重复下单用户数（2单以上）"""
    sql = f""" SELECT u.`user_id` 
                FROM `om_order_info` o  LEFT JOIN `um_user_info` u ON u.`user_id`= o.`user_id` 
                WHERE `pharmacy_id`  IN ({ydId}) 
                and o.order_create_time <= '{end}' 
                AND o.`order_status`= 44 
                and o.`order_type`= 'normal' GROUP BY o.`user_id` HAVING  COUNT(o.`order_id`)>= 2
            ; """
    res = insertSQL(sql)
    logging.info(f"App累计重复下单用户数（2单以上）：人数为： {res['count']} --- 从{start} 到 {end} 在{ydId}药店下单")
    return res['count']

def selectRepeatOrderUsersMoreThan3(ydId,start,end):
    """App累计重复下单用户数（3单以上）"""
    sql = f"""  SELECT u.`user_id` 
                FROM `om_order_info` o  LEFT JOIN `um_user_info` u ON u.`user_id`= o.`user_id` 
                WHERE `pharmacy_id`  IN ({ydId}) 
                and o.order_create_time <= '{end}' 
                AND o.`order_status`= 44 
                and o.`order_type`= 'normal' GROUP BY o.`user_id` HAVING  COUNT(o.`order_id`)>= 3; """
    res = insertSQL(sql)
    logging.info(f"App累计重复下单用户数（3单以上）：人数为： {res['count']} --- 从{start} 到 {end} 在{ydId}药店下单")
    return res['count']
def selectNewOrderUsers(ydId,start,end):
    """本月新增下单用户数"""
    sql = f"""   SELECT o.`user_id` FROM `om_order_info` o   
                WHERE `pharmacy_id`IN ({ydId})  
                and o.order_create_time BETWEEN  '{start}'  and '{end}' 
                AND o.`order_status`= 44 and o.`order_type`= 'normal' and o.`user_id` NOT IN(  
                SELECT o1.`user_id` FROM `om_order_info` o1  
                WHERE o1.`pharmacy_id` IN ({ydId})  
                and o1.order_create_time < '{start}' 
                AND o1.`order_status`= 44 and o1.`order_type`= 'normal' GROUP BY o1.`user_id`) GROUP BY o.`user_id`  ; """
    res = insertSQL(sql)
    logging.info(f"本月新增下单用户数：             人数为： {res['count']} --- 从{start} 到 {end} 在{ydId}药店下单")
    return res['count']
#   console.log("总注册人数 执行的sql：" + sqlzzcrs);
if __name__ == "__main__":
    ydId = '1600,1601'
    start = '2020-03-01'
    end = '2020-04-01'
    selectNewRegister(ydId,start,end)
    selectOrderUsers(ydId,start,end)
    selectRepeatOrderUsersMoreThan2(ydId,start,end)
    selectRepeatOrderUsersMoreThan3(ydId,start,end)
    selectNewOrderUsers(ydId,start,end)
    db.commit()