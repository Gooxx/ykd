from db2 import db,cursor,querySQL,updateSQL,insertSQL,selectBy,selectOneBy
import time
import datetime
import logging
from actclass import ActManager
# test
class ActInfo:
    sku_id=''
    act_id=''
    act_start_time=''
    act_end_time=''
    item_id=''
    item_name=''
    item_desc=''
    item_code=''
    item_type=''
    item_attr=''
    item_remark =''
    item_img =''
    item_num=''
    item_priority=''

    range_id =''
    details_id=''
    details_type=''
    details_val_type=''
    details_value=''
    details_remark=''
    details_content=''
    rule_id =''
    rule_value=''

    quota_id =''
    quota_remark=''
    quota_content=''
    quota_id=''
    quota_rule=''
    qutoa_group=''
    kc_day=''
    days=''
    limit=''
    limit_group=''

    dir_id=''
    dir_code=''
    dir_name=''
    dir_num=''
    dir_img=''
    pharmacy_id=''

    def __init__(self, dic={}):
        # print('初始化')
        self.fromDic(dic)

    def fromDic(self, dic={}):
        # print(dic)
        keys = dic.keys()
        for key in keys:
            # print(key)
            # print(dic[key])
            if hasattr(self,key):
                value = dic[key]
                setattr(self,key,value)

    # def createActInfo(self, actId,actName,startTime,endTime,pharmacyId):
    #     '''创建am_act_info'''
    #     sql = f"""INSERT INTO `medstore`.`am_act_info` (`act_id`, `act_name`, `act_type`, `act_status`, `act_content`
    #             , `act_update_time`, `act_create_time`, `act_start_time`, `act_end_time`, `act_level`, `act_remark`
    #             , `act_img`, `act_url`, `pharmacy_id`)
    #             VALUES ('{actId}', '{actName}', 'date', '1', '活动', now(), now(), '{startTime}', '{endTime}', '1', '', '', '', '{pharmacyId}');"""
    #     res = insertSQL(sql)
    #     id = res['lastId']
    #     # logging.debug(f'完成创建am_act_info1----id:{id}')
    #     # logging.info(f'完成创建am_act_info2----id:{id}')

    #     try:
    #         # cursor.execute(sql2)
    #         # # db.commit()

    #         # print(cursor.lastrowid)
    #         # cursor.execute(sql)
            
    #         # res = insertSQL(sql2)
    #         # res2 = insertSQL(sql3)
    #         res3 = insertSQL(sql)
    #         id = res['lastId']
    #         id2 = res2['lastId']
    #         id3 = res3['lastId']
    #         logging.info(f'完成创建am_act_info2----id:{id}')
    #         logging.info(f'完成创建am_act_info3----id:{id2}')
    #         logging.info(f'完成创建am_act_info4----id:{id3}')
    #         db.commit()
    #         id = res['lastId']
    #         logging.info(f'完成创建am_act_info2----id:{id}')

    #     # except Exception:
    #     except Exception as err:
    #         logging.error("Error %s for execute sql: %s" % (err, sql))
    #         logging.debug('语句失败！！！')
    #         db.rollback()
    #         return {
    #             'code':404,
    #             'count':0,
    #             'lastId':0,
    #             'data':[]
    #         }
    #     return id
    def test(self, actId,actName,startTime,endTime,pharmacyId):
        '''创建am_act_info'''
        sql = f"""INSERT INTO `medstore`.`am_act_info` (`act_id`, `act_name`, `act_type`, `act_status`, `act_content`
                , `act_update_time`, `act_create_time`, `act_start_time`, `act_end_time`, `act_level`, `act_remark`
                , `act_img`, `act_url`, `pharmacy_id`)
                VALUES ('{actId}', '{actName}', 'date', '1', '活动', now(), now(), '{startTime}', '{endTime}', '1', '', '', '', '{pharmacyId}');"""
        # print(sql)
        # res = insertSQL(sql)
        # id = res['lastId']
        # logging.debug(f'完成创建am_act_info1----id:{id}')
        # logging.info(f'完成创建am_act_info2----id:{id}')

        try:
            # cursor.execute(sql2)
            # # db.commit()

            # print(cursor.lastrowid)
            # cursor.execute(sql)
            
            # res = insertSQL(sql2)
            # res2 = insertSQL(sql3)
            res3 = insertSQL(sql)
            id = res['lastId']
            id2 = res2['lastId']
            id3 = res3['lastId']
            logging.info(f'完成创建am_act_info2----id:{id}')
            logging.info(f'完成创建am_act_info3----id:{id2}')
            logging.info(f'完成创建am_act_info4----id:{id3}')
            db.commit()
            id = res['lastId']
            logging.info(f'完成创建am_act_info2----id:{id}')

        # except Exception:
        except Exception as err:
            logging.error("Error %s for execute sql: %s" % (err, sql))
            logging.debug('语句失败！！！')
            db.rollback()
            return {
                'code':404,
                'count':0,
                'lastId':0,
                'data':[]
            }
        return id

# class ActManager:

#     def __init__(self,list=[]):
#         actlist = []
#         for dic in list:
#             actlist.add(ActInfo(dic))
#         return actlist
 
 
# act = ActManger()
# act.createActInfo('227','无接触配送','2020-03-10','2020-12-31',200)





def test1():
    print('aaatest')




## ---------------------
# 根据货号查skuid
def querySkuId(huohao,drugstoreId):
    sql = '''
        SELECT sku_id FROM `pm_prod_sku` 
        WHERE `pharmacy_huohao`  = '{0}' 
        and `drugstore_id` ={1};
    '''.format(huohao,drugstoreId)
    dic = selectOneBy(sql)
    return dic.get('sku_id')

def queryTable(tableName,result='*',where =''):
    '''基础查询表内容
    返回数组结构 []'''
    if where !='':
        where  = ' where '+where
    sql = '''select {} from {} {} '''.format(result,tableName,where)
    res =querySQL(sql)
    if res['code']==200:
        return res['data']
    else:
        return []

def queryTableLastOne(tableName,field='*',where =''):
    '''基础查询表内容
    返回数组结构 []'''
    if where !='':
        where  = ' where '+where
    sql = f'''select {field} from {tableName} {where}  order by {field} desc limit 1'''
    res =selectOneBy(sql)
    return res[field]

def querySkuIdByTable(  tableName,drugstoreId,where='1=1'):
    '''基础查询表内容'''
    sql = f''' select * 
            from {tableName} a,pm_prod_sku s
            WHERE    a.huohao = s.pharmacy_huohao
            and s.drugstore_id = {drugstoreId}  
            and {where}
    '''
    res =querySQL(sql)
    if res['code']==200:
        return res['data']
    else:
        return []
def queryBaseDirCode(drugstoreId):
    '''查询药店的基础dircode， 相应药店下的子级目录需要 以此code开头
    '''
    # for drugstoreId in self.drugstoreIdList:
    sql = '''
            SELECT * from pm_dir_info WHERE 
            dir_name = '功能主目录' 
            and pharmacy_id ={};
        '''.format(drugstoreId)
    dic = selectOneBy(sql)
    return dic.get('dir_code')

def selectActInfo(itemId):
    """根据itemid查询活动信息"""
    sql = f"""SELECT a.act_start_time, a.act_end_time,a.act_id,
             b.item_id,b.item_name,b.item_desc,b.item_type,b.item_attr ,b.item_remark,b.item_img,b.item_num,b.item_priority
            ,dd.dir_id,dd.dir_code,dd.dir_name,dd.pharmacy_id
            ,e.details_id,e.details_type,e.details_val_type,e.details_value,e.details_remark,e.details_content
            ,g.rule_id,g.rule_value
            ,h.quota_remark,h.quota_content,h.quota_id,h.quota_rule,h.qutoa_group
            from  am_act_item b 
            LEFT JOIN am_item_range c on b.item_id = c.item_id 
            LEFT JOIN am_act_range d on c.range_id = d.range_id 
            LEFT JOIN pm_dir_info dd on d.range_value = dd.dir_id
            LEFT JOIN am_item_details e on b.item_id = e.item_id 
            LEFT JOIN am_details_rule f on e.details_id = f.details_id
            LEFT JOIN am_act_rule g on f.rule_id = g.rule_id
            LEFT JOIN am_quota_info h on b.item_id = h.item_id
            LEFT JOIN am_act_info a on a.act_id = b.act_id
            WHERE b.item_id = {itemId}"""
    list = selectOneBy(sql)
    return list

def selectMsActInfo(itemId):
    """根据itemid查询活动信息"""
    sql = f"""SELECT a.act_start_time, a.act_end_time,a.act_id,
             b.item_id,b.item_name,b.item_desc,b.item_type,b.item_attr ,b.item_remark,b.item_img,b.item_num,b.item_priority
            ,dd.dir_id,dd.dir_code,dd.dir_name,dd.pharmacy_id
            ,e.details_id,e.details_type,e.details_val_type,e.details_value,e.details_remark,e.details_content
            ,g.rule_id,g.rule_value
            ,h.quota_remark,h.quota_content,h.quota_id,h.quota_rule,h.qutoa_group
            from  am_act_item b 
            LEFT JOIN am_item_range c on b.item_id = c.item_id 
            LEFT JOIN am_act_range d on c.range_id = d.range_id 
            LEFT JOIN pm_dir_info dd on d.range_value = dd.dir_id
            LEFT JOIN am_item_details e on b.item_id = e.item_id 
            LEFT JOIN am_details_rule f on e.details_id = f.details_id
            LEFT JOIN am_act_rule g on f.rule_id = g.rule_id
            LEFT JOIN am_quota_info h on b.item_id = h.item_id
            LEFT JOIN am_act_info a on a.act_id = b.act_id
            WHERE b.item_id = {itemId}"""
    list = selectOneBy(sql)
    return list

def addPmDirInfo(sufDirCode,dirName,drugstoreId,img='',color='',num='1',level='1',parentDirId=''):
    logging.debug('根据提供的盘货信息，创建展示目录 dir ')
    genCode = queryBaseDirCode(drugstoreId)
    dirCode = genCode+sufDirCode
    sql = f'''
        INSERT INTO `medstore`.`pm_dir_info` (  `dir_code`, `dir_name`, `dir_type`, `dir_status`
        , `dir_revalue`, `prod_sum`, `dir_num`, `dir_level`, `dir_img`, `parent_dir_id`, `dir_update_time`
        , `dir_create_time`, `dir_remark`, `dir_all_name`, `category_id`, `pharmacy_id`, `dir_gotocata`, `dir_main_show`)
        value ('{dirCode}','{dirName}','dir','1',NULL,100,'{num}',{level},'{img}','{parentDirId}',NOW(),NOW(),'{color}','',NULL,'{drugstoreId}',NULL,NULL) ;
    '''
    res = insertSQL(sql)
    if res["code"]==200:
        return {
            'dir_id':res['lastId'],
            'dir_code':dirCode,
            'dir_name':dirName,
            'dir_level':level,
            'pharmacy_id':drugstoreId
        } 
    return None

