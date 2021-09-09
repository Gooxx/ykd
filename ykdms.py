#coding=utf-8
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
                and s.pharmacy_id = {ydId};'''
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


def 创建秒杀(actId=0,actName = '',tableName ='',ydList = [],startTime='',endTime='',img = '',color = '',linkimg = '',linkurl = '',linkView = '',windowimg= ''):
    logging.debug('开始创建秒杀，名称为{{actName}}--数据表{{tableName}}-----所属药店{{ydList}} ----起止时间 {{startTime}}-{{endTime}}')
    if actId==0:
        iAct = queryTableLastOne('am_act_info',field='act_id',where ='',order='act_id desc')
        iActId = iAct['act_id']
        actId = iActId+1
    logging.debug(f'create活动act——id{actId}')
    for index in range(len(ydList)):
        try:
            drugstoreId = ydList[index]
            # 创建特价
            addPmActSale(tableName,drugstoreId,startTime,endTime)
            logging.info('创建价格------------')
            
            addAmActInfo(actId,actName,startTime,endTime,drugstoreId=drugstoreId)
            skuList = querySkuIdByTable(tableName,drugstoreId)
            dirList = queryTable(tableName,where=' dir_code !="" group by dir_code')
            itemList = queryTable(tableName,where='  item_code !="" group by item_code')
            if len(dirList)>0 or len(itemList)>0:
                logging.info(f'开始创建活动目录 {drugstoreId}')
                # logging.error('开始创建活动目录error')
                parentdirDic = addPmDirInfo(f'act{actId}',actName,drugstoreId,img=img,color=color,num='1',level='2',parentDirId='')
                parentDirId = parentdirDic['dir_id']
                logging.info(f'创建zhu活动目录 {parentdirDic}')
                
            for dir in dirList:
                # logging.info(f'创建子目录 {dir}')
                dirInfo = ActInfo(dir)
                sufDirCode = dirInfo.dir_code
                # logging.info(f'创建子活动目录 {dirInfo}')
                genCode = queryBaseDirCode(drugstoreId)
                sdirCode = f'{genCode}act{actId}{sufDirCode}{sufDirCode}'
                sdir = queryTableLastOne('pm_dir_info','*',f"dir_code = '{sdirCode}'",'dir_id desc')
                remark = ''
                if sdir!=None:
                    remark = sdir['dir_id']
                dic = addPmDirInfo(f'act{actId}{dirInfo.dir_code}',dirInfo.dir_name,drugstoreId,img=dirInfo.dir_img,color=remark,num=dirInfo.dir_num,level='3',parentDirId=parentDirId)
                dicId = dic['dir_id']
                dicCode = dic['dir_code']
                sufdicCode = dir['dir_code']
                logging.info(f'创建子会场目录 {dic}')
                for sku in skuList:
                    skuDicCodeId=sku['dir_code']
                    order = sku['xh']
                    if skuDicCodeId==sufdicCode:
                        skuId=sku['sku_id']
                        addPmSkuDir(skuId,dicId,dicCode,order)
                        
            for item in itemList:
                itemFlag = ''
                if 'is_eq' in dic.keys() and dic['is_xq']!=None and dic['is_xq']==1:
                    itemFlag = 'false'
                            # copyAmStatInfoBySkuId( 78,sku_id)

                itemInfo = ActInfo(item)
                itemName = itemInfo.item_name
                itemDesc = itemInfo.item_desc
                itemType = itemInfo.item_type
                itemCode = itemInfo.item_code



                itemImg = itemInfo.item_img
                itemImgR = itemInfo.item_img_r
                otherImg = f'{{"itemImageR":"{itemImgR}","itemImage":"{itemImg}"}}' if itemImg!='' and itemImgR!='' else ''

                # dirDic = addPmDirInfo(f'act{actId}{itemCode}',itemName,drugstoreId,level='3')
                # idicInfo = ActInfo(dirDic)
                # rangeId =addAmActRange( idicInfo.dir_id,itemName,itemDesc)
                itemId = addAmActItem(itemName,itemDesc,itemType,actId,drugstoreId,img=itemImg,imgR=itemImgR,flag=itemFlag)
                addAmItemRange(itemId,rangeId)
                logging.info(f'创建 活动 item range dir    {itemId}     {itemName}')
                quotaId= ''
                # logging.info(f'itemType-- -{itemType};details_value--{itemInfo.details_value}')
                if itemType=='quota':
                    limit = itemInfo.quota_rule
                    if limit!='':
                        limit_group = itemInfo.quota_group
                        quotaId = addAmQuotaInfo( itemId,limit,itemDesc,limit_group)
                        logging.info(f'创建 限购规则 quota  {itemName}{itemDesc}')
                if itemType=='discount':
                    details_values =itemInfo.details_value
                    rule_values =itemInfo.rule_value
                    logging.info(f'创建 活动规则 details  {itemName}- {itemDesc} -{details_values}- {rule_values}')
                    # logging.info(f'details_value-- -{details_value};rule_value--{rule_value}')
                    if details_values!='':
                        details_remark = itemName
                        details_content =itemDesc
                        details_value_list = details_values.split(',')
                        for details_value in details_value_list:
                        # logging.info(f'detailsId------------------------{itemId,details_value,details_remark,details_content}')
                            details_level = details_value_list.index(details_value)+1
                            detailsId = addAmItemDetails( itemId,details_value,details_remark,details_content,details_type='discount',details_level=details_level)
                            
                            # logging.info(f'detailsId------------------------{detailsId}')
                            if detailsId!='' and rule_values !='':
                                rule_value_list = rule_values.split(',')
                                # for details_value in details_value_list:
                                rule_value = rule_value_list[details_value_list.index(details_value)]
                                addAmDetailsRule(detailsId,rule_value)
                    # quotaId = addAmQuotaInfo( itemId,itemInfo.limit,itemDesc,itemInfo.limit_group)
                    
                # dicId = dirDic['dir_id']
                # dicCode = dirDic['dir_code']
                sufdicCode = item['item_code']
                for sku in skuList:
                    skuDicCodeId=sku['item_code']
                    if skuDicCodeId==sufdicCode:
                        skuId=sku['sku_id']
                        # addPmSkuDir(skuId,dicId,dicCode)
                        # if hasattr(item,'kc_day') and item.get('kc_day')!='':
                        #     skuTotal = item.get('kc_day',0)
                        #     days = item.get('days',0)
                        #     maxTotal = int(days)*int(skuTotal)
                        #     addAmStockLimit(skuId,itemId,quotaId,skuTotal,maxTotal,remark='')
                        #     addAmStockPday(skuId,actId,itemId,quotaId,drugstoreId,skuTotal,maxTotal,remark='')
                        addAmStatInfo(skuId,actId,itemId,itemName,itemDesc,itemType,startTime,endTime,quotaId =quotaId,otherStr1=otherImg,flag=itemFlag)
                    # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)
                        # logging.info(f'创建 addAmStatInfo')
            # db.commit()
            logging.info('创建成功')
            db.commit()
        except Exception as err:
            logging.error(err)
            db.rollback()

            
if __name__ == "__main__":
    logging.info(f'创建秒杀')


    logging.info('开始延期秒杀活动啦--------------------------------------------------')

    # day = '2021-06-28'
    # addDays = 186 # 到 年底
    # for ydId in [200]:
    #     delayMsDateFrom(day,addDays,ydId)
    #     logging.info(f'延期秒杀活动完成， 根据{day}的秒杀数据，在{ydId}店---延期了{addDays}天')

    day = '2021-06-29'
    addDays = 185 # 到 年底
    for ydId in [1600,1601,1603]:
        delayMsDateFrom(day,addDays,ydId)
        logging.info(f'延期秒杀活动完成， 根据{day}的秒杀数据，在{ydId}店---延期了{addDays}天')


    # day = '2021-02-28'
    # addDays = 120 # 到  6月 28 基本和欣臣一致
    # for ydId in [200]:
    #     delayMsDateFrom(day,addDays,ydId)
    #     # copyMsSale(day,addDays,ydId)
    #     # copyMsStat(day,addDays,ydId)
    #     # logging.info('----------------------------------over---------------------------')
    #     # db.commit()
    #     logging.info(f'延期秒杀活动完成， 根据{day}的秒杀数据，在{ydId}店---延期了{addDays}天')

    # day = '2020-12-31'
    # addDays = 180
    # for ydId in [1600,1601,1603]:
    #     delayMsDateFrom(day,addDays,ydId)
    #     logging.info(f'延期秒杀活动完成， 根据{day}的秒杀数据，在{ydId}店---延期了{addDays}天')
    # day2 = '2020-08-09'
    # addDays2 = 143
    # ydId2 = '1601'
    # delayMsDateFrom(day2,addDays2,ydId2)

    # day3 = '2020-08-09'
    # addDays3 = 143
    # ydId3 = '1603'
    # delayMsDateFrom(day3,addDays3,ydId3)
    # db.commit()
 
    # db.commit()
#  秒杀延期
    # logging.info(f'延期秒杀活动完成， 根据{day}的秒杀数据，在{ydId}店---延期了{addDays}天--------------------------------------------------')
 




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

#  秒杀延期
    # day = '2020-08-12'
    # addDays = 141
    # ydId = '1603'
    # delayMsDateFrom(day,addDays,ydId)
    # db.commit()
#  秒杀延期
    # logging.info(f'延期秒杀活动完成， 根据{day}的秒杀数据，在{ydId}店---延期了{addDays}天--------------------------------------------------')

    # copyMsSale(day,addDays,ydId)
    # copyMsStat(day,addDays,ydId)
    # db.commit()