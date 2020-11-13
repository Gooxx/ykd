
from db2 import db,logging,cursor,querySQL,updateSQL,insertSQL,selectBy,selectOneBy
import time
import datetime
import logging
import act

def delayMsDateFrom(day,addDays,ydId):
    """延期秒杀活动专用，day为目前已有秒杀的最后一天时间，adddays是要延期的天数，ydid是药店id"""
    try:
        sql = f'''SELECT * from am_stages_sale s 
                WHERE sg_start_time >= '{day} 00:00:00' and sg_end_time <= '{day} 23:59:59'
                and s.pharmacy_id = {ydId}
                ;'''
        stagesList = selectBy(sql)
        
        for dic in stagesList:
            lineSql =''
            sgId = dic['sg_id']

            # dirId = dic['dir_id']
            # remark = dic['sg_detail_remark'] if dic['sg_detail_remark']!=None else 'NULL'
            # flag = dic['sg_detail_flag']
            # type = dic['sg_detail_type']
            start = dic['sg_start_time'].strftime('%Y-%m-%d %H:%M:%S')
            end = dic['sg_end_time'].strftime('%Y-%m-%d %H:%M:%S')
            for i in range(addDays):
                # logging.info(datetime.datetime.strptime(day,'%Y-%m-%d')+datetime.timedelta(days=i+1))
                today = (datetime.datetime.strptime(day,'%Y-%m-%d')+datetime.timedelta(days=i+1)).strftime('%Y-%m-%d')
                # logging.info('%s----%s----%s',day,today,type(start))
                sd = start.replace(day, today)
                nd = end.replace(day, today)
                # logging.info('%s----%s----',sd,nd)
                lineSql += f"""('{dic['pharmacy_id']}','{dic['sg_title']}','{dic['sg_status']}','{sd}','{nd}','{dic['quota_id']}','{dic['act_id']}','{dic['item_id']}',now(),now()),"""
            lineSql=lineSql[:-1]


            sql = f"""INSERT INTO `medstore`.`am_stages_sale` ( `pharmacy_id`, `sg_title`, `sg_status`, `sg_start_time`, `sg_end_time`, `quota_id`, `act_id`, `item_id`, `sg_create_time`, `sg_update_time`)
                    VALUES {lineSql} ; """
            res = insertSQL(sql)

            # logging.info(sql)
            firstId = res['lastId']
            count = res['count']
            lastId = firstId+count-1

            sql = f'''SELECT * from am_stages_sale s left join am_stages_sale_detail sd on s.sg_id = sd.sg_id 
                WHERE sg_start_time >= '{day} 00:00:00' and sg_end_time <= '{day} 23:59:59'
                and s.pharmacy_id = {ydId}
                and s.sg_id = {sgId}
                ;'''
            stagesdetailList = selectBy(sql)
            for ddic in stagesdetailList:
                dirId = ddic['dir_id']
                remark = ddic['sg_detail_remark'] if ddic['sg_detail_remark']!=None else 'NULL'
                flag = ddic['sg_detail_flag']
                type = ddic['sg_detail_type']

                detailSql= f"""INSERT INTO `medstore`.`am_stages_sale_detail` (  `sg_id`, `act_id`, `item_id`, `quota_id`, `pharmacy_id`, `dir_id`, `sg_detail_create_time`, `sg_detail_update_time`, `sg_detail_remark`, `sg_detail_flag`, `sg_detail_type`) 
                                SELECT `sg_id`, `act_id`, `item_id`, `quota_id`, `pharmacy_id`,'{dirId}' `dir_id`,NOW() `sg_detail_create_time`,NOW() `sg_detail_update_time`
                                ,'{remark}' `sg_detail_remark`,'{flag}' `sg_detail_flag`,'{type}' `sg_detail_type` 
                                from am_stages_sale
                                WHERE sg_id between {firstId} and {lastId} ;"""
                insertSQL(detailSql)

            # saleSql= f"""INSERT INTO `medstore`.`am_stages_sale_detail` (  `sg_id`, `act_id`, `item_id`, `quota_id`, `pharmacy_id`, `dir_id`, `sg_detail_create_time`, `sg_detail_update_time`, `sg_detail_remark`, `sg_detail_flag`, `sg_detail_type`) 
            #                 SELECT `sg_id`, `act_id`, `item_id`, `quota_id`, `pharmacy_id`,'{dirId}' `dir_id`,NOW() `sg_detail_create_time`,NOW() `sg_detail_update_time`
            #                 ,{remark} `sg_detail_remark`,'{flag}' `sg_detail_flag`,'{type}' `sg_detail_type` 
            #                 from am_stages_sale
            #                 WHERE sg_id between {firstId} and {lastId} ;"""
            # insertSQL(saleSql)
        copyMsSale(day,addDays,ydId)
        copyMsStat(day,addDays,ydId)
        logging.info('----------------------------------over---------------------------')
        db.commit()
    except Exception as err:
        logging.error("Error %s for execute sql: %s" % (err, tableName))
        db.rollback()


    