def addPmProdSku(prodId,prodName,huohao,skuPrice,skuFee,drugstoreId,spec,skuStatus='0',skuActivate='0',skuRemark='',skuType='normal',sku_sum_flag='0'):
    """创建商品sku 普通商品（如需创建组合商品需扩展后面的字段）"""
    sql = f"""
        INSERT INTO `medstore`.`pm_prod_sku` (  `prod_id`, `sku_status`, `sku_price`, `sku_fee`
        , `drugstore_id`, `brand_id`, `sku_update_time`, `sku_create_time`, `sku_remark`, `sku_logistics`
        , `prod_name`, `pharmacy_huohao`, `source_id`, `sku_json`, `sku_attr`, `sku_img`, `sku_sum`
        , `sku_activate`, `sales_info`, `sku_sum_flag`, `sku_hot_order`, `sku_sort`, `sku_rank`, `sku_type`
       ) 
        VALUES ( '{prodId}', '{skuStatus}', '{skuPrice}', '{skuFee}', '{drugstoreId}', '1', NOW(),NOW()
        , '{skuRemark}', '', '{prodName}', '{huohao}', '1', '{{"prod_spec":"{spec}"}}', NULL, NULL, '0'
        , '{skuActivate}', NULL, '{sku_sum_flag}', '0', '0', NULL, '{skuType}');
        """
    res = insertSQL(sql)
    return res['lastId']

def addNewSku4JHSMS(tableName,preHuohao,drugstoreId):
    '''创建聚划算和秒杀的商品sku，根据base——huohao来确认商品，然后复制一个富裕新huohao
    '''
    sql = '''
        UPDATE {} set huohao = CONCAT('{}',base_huohao);
        '''.format(tableName,preHuohao)
    res = insertSQL(sql)
    if res['code']==200:
        sql1 = '''
                INSERT INTO `medstore`.`pm_prod_sku` (  `prod_id`, `sku_status`, `sku_price`, `sku_fee`, `drugstore_id`, `brand_id`, `sku_update_time`, `sku_create_time`, `sku_remark`, `sku_logistics`, `prod_name`, `pharmacy_huohao`, `source_id`, `sku_json`, `sku_attr`, `sku_img`, `sku_sum`, `sku_activate`, `sales_info`, `sku_sum_flag`, `sku_hot_order`, `sku_sort`, `sku_rank`, `sku_type`, `is_set`, `set_num`, `dis_before_price`, `dis_after_price`, `discount_price`, `pre_prod_name`)
                SELECT  s.`prod_id`, `sku_status`, `sku_price`, `sku_fee`, `drugstore_id`, `brand_id`,NOW() `sku_update_time`,NOW() `sku_create_time`, `sku_remark`, `sku_logistics`, `prod_name`
                ,a.huohao `pharmacy_huohao`, `source_id`, `sku_json`, `sku_attr`, `sku_img`, `sku_sum`, `sku_activate`, `sales_info`, `sku_sum_flag`, `sku_hot_order`, `sku_sort`, `sku_rank`, `sku_type`, `is_set`, `set_num`, `dis_before_price`, `dis_after_price`, `discount_price`, `pre_prod_name` 
                from {} a,pm_prod_sku s
                WHERE a.base_huohao = s.pharmacy_huohao
                and s.drugstore_id = {};
            '''.format(tableName,drugstoreId)
        res = insertSQL(sql1)
def addPmActSale(tableName,drugstoreId,startTime,endTime):
    '''创建活动价格 fee price
    '''
    # for drugstoreId in self.drugstoreIdList:
    sql1 = '''
            INSERT INTO `medstore`.`pm_sku_sale` ( `sku_id`, `sale_fee`, `sale_price`, `sale_start_time`, `sale_end_time`, `sale_status`, `sale_create_time`, `sale_update_time`, `sale_remark`) 
            SELECT s.`sku_id`,a.fee*100 `sale_fee`,a.price*100 `sale_price`
            ,'{}' `sale_start_time`,'{}' `sale_end_time`
            ,0 `sale_status`,NOW() `sale_create_time`,NOW() `sale_update_time`,'' `sale_remark` 
            from {} a,pm_prod_sku s
            WHERE a.huohao = s.pharmacy_huohao
            and s.drugstore_id = {}
        '''.format(startTime,endTime,tableName,drugstoreId)
    res = insertSQL(sql1)
    return res['code']
def addAmStatInfo(skuId,actId,itemId,itemName,itemDesc,itemType,startTime,endTime,quotaId='',itemPriority='100',itemAttr='multi',otherStr1=''):
    configSql = '''SELECT config_value from sm_config WHERE config_key = 'act_batch';'''
    configDic = selectOneBy(configSql)
    configValue =configDic.get('config_value')
    sql = f"""INSERT INTO am_stat_info (  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark` , `item_name`
    , `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`
        , `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`) 
        VALUES ( '{configValue}', '{skuId}', '{actId}', '{itemId}', '{itemDesc}', '{itemName}'
        , '{itemAttr}', now(), now(), '{startTime}', '{endTime}'
        , '{itemType}', '{otherStr1}', '{quotaId}', NULL, '{itemPriority}');
        """
    res = insertSQL(sql)
    return res['lastId']

def addPmSkuDir(skuId,dirId,dirCode,order='1'):
    sql = f"""INSERT INTO `medstore`.`pm_sku_dir` (  `dir_id`, `sku_id`, `dir_code`, `sku_order`, `update_time`) 
            VALUES ( '{dirId}', '{skuId}', '{dirCode}', '{order}', now());"""
    res = insertSQL(sql)
    return res['lastId']

def addAmActInfo(actId,actName,startTime,endTime,drugstoreId='200'):
    logging.info('创建活动主体，包括活动名，开始结束时间')

    list = queryTable('am_act_info',result='*',where =f'  act_id="{actId}"')
    if len(list)>0:
        return ''
    sql = f'''
        INSERT INTO `medstore`.`am_act_info` (`act_id`, `act_name`, `act_type`, `act_status`, `act_content`
        , `act_update_time`, `act_create_time`, `act_start_time`, `act_end_time`, `act_level`, `act_remark`
        , `act_img`, `act_url`, `pharmacy_id`)
        VALUES ('{actId}', '{actName}', 'date', '1', '活动', now(), now(), '{startTime}', '{endTime}', '1', '', '', '', '{drugstoreId}');
    '''
    res =insertSQL(sql)
    if res['code']==200:
        # res = insertSQL(sql)
        logging.info('创建活动成功')
        return res['lastId']
        
def addAmActRange( dirId,dirName,dirRemark=''):
        '''创建 range item   通过目录id来创建
        '''
        sql = F'''
            INSERT INTO `medstore`.`am_act_range` (  `range_type`, `range_value`, `range_status`
            , `range_name`, `range_remark`, `range_update_time`, `range_create_time`)
            values('category', {dirId}, '1', '{dirName}', '{dirRemark}', NOW(), NOW()) 
        '''
        res = insertSQL(sql)
        return res['lastId']
def addAmActItem(itemName,itemDesc,itemType,actId,drugstoreId,img='',flag=''):
        '''创建 range item   通过目录id来创建
        '''
        # itemName = dic['item_name']
        # itemDesc = dic['item_desc']
        # itemType = dic['item_type']
        sql = f'''
            INSERT INTO `medstore`.`am_act_item` ( `item_attr`, `item_name`, `act_id`
            , `item_status`, `item_priority`, `item_type`, `item_desc`, `item_update_time`
            , `item_create_time`, `item_remark`, `item_img`, `pharmacy_id`, `item_flag`
            , `sales_goto_type`, `sales_goto_title`, `sales_goto_url`, `item_num`, `item_title`
            , `activity_img`, `activity_img_ratio`)
            VALUES ('single', '{itemName}', '{actId}', '1', '90', '{itemType}','{itemDesc}', NOW(), NOW()
            ,'', '{img}', '{drugstoreId}', '{flag}', '', '', '', '0', '', '', '')
            ;
        '''
        res = insertSQL(sql)
        return res['lastId']
def addAmItemRange(itemId,rangeId):
        '''创建 range item  的关连
        '''
        sql = '''
            INSERT INTO `medstore`.`am_item_range` ( `range_id`, `item_id`) VALUES ( '{}', '{}');
        '''.format(rangeId,itemId)
        res = insertSQL(sql)
        return res['code']
def addAmQuotaInfo( itemId,limit,desc,group='0'):
        '''创建 range item   通过目录id来创建
        '''
        sql = f'''
            INSERT INTO `medstore`.`am_quota_info` ( `item_id`, `quota_rule`, `quota_kind`
            , `quota_type`, `quota_status`, `quota_total`, `quota_update_time`, `quota_create_time`
            , `quota_remark`, `quota_content`, `qutoa_group`) 
            VALUES ( '{itemId}', '{limit}', 'main', 'force', '1', '0', now(), now(), '{desc}', '活动商品{desc}', '{group}');
        '''
        res = insertSQL(sql)
        return res['lastId']
def addAmStockLimit(skuId,itemId,quotaId,skuTotal,maxTotal,remark=''):
    """添加到活动中去"""
    sql = f"""INSERT INTO `medstore`.`am_stock_limit` (  `item_id`, `quota_id`, `sku_id`, `sku_total`, `as_remark`, `max_total`)
            VALUES (  '{itemId}', '{quotaId}', '{skuId}', '{skuTotal}', '{remark}', '{maxTotal}');"""
    res = insertSQL(sql)
    return res['lastId']

def addAmStockPday(skuId,actId,itemId,quotaId,drugstoreId,skuTotal,maxTotal,remark=''):
        sql = f'''
            INSERT INTO `medstore`.`am_stock_pday` ( `act_id`, `item_id`, `quota_id`,  `sku_id`,  `pharmacy_id`, `sku_num`,  `sku_total`,  `remark`)
            VALUES (  '{actId}','{itemId}', '{quotaId}', '{skuId}','{drugstoreId}', '{skuTotal}', '{maxTotal}', '{remark}');
        '''
        res = insertSQL(sql)
        return res['lastId']

