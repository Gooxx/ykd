from db2 import db,cursor,querySQL,updateSQL,insertSQL,selectBy,selectOneBy
import time
import datetime
# import datetime from dateutil.relativedelta import relativedelta
import json
import logging
import xlwt
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
# worksheet = workbook.add_sheet('检查一下56')
style = xlwt.XFStyle()

style.num_format_str = 'M/D/YY h:mm:ss'

# import xlwt
# # 创建一个workbook 设置编码
# workbook = xlwt.Workbook(encoding = 'utf-8')
# # 创建一个worksheet
# # worksheet = workbook.add_sheet('检查一下56')
# style = xlwt.XFStyle()

# style.num_format_str = 'M/D/YY h:mm:ss'

# Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0


# 写入excel
# 参数对应 行, 列, 值
# worksheet.write(1,0, label = 'this is test')

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
    res = querySQL(sql)
    logging.info(f"本月新增下单用户数：             人数为： {res['count']} --- 从{start} 到 {end} 在{ydId}药店下单")
    return res['count']
#   console.log("总注册人数 执行的sql：" + sqlzzcrs);

def selectTYUserGrow():
    """ -- 1、天一店在20190501-20200430期间，以月为单位，每个月历史累计下过1单（不含首单）、2单（不含首单）、3单（不含首单）、4单（不含首单）、5单（不含首单）、6单（不含首单）、7单及以上（不含首单）的用户明细，以及这些用户历史首次下单的时间（年月日）；
        -- 例如5月份：
        -- 1、A用户5月31日前无下单记录，在5月份当月下过1单，不统计进来；
        -- 2、A用户5月31日前无下单记录，在5月份当月下过2单，计算在1单用户中；
        -- 3、A用户5月31日前无下单记录，在5月份当月下过3单，计算在2单用户中，以此类推"""
    day = '2019-05-01'
    worksheet = workbook.add_sheet(day)
    for i in range(13):
        # nextMonth = datetime.datetime.strptime(day,'%Y-%m-%d') + relativedelta(months=+i)
        # logging.info(f"nextMonth {nextMonth}")
        # today = (datetime.datetime.strptime(day,'%Y-%m-%d')+datetime.timedelta(month=i+1)).strftime('%Y-%m-%d')
        sql = f"""  SELECT COUNT(a.dan) ds,a.dan from (
                        SELECT COUNT(o.user_id) cu
                        ,CASE WHEN COUNT(o.user_id)=1 then '0' 
                        WHEN COUNT(o.user_id)=2 then '1' 
                        WHEN COUNT(o.user_id)=3 then '2' 
                        WHEN COUNT(o.user_id)=4 then '3' 
                        WHEN COUNT(o.user_id)=5 then '4' 
                        WHEN COUNT(o.user_id)=6 then '5' 
                        WHEN COUNT(o.user_id)=7 then '6' 
                        else '7' end dan, o.user_id
                        FROM om_order_info o 
                        WHERE 
                        o.order_create_time < date_add(STR_TO_DATE('{day}', '%Y-%m-%d'),interval {i} MONTH) 
                        and o.pharmacy_id = 200
                        and o.order_status = 44
                        GROUP BY o.user_id
                    ) a
                    GROUP BY dan ; """
        res = querySQL(sql)
        logging.info(f"天一店在20190501-20200430期间，以月为单位：{day} + {i} -- {res['data']} ---")
        for dic in res['data']:
            dan = dic['dan']
            ds = dic['ds']
            if int(dan)==0:
                worksheet.write(i,0, label = f'{day}+{i}')
            else:
                worksheet.write(i,int(dan), label = ds)
            # for (key,value) in dic:
            #     worksheet.write(i,0, label = 'this is test')
        # today = time.strftime("%Y%m%d%H%M%S", time.localtime())  # (datetime.datetime.strptime(day,'%Y-%m-%d')+datetime.timedelta(days=i+1)).strftime('%Y-%m-%d')
    workbook.save(f'{day}.xls')
        # return res['count']


