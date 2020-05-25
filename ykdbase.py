from db2 import db,cursor,querySQL,updateSQL,insertSQL,selectBy,selectOneBy
import time
import datetime
import logging
# from actclass import ActManager
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
    createComb(baseSkuId,combProdId,fee,price,count=count)

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

def addNewSkuWithPre(huohao,preHuohao,drugstoreId):
    '''创建聚划算和秒杀的商品sku，根据base——huohao来确认商品，然后复制一个富裕新huohao
    '''
    
    sql1 = f'''
            INSERT INTO `medstore`.`pm_prod_sku` (  `prod_id`, `sku_status`, `sku_price`, `sku_fee`, `drugstore_id`, `brand_id`, `sku_update_time`, `sku_create_time`, `sku_remark`, `sku_logistics`, `prod_name`, `pharmacy_huohao`, `source_id`, `sku_json`, `sku_attr`, `sku_img`, `sku_sum`, `sku_activate`, `sales_info`, `sku_sum_flag`, `sku_hot_order`, `sku_sort`, `sku_rank`, `sku_type`, `is_set`, `set_num`, `dis_before_price`, `dis_after_price`, `discount_price`, `pre_prod_name`)
            SELECT  s.`prod_id`, `sku_status`, `sku_price`, `sku_fee`, `drugstore_id`, `brand_id`,NOW() `sku_update_time`,NOW() `sku_create_time`, `sku_remark`, `sku_logistics`, `prod_name`
            ,'{preHuohao}{huohao}' `pharmacy_huohao`, `source_id`, `sku_json`, `sku_attr`, `sku_img`, `sku_sum`, `sku_activate`, `sales_info`, `sku_sum_flag`, `sku_hot_order`, `sku_sort`, `sku_rank`, `sku_type`, `is_set`, `set_num`, `dis_before_price`, `dis_after_price`, `discount_price`, `pre_prod_name` 
            from pm_prod_sku s
            WHERE  s.pharmacy_huohao = '{huohao}'
            and s.drugstore_id = {drugstoreId};
        '''
    res = insertSQL(sql1)

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
def xrzq2():
    '''新版新人专区 有会场  分楼层 '''
    ydList = [1600,1601]
    startTime='2020-04-09'
    endTime='2020-12-31'
    tableName ='as_test.202004_xc_xr'

    actIds = [233,234]
    actName = '欣臣4月新人专区'

    img = 'http://image.ykd365.cn/act/202004/01.jpg'
    color = '#ff6a6c'
    # for drugstoreId in ydList:
    for index in range(len(ydList)):
        drugstoreId = ydList[index]
        actId = actIds[index]
        addNewSku4JHSMS(tableName,'xr',drugstoreId)
        addPmActSale(tableName,drugstoreId,startTime,endTime)
        db.commit()
        buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color)

def test():
    logging.info('test---------')