def createComb(baseSkuId,combProdId,fee,price,count=1):
    """根据单件的skuid和多盒的prodid创建 ，多盒的sku"""
    prodsql = f"select * from pm_prod_info where prod_id = {combProdId}"
    prodres = selectOneBy(prodsql)
    logging.info(prodres)

    prename = f'{count}件装' # prodres.get('pre_prod_name')
    # prename = prodres.get('pre_prod_name')
    prodname = prodres.get('prod_name')
    spec = prodres.get('prod_spec')
    specjson = f'{{"prod_spec":"{spec}"}}'
    sql = f"""
        INSERT INTO `medstore`.`pm_prod_sku` (  `prod_id`, `sku_status`, `sku_price`, `sku_fee`
        , `drugstore_id`, `brand_id`, `sku_update_time`, `sku_create_time`, `sku_remark`, `sku_logistics`
        , `prod_name`, `pharmacy_huohao`, `source_id`, `sku_json`, `sku_attr`, `sku_img`, `sku_sum`
        , `sku_activate`, `sales_info`, `sku_sum_flag`, `sku_hot_order`, `sku_sort`, `sku_rank`, `sku_type`
        , `is_set`, `set_num`, `dis_before_price`, `dis_after_price`, `discount_price`, `pre_prod_name`) 
        select '{combProdId}', `sku_status`, {price}, {fee}
        , `drugstore_id`, `brand_id`, now(), now(), `sku_remark`, `sku_logistics`
        , concat('{prename}',prod_name) ,concat('{prename}',pharmacy_huohao) , `source_id`
        ,'{specjson}', `sku_attr`, `sku_img`, `sku_sum`
        , `sku_activate`, `sales_info`, `sku_sum_flag`, `sku_hot_order`, `sku_sort`, `sku_rank`, 'comb'
        ,1 `is_set`,{count} `set_num`
        ,sku_price `dis_before_price`,{price/count} `dis_after_price`,sku_price-{price/count} `discount_price`,'{prename}' `pre_prod_name`
        from pm_prod_sku
        where sku_id = {baseSkuId} ;
        """
    # logging.info(sql)
    try:
        res = insertSQL(sql)
        combSkuId= res['lastId']
        skusql = f"select * from pm_prod_sku where sku_id = {combSkuId}"
        skures = selectOneBy(skusql)
        logging.info(skures)
        
        name = skures['prod_name']
        huohao = skures['pharmacy_huohao']
        drugstoreId = skures['drugstore_id']
        fee = skures['sku_fee']
        price = skures['sku_price']
        beforeprice = skures['dis_before_price']
        disprice = skures['dis_after_price']
        packetId= addPmPacketInfo(combSkuId, name,prename,huohao,drugstoreId,fee,price)
        
        addPmPacketSku(packetId,baseSkuId,combSkuId, prodname,huohao,drugstoreId,disprice,beforeprice,count,price)
        db.commit()
    except:
        db.rollback()
    

def addPmPacketInfo(skuId, name,prename,huohao,drugstoreId,fee,price):
    """根据多盒sku创建多盒装packet"""
    sql = f"""INSERT INTO `medstore`.`pm_packet_info` ( `packet_huohao`, `packet_name`, `packet_status`, `packet_type`
            , `packet_price`, `packet_fee`, `packet_category`, `packet_content`, `packet_stock`, `packet_img`, `drugstore_id`
            , `packet_update_time`, `packet_create_time`, `packet_remark`, `sku_id`, `pre_prod_name`, `packet_coures`, `packet_title_formula`) 
            VALUES ( '{huohao}', '{name}', '1', 'normal', '{price}', '{fee}', '1001000296', '{huohao}', '1', NULL
            , '{drugstoreId}', now(), now(), '', '{skuId}', '{prename}', 'single'
            , '{name}');
            """
    res = insertSQL(sql)
    return res['lastId']

def addPmPacketSku(packetId,skuId,combSkuId, name,packethuohao,drugstoreId,disprice,price,count,combPrice):
    """关联多盒Packetsku 和单盒sku"""
    sql = f"""INSERT INTO `medstore`.`pm_packet_sku` ( `packet_id`, `sku_id`, `prod_name`, `sku_huohao`
    , `packet_sku_id`, `packet_sku_price`, `sku_fee`, `sku_seq`, `sku_amount`, `total_price`, `link_remark`)
     VALUES (  '{packetId}', '{skuId}', '{name}', '{packethuohao}', '{combSkuId}', '{disprice}', '{price}', '1', '{count}', '{combPrice}'
     , '');
            """
    res = insertSQL(sql)
    return res['lastId']
# 创建列表页的药品名左侧的标志，当日送达
def addAmskuImage(huohao,drugstoreId,img='http://image.ykd365.cn/icon/home/drsd.png',radio='342',title='当日送达',startTime='2020-03-01',endTime='2028-03-01'):
    """创建列表页的药品名左侧的标志，当日送达"""
    # logging.info('创建列表页的药品名左侧的标志，当日送达')
    sql = '''
        INSERT INTO am_sku_img (  `sku_id`, `act_type`, `act_start_time`, `act_end_time`, `act_status`, `create_time`, `update_time`, `act_img_url`, `aspect_ratio`, `remark`)
        SELECT s.sku_id,'logo','{}', '{}', '1', NOW(), NOW(), '{}', '{}', '{}'
        from  pm_prod_sku s
        WHERE pharmacy_huohao  = '{}'  and  s.drugstore_id = {};
    '''.format(startTime,endTime,img,radio,title,huohao,drugstoreId)
    res = insertSQL(sql)
    return res['lastId']

def addAmStatInfoByDrugstoreId(drugstoreId):
    """给整个药店下的所有item活动. 添加到amstatinfo""" 
    configSql = '''SELECT config_value from sm_config WHERE config_key = 'act_batch';'''
    configDic = selectOneBy(configSql)
    configValue =configDic.get('config_value')

    items =  queryTable(' am_act_item ',result='*',where =f' pharmacy_id = {drugstoreId}')
    for item in items:
        itemId = item['item_id']
        dic = selectActInfo(itemId)
        # logging.info('活动信息 %s',dic)
        logging.info('活动信息 %s  %s  %s  %s ',dic['item_id'],dic['item_name'],dic['item_desc'],dic['dir_id'])
        # skuId,actId,itemId,itemName,itemDesc,itemTyoe,startTime,endTime
        # skuId = querySkuId(huohao,drugstoreId)
        # logging.info('skuId %s',skuId)
        actId = dic.get('act_id')
        
        itemName = dic.get('item_name')
        itemDesc = dic.get('item_desc')
        itemType = dic.get('item_type')
        startTime = dic.get('act_start_time')
        endTime = dic.get('act_end_time')
        quotaId = dic.get('quota_id') if dic.get('quota_id')!=None else 'NULL'
        logging.error('quotaId-------%s---%s--',dic.get('quota_id'),dic.get('quota_id') if dic.get('quota_id')!=None else '')
        dirId = dic.get('dir_id')
        dirCode = dic.get('dir_code')

        itemAttr = dic.get('item_attr')
        otherStr1 = dic.get('other_str1','')
        itemPriority = dic.get('item_priority')
        # res = addAmStatInfo(skuId,actId,itemId,itemName,itemDesc,itemType,startTime,endTime,quotaId =quotaId)
        dirId=None # 为了只配置秒杀,所以目录id弄成空
        if dirId!=None:
            sql = f"""INSERT INTO am_stat_info (  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark` , `item_name`
            , `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`
                , `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`) 
                select '{configValue}',sku_id, '{actId}', '{itemId}', '{itemDesc}', '{itemName}'
                , '{itemAttr}', now(), now(), '{startTime}', '{endTime}'
                , '{itemType}', '{otherStr1}', {quotaId}, NULL, '{itemPriority}'
                from pm_sku_dir 
                where dir_id = {dirId};
                """
            res = insertSQL(sql)
        else:
            sgSql = f"""SELECT ssd.dir_id ,ss.pharmacy_id,ss.sg_id,ss.sg_title,ss.sg_start_time,ss.sg_end_time from am_stages_sale_detail ssd,am_stages_sale ss 
                        WHERE 
                        ssd.sg_id = ss.sg_id 
                        and ssd.item_id = {itemId}
                        and ss.sg_start_time>= NOW()
                        and ss.pharmacy_id = {drugstoreId}"""
            sgList = selectBy(sgSql)
            for sg in sgList:
                dirId = sg['dir_id']
                startTime = sg['sg_start_time']
                endTime = sg['sg_end_time']
                sql = f"""INSERT INTO am_stat_info (  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark` , `item_name`
                , `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`
                    , `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`) 
                    select '{configValue}',sku_id, '{actId}', '{itemId}', '{itemDesc}', '{itemName}'
                    , '{itemAttr}', now(), now(), '{startTime}', '{endTime}'
                    , '{itemType}', '{otherStr1}', {quotaId}, NULL, '{itemPriority}'
                    from pm_sku_dir 
                    where dir_id = {dirId};
                    """
                res = insertSQL(sql)


def addAmStatInfoByItemId(itemId,drugstoreId):
    """给整个药店下的所有item活动. 添加到amstatinfo""" 
    configSql = '''SELECT config_value from sm_config WHERE config_key = 'act_batch';'''
    configDic = selectOneBy(configSql)
    configValue =configDic.get('config_value')

    # items =  queryTable(' am_act_item ',result='*',where =f' pharmacy_id = {drugstoreId}')
    # for item in items:
    # itemId = item['item_id']
    dic = selectActInfo(itemId)
    # logging.info('活动信息 %s',dic)
    logging.info('活动信息 %s  %s  %s  %s ',dic['item_id'],dic['item_name'],dic['item_desc'],dic['dir_id'])
    # skuId,actId,itemId,itemName,itemDesc,itemTyoe,startTime,endTime
    # skuId = querySkuId(huohao,drugstoreId)
    # logging.info('skuId %s',skuId)
    actId = dic.get('act_id')
    
    itemName = dic.get('item_name')
    itemDesc = dic.get('item_desc')
    itemType = dic.get('item_type')
    startTime = dic.get('act_start_time')
    endTime = dic.get('act_end_time')
    quotaId = dic.get('quota_id') if dic.get('quota_id')!=None else 'NULL'
    logging.error('quotaId-------%s---%s--',dic.get('quota_id'),dic.get('quota_id') if dic.get('quota_id')!=None else '')
    dirId = dic.get('dir_id')
    dirCode = dic.get('dir_code')

    itemAttr = dic.get('item_attr')
    otherStr1 = dic.get('other_str1','')
    itemPriority = dic.get('item_priority')
    # res = addAmStatInfo(skuId,actId,itemId,itemName,itemDesc,itemType,startTime,endTime,quotaId =quotaId)
    dirId=None # 为了只配置秒杀,所以目录id弄成空
    if dirId!=None:
        sql = f"""INSERT INTO am_stat_info (  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark` , `item_name`
        , `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`
            , `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`) 
            select '{configValue}',sku_id, '{actId}', '{itemId}', '{itemDesc}', '{itemName}'
            , '{itemAttr}', now(), now(), '{startTime}', '{endTime}'
            , '{itemType}', '{otherStr1}', {quotaId}, NULL, '{itemPriority}'
            from pm_sku_dir 
            where dir_id = {dirId};
            """
        res = insertSQL(sql)
    else:
        sgSql = f"""SELECT ssd.dir_id ,ss.pharmacy_id,ss.sg_id,ss.sg_title,ss.sg_start_time,ss.sg_end_time from am_stages_sale_detail ssd,am_stages_sale ss 
                    WHERE 
                    ssd.sg_id = ss.sg_id 
                    and ssd.item_id = {itemId}
                    and ss.sg_start_time>= NOW()
                    and ss.pharmacy_id = {drugstoreId}"""
        sgList = selectBy(sgSql)
        for sg in sgList:
            dirId = sg['dir_id']
            startTime = sg['sg_start_time']
            endTime = sg['sg_end_time']
            sql = f"""INSERT INTO am_stat_info (  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark` , `item_name`
            , `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`
                , `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`) 
                select '{configValue}',sku_id, '{actId}', '{itemId}', '{itemDesc}', '{itemName}'
                , '{itemAttr}', now(), now(), '{startTime}', '{endTime}'
                , '{itemType}', '{otherStr1}', {quotaId}, NULL, '{itemPriority}'
                from pm_sku_dir 
                where dir_id = {dirId};
                """
            res = insertSQL(sql)