def selectTYThisMonthOrderUsers():
    """ 2、20190501-20200430期间，以月为单位，当月下单的老用户数（即当月下单的全部用户减去在当月下首单的用户），以及这些老用户当月产生的订单总数；"""
    day = '2019-05-01'
    worksheet = workbook.add_sheet(day)
    for i in range(13):
        # nextMonth = datetime.datetime.strptime(day,'%Y-%m-%d') + relativedelta(months=+i)
        # logging.info(f"nextMonth {nextMonth}")
        # today = (datetime.datetime.strptime(day,'%Y-%m-%d')+datetime.timedelta(month=i+1)).strftime('%Y-%m-%d')
        # sql = f""" SELECT DATE_FORMAT(o.order_create_time,'%Y-%m') as 年月 ,COUNT(DISTINCT o.user_id) 用户数量,COUNT(o.order_id) 订单数量
        #             FROM om_order_info o 
        #             WHERE 
        #             o.order_create_time BETWEEN date_add(STR_TO_DATE('{day}', '%Y-%m-%d'),interval {i} MONTH) and date_add(STR_TO_DATE('{day}', '%Y-%m-%d'),interval {i+1} MONTH)
        #             and o.pharmacy_id = 200
        #             and o.order_status = 44 
        #             and   EXISTS (
        #                     SELECT * -- user_id 
        #                     from  om_order_info oi
        #                     WHERE oi.order_create_time < date_add(STR_TO_DATE('{day}', '%Y-%m-%d'),interval {i} MONTH) 
        #                     and oi.pharmacy_id = 200
        #                     and oi.order_status = 44 
        #                     and o.user_id = oi.user_id
                    
        #             )
        #             GROUP BY 年月; """
        sql = f"""SELECT o.*,o1.*,COUNT(o.user_id) tmcount
                    from (
                    SELECT DATE_FORMAT(o.order_create_time,'%Y-%m') as 年月,DATE_FORMAT(DATE_ADD(o.order_create_time,interval -day(o.order_create_time)+1 day),'%Y-%m-%d') 年月日,o.order_id,o.user_id,o.pharmacy_id,o.order_create_time
                    FROM om_order_info o 
                    WHERE 
                    o.order_create_time BETWEEN date_add(STR_TO_DATE('{day}', '%Y-%m-%d'),interval {i} MONTH) and date_add(STR_TO_DATE('{day}', '%Y-%m-%d'),interval {i+1} MONTH)
                    and o.pharmacy_id = 200
                    and o.order_status = 44 ) o, 
                    (SELECT MIN(o1.order_create_time) mt,COUNT(o1.user_id) pastcount,o1.user_id
                        from  om_order_info o1 
                        where 
                        o1.pharmacy_id = 200
                        and o1.order_create_time < date_add(STR_TO_DATE('{day}', '%Y-%m-%d'),interval {i} MONTH)
                        and o1.order_status = 44
                        GROUP BY o1.user_id
                    ) o1
                    WHERE o.user_id= o1.user_id
                    GROUP BY o.user_id;""" 

        res = querySQL(sql)
        # logging.info(f"20190501-20200430期间，以月为单位，当月下单的老用户数：{day} + {i} -- {res['count']} ---")

        list = res['data']
        totleUsers = res['count']
        totleOrders = 0
        o2eOrderList=[0]*16
        # o2eOrderDic ={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0} #{} # {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
        for dic in list:
            mon = dic['年月']

            tmcount = dic['tmcount']
            totleOrders=totleOrders+tmcount
            pastcount = dic['pastcount']
            if int(pastcount)>=8:
                # o2eOrderDic[8] = o2eOrderDic[8]+ tmcount
                o2eOrderList[8*2-2]=o2eOrderList[8*2-2]+1
                o2eOrderList[8*2-1]=o2eOrderList[8*2-1]+tmcount
            else:
                o2eOrderList[pastcount*2-2]=o2eOrderList[pastcount*2-2]+1
                o2eOrderList[pastcount*2-1]=o2eOrderList[pastcount*2-1]+tmcount
                # o2eOrderDic[pastcount] = o2eOrderDic[pastcount]+tmcount

        logging.info(f"{mon},{totleUsers},{totleOrders},{o2eOrderList}")
        # for dic in res['data']:
        #     dan = dic['dan']
        #     ds = dic['ds']
        #     if int(dan)==0:
        #         worksheet.write(i,0, label = f'{day}+{i}')
        #     else:
        #         worksheet.write(i,int(dan), label = ds)
            # for (key,value) in dic:
            #     worksheet.write(i,0, label = 'this is test')
        # today = time.strftime("%Y%m%d%H%M%S", time.localtime())  # (datetime.datetime.strptime(day,'%Y-%m-%d')+datetime.timedelta(days=i+1)).strftime('%Y-%m-%d')
    # workbook.save(f'{day}.xls')
if __name__ == "__main__":
    # selectTYUserGrow()
    selectTYThisMonthOrderUsers()
    db.commit()
    # ydId = '1600,1601'
    # start = '2020-03-01'
    # end = '2020-04-01'
    # selectNewRegister(ydId,start,end)
    # selectOrderUsers(ydId,start,end)
    # selectRepeatOrderUsersMoreThan2(ydId,start,end)
    # selectRepeatOrderUsersMoreThan3(ydId,start,end)
    # selectNewOrderUsers(ydId,start,end)
    # db.commit()