# 创建多盒商品 createCombByHuohao('1007150',1601,331474,490,490,count=5)
# 添加商品到amstatinfo 和 pmskudir中 ，根据货号和itemid addSkuDirByItemId(huohao,1600,1590)
# 给商品添加首单免费 下单返券 当日达 标签 buildSkuBaseByHuohao(huohao,1601,itemId=0,quotaId=0)
# 根据表 创建全套的活动 buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime,endTime,img='',color='')
# 根据表 创建sku createNewSkuByTable(tableName)
# 根据货号 查skuid querySkuId(huohao,drugstoreId)
if __name__ == "__main__":
    huohao = '06100344'
    ydId = 200
    dirId= '1002763460'
    dirCode='1000act226qxs'
    order =10
    buildSkuBaseByHuohao(huohao,ydId,skuImage='30分钟')
    skuId = querySkuId(huohao,ydId)
    addPmSkuDir(skuId,dirId,dirCode,order=order)

    # dirList =  queryTable('pm_dir_info',result='*',where =f'pharmacy_id={ydId} and dir_code like "%act228dkz" limit 1')
    # for dir in dirList:
    #     logging.debug(dir)
    #     dirId = dir['dir_id']
    #     dirCode = dir['dir_code']
    #     order = i+110
    #     addPmSkuDir(skuId,dirId,dirCode,order=order)

    # huohao = '1007268'
    # yds = [1600,1601]
    # for ydId in yds:
        # createCombByHuohao(huohao,ydId,331514,1000,1000,count=5)
        # addNewSkuWithPre('5件装'+huohao,'xr',ydId)

    # huohaos = [1007256,
    #             1007234,
    #             1007251,
    #             1007260,
    #             1007268,
    #             '5件装1007268',
    #             'xr5件装1007268'
    #             ]
    # # huohaos = ['xr5件装1007268']
    # yds = [1600,1601]
    # for ydId in yds:
    #     for huohao in huohaos:
    #         buildSkuBaseByHuohao(huohao,ydId,skuImage='30分钟')

    # huohaos = [1007256,
    #             1007234,
    #             1007251,
    #             1007260,
    #             '5件装1007268'
    #             ]
    # # huohaos = ['xr5件装1007268']
    # yds = [1600,1601]
    # for ydId in yds:
    #     # for huohao in huohaos:
    #     for i in range(len(huohaos)):
    #         huohao = huohaos[i]
    #         # buildSkuBaseByHuohao(huohao,ydId,skuImage='30分钟')
    #         skuId = querySkuId(huohao,ydId)
    #         dirList =  queryTable('pm_dir_info',result='*',where =f'pharmacy_id={ydId} and dir_code like "%act228dkz"')
    #         for dir in dirList:
    #             logging.debug(dir)
    #             dirId = dir['dir_id']
    #             dirCode = dir['dir_code']
    #             order = i+110
    #             addPmSkuDir(skuId,dirId,dirCode,order=order)
    # db.commit()



    # huohaos = ['xr5件装1007268']
    # yds = [1600,1601]
    # for ydId in yds:
    #     # for huohao in huohaos:
    #     for i in range(len(huohaos)):
    #         huohao = huohaos[i]
    #         # buildSkuBaseByHuohao(huohao,ydId,skuImage='30分钟')
    #         skuId = querySkuId(huohao,ydId)
    #         dirList =  queryTable('pm_dir_info',result='*',where =f'pharmacy_id={ydId} and dir_code like "%yxtj"')
    #         for dir in dirList:
    #             logging.debug(dir)
    #             dirId = dir['dir_id']
    #             dirCode = dir['dir_code']
    #             order = 9
    #             addPmSkuDir(skuId,dirId,dirCode,order=order)
    # db.commit()

    # huohao = 'xr5件装1007268'
    # # yds = [1600,1601]
    # # for ydId in yds:
    # addSkuDirByItemId(huohao,1600,1660)
    # addSkuDirByItemId(huohao,1601,1661)
    # db.commit()

    # huohaos = ['xr5件装1007268']
    # yds = [1600,1601]
    # for ydId in yds:
    #     # for huohao in huohaos:
    #     for i in range(len(huohaos)):
    #         huohao = huohaos[i]
    #         # buildSkuBaseByHuohao(huohao,ydId,skuImage='30分钟')
    #         skuId = querySkuId(huohao,ydId)
    #         dirList =  queryTable('pm_dir_info',result='*',where =f'  dir_code like "%233quan"')
    #         for dir in dirList:
    #             logging.debug(dir)
    #             dirId = dir['dir_id']
    #             dirCode = dir['dir_code']
    #             order = 9
    #             addPmSkuDir(skuId,dirId,dirCode,order=order)
    # db.commit()


    # huohao = '18102374'
    # buildSkuBaseByHuohao(huohao,200,skuImage='30分钟')
    # xrzq2()
    # createCombByHuohao('1007223',1600,331506,14500,1450,count=5)
    # createCombByHuohao('1007223',1601,331506,14500,1450,count=5)    