# 根据查询到的活动信息，复制amstatinfo数据，修改skuid即可
def copyAmStatInfoBySkuId( item_id,sku_id):
    '''根据查询到的活动信息，复制amstatinfo数据，修改skuid即可'''
    statSql = '''
        INSERT INTO am_stat_info (  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark`, `item_name`, `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`, `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`)
        SELECT `batch_num`,'{}' `sku_id`, `act_id`, `item_id`, `item_remark`, `item_name`, `item_attr`,NOW() `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`, `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`
        from am_stat_info
        WHERE `item_id` = {}
        limit 1;
        '''.format(sku_id,item_id)
    res = insertSQL(statSql)
    # return res['lastId']
def copyAmStatInfoByHuohao( itemId,huohao,drugstoreId):
    '''根据查询到的活动信息，复制amstatinfo数据，修改skuid即可'''
    sql = '''
        SELECT * FROM `pm_prod_sku` 
        WHERE `pharmacy_huohao`  = '{0}' 
        and `drugstore_id` ={1};
    '''.format(huohao,drugstoreId)
    res = querySQL(sql)
    if res['code']==200 and res['count']>0:
        sku = res['data'][0]
        skuId = sku['sku_id']
        copyAmStatInfoBySkuId(itemId,skuId)

def createCombByHuohao(huohao,drugstoreId,combProdId,fee,price,count=1):
    skusql = f"select * from pm_prod_sku where pharmacy_huohao = {huohao} and drugstore_id= {drugstoreId}"
    skures = selectOneBy(skusql)
    logging.info(skures)
    baseSkuId = skures['sku_id']
    createComb(baseSkuId,combProdId,fee,price,count=5)

# def changeDic2ActInfo(parameter_list):
#     pass



def buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime,endTime,img='',color=''):
    """ 创建基础表的时候，如果有会场，保证有dir_code,dir_name,pharmacy_id 可选 dir_img,dir_num
        如果有活动 保证有 item_code(在dirinfo中使用),item_name,item_desc,item_type()
        **** 都有code为准，名称重复率太高
        1：item_type = quota 需要有limit （格式为 1:1:1） 可选limit group， 如果有库存 需要有 kc_day , （此处需扩展为 每日库存，总库存，天数）
        2：item_type = discount 需要有 子级手动配置detail（因为活动中类比较多） 
        3：item_type = drugtag ,由于文字不会显示在list和detail，一般是配置dir_img用的
        3：item_type = cut  满减
        5：item_type = nothing  列表页显示，详情页不显示
        buy	购买婴幼儿奶粉加9元换购特殊商品，满1000元加19元换购其他商品
        gift	购买热销商品满100元送体温计，满200元送电子体温计 
        excoupon	不可使用优惠券
    
    'dir','actskudir','skudir','item','range','itemrange','quota','stock','stock-pday','ms-sale','ms-packet'"""
    try:
        addAmActInfo(actId,actName,startTime,endTime,drugstoreId='200')
        skuList = querySkuIdByTable(tableName,drugstoreId)
        dirList = queryTable(tableName,where=' dir_code !="" group by dir_code')
        itemList = queryTable(tableName,where='  item_code !="" group by item_code')
        if len(dirList)>0 or len(itemList)>0:
            logging.info('开始创建活动目录')
            # logging.error('开始创建活动目录error')
            parentdirDic = addPmDirInfo(f'act{actId}',actName,drugstoreId,img=img,color=color,num='1',level='2',parentDirId='')
            parentDirId = parentdirDic['dir_id']
            logging.info(f'创建zhu活动目录 {parentdirDic}')
        for dir in dirList:
            # logging.info(f'创建子目录 {dir}')
            dirInfo = ActInfo(dir)
            # logging.info(f'创建子活动目录 {dirInfo}')
            dic = addPmDirInfo(f'act{actId}{dirInfo.dir_code}',dirInfo.dir_name,drugstoreId,img=dirInfo.dir_img,num=dirInfo.dir_num,level='3',parentDirId=parentDirId)
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
            logging.info(f'创建子活动目录 {item}')
            itemInfo = ActInfo(item)
            itemName = itemInfo.item_name
            itemDesc = itemInfo.item_desc
            itemType = itemInfo.item_type
            itemCode = itemInfo.item_code

            dirDic = addPmDirInfo(f'act{actId}{itemCode}',itemName,drugstoreId,level='3')
            idicInfo = ActInfo(dirDic)
            rangeId =addAmActRange( idicInfo.dir_id,itemName,itemDesc)
            itemId = addAmActItem(itemName,itemDesc,itemType,actId,drugstoreId,img='')
            addAmItemRange(itemId,rangeId)

            quotaId= ''
            if itemInfo.item_type=='quota':
                quotaId = addAmQuotaInfo( itemId,itemInfo.limit,itemDesc,itemInfo.limit_group)
                
            dicId = dirDic['dir_id']
            dicCode = dirDic['dir_code']
            sufdicCode = item['item_code']
            for sku in skuList:
                skuDicCodeId=sku['item_code']
                if skuDicCodeId==sufdicCode:
                    skuId=sku['sku_id']
                    addPmSkuDir(skuId,dicId,dicCode)
                    if hasattr(item,'kc_day'):
                        skuTotal = item.get('kc_day',0)
                        days = item.get('days',0)
                        maxTotal = int(days)*int(skuTotal)
                        addAmStockLimit(skuId,itemId,quotaId,skuTotal,maxTotal,remark='')
                        addAmStockPday(skuId,actId,itemId,quotaId,drugstoreId,skuTotal,maxTotal,remark='')
                    addAmStatInfo(skuId,actId,itemId,itemName,itemDesc,itemType,startTime,endTime,quotaId =quotaId)
        db.commit()
        logging.info('创建成功')
    except Exception as err:
        logging.error(err)
        db.rollback()
    
def addSkuDirByItemId(huohao,drugstoreId,itemId,skuTotal=0,maxTotal=0):
    """根据itemid增加到对应dir中 添加到amstatinfo中，如果库存不为0，增加到对应stock库存中"""
    # selectActInfo('1598')'1668'
    dic = selectActInfo(itemId)
    logging.info('活动信息 %s',dic)
    # skuId,actId,itemId,itemName,itemDesc,itemTyoe,startTime,endTime
    skuId = querySkuId(huohao,drugstoreId)
    logging.info('skuId %s',skuId)
    actId = dic.get('act_id')
    
    itemName = dic.get('item_name')
    itemDesc = dic.get('item_desc')
    itemType = dic.get('item_type')
    startTime = dic.get('act_start_time')
    endTime = dic.get('act_end_time')
    quotaId = dic.get('quota_id')

    dirId = dic.get('dir_id')
    dirCode = dic.get('dir_code')
    res = addAmStatInfo(skuId,actId,itemId,itemName,itemDesc,itemType,startTime,endTime,quotaId =quotaId)
    # logging.info('statId %s',res)
    addPmSkuDir(skuId,dirId,dirCode)
    if skuTotal!=0 or maxTotal!=0:
        addAmStockLimit(skuId,itemId,quotaId,skuTotal,maxTotal,remark='')
        addAmStockPday(skuId,actId,itemId,quotaId,drugstoreId,skuTotal,maxTotal,remark='')
    # db.commit()

def buildxxx(tableName,itemId,drugstoreId):
    list = querySkuIdByTable(tableName,drugstoreId)
    for sku in list:
        skuId = sku['sku_id']
        # addAmStatInfo(skuId,'actId',itemId,itemName,itemDesc,itemType,startTime,endTime,quotaId='',itemPriority='100',itemAttr='multi',otherStr1='')
        dic = selectActInfo(itemId)
        # logging.info('活动信息 %s',dic)
        # skuId,actId,itemId,itemName,itemDesc,itemTyoe,startTime,endTime
        # skuId = querySkuId(huohao,drugstoreId)
        # logging.info('skuId %s',skuId)
        actId = dic.get('act_id')
        
        itemName = dic.get('item_name')
        itemDesc = dic.get('item_desc')
        itemType = dic.get('item_type')
        startTime = dic.get('act_start_time')
        endTime = dic.get('act_end_time')
        quotaId = dic.get('quota_id')

        dirId = dic.get('dir_id')
        dirCode = dic.get('dir_code')
        res = addAmStatInfo(skuId,actId,itemId,itemName,itemDesc,itemType,startTime,endTime,quotaId =quotaId)
        logging.info('活动信息 %s',res)
        db.commit()

def createNewSkuByTable(tableName):
    """根据excel给的prodid创建sku，需确定drugstoreid和价格 上下架状态"""
    logging.debug('新建商品的pm_prod_sku，huohao,零售价，上下架状态外其他信息用 prod 的原始信息，不用execl中的')
    sql = '''
        INSERT INTO `medstore`.`pm_prod_sku` (`prod_id`, `sku_status`, `sku_price`, `sku_fee`
        , `drugstore_id`, `brand_id`, `sku_update_time`, `sku_create_time`, `sku_remark`, `sku_logistics`
        , `prod_name`, `pharmacy_huohao`, `source_id`, `sku_json`, `sku_attr`, `sku_img`, `sku_sum`) 
        SELECT p.prod_id
        ,a.sku_status as sku_status
        ,a.price*100 as sku_price
        ,a.fee*100 as sku_fee
        ,a.drugstore_id,'1' as brand_id ,now() as sku_update_time,now() as   sku_create_time
        ,'' as sku_remark,p.prod_logist,p.`prod_name` 
        ,a.huohao  as pharmacy_huohao,'1' as source_id
        ,concat('{{\"prod_spec\":\"',p.prod_spec,'\"}}'),'11100' as sku_attr,'' as sku_img,'' as sku_sum
        from {0} a,pm_prod_info p
        WHERE a.prod_id = p.prod_id ;
        '''.format(tableName)
    try:
        insertSQL(sql)
        db.commit()
    except Exception as err:
        logging.error("Error %s for execute sql: %s" % (err, sql))
        logging.debug('新建商品的pm_prod_sku，insert语句失败！！！')
        db.rollback()

# 收单免费、下单抽奖、当日达	 
def buildSkuBaseByHuohao(huohao,drugstoreId,itemId=0,quotaId=0,skuImage='当日达',limitquan=False):
    
    # 首单免费
    copyAmStatInfoByHuohao( '1350',huohao,drugstoreId) 
    logging.debug('首单免费')
    # 下单返券
    copyAmStatInfoByHuohao( '1517',huohao,drugstoreId)
    logging.debug('下单返券')
    # 当日送达
    if skuImage=='当日达':
        addAmskuImage(huohao,drugstoreId)
    elif skuImage=='30分钟':
        addAmskuImage(huohao,drugstoreId,img='http://image.ykd365.cn/icon/home/30minbd.png',radio='393',title='30分钟送达')

    logging.debug('当日送达')
    # skuId = querySkuId(huohao,drugstoreId)
    # 防疫防护  
    # addPmLabelImage('防疫防护','http://image.ykd365.cn/act/2002/notouch/list.png','1','200',skuId=skuId)
    # 限券
    if limitquan==True:
        # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)
        addSkuDirByItemId(huohao,drugstoreId,78)
    
    # skuId = querySkuId(huohao,drugstoreId)
    # createStock(skuId,itemId,quotaId,160,remark='欣臣限购',days=3)
    # createStockPday('217',skuId,itemId,quotaId,160,drugstoreId,remark='欣臣限购',days=3)

    # skuId = querySkuId(huohao,drugstoreId)
    # addSkudirBySkuId(skuId,dirId,dirCode)
    db.commit()