def copyMsSale(day,addDays,ydId):
    sql = f'''SELECT * from pm_sku_sale sale,pm_prod_sku s
                WHERE sale.sku_id = s.sku_id and s.drugstore_id={ydId} 
                and sale_start_time >= '{day} 00:00:00' and sale_end_time <= '{day} 23:59:59';'''
    saleList = selectBy(sql)
    
    for dic in saleList:
        lineSql =''
        sku_id = dic['sku_id']
        sale_fee = dic['sale_fee']
        sale_price = dic['sale_price']
        sale_status = dic['sale_status']
        sale_remark = dic['sale_remark']

        start = dic['sale_start_time'].strftime('%Y-%m-%d %H:%M:%S')
        end = dic['sale_end_time'].strftime('%Y-%m-%d %H:%M:%S')
        for i in range(addDays):
            today = (datetime.datetime.strptime(day,'%Y-%m-%d')+datetime.timedelta(days=i+1)).strftime('%Y-%m-%d')
            sd = start.replace(day, today)
            nd = end.replace(day, today)
            lineSql += f"""('{sku_id}','{sale_fee}','{sale_price}','{sd}','{nd}','{sale_status}',now(),now(),'{sale_remark}'),"""
        lineSql=lineSql[:-1]
        sql = f"""INSERT INTO `medstore`.`pm_sku_sale` ( `sku_id`, `sale_fee`, `sale_price`, `sale_start_time`, `sale_end_time`, `sale_status`, `sale_create_time`, `sale_update_time`, `sale_remark`)
                VALUES {lineSql} ; """
        res = insertSQL(sql)

        # logging.info(sql)
        # firstId = res['lastId']
        # count = res['count']
        # lastId = firstId+count-1
def copyMsStat(day,addDays,ydId):
    sql = f'''SELECT * from am_stat_info stat,pm_prod_sku s
                WHERE stat.sku_id = s.sku_id and s.drugstore_id={ydId}  
                and item_effect_time >= '{day} 00:00:00' and item_expire_time <= '{day} 23:59:59'
                ;'''
    statList = selectBy(sql)
    configSql = '''SELECT config_value from sm_config WHERE config_key = 'act_batch';'''
    configDic = selectOneBy(configSql)
    configValue =configDic.get('config_value')
    for dic in statList:
        lineSql =''
        skuId = dic.get('sku_id')
        actId = dic.get('act_id')
        itemId = dic.get('item_id')
        itemName = dic.get('item_name')
        itemRemark = dic.get('item_remark')
        itemType = dic.get('item_type')

        quotaId = dic.get('quota_id') if dic.get('quota_id')!=None else ''
        # logging.error('quotaId-------%s---%s--',dic.get('quota_id'),dic.get('quota_id') if dic.get('quota_id')!=None else '')
        # dirId = dic.get('dir_id')
        # dirCode = dic.get('dir_code')

        itemAttr = dic.get('item_attr')
        otherStr1 = dic.get('other_str1','') if dic.get('other_str1')!=None else ''
        itemPriority = dic.get('item_priority')

        start = dic['item_effect_time'].strftime('%Y-%m-%d %H:%M:%S')
        end = dic['item_expire_time'].strftime('%Y-%m-%d %H:%M:%S')
        for i in range(addDays):
            today = (datetime.datetime.strptime(day,'%Y-%m-%d')+datetime.timedelta(days=i+1)).strftime('%Y-%m-%d')
            sd = start.replace(day, today)
            nd = end.replace(day, today)
            lineSql += f"""( '{configValue}', '{skuId}', '{actId}', '{itemId}', '{itemRemark}', '{itemName}'
                    , '{itemAttr}', now(), now(), '{sd}', '{nd}'
                    , '{itemType}', '{otherStr1}', '{quotaId}', NULL, '{itemPriority}'),"""
            # lineSql += f"""('{sku_id}','{sale_fee}','{sale_price}','{sd}','{nd}','{sale_status}',now(),now(),'{sale_remark}'),"""
        lineSql=lineSql[:-1]
        sql = f"""INSERT INTO am_stat_info (  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark` , `item_name`
                , `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`
                , `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`) 
                VALUES {lineSql} ; """
        res = insertSQL(sql)

        # logging.info(sql)

# def creatJHS(tableName,drugstoreId,startTime,endTime):
#     try:
     
#         addNewSku4JHSMS(tableName,'JHS',drugstoreId)
#         addPmActSale(tableName,drugstoreId,startTime,endTime)
        
#         # 1501
#         db.commit()
#     except Exception as err:
#         logging.error("Error %s for execute sql: %s" % (err, tableName))
#         db.rollback()

if __name__ == "__main__":
    # am_act_info am_act_item 
    # am_stage_sale am_stage_sale_detai,
    #  pm_sku_sale,
    # am_stat_info
    logging.info('首先创建一天的秒杀活动， 然后延期到计划的天数，')




    logging.info('开始延期秒杀活动啦--------------------------------------------------')
    # day1 = '2020-08-12'
    # addDays1 = 141
    # ydId1 = '1600'
    # delayMsDateFrom(day1,addDays1,ydId1)

    # day2 = '2020-08-09'
    # addDays2 = 143
    # ydId2 = '1601'
    # delayMsDateFrom(day2,addDays2,ydId2)

    # day3 = '2020-08-09'
    # addDays3 = 143
    # ydId3 = '1603'
    # delayMsDateFrom(day3,addDays3,ydId3)
    # db.commit()

    day = '2020-08-12'
    addDays = 141
    ydId = '1603'
    delayMsDateFrom(day,addDays,ydId)
    db.commit()

    logging.info(f'延期秒杀活动完成， 根据{day}的秒杀数据，在{ydId}店---延期了{addDays}天--------------------------------------------------')

    # copyMsSale(day,addDays,ydId)
    # copyMsStat(day,addDays,ydId)
    # db.commit()