#     iDirId = 4681000
#     iSkuId = 25562000
#     iSmId = 7100
#     drugstoreId =1602
#     baseDrugstoreId=1601
    # kdskudir(1602,'ykd21041003',4681000,25562000,baseDrugstoreId= 1601,baseDirCode='ykd21041002')

    # addPmPharmacyDir(1602,4681000,baseDrugstoreId= 1601)
    # 
    # copyOmDeliverFee(1602,1601)
    # copySmImageLink(drugstoreId,iSmId,iDirId,baseDrugstoreId)

    # copyLmTem(drugstoreId,iSmId,baseDrugstoreId)

    # copySmShareInfo(drugstoreId,baseDrugstoreId)
    # copySmUserBanner(drugstoreId,baseDrugstoreId)

    # db.commit()

    # iDirId = 4683000
    # iSkuId = 25566000
    # iSmId = 7200
    # drugstoreId =1603
    # baseDrugstoreId=1601
    # baseDrugstoreId=1601
    # huohao = '1007186'
    # proId = '331502'
    # createCombByHuohao(huohao,1600,proId,1000,1000,count=5)
    # createCombByHuohao(huohao,1601,proId,1000,1000,count=5)


    # huohao = '5件装1007186'
    # addSkuDirByItemId(huohao,1600,1633) # 限购一个 
    # addSkuDirByItemId(huohao,1601,1634)

    # buildSkuBaseByHuohao(huohao,1600)
    # buildSkuBaseByHuohao(huohao,1601)

    # huohao2 = '1007186'
    # addSkuDirByItemId(huohao2,1600,1633) # 限购一个 
    # addSkuDirByItemId(huohao2,1601,1634)

    # logging.info('-----main---------------')
    # huohaos=[18102372,18102373]
    # drugstoreId=200
    # for huohao in huohaos:
    #     buildSkuBaseByHuohao(huohao,drugstoreId,skuImage='30分钟',limitquan=True)
 
    # huohao = '1007172'
    # createCombByHuohao(huohao,1600,331488,1000,1000,count=5)
    # createCombByHuohao(huohao,1601,331488,1000,1000,count=5)
    # huohao = '5件装1007172'
    # # buildSkuBaseByHuohao(huohao,1600,itemId=0,quotaId=0)
    # # buildSkuBaseByHuohao(huohao,1601,itemId=0,quotaId=0)

    # addSkuDirByItemId(huohao,1600,1631,skuTotal=0,maxTotal=1)
    # addSkuDirByItemId(huohao,1601,1632,skuTotal=0,maxTotal=1)
    # db.commit()
 
    # tableName = 'as_test.20032_xc_sku'
    # createNewSkuByTable(tableName)
    # list= queryTable(tableName)
    # for dic in list:
    #     huohao = dic['huohao']
    #     drugstoreId= dic['drugstore_id']
    #     buildSkuBaseByHuohao(huohao,drugstoreId)
    # 以上 创建了sku 并且添加了 首单免费 下单返券 当日送达

    # huohao = '1007160'
    # buildSkuBaseByHuohao(huohao,1600)
    # buildSkuBaseByHuohao(huohao,1601)

    # huohao = '1007172'
    # proId = '331488'
    # ydIds = [1600,1601]
    # itemIds = {'1600':'1631','1601':'1632'}
    # # dirIds = {'1600':'1631','1601':'1632'}
    # fee= 1000
    # price = 1000
    # count = 5
    # for ydId in ydIds:
    #     createCombByHuohao(huohao,ydId,proId,fee,price,count=count)
    #     buildSkuBaseByHuohao(huohao,ydId)
    #     addSkuDirByItemId(huohao,ydId,itemIds[ydId])

        # addPmSkuDir(skuId,dirId,dirCode)

    # querySkuId
    # dirIds =[1002763471
    # tableName = 'as_test.20032_xc_lcz_323'
    # startTime='2020-03-23'
    # endTime='2020-12-31'
    # buildActInfoByTable(tableName,'222','',1600,startTime,endTime,img='',color='')
    # buildActInfoByTable(tableName,'223','',1601,startTime,endTime,img='',color='')

    # addSkuDirByItemId(huohao,1600,1590)
    # addSkuDirByItemId(huohao,1600,1592)

    # xrzq()
    

    # tableName = 'as_test.20032_xc_sku'
    # createNewSkuByTable(tableName)
    # list= queryTable(tableName)
    # for dic in list:
    #     huohao = dic['huohao']
    #     drugstoreId= dic['drugstore_id']
    #     buildSkuBaseByHuohao(huohao,drugstoreId,itemId=0,quotaId=0)
    # 以上 创建了sku 并且添加了 首单免费 下单返券 当日送达

#fec2b9

    # ydList = [ 1620,
    #     1621,
    #     1622,
    #     1627,
    #     1629,
    #     1631]
    # startTime='2020-03-18'
    # endTime='2020-12-31'
    # tableName ='as_test.20031_bj_jhs'
    # for drugstoreId in ydList:
    #     addNewSku4JHSMS(tableName,'3JHS',drugstoreId)
    #     addPmActSale(tableName,drugstoreId,startTime,endTime)
    #     # db.commit()
    #     buildActInfoByTable(tableName,'230','北京3月聚划算',drugstoreId,startTime=startTime,endTime=endTime,img='http://image.ykd365.cn/act/1907/jhs_01.jpeg',color='#0090ff')
# buildxxx(1605,1600)
# buildxxx(1606,1601)

# addXXX('5件装1007150','1600','1598',skuTotal=200,maxTotal=1000) # 每人每7天限购1个 的itemid
# addXXX('5件装1007150','1601','1599',skuTotal=200,maxTotal=1000) # 每人每7天限购1个
 


 