def xrzq():
    '''新人专区 有会场不分楼层，一个限购  ,需要手动修改第一个口罩的价格为10元'''
    ydList = [1600,1601]
    startTime='2020-03-20'
    endTime='2020-12-31'
    tableName ='as_test.20032_xc_xr'

    actId = 231
    actName = '欣臣3月新人专区'

    img = 'http://image.ykd365.cn/act/202003/xr/01.jpg'
    color = '#fec2b9'
    for drugstoreId in ydList:
        # addNewSku4JHSMS(tableName,'3JHS',drugstoreId)
        # addPmActSale(tableName,drugstoreId,startTime,endTime)
        # db.commit()
        buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color)
        logging.info(
"""--------------------------------------------------------------------------------------
-------------------------------------------------------------------------
UPDATE pm_prod_sku set sku_fee=1000,sku_price =1000 WHERE sku_id in (25559729,25559728);
SELECT* from pm_sku_dir WHERE sku_id in (25559729,25559728) and dir_code like '%quota%';
--------------------------------------------------------------------------------------
"""
)

def kd(drugstoreId,dirCode,initDirID,initSkuId,iActId,iItemId,iRangeId,iQuotaId,iDetailId,baseDrugstoreId,baseDirCode):
    try:
        # 复制创建药店基本信息表
        # drugstoreSQL = f"""INSERT INTO `medstore`.`sm_drugstore_info` (`drugstore_id`, `drugstore_type`, `drugstore_name`, `drugstore_phone`, `drugstore_address`, `drugstore_model`, `drugstore_model_new`, `parent_id`, `drugstore_code`, `drugstore_level`, `drugstore_busi`, `drugstore_update_time`, `drugstore_create_time`, `drugstore_time`, `operator`, `drugstore_remark`, `drugstore_position`, `drugstore_range`, `drugstore_rect`, `drugstore_area`, `deliver_time`, `drugstore_sid`, `drugstore_smqid`, `drugstore_url`, `drugstore_purchase`, `drugstore_certificate`, `drugstore_show`, `drugstore_notice`, `drugstore_principal`, `drugstore_prin_phone`, `drugstore_wel_word`, `drugstore_wel_word_open`, `drugstore_wel_word_url`, `drugstore_wel_word_title`, `enable_3rdlogist`, `drugstore_contact`, `lack_title`, `lack_weburl`, `lack_webtitle`, `lack_state_pic`, `drugstore_deliver_way`, `addonitem_title`, `addonitem_subtitle`, `addonitem_goname`, `addonitem_weburl`, `addonitem_webname`, `enable_sflogist`, `drugstore_home_url`, `drugstore_home_ratio`, `fn_time_range`, `share_btn_image`, `share_btn_image_ratio`, `share_alert_image`, `support_collect`, `drugstore_deliver_desc`, `authority_tip_title`, `authority_tip_content`, `submit_order_remind_title`, `submit_order_remind`) 
        #     select {drugstoreId} `drugstore_id`, `drugstore_type`, `drugstore_name`, `drugstore_phone`, `drugstore_address`, `drugstore_model`, `drugstore_model_new`, `parent_id`, `drugstore_code`, `drugstore_level`, `drugstore_busi`, `drugstore_update_time`, `drugstore_create_time`, `drugstore_time`, `operator`, `drugstore_remark`, `drugstore_position`
        #     ,'' `drugstore_range`, `drugstore_rect`, `drugstore_area`, `deliver_time`, `drugstore_sid`, `drugstore_smqid`, `drugstore_url`, `drugstore_purchase`, `drugstore_certificate`, `drugstore_show`, `drugstore_notice`, `drugstore_principal`, `drugstore_prin_phone`, `drugstore_wel_word`, `drugstore_wel_word_open`, `drugstore_wel_word_url`, `drugstore_wel_word_title`, `enable_3rdlogist`, `drugstore_contact`, `lack_title`, `lack_weburl`, `lack_webtitle`, `lack_state_pic`, `drugstore_deliver_way`, `addonitem_title`, `addonitem_subtitle`, `addonitem_goname`, `addonitem_weburl`, `addonitem_webname`, `enable_sflogist`, `drugstore_home_url`, `drugstore_home_ratio`, `fn_time_range`, `share_btn_image`, `share_btn_image_ratio`, `share_alert_image`, `support_collect`, `drugstore_deliver_desc`, `authority_tip_title`, `authority_tip_content`, `submit_order_remind_title`, `submit_order_remind`
        #      from sm_drugstore_info WHERE drugstore_id ={baseDrugstoreId}"""
        # insertSQL(drugstoreSQL)

        # 复制药店的运费配置
        copyOmDeliverFee(drugstoreId,baseDrugstoreId)

        # 创建首页的结构
        copyPmPharmacyDir(drugstoreId,initDirID,baseDrugstoreId)
        
        
       

        

        

        # #根据基础dir信息 创建一套新的dir info
        copyPmDirInfo(drugstoreId,dirCode,initDirID,initSkuId,baseDrugstoreId,baseDirCode)
        # #根据基础sku信息 创建一套新的prodsku
        copyPmProdSku(drugstoreId,dirCode,initDirID,initSkuId,baseDrugstoreId,baseDirCode)
        # #根据基础sku 和 dir 信息 创建一套新的skudir
        copyPmSkuDir(drugstoreId,dirCode,initDirID,initSkuId,baseDrugstoreId,baseDirCode)

        copySmImageLink(drugstoreId,iSmId,iDirId,baseDrugstoreId)

        copyLmTem(drugstoreId,iSmId,baseDrugstoreId)

        copySmShareInfo(drugstoreId,baseDrugstoreId)

        copySmUserBanner(drugstoreId,baseDrugstoreId)

        copyPmPacketInfo(drugstoreId,iPacketId,iSkuId,baseDrugstoreId)
        copyPmPacketSku(drugstoreId,iPacketId,iSkuId,baseDrugstoreId)

        copyPmSkuSale(drugstoreId,iSkuId,baseDrugstoreId)

        

        copyAmActInfo(iActId,drugstoreId,baseDrugstoreId)
        copyAmActItem(iItemId,iActId,drugstoreId)
        copyAmActRange(iRangeId,iDirId)
        copyAmActItemRange(iRangeId,iItemId)
        copyAmItemDetails(iDetailId,iItemId)
        copyAmDetailsRule(iDetailId)
        copyAmQuotaInfo(iItemId,iQuotaId)
        copyAmStockLimit(iSkuId,iItemId,iQuotaId)
        copyAmStockPday(iSkuId,iActId,iItemId,iQuotaId,drugstoreId)
        copyAmStagesSale(iSgId,iActId,iItemId,iQuotaId,drugstoreId)
        copyAmStagesSaleDetail(iSgId,iDirId,iActId,iItemId,iQuotaId,drugstoreId)

        # 首单免费
        # copyAmStatInfoBaseByItemId('1350',drugstoreId)
        # 下单返券
        copyAmStatInfoBaseByItemId('1517',drugstoreId)
        #30分钟送达
        copyAmskuImage(drugstoreId,img='http://image.ykd365.cn/icon/home/30minbd.png',radio='393',title='30分钟送达')

        addAmStatInfoByDrugstoreId(drugstoreId)

        copyStAnalysisCate(iDirId,baseDrugstoreId,drugstoreId)
        db.commit()
    except Exception as identifier:
        logging.debug('报错啦 %s',identifier)
        db.rollback()

def copyPmDirInfo(drugstoreId,dirCode,initDirID,initSkuId,baseDrugstoreId,baseDirCode):
     #根据基础dir信息 创建一套新的dir info
    dirSQL = f"""INSERT INTO pm_dir_info (`dir_id`, `dir_code`, `dir_name`, `dir_type`, `dir_status`, `dir_revalue`, `prod_sum`, `dir_num`, `dir_level`, `dir_img`, `parent_dir_id`, `dir_update_time`, `dir_create_time`, `dir_remark`, `dir_all_name`, `category_id`, `pharmacy_id`, `dir_gotocata`, `dir_main_show`)
            select `dir_id`+{initDirID},replace(replace(old_dir_code,'{baseDirCode}','{dirCode}'),'{baseDrugstoreId}act','{drugstoreId}act')  `dir_code`, `dir_name`, `dir_type`, `dir_status`, `dir_revalue`, `prod_sum`, `dir_num`, `dir_level`, `dir_img`
            , `parent_dir_id`+{initDirID},NOW() `dir_update_time`,NOW() `dir_create_time`, `dir_remark`, `dir_all_name`, `category_id`
            ,{drugstoreId} `pharmacy_id`, `dir_gotocata`, `dir_main_show`
            from  as_test.`kd_pm_dir_info` ;"""
    insertSQL(dirSQL)

def copyPmProdSku(drugstoreId,dirCode,initDirID,initSkuId,baseDrugstoreId,baseDirCode):
    #根据基础sku信息 创建一套新的prodsku
    skuSQL = f""" INSERT INTO  pm_prod_sku (`sku_id`, `prod_id`, `sku_status`, `sku_price`, `sku_fee`, `drugstore_id`, `brand_id`, `sku_update_time`, `sku_create_time`, `sku_remark`, `sku_logistics`, `prod_name`, `pharmacy_huohao`, `source_id`, `sku_json`, `sku_attr`, `sku_img`, `sku_sum`, `sku_activate`, `sales_info`, `sku_sum_flag`, `sku_hot_order`, `sku_sort`, `sku_rank`, `sku_type`, `is_set`, `set_num`, `dis_before_price`, `dis_after_price`, `discount_price`, `pre_prod_name`, `is_prescription`, `is_interrogation`, `special_buy`) 
            select `sku_id`+{initSkuId}, `prod_id`, `sku_status`, `sku_price`, `sku_fee`
            ,{drugstoreId}  `drugstore_id`, `brand_id`,now() `sku_update_time`,now() `sku_create_time`, `sku_remark`, `sku_logistics`, `prod_name`, `pharmacy_huohao`, `source_id`, `sku_json`, `sku_attr`, `sku_img`, `sku_sum`, `sku_activate`, `sales_info`, `sku_sum_flag`, `sku_hot_order`, `sku_sort`, `sku_rank`, `sku_type`, `is_set`, `set_num`, `dis_before_price`, `dis_after_price`, `discount_price`, `pre_prod_name`, `is_prescription`, `is_interrogation`, `special_buy`
            FROM  as_test.`kd_pm_prod_sku` ;"""
    insertSQL(skuSQL)

def copyPmSkuDir(drugstoreId,dirCode,initDirID,initSkuId,baseDrugstoreId,baseDirCode):
    #根据基础sku 和 dir 信息 创建一套新的skudir
    skudirSQL = f""" INSERT INTO pm_sku_dir (   `dir_id`, `sku_id`, `dir_code`, `sku_order`, `update_time`)
                select  sd.`dir_id`+{initDirID}, `sku_id`+{initSkuId},replace(replace(sd.old_dir_code,'{baseDirCode}','{dirCode}'),'{baseDrugstoreId}act','{drugstoreId}act') `dir_code`, `sku_order`,now() `update_time`
                from as_test.kd_pm_sku_dir   sd ;"""
    insertSQL(skudirSQL)

def copyPmPharmacyDir(drugstoreId,initDirID,baseDrugstoreId):
    '''#根据基础app首页 PmPharmacyDir 信息 创建一套新的PmPharmacyDir'''
    phdirSQL = f""" INSERT INTO `medstore`.`pm_pharmacy_dir` (  `dir_id`, `pharmacy_id`, `dir_level`, `dir_type`) 
                SELECT  d.dir_id+{initDirID} ,{drugstoreId}  `pharmacy_id`, pd.`dir_level`, pd.`dir_type`
                from pm_pharmacy_dir pd ,as_test.kd_pm_dir_info d
                WHERE  pd.dir_id = d.old_dir_id
                and pd.pharmacy_id = {baseDrugstoreId};"""
    insertSQL(phdirSQL)

def copyOmDeliverFee(drugstoreId,baseDrugstoreId):
    '''#根据  运费信息 OmDeliverFee 信息 创建一套新的'''
    phdirSQL = f""" INSERT INTO `medstore`.`om_deliver_fee` ( `pharmacy_id`, `threshold_value`, `deliver_fee`, `deliver_type`, `deliver_status`, `date_range`, `time_range`, `deliver_sort`, `deliver_remark`, `deliver_other`, `deliver_order2`, `user_old_or_new`) 
                select {drugstoreId} `pharmacy_id`, `threshold_value`, `deliver_fee`, `deliver_type`, `deliver_status`, `date_range`, `time_range`, `deliver_sort`, `deliver_remark`, `deliver_other`, `deliver_order2`, `user_old_or_new`   
                from om_deliver_fee
                WHERE pharmacy_id = {baseDrugstoreId};"""
    insertSQL(phdirSQL)

def copySmImageLink(drugstoreId,iSmId,iDirId,baseDrugstoreId):
    '''#轮播 通栏 九宫格'''
    smSQL = f""" INSERT INTO  sm_image_link (`link_id`, `drugstore_id`, `seq_num`, `image_url`, `link_url`, `link_type`, `link_name`, `link_param`, `link_status`, `link_update_time`, `link_create_time`, `link_remark`, `link_start_time`, `link_end_time`, `link_view`, `link_version`) 
                select `link_id`+{iSmId},'{drugstoreId}' `drugstore_id`, `seq_num`, `image_url`,REPLACE(link_url,ks.link_param,kd.dir_id+{iDirId}) `link_url`, `link_type`, `link_name`,kd.dir_id+{iDirId} `link_param`, `link_status`, `link_update_time`, `link_create_time`, `link_remark`, `link_start_time`, `link_end_time`, `link_view`, `link_version`
                FROM  as_test.`kd_sm_image_link`  ks LEFT JOIN as_test.kd_pm_dir_info kd on ks.link_param = kd.old_dir_id ;"""
    insertSQL(smSQL)

def copyLmTem(drugstoreId,iSmId,baseDrugstoreId):
    '''# 九宫格 的布局'''
    insSQL = f""" INSERT INTO `medstore`.`lm_tem_instance` ( `tem_id`, `pharmacy_id`, `effect_time`, `invalid_time`, `ins_priority`, `ins_rule`, `other_info`)
            SELECT `tem_id`,'{drugstoreId}' `pharmacy_id`, `effect_time`, `invalid_time`, `ins_priority`, `ins_rule`, `other_info`
            from lm_tem_instance WHERE pharmacy_id ={baseDrugstoreId};"""
    ins = insertSQL(insSQL)   
    teminsId = ins['lastId']
    temiteminsSQL = f""" INSERT INTO `medstore`.`lm_tem_item_ins` (  `tem_ins_id`, `tem_item_id`, `relation_object`, `relation_id`, `ins_desc`) 
                SELECT '{teminsId}' `tem_ins_id`, ii.`tem_item_id`, ii.`relation_object`,si.link_id+{iSmId} `relation_id`,ii.`ins_desc`
                from lm_tem_instance i 
                LEFT JOIN lm_tem_item_ins ii on i.tem_ins_id = ii.tem_ins_id 
                LEFT JOIN as_test.kd_sm_image_link si on ii.relation_id = si.old_link_id
                WHERE i.pharmacy_id ={baseDrugstoreId};"""
    insertSQL(temiteminsSQL)   

def copySmShareInfo(drugstoreId,baseDrugstoreId):
    '''# 九宫格 的布局'''
    shareSQL = f""" INSERT INTO `medstore`.`sm_shared_info` ( `pharmacy_id`, `shared_type`, `shared_url`, `shared_title`, `shared_content`, `shared_img_url`, `shared_status`, `shared_create_time`, `shared_update_time`, `shared_remark`, `share_go_type`, `share_go_data`, `share_go_title`, `share_go_can`)
                SELECT {drugstoreId} `pharmacy_id`, `shared_type`,replace(`shared_url`,'pharmacyId={baseDrugstoreId}','pharmacyId={drugstoreId}'), `shared_title`, `shared_content`, `shared_img_url`, `shared_status`, `shared_create_time`, `shared_update_time`, `shared_remark`, `share_go_type`, `share_go_data`, `share_go_title`, `share_go_can`
                from sm_shared_info 
                WHERE pharmacy_id ={baseDrugstoreId};"""
    insertSQL(shareSQL)   
    
def copySmUserBanner(drugstoreId,baseDrugstoreId):
    '''# 九宫格 的布局'''
    shareSQL = f""" INSERT INTO `medstore`.`sm_user_banner` (  `banner_name`, `banner_image`, `banner_url`, `banner_type`, `pharmacy_id`, `banner_remark`, `banner_create_time`, `banner_update_time`, `banner_flag`, `banner_ratio`, `banner_attr`, `banner_priority`, `banner_param`) 
                SELECT  `banner_name`, `banner_image`, `banner_url`, `banner_type`,{drugstoreId} `pharmacy_id`, `banner_remark`, `banner_create_time`, `banner_update_time`, `banner_flag`, `banner_ratio`, `banner_attr`, `banner_priority`, `banner_param`
                from sm_user_banner WHERE pharmacy_id = {baseDrugstoreId};"""
    insertSQL(shareSQL) 

def copyPmPacketInfo(drugstoreId,iPacketId,iSkuId,baseDrugstoreId):
    '''# 疗程购的多盒品 packet'''
    packetSQL = f""" INSERT INTO `medstore`.`pm_packet_info` (`packet_id`, `packet_huohao`, `packet_name`, `packet_status`, `packet_type`, `packet_price`, `packet_fee`, `packet_category`, `packet_content`, `packet_stock`, `packet_img`, `drugstore_id`, `packet_update_time`, `packet_create_time`, `packet_remark`, `sku_id`, `pre_prod_name`, `packet_coures`, `packet_title_formula`)
                SELECT `packet_id`+{iPacketId}, `packet_huohao`, `packet_name`, `packet_status`, `packet_type`, `packet_price`, `packet_fee`, `packet_category`, `packet_content`, `packet_stock`, `packet_img`
                ,'{drugstoreId}' `drugstore_id`, `packet_update_time`, `packet_create_time`, `packet_remark`
                ,ks.sku_id+{iSkuId} `sku_id`, kp.`pre_prod_name`, `packet_coures`, `packet_title_formula` 
                from as_test.`kd_pm_packet_info` kp JOIN as_test.kd_pm_prod_sku ks on kp.sku_id = ks.old_sku_id;"""
    insertSQL(packetSQL) 

def copyPmPacketSku(drugstoreId,iPacketId,iSkuId,baseDrugstoreId):
    '''# 疗程购的单品   packet'''
    packetSQL = f"""  INSERT INTO `medstore`.`pm_packet_sku` ( `packet_id`, `sku_id`, `prod_name`, `sku_huohao`, `packet_sku_id`, `packet_sku_price`, `sku_fee`, `sku_seq`, `sku_amount`, `total_price`, `link_remark`) 
                SELECT   pi.`packet_id`+{iPacketId}, s.`sku_id`+{iSkuId}, ps.`prod_name`, `sku_huohao`
                ,s2.sku_id+{iSkuId} `packet_sku_id`, `packet_sku_price`, ps.`sku_fee`, `sku_seq`, `sku_amount`, `total_price`, `link_remark` 
                from pm_packet_sku ps   
                JOIN as_test.kd_pm_prod_sku s ON ps.sku_id = s.old_sku_id 
                JOIN as_test.kd_pm_prod_sku s2 ON ps.packet_sku_id = s2.old_sku_id 
                JOIN as_test.kd_pm_packet_info pi on pi.old_packet_id = ps.packet_id
                ORDER BY link_id desc;"""
    insertSQL(packetSQL)

def copyPmSkuSale(drugstoreId,iSkuId,baseDrugstoreId):
    '''# 价格 PmSkuSale   '''
    packetSQL = f"""  INSERT INTO `medstore`.`pm_sku_sale` (  `sku_id`, `sale_fee`, `sale_price`, `sale_start_time`, `sale_end_time`, `sale_status`, `sale_create_time`, `sale_update_time`, `sale_remark`)
                SELECT ps.`sku_id`+{iSkuId} , `sale_fee`, `sale_price`, `sale_start_time`, `sale_end_time`, `sale_status`, `sale_create_time`, `sale_update_time`, `sale_remark` 
                from pm_sku_sale ssa , as_test.kd_pm_prod_sku ps
                WHERE ssa.sku_id = ps.old_sku_id ;"""
    insertSQL(packetSQL)


# 根据查询到的活动信息，复制amstatinfo数据  
def copyAmStatInfoBaseByItemId(itemId,drugstoreId):
    """ 该药店下  所有商品都会被加入一条 am stat info信息,是更具itemid 得到的活动信息,通常就是标签 """
    configSql = '''SELECT config_value from sm_config WHERE config_key = 'act_batch';'''
    configDic = selectOneBy(configSql)
    configValue =configDic.get('config_value')

    dic = selectActInfo(itemId)
    logging.info('活动信息 %s',dic)
    # skuId,actId,itemId,itemName,itemDesc,itemTyoe,startTime,endTime
    # skuId = querySkuId(huohao,drugstoreId)
    # logging.info('skuId %s',skuId)
    actId = dic.get('act_id')
    
    itemName = dic.get('item_name')
    itemDesc = dic.get('item_desc')
    itemType = dic.get('item_type')
    startTime = dic.get('act_start_time')
    endTime = dic.get('act_end_time')
    quotaId = dic.get('quota_id') if dic.get('quota_id')!=None else 'NULL'

    dirId = dic.get('dir_id')
    dirCode = dic.get('dir_code')

    itemAttr = dic.get('item_attr')
    otherStr1 = dic.get('other_str1','')
    itemPriority = dic.get('item_priority')
    # res = addAmStatInfo(skuId,actId,itemId,itemName,itemDesc,itemType,startTime,endTime,quotaId =quotaId)


    sql = f"""INSERT INTO am_stat_info (  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark` , `item_name`
    , `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`
        , `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`) 
        select '{configValue}',sku_id, '{actId}', '{itemId}', '{itemDesc}', '{itemName}'
        , '{itemAttr}', now(), now(), '{startTime}', '{endTime}'
        , '{itemType}', '{otherStr1}', '{quotaId}', NULL, '{itemPriority}'
        from pm_prod_sku 
        where drugstore_id = {drugstoreId};
        """
    res = insertSQL(sql)
    # return res['lastId']




# 创建列表页的药品名左侧的标志，当日送达
def copyAmskuImage(drugstoreId,img='http://image.ykd365.cn/icon/home/drsd.png',radio='342',title='当日送达',startTime='2020-03-01',endTime='2028-03-01'):
    """创建列表页的药品名左侧的标志，当日送达"""
    # logging.info('创建列表页的药品名左侧的标志，当日送达')
    sql = f'''
        INSERT INTO am_sku_img (  `sku_id`, `act_type`, `act_start_time`, `act_end_time`, `act_status`, `create_time`, `update_time`, `act_img_url`, `aspect_ratio`, `remark`)
        SELECT s.sku_id,'logo','{startTime}', '{endTime}', '1', NOW(), NOW(), '{img}', '{radio}', '{title}'
        from  pm_prod_sku s
        WHERE   s.drugstore_id = {drugstoreId};
    ''' 
    res = insertSQL(sql)

def copyAmActInfo(iActId,drugstoreId,baseDrugstoreId):
    '''# 复制活动actinto'''
    sql = f""" INSERT INTO `medstore`.`am_act_info` (  act_id,`act_name`, `act_type`, `act_status`, `act_content`, `act_update_time`, `act_create_time`, `act_start_time`, `act_end_time`, `act_level`, `act_remark`, `act_img`, `act_url`, `pharmacy_id`) 
                    SELECT  act_id+{iActId},`act_name`, `act_type`, `act_status`, `act_content`,now() `act_update_time`,now() `act_create_time`, `act_start_time`, `act_end_time`, `act_level`, `act_remark`, `act_img`, `act_url`
                    ,{drugstoreId} `pharmacy_id`
                    FROM as_test.`kd_am_act_info` 
                    WHERE pharmacy_id ={baseDrugstoreId};"""
    insertSQL(sql)

def copyAmActItem(iItemId,iActId,drugstoreId):
    '''# 复制活动act item'''
    sql = f""" INSERT INTO am_act_item (`item_id`, `item_attr`, `item_name`, `act_id`, `item_status`, `item_priority`, `item_type`, `item_desc`, `item_update_time`, `item_create_time`, `item_remark`, `item_img`, `pharmacy_id`, `item_flag`, `sales_goto_type`, `sales_goto_title`, `sales_goto_url`, `item_num`, `item_title`, `activity_img`, `activity_img_ratio`)
            SELECT `item_id`+{iItemId}, `item_attr`, `item_name`, a.`act_id`+{iActId}, `item_status`, `item_priority`, `item_type`, `item_desc`, `item_update_time`, `item_create_time`, `item_remark`, `item_img`
            ,'{drugstoreId}' `pharmacy_id`, `item_flag`, `sales_goto_type`, `sales_goto_title`, `sales_goto_url`, `item_num`, `item_title`, `activity_img`, `activity_img_ratio`
            FROM as_test.`kd_am_act_item` i ,as_test.kd_am_act_info a
            WHERE i.act_id = a.old_act_id;"""
    insertSQL(sql)

def copyAmActRange(iRangeId,iDirId):
    '''# 复制活动act range'''
    sql = f""" INSERT INTO `medstore`.`am_act_range` (`range_id`, `range_type`, `range_value`, `range_status`, `range_name`, `range_remark`, `range_update_time`, `range_create_time`) 
                SELECT `range_id`+{iRangeId}, `range_type`,d.dir_id+{iDirId} `range_value`, `range_status`, `range_name`, `range_remark`, `range_update_time`, `range_create_time`
                FROM as_test.`kd_am_act_range` r ,as_test.kd_pm_dir_info d
                WHERE r.old_range_value = d.old_dir_id ;"""
    insertSQL(sql)

def copyAmActItemRange(iRangeId,iItemId):
    '''# 复制活动act item range'''
    sql = f""" INSERT INTO `medstore`.`am_item_range` ( `range_id`, `item_id`)
                SELECT r.range_id+{iRangeId},i.item_id+{iItemId} 
                from am_item_range ir,as_test.kd_am_act_item i ,as_test.kd_am_act_range r
                WHERE ir.item_id = i.old_item_id
                and ir.range_id = r.old_range_id;"""
    insertSQL(sql)

def copyAmItemDetails(iDetailId,iItemId):
    '''# 复制活动am_item_details xx折'''
    sql = f""" INSERT INTO `medstore`.`am_item_details` (`details_id`, `details_level`, `item_id`, `details_type`, `details_val_type`, `details_value`, `details_update_time`, `details_create_time`, `details_remark`, `details_content`) 
                SELECT `details_id`+{iDetailId}, `details_level`, i.`item_id`+{iItemId}, `details_type`, `details_val_type`, `details_value`, `details_update_time`, `details_create_time`, `details_remark`, `details_content`
                from as_test.kd_am_item_details d,as_test.kd_am_act_item i
                WHERE d.old_item_id = i.old_item_id;"""
    insertSQL(sql)   

def copyAmDetailsRule(iDetailId):
    '''# 复制活动  am_details_rule  '''
    sql = f""" INSERT INTO `medstore`.`am_details_rule` (  `details_id`, `rule_id`)  
                SELECT  d.`details_id`+{iDetailId}, dr.`rule_id`
                from am_details_rule dr,as_test.kd_am_item_details d
                WHERE dr.details_id = d.old_details_id ;"""
    insertSQL(sql)     

def copyAmQuotaInfo(iItemId,iQuotaId):
    '''# 复制活动  copyAmQuotaInfo  '''
    sql = f""" INSERT INTO `medstore`.`am_quota_info` (`quota_id`, `item_id`, `quota_rule`, `quota_kind`, `quota_type`, `quota_status`, `quota_total`, `quota_update_time`, `quota_create_time`, `quota_remark`, `quota_content`, `qutoa_group`) 
                SELECT `quota_id`+{iQuotaId}, i.`item_id`+{iItemId}, `quota_rule`, `quota_kind`, `quota_type`, `quota_status`, `quota_total`, `quota_update_time`, `quota_create_time`, `quota_remark`, `quota_content`, `qutoa_group`
                from as_test.kd_am_quota_info id,as_test.kd_am_act_item i
                WHERE id.old_item_id = i.old_item_id;"""
    insertSQL(sql)

def copyAmStockLimit(iSkuId,iItemId,iQuotaId):
    '''# 复制活动  copyAmQuotaInfo  '''
    sql = f""" INSERT INTO `medstore`.`am_stock_limit` (  `item_id`, `quota_id`, `sku_id`, `sku_total`, `as_remark`, `max_total`)
                SELECT  a.`item_id`+{iItemId},a.`quota_id`+{iQuotaId},s.sku_id+{iSkuId} ,  a.`sku_total`, a.`as_remark`, a.`max_total`
                from 
                (SELECT   q.`quota_id`,i.`item_id`,  `sku_total`, `as_remark`, `max_total`,a.sku_id  
                from as_test.kd_am_quota_info q ,as_test.kd_am_act_item i   ,am_stock_limit a 
                WHERE a.quota_id = q.old_quota_id
                and i.old_item_id = a.item_id
                ) a ,as_test.kd_pm_prod_sku s
                WHERE a.sku_id = s.old_sku_id ;"""
    insertSQL(sql)

def copyAmStockPday(iSkuId,iActId,iItemId,iQuotaId,drugstoreId):
    '''# 复制活动  am_stock_pday  '''
    sql = f""" INSERT INTO `medstore`.`am_stock_pday` (  `act_id`, `item_id`, `quota_id`,  `sku_id`, `prod_name`, `pharmacy_id`, `sku_num`,  `sku_total`, `remark`) 
                SELECT  `act_id`+{iActId}, `item_id`+{iItemId}, `quota_id`+{iQuotaId},  s.`sku_id`+{iSkuId}, `prod_name`,'{drugstoreId}'  `pharmacy_id`, a.`sku_num`,  a.`sku_total`, `remark`
                from 
                (SELECT   q.`quota_id`,i.`item_id`,sku_num,  `sku_total`, `remark`,a.sku_id ,ac.act_id -- ,s.`sku_id`
                from as_test.kd_am_quota_info q ,as_test.kd_am_act_item i   ,am_stock_pday a ,as_test.kd_am_act_info ac
                WHERE a.act_id = ac.old_act_id
                and  a.quota_id = q.old_quota_id
                and i.old_item_id = a.item_id
                ) a ,as_test.kd_pm_prod_sku s
                WHERE a.sku_id = s.old_sku_id ;"""
    insertSQL(sql)

def copyAmStagesSale(iSgId,iActId,iItemId,iQuotaId,drugstoreId):
    '''# 复制活动  am_stages_sale  '''
    sql = f""" INSERT INTO `medstore`.`am_stages_sale` (`sg_id`, `pharmacy_id`, `sg_title`, `sg_status`, `sg_start_time`, `sg_end_time`, `quota_id`, `act_id`, `item_id`, `sg_create_time`, `sg_update_time`, `sg_json`, `sg_remark`, `sg_color`) 
                SELECT `sg_id`+{iSgId},'{drugstoreId}' `pharmacy_id`, `sg_title`, `sg_status`, `sg_start_time`, `sg_end_time`
                , q.`quota_id`+{iQuotaId}, ac.`act_id`+{iActId}, i.`item_id`+{iItemId}, `sg_create_time`, `sg_update_time`, `sg_json`, `sg_remark`, `sg_color`
                -- SELECT *
                from as_test.kd_am_stages_sale a ,as_test.kd_am_quota_info q,as_test.kd_am_act_item i ,as_test.kd_am_act_info ac
                WHERE a.quota_id = q.old_quota_id
                and i.old_item_id = a.item_id
                and a.act_id = ac.old_act_id;"""
    insertSQL(sql)

def copyAmStagesSaleDetail(iSgId,iDirId,iActId,iItemId,iQuotaId,drugstoreId):
    '''# 复制活动  am_stages_sale  '''
    sql = f""" INSERT INTO `medstore`.`am_stages_sale_detail` ( `sg_id`, `act_id`, `item_id`, `quota_id`, `pharmacy_id`, `dir_id`, `sg_detail_create_time`, `sg_detail_update_time`, `sg_detail_remark`, `sg_detail_flag`, `sg_detail_type`) 
                SELECT   a.`sg_id`+{iSgId}, ac.`act_id`+{iActId}, i.`item_id`+{iItemId}, q.`quota_id`+{iQuotaId},'{drugstoreId}' `pharmacy_id`, d.`dir_id`+{iDirId}, NOW()  `sg_detail_create_time`,NOW() `sg_detail_update_time`, `sg_detail_remark`, `sg_detail_flag`, `sg_detail_type`
                from am_stages_sale_detail sd,as_test.kd_am_stages_sale a ,as_test.kd_am_quota_info q,as_test.kd_am_act_item i ,as_test.kd_am_act_info ac,as_test.kd_pm_dir_info d
                WHERE sd.sg_id = a.old_sg_id
                and a.quota_id = q.old_quota_id
                and i.old_item_id = a.item_id
                and a.act_id = ac.old_act_id
                and sd.dir_id = d.old_dir_id;"""
    insertSQL(sql)

def copyStAnalysisCate(iDirId,baseDrugstoreId,drugstoreId):
    '''# 复制多买少算活动  st_analysis_cate  '''
    sql = f""" INSERT INTO `medstore`.`st_analysis_cate` (  `pharmacy_id`, `category_name`, `category_icon_url`, `category_state`, `category_order`, `category_id`) 
                SELECT '{drugstoreId}' `pharmacy_id`, `category_name`, `category_icon_url`, `category_state`, `category_order`
                ,d.dir_id+{iDirId} `category_id`
                from st_analysis_cate a,as_test.kd_pm_dir_info d
                WHERE a.category_id = d.old_dir_id 
                and a.pharmacy_id = {baseDrugstoreId};"""
    insertSQL(sql)



def createLmTem(drugstoreId,iSmId,baseDrugstoreId):
    '''# 新建 九宫格 的布局'''
    tem_name = '新版布1'
    tem_desc = '左上占2行2列,其余5格包围他'
    ydids = [200,1600]
    items = [{'item_seq':'1','row_seq':'1','col_seq':'1','col_width':'66','col_aspect_radio':'100','col_span':'4','row_span':'2'},
            {'item_seq':'2','row_seq':'1','col_seq':'2','col_width':'33','col_aspect_radio':'100','col_span':'2','row_span':'1'},
            {'item_seq':'3','row_seq':'2','col_seq':'2','col_width':'33','col_aspect_radio':'100','col_span':'2','row_span':'1'},
            {'item_seq':'4','row_seq':'3','col_seq':'1','col_width':'33','col_aspect_radio':'100','col_span':'2','row_span':'1'},
            {'item_seq':'5','row_seq':'3','col_seq':'2','col_width':'33','col_aspect_radio':'100','col_span':'2','row_span':'1'},
            {'item_seq':'6','row_seq':'3','col_seq':'3','col_width':'33','col_aspect_radio':'100','col_span':'2','row_span':'1'},]


    temsql =  f'''INSERT INTO `lm_template` (`tem_status`, `tem_name`, `tem_desc`, `tem_create_time`, `tem_update_time`) 
    VALUES (1, '{tem_name}', '{tem_desc}', now(), now());'''
    temres = insertSQL(temsql)
    tem_id = temres['lastId']

    for item in items:
        itemsql = f'''INSERT INTO `lm_tem_item` ( `tem_id`, `item_seq`, `row_seq`, `col_seq`, `col_width`, `col_aspect_radio`, `col_span`, `row_span`) VALUES
                    ( '{tem_id}','{item["item_seq"]}', '{item["row_seq"]}', '{item["col_seq"]}', '{item["col_width"]}', '{item["col_aspect_radio"]}', '{item["col_span"]}', '{item["row_span"]}');'''
        itemres = insertSQL(itemsql)
        item_id = itemres['lastId']

        for ydid in ydids:
            inssql = f'''INSERT INTO `lm_tem_instance` ( `tem_id`, `pharmacy_id`, `effect_time`, `invalid_time`, `ins_priority`, `ins_rule`, `other_info`) VALUES
                    ( '{tem_id}', '{ydid}', '2020-07-01 00:00:00', '2028-01-01 23:59:59', 2, '', '药店新');'''
            insres = insertSQL(inssql)
            ins_id = insres['lastId']

    insSQL = f""" INSERT INTO `medstore`.`lm_tem_instance` ( `tem_id`, `pharmacy_id`, `effect_time`, `invalid_time`, `ins_priority`, `ins_rule`, `other_info`)
            SELECT `tem_id`,'{drugstoreId}' `pharmacy_id`, `effect_time`, `invalid_time`, `ins_priority`, `ins_rule`, `other_info`
            from lm_tem_instance WHERE pharmacy_id ={baseDrugstoreId};"""
    ins = insertSQL(insSQL)   
    teminsId = ins['lastId']
    temiteminsSQL = f""" INSERT INTO `medstore`.`lm_tem_item_ins` (  `tem_ins_id`, `tem_item_id`, `relation_object`, `relation_id`, `ins_desc`) 
                SELECT '{teminsId}' `tem_ins_id`, ii.`tem_item_id`, ii.`relation_object`,si.link_id+{iSmId} `relation_id`,ii.`ins_desc`
                from lm_tem_instance i 
                LEFT JOIN lm_tem_item_ins ii on i.tem_ins_id = ii.tem_ins_id 
                LEFT JOIN as_test.kd_sm_image_link si on ii.relation_id = si.old_link_id
                WHERE i.pharmacy_id ={baseDrugstoreId};"""
    insertSQL(temiteminsSQL)  
    
    # return res['lastId']
# 创建多盒商品 createCombByHuohao('1007150',1601,331474,490,490,count=5)
# 添加商品到amstatinfo 和 pmskudir中 ，根据货号和itemid addSkuDirByItemId(huohao,1600,1590)
# 给商品添加首单免费 下单返券 当日达 标签 buildSkuBaseByHuohao(huohao,1601,itemId=0,quotaId=0)
# 根据表 创建全套的活动 buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime,endTime,img='',color='')
# 根据表 创建sku createNewSkuByTable(tableName)
if __name__ == "__main__":
    
    baseDrugstoreId=1601
    baseDirCode='ykd21041002'

    drugstoreId =1602
    dirCode='ykd21041003'

    # drugstoreId =1603
    # dirCode='ykd21041004'

    iDirId = queryTableLastOne('pm_dir_info',field='dir_id',where =' dir_id<10000000')
    iSkuId = queryTableLastOne('pm_prod_sku',field='sku_id',where ='')
    iSmId = queryTableLastOne('sm_image_link',field='link_id',where ='')
    iPacketId = queryTableLastOne('pm_packet_info',field='packet_id',where ='')

    iActId = queryTableLastOne('am_act_info',field='act_id',where ='')
    iItemId = queryTableLastOne('am_act_item',field='item_id',where ='')
    iRangeId = queryTableLastOne('am_act_range',field='range_id',where ='')
    iDetailId = queryTableLastOne('am_item_details',field='details_id',where ='')
    iQuotaId = queryTableLastOne('am_quota_info',field='quota_id',where ='')
    iSgId = queryTableLastOne('am_stages_sale',field='sg_id',where ='')

    # logging.debug(iDirId,iSkuId)
    kd(drugstoreId,dirCode,iDirId,iSkuId,iActId,iItemId,iRangeId,iQuotaId,iDetailId,baseDrugstoreId,baseDirCode)
    # db.commit()


    # iDirId = 4681000
    # iSkuId = 25562000
    # iSmId = 7100
    # iPacketId = 14000
    # iActId = 240
    # iItemId= 1670
    # iRangeId = 3600
    # iDetailId = 1030
    # iQuotaId = 950
    # iSgId = 106000

    # baseDrugstoreId=1601
    # baseDirCode='ykd21041002'

    # drugstoreId =1602
    # dirCode='ykd21041003'

    
    

    # kd(drugstoreId,dirCode,iDirId,iSkuId,iActId,iItemId,iRangeId,iQuotaId,iDetailId,baseDrugstoreId,baseDirCode)


    # addAmStatInfoByDrugstoreId(drugstoreId)
    # copyStAnalysisCate(iDirId,baseDrugstoreId,drugstoreId)
    # db.commit()




    # iDirId = 4681000
    # iSkuId = 25562000
    # iSmId = 7100
    # iPacketId = 14000

    # iActId = 240
    # iItemId= 1670
    # iRangeId = 3600
    # iDetailId = 1030
    # iQuotaId = 950
    # iSgId = 106000





    # kdskudir(1602,'ykd21041003',4681000,25562000,baseDrugstoreId= 1601,baseDirCode='ykd21041002')

    # addPmPharmacyDir(1602,4681000,baseDrugstoreId= 1601)
    # 
    # copyOmDeliverFee(1602,1601)
    # copySmImageLink(drugstoreId,iSmId,iDirId,baseDrugstoreId)

    # copyLmTem(drugstoreId,iSmId,baseDrugstoreId)

    # copySmShareInfo(drugstoreId,baseDrugstoreId)
    # copySmUserBanner(drugstoreId,baseDrugstoreId)
    # copyPmPacketInfo(drugstoreId,iPacketId,iSkuId,baseDrugstoreId)
    # copyPmPacketSku(drugstoreId,iPacketId,iSkuId,baseDrugstoreId)

    # copyPmSkuSale(drugstoreId,iSkuId,baseDrugstoreId)
    # # 首单免费
    # copyAmStatInfoBaseByItemId('1350',drugstoreId)
    # # 下单返券
    # copyAmStatInfoBaseByItemId('1517',drugstoreId)
    # #30分钟送达
    # copyAmskuImage(drugstoreId,img='http://image.ykd365.cn/icon/home/30minbd.png',radio='393',title='30分钟送达')

    

    # try:
        # copyAmActInfo(iActId,drugstoreId,baseDrugstoreId)
        # copyAmActItem(iItemId,iActId,drugstoreId)
        # copyAmActRange(iRangeId,iDirId)
        # copyAmActItemRange(iRangeId,iItemId)
        # copyAmItemDetails(iDetailId,iItemId)
        # copyAmDetailsRule(iDetailId)
        # copyAmQuotaInfo(iItemId,iQuotaId)
        # copyAmStockLimit(iSkuId,iItemId,iQuotaId)
        # copyAmStockPday(iSkuId,iActId,iItemId,iQuotaId,drugstoreId)
        # copyAmStagesSale(iSgId,iActId,iItemId,iQuotaId,drugstoreId)
        # copyAmStagesSaleDetail(iSgId,iDirId,iActId,iItemId,iQuotaId,drugstoreId)
    #     db.commit()
    # except Exception as identifier:
    #         logging.debug('报错啦---- %s',identifier)
    #         db.rollback()
    # iDirId = 4683000
    # iSkuId = 25566000
    # iSmId = 7200
    # iPacketId = 14000
    # drugstoreId =1603
    # baseDrugstoreId=1601
 
    # huohao = '1007186'
    # proId = '331502'
    # createCombByHuohao(huohao,1600,proId,1000,1000,count=5)
    # createCombByHuohao(huohao,1601,proId,1000,1000,count=5)
