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

# Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0


# 写入excel
# 参数对应 行, 列, 值
# worksheet.write(1,0, label = 'this is test')

# logger = logging.getLogger()
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename='my-426.log', level=logging.DEBUG, format=LOG_FORMAT)
# #  创建一个handler，用于将日志输出到控制台
# # log = logging.StreamHandler()
# # log.setLevel(logging.DEBUG)
# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)
# logger.addHandler(ch)
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
    item_img_r=''
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



def queryTable(tableName,result='*',where ='',order=''):
    '''基础查询表内容
    返回数组结构 []'''
    # worksheet = workbook.add_sheet(tableName)
    if where !='':
        where  = ' where '+where
    if order !='':
        order  = ' order by '+order 
    sql =  f'''select {result} from {tableName} {where} {order} ''' #'''select {} from {} {} '''.format(result,tableName,where)
    res =querySQL(sql)

    if res['code']==200:
        list = res['data']
        # for i in range(len(list)):
        #     dic = list[i]
        #     # logging.info(dic)
        #     j=0
        #     if i==0:
                
        #         for k,v in  dic.items():
        #             # logging.info(k)
        #         #     # logging.info(j,dic[j])
        #             worksheet.write(i,j, label = k)
        #             j=j+1
        #         # keyList = dic.items()
        #         # logging.info(keyList)
        #         # for j in range(len(keyList)):
        #         #     logging.info(j)
        #             # logging.info(keyList[j])
        #             # worksheet.write(i,j, label = keyList[j])
        #     else:
        #        for k,v in  dic.items():
        #             # logging.info(k)
        #         #     # logging.info(j,dic[j])
        #             worksheet.write(i,j, label = v)
        #             j=j+1
        #     # for (key,value) in dic:
        #     #     worksheet.write(i,0, label = 'this is test')
        # workbook.save('检查.xls')
        # logging.info('输入到检查.xls over')
        return res['data']
    else:
        return []


def checkTable(tableName,result='*',where ='',order=''):
    '''基础查询表内容
    返回数组结构 []'''
    worksheet = workbook.add_sheet(tableName)
    style = xlwt.XFStyle()
    style.num_format_str = 'M/D/YY h:mm:ss'
    if where !='':
        where  = ' where '+where
    if order !='':
        order  = ' order by '+order 
    sql =  f'''select {result} from {tableName} {where} {order} ''' #'''select {} from {} {} '''.format(result,tableName,where)
    res =querySQL(sql)

    if res['code']==200:
        list = res['data']
        for i in range(len(list)):
            dic = list[i]
            # logging.info(dic)
            j=0
            if i==0:
                for k,v in  dic.items():
                    worksheet.write(i,j, label = k)
                    j=j+1
            else:
               for k,v in  dic.items():
                    # logging.info(k)
                #     # logging.info(j,dic[j])
                    worksheet.write(i,j, label = v)
                    j=j+1
            # for (key,value) in dic:
            #     worksheet.write(i,0, label = 'this is test')
        today = time.strftime("%Y%m%d%H%M%S", time.localtime())  # (datetime.datetime.strptime(day,'%Y-%m-%d')+datetime.timedelta(days=i+1)).strftime('%Y-%m-%d')
        workbook.save(f'{today}.xls')

        logging.info(f'{today}.xls')
        return res['data']
    else:
        return []

def queryTableLastOne(tableName,field='*',where ='',order=''):
    '''基础查询表内容
    返回字典结构 {}'''
    if where !='':
        where  = ' where '+where
    if order !='':
        order  = ' order by '+order 
    sql = f'''select {field} from {tableName} {where} {order}  limit 1'''
    res =selectOneBy(sql)
    return res

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

def addPmDirInfo(sufDirCode,dirName,drugstoreId,img='',color='',num='1',level='1',parentDirId='',dirId='',):
    logging.debug('根据提供的盘货信息，创建展示目录 dir ')
    genCode = queryBaseDirCode(drugstoreId)
    dirCode = genCode+sufDirCode
    if dirId=='':
        sql = f'''
            INSERT INTO `medstore`.`pm_dir_info` (  `dir_code`, `dir_name`, `dir_type`, `dir_status`
            , `dir_revalue`, `prod_sum`, `dir_num`, `dir_level`, `dir_img`, `parent_dir_id`, `dir_update_time`
            , `dir_create_time`, `dir_remark`, `dir_all_name`, `category_id`, `pharmacy_id`, `dir_gotocata`, `dir_main_show`)
            value ('{dirCode}','{dirName}','dir','1',NULL,100,'{num}',{level},'{img}','{parentDirId}',NOW(),NOW(),'{color}','',NULL,'{drugstoreId}',NULL,NULL) ;
        '''
    else:
        sql = f'''
            INSERT INTO `medstore`.`pm_dir_info` ( dir_id, `dir_code`, `dir_name`, `dir_type`, `dir_status`
            , `dir_revalue`, `prod_sum`, `dir_num`, `dir_level`, `dir_img`, `parent_dir_id`, `dir_update_time`
            , `dir_create_time`, `dir_remark`, `dir_all_name`, `category_id`, `pharmacy_id`, `dir_gotocata`, `dir_main_show`)
            value ('{dirId}','{dirCode}','{dirName}','dir','1',NULL,100,'{num}',{level},'{img}','{parentDirId}',NOW(),NOW(),'{color}','',NULL,'{drugstoreId}',NULL,NULL) ;
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
    '''创建活动价格 fee price  ,只要 price 不是null 不等于0 就会取 fee 和price的数值 *100
    '''
    # for drugstoreId in self.drugstoreIdList:
    sql1 = '''
            INSERT INTO `medstore`.`pm_sku_sale` ( `sku_id`, `sale_fee`, `sale_price`, `sale_start_time`, `sale_end_time`, `sale_status`, `sale_create_time`, `sale_update_time`, `sale_remark`) 
            SELECT s.`sku_id`,a.fee*100 `sale_fee`,a.price*100 `sale_price`
            ,'{}' `sale_start_time`,'{}' `sale_end_time`
            ,0 `sale_status`,NOW() `sale_create_time`,NOW() `sale_update_time`,'' `sale_remark` 
            from {} a,pm_prod_sku s
            WHERE a.huohao = s.pharmacy_huohao
            and s.drugstore_id = {} and a.price is not null  and a.price !=0
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
def addAmActItem(itemName,itemDesc,itemType,actId,drugstoreId,img='',imgR='',flag=''):
        '''创建 range item   通过目录id来创建
        '''
        # itemName = dic['item_name']
        # itemDesc = dic['item_desc']
        # itemType = dic['item_type']
        if imgR!='':
            imgR = f'{{"itemImageR":"{imgR}"}}'
        sql = f'''
            INSERT INTO `medstore`.`am_act_item` ( `item_attr`, `item_name`, `act_id`
            , `item_status`, `item_priority`, `item_type`, `item_desc`, `item_update_time`
            , `item_create_time`, `item_remark`, `item_img`, `pharmacy_id`, `item_flag`
            , `sales_goto_type`, `sales_goto_title`, `sales_goto_url`, `item_num`, `item_title`
            , `activity_img`, `activity_img_ratio`)
            VALUES ('single', '{itemName}', '{actId}', '1', '90', '{itemType}','{itemDesc}', NOW(), NOW()
            ,'{imgR}', '{img}', '{drugstoreId}', '{flag}', '', '', '', '0', '', '', '')
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

def addAmItemDetails( itemId,details_value,details_remark,details_content,details_type='discount',details_level=1):
        '''创建am_item_details
        '''
        sql = f'''
            INSERT INTO `medstore`.`am_item_details` (  `details_level`, `item_id`, `details_type`
            , `details_val_type`, `details_value`, `details_update_time`, `details_create_time`
            , `details_remark`, `details_content`) 
            VALUES ( '{details_level}', '{itemId}', '{details_type}', 'rate', '{details_value}', now(), now(), '{details_remark}', '{details_content}');
        '''
        res = insertSQL(sql)
        return res['lastId']

def addAmDetailsRule(detailsId,rule_value):
        ''' am_details_rule
        '''
        rulesql = f'''
           SELECT * from am_act_rule where rule_value = '>={rule_value}';
        '''
        rule = selectOneBy(rulesql)
        ruleId = rule["rule_id"]
        sql = f'''
            INSERT INTO `medstore`.`am_details_rule` (  `details_id`, `rule_id`) 
            VALUES (  '{detailsId}', '{ruleId}');
        '''
        res = insertSQL(sql)
        return res['lastId']

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

def stopPacket(tableName,drugstoreId,where = '1=1',stop=0):
    """下架疗程购 也就是将多盒商品下架"""
    sql = f""" UPDATE {tableName} a ,pm_packet_sku b,pm_prod_sku c  ,pm_prod_sku cd
            set cd.sku_status = {stop}
            WHERE  a.huohao = c.pharmacy_huohao
            and c.drugstore_id = {drugstoreId}
            and b.sku_id = c.sku_id and b.packet_sku_id = cd.sku_id
            and {where} ;
            """
    res = updateSQL(sql)

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

# 添加list列表页左侧图片的角标 label_type 1左上 2 右下 0居中
def addPmLabelImage(name,image,type,drugstoreId,skuId='',skuIdList=[]):
    if skuId=='' and len(skuIdList) ==0:
        return ''
    sql = '''
        INSERT INTO `medstore`.`pm_label_image` (  `label_name`, `label_url`, `label_url_double`, `label_type`, `label_status`, `label_create_time`, `label_update_time`, `pharmacy_id`, `label_flag`, `sku_id`)
        VALUES 
    '''
    if len(skuIdList) >0:
        for tskuId in skuIdList:
            # sql = sql+" (  '"+name+"', '"+image+"', '"+image+"', '"+type+"', '1', now(),now(), '"+drugstoreId+"', '0', '"+tskuId+"'),"
            sql = " {} (  '{}', '{}', '{}', '{}', '1', now(),now(), '{}', '0', '{}'),".format(sql,name,image,image,type,drugstoreId,tskuId)
        sql = sql[:-1]   
    elif  skuId!='':
        sql = " {} (  '{}', '{}', '{}', '{}', '1', now(),now(), '{}', '0', '{}');".format(sql,name,image,image,type,drugstoreId,skuId)
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

def addSmImageLink(drugstoreId,index,img,url,name,dirId,start,end,link_view):
    sql = f'''
        INSERT INTO `medstore`.`sm_image_link` (  `drugstore_id`, `seq_num`, `image_url`, `link_url`, `link_type`, `link_name`, `link_param`, `link_status`, `link_update_time`, `link_create_time`, `link_remark`, `link_start_time`, `link_end_time`, `link_view`, `link_version`)
        VALUES (  '{drugstoreId}', '{index}', '{img}', '{url}{dirId}', 'url', '{name}', '{dirId}', '1', now(), now(), '', '{start} 00:00:00', '{end} 23:59:59', '{link_view}', '1');
        '''
    res = insertSQL(sql)
    logging.info(f"创建sm_image_link类型为 {link_view} 的{name} 活动 , dirId= {dirId} ,url={url}{dirId},药店:{drugstoreId} ")
    return res['lastId']

def addSmImageLinkWindow(drugstoreId,index,img,url,name,dirId,start,end,type='everyday'):
    sql = f'''
    INSERT INTO `medstore`.`sm_image_link_window` (  `drugstore_id`, `seq_num`, `image_url`, `window_url`, `window_type`
    , `window_name`, `window_param`, `window_status`, `window_update_time`, `window_create_time`
    , `window_remark`, `window_start_time`, `window_end_time`, `window_view`, `window_go_type`) 
    VALUES (  '{drugstoreId}', '{index}', '{img}', '{url}{dirId}', '{type}', '{name}', '{dirId}', '1', now(), now(), '', '{start} 00:00:00', '{end} 23:59:59', '', '0');
        '''
    res = insertSQL(sql)
    logging.info(f"创建sm_image_link_window  的{name} 活动 , dirId= {dirId} ,url={url}{dirId},药店:{drugstoreId} ")
    return res['lastId']

def updateAllEnssence(drugstoreId,image):
    '# 修改九宫格的大图'
    sql = f'''
     UPDATE sm_image_link set image_url = '{image}' 
        WHERE drugstore_id = {drugstoreId}
        and link_status=1
        and link_view = 'all_essence'
        ORDER BY link_id desc   '''
    res = insertSQL(sql)
    logging.info(f"修改sm_image_link类型为all_essence  的九宫格大图 药店:{drugstoreId}，图片{image} ")
    return res['lastId']

def updateEnssence(drugstoreId,part,start,end,toDirName='夏至·春未央'):
    '''修改九宫格中某个位置的链接,和开始结束时间'''
    sql=f'''UPDATE lm_tem_instance a LEFT JOIN lm_tem_item_ins b on a.tem_ins_id = b.tem_ins_id 
        LEFT JOIN sm_image_link c on b.relation_id = c.link_id 
        LEFT JOIN sm_image_link c2 on c.drugstore_id = c2.drugstore_id
        set c.link_remark = c.link_url, c.link_url =  c2.link_url,c.link_name=c2.link_name ,c.link_start_time='{start}',c.link_end_time='{end}'
        WHERE pharmacy_id = {drugstoreId} and tem_id = 7 and c2.link_name = '{toDirName}' and c2.link_view = ''
        and ins_desc = {part};'''
    res = insertSQL(sql)
    logging.info(f"修改sm_image_link类型为 essence 的九宫格 第 {part}格链接, 药店:{drugstoreId}，开始{start}-结束{end} ")
    return res['lastId']
        
def createCombByHuohao(huohao,drugstoreId,combProdId,fee,price,count=1):
    skusql = f"select * from pm_prod_sku where pharmacy_huohao = {huohao} and drugstore_id= {drugstoreId}"
    skures = selectOneBy(skusql)
    logging.info(skures)
    baseSkuId = skures['sku_id']
    createComb(baseSkuId,combProdId,fee,price,count=count)

# def updateSmImageLink(drugstoreId,index,img,url,name,dirId,start,end,link_view):
#     sql = f'''
#     update sm_image_link set 
#         INSERT INTO `medstore`.`sm_image_link` (  `drugstore_id`, `seq_num`, `image_url`, `link_url`, `link_type`, `link_name`, `link_param`, `link_status`, `link_update_time`, `link_create_time`, `link_remark`, `link_start_time`, `link_end_time`, `link_view`, `link_version`)
#         VALUES (  '{drugstoreId}', '{index}', '{img}', '{url}{dirId}', 'url', '{name}', '{dirId}', '1', now(), now(), '', '{start} 00:00:00', '{end} 23:59:59', '{link_view}', '1');
#         '''
#     res = insertSQL(sql)
#     logging.info(f"创建sm_image_link类型为 %s 的{name} 活动 , dirId= %s ,url={url}{dirId},药店:{drugstoreId} ")
#     return res['lastId']
# def changeDic2ActInfo(parameter_list):
#     pass

def updateActTable(tableName,set='1=1',where='1=1'):
    sql = f'''update {tableName} set {set} WHERE {where}'''
    res = updateSQL(sql)

def buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime,endTime,img='',color='',linkurl='',linkimg='',linkView = '',windowimg=''):
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
        如果会场需要有楼层跳转到某个链接或者目录。，需要预先创建好子级dirinfo，然后再创建主页面dirinfo，【把子页面的dir_code 设置为主页面对应楼层的dircode*2 ，ps:主 abc, 子  abcabc】
    'dir','actskudir','skudir','item','range','itemrange','quota','stock','stock-pday','ms-sale','ms-packet'"""
    # try:
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
        if linkurl!='' and linkimg!='':
            addSmImageLink(drugstoreId,1,linkimg,linkurl,actName,parentDirId,startTime,endTime,linkView)
        if linkurl!='' and windowimg!='':
            addSmImageLinkWindow(drugstoreId,1,windowimg,linkurl,actName,parentDirId,startTime,endTime)
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
        
        itemInfo = ActInfo(item)
        itemName = itemInfo.item_name
        itemDesc = itemInfo.item_desc
        itemType = itemInfo.item_type
        itemCode = itemInfo.item_code

        itemImg = itemInfo.item_img
        itemImgR = itemInfo.item_img_r
        otherImg = f'{{"itemImageR":"{itemImgR}","itemImage":"{itemImg}"}}' if itemImg!='' and itemImgR!='' else ''

        dirDic = addPmDirInfo(f'act{actId}{itemCode}',itemName,drugstoreId,level='3')
        idicInfo = ActInfo(dirDic)
        rangeId =addAmActRange( idicInfo.dir_id,itemName,itemDesc)
        itemId = addAmActItem(itemName,itemDesc,itemType,actId,drugstoreId,img=itemImg,imgR=itemImgR)
        addAmItemRange(itemId,rangeId)
        logging.info(f'创建 活动 item range dir    {itemId}  {rangeId}  {idicInfo.dir_id} {itemName}')
        quotaId= ''
        # logging.info(f'itemType-- -{itemType};details_value--{itemInfo.details_value}')
        if itemType=='quota':
            limit = itemInfo.limit
            if limit!='':
                limit_group = itemInfo.limit_group
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
                    details_level = details_value_list.index(details_value)
                    detailsId = addAmItemDetails( itemId,details_value,details_remark,details_content,details_type='discount',details_level=details_level)
                    
                    # logging.info(f'detailsId------------------------{detailsId}')
                    if detailsId!='' and rule_values !='':
                        rule_value_list = rule_values.split(',')
                        # for details_value in details_value_list:
                        rule_value = rule_value_list[details_value_list.index(details_value)]
                        addAmDetailsRule(detailsId,rule_value)
            # quotaId = addAmQuotaInfo( itemId,itemInfo.limit,itemDesc,itemInfo.limit_group)
            
        dicId = dirDic['dir_id']
        dicCode = dirDic['dir_code']
        sufdicCode = item['item_code']
        for sku in skuList:
            skuDicCodeId=sku['item_code']
            if skuDicCodeId==sufdicCode:
                skuId=sku['sku_id']
                addPmSkuDir(skuId,dicId,dicCode)
                if hasattr(item,'kc_day') and item.get('kc_day')!='':
                    skuTotal = item.get('kc_day',0)
                    days = item.get('days',0)
                    maxTotal = int(days)*int(skuTotal)
                    addAmStockLimit(skuId,itemId,quotaId,skuTotal,maxTotal,remark='')
                    addAmStockPday(skuId,actId,itemId,quotaId,drugstoreId,skuTotal,maxTotal,remark='')
                addAmStatInfo(skuId,actId,itemId,itemName,itemDesc,itemType,startTime,endTime,quotaId =quotaId,otherStr1=otherImg)
            # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)
                # logging.info(f'创建 addAmStatInfo')
    # db.commit()
    logging.info('创建成功')
    # except Exception as err:
    #     logging.error(err)
    #     db.rollback()

def createDirByTable(actId,drugstoreId,tableName='as_test.ykd_base_dir'):
    """根据所给 ykd_base_dir 创建活动目录"""
    idir = queryTableLastOne('pm_dir_info',field='dir_id',where ='',order='dir_id desc')
    idirId = idir['dir_id']
    dirList = queryTable(tableName,where=' act ="202006618" ')
    # logging.info(dirList)
    for dir in dirList:
        name = dir['name']
        code = dir['code']
        img = dir['img']
        num = dir['num']
        dirId = idirId+dirList.index(dir)+1
        parentId = '' if dir['parent_id']==None else  dir['parent_id']+idirId
        lvl = dir['lvl']
        toDirId = '' if dir['to_dir_id']== None else dir['to_dir_id']+idirId

        addPmDirInfo(f'act{actId}{code}',name,drugstoreId,img=img,color=toDirId,num=num,level=lvl,parentDirId=parentId,dirId=dirId)


def buildActInfoByTableWithChild(tableName,actId,actName,drugstoreId,startTime,endTime,img='',color='',linkurl='',linkimg='',linkView = '',windowimg=''):
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
        如果会场需要有楼层跳转到某个链接或者目录。，需要预先创建好子级dirinfo，然后再创建主页面dirinfo，【把子页面的dir_code 设置为主页面对应楼层的dircode*2 ，ps:主 abc, 子  abcabc】
    'dir','actskudir','skudir','item','range','itemrange','quota','stock','stock-pday','ms-sale','ms-packet'"""
    # try:
    addAmActInfo(actId,actName,startTime,endTime,drugstoreId=drugstoreId)
    skuList = querySkuIdByTable(tableName,drugstoreId)
    # dirList = queryTable(tableName,where=' dir_code !="" group by dir_code')
    dirList = queryTable('pm_dir_info',result='*',where =f' dir_code like "%act{actId}%" and pharmacy_id = "{drugstoreId}" ',order='')
    itemList = queryTable(tableName,where='  item_code !="" group by item_code')
    if len(dirList)>0 or len(itemList)>0:
        logging.info(f'开始创建活动目录 {drugstoreId}')
        # logging.error('开始创建活动目录error')
        # parentdirDic = addPmDirInfo(f'act{actId}',actName,drugstoreId,img=img,color=color,num='1',level='2',parentDirId='')
        parentdirDic = dirList[0]
        parentDirId = parentdirDic['dir_id']
        logging.info(f'创建zhu活动目录 {parentdirDic}')
        if linkurl!='' and linkimg!='':
            addSmImageLink(drugstoreId,1,linkimg,linkurl,actName,parentDirId,startTime,endTime,linkView)
        if linkurl!='' and windowimg!='':
            addSmImageLinkWindow(drugstoreId,1,windowimg,linkurl,actName,parentDirId,startTime,endTime)
    for dir in dirList:
        # logging.info(f'创建子目录 {dir}')
        # dirInfo = ActInfo(dir)
        # sufDirCode = dirInfo.dir_code
        # # logging.info(f'创建子活动目录 {dirInfo}')
        # genCode = queryBaseDirCode(drugstoreId)
        # sdirCode = f'{genCode}act{actId}{sufDirCode}{sufDirCode}'
        # sdir = queryTableLastOne('pm_dir_info','*',f"dir_code = '{sdirCode}'",'dir_id desc')
        # remark = ''
        # if sdir!=None:
        #     remark = sdir['dir_id']
        # dic = addPmDirInfo(f'act{actId}{dirInfo.dir_code}',dirInfo.dir_name,drugstoreId,img=dirInfo.dir_img,color=remark,num=dirInfo.dir_num,level='3',parentDirId=parentDirId)
        genCode = queryBaseDirCode(drugstoreId)
        dic = dir
        dicId = dic['dir_id']
        dicCode = dic['dir_code']
        # sufdicCode = dir['dir_code']
        logging.info(f'创建子会场目录 {dic}')
        for sku in skuList:
            # skuDicCodeId=sku['dir_code']
            pSkuDirCode =sku['dir_code']
            skuDicCodeId=f'{genCode}act{actId}{pSkuDirCode}'
            order = sku['xh']
            if skuDicCodeId==dicCode:
                skuId=sku['sku_id']
                addPmSkuDir(skuId,dicId,dicCode,order)
                
    for item in itemList:
        
        itemInfo = ActInfo(item)
        itemName = itemInfo.item_name
        itemDesc = itemInfo.item_desc
        itemType = itemInfo.item_type
        itemCode = itemInfo.item_code

        itemImg = itemInfo.item_img
        itemImgR = itemInfo.item_img_r
        otherImg = f'{{"itemImageR":"{itemImgR}","itemImage":"{itemImg}"}}' if itemImg!='' and itemImgR!='' else ''

        dirDic = addPmDirInfo(f'act{actId}{itemCode}',itemName,drugstoreId,level='3')
        idicInfo = ActInfo(dirDic)
        rangeId =addAmActRange( idicInfo.dir_id,itemName,itemDesc)
        itemId = addAmActItem(itemName,itemDesc,itemType,actId,drugstoreId,img=itemImg,imgR=itemImgR)
        addAmItemRange(itemId,rangeId)
        logging.info(f'创建 活动 item range dir    {itemId}  {rangeId}  {idicInfo.dir_id} {itemName}')
        quotaId= ''
        # logging.info(f'itemType-- -{itemType};details_value--{itemInfo.details_value}')
        if itemType=='quota':
            limit = itemInfo.limit
            if limit!='':
                limit_group = itemInfo.limit_group
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
                    details_level = details_value_list.index(details_value)
                    detailsId = addAmItemDetails( itemId,details_value,details_remark,details_content,details_type='discount',details_level=details_level)
                    
                    # logging.info(f'detailsId------------------------{detailsId}')
                    if detailsId!='' and rule_values !='':
                        rule_value_list = rule_values.split(',')
                        # for details_value in details_value_list:
                        rule_value = rule_value_list[details_value_list.index(details_value)]
                        addAmDetailsRule(detailsId,rule_value)
            # quotaId = addAmQuotaInfo( itemId,itemInfo.limit,itemDesc,itemInfo.limit_group)
            
        dicId = dirDic['dir_id']
        dicCode = dirDic['dir_code']
        sufdicCode = item['item_code']
        for sku in skuList:
            skuDicCodeId=sku['item_code']
            if skuDicCodeId==sufdicCode:
                skuId=sku['sku_id']
                addPmSkuDir(skuId,dicId,dicCode)
                if hasattr(item,'kc_day') and item.get('kc_day')!='':
                    skuTotal = item.get('kc_day',0)
                    days = item.get('days',0)
                    maxTotal = int(days)*int(skuTotal)
                    addAmStockLimit(skuId,itemId,quotaId,skuTotal,maxTotal,remark='')
                    addAmStockPday(skuId,actId,itemId,quotaId,drugstoreId,skuTotal,maxTotal,remark='')
                addAmStatInfo(skuId,actId,itemId,itemName,itemDesc,itemType,startTime,endTime,quotaId =quotaId,otherStr1=otherImg)
            # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)
                # logging.info(f'创建 addAmStatInfo')
    # db.commit()
    logging.info('创建成功')
    # except Exception as err:
    #     logging.error(err)
    #     db.rollback()
    
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

    itemRemark = dic.get('item_remark')
    otherImg = ''
    if itemRemark!=None:
        logging.info("itemRemark------------------")
        logging.info(itemRemark)
        if itemRemark!=None and itemRemark!='':
            dicRemark = json.loads(itemRemark)
            logging.info(dicRemark)
            itemImgR = dicRemark['itemImageR']
            itemImg = dic.get('item_img') 
            otherImg = f'{{"itemImageR":"{itemImgR}","itemImage":"{itemImg}"}}' if itemImg!='' and itemImgR!='' else ''
            logging.info(otherImg)
    res = addAmStatInfo(skuId,actId,itemId,itemName,itemDesc,itemType,startTime,endTime,quotaId =quotaId,otherStr1=otherImg)
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
    # copyAmStatInfoByHuohao( '1350',huohao,drugstoreId) 
    # logging.debug('首单免费')
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
    ydList = [200]
    startTime='2020-05-01'
    endTime='2020-05-17'
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
    # ydList = [1600,1601]
    ydList = [1602,1603]
    startTime='2020-04-09'
    endTime='2020-12-31'
    tableName ='as_test.202004_xc_xr'

    # actIds = [233,234]
    actIds = [275,276]
    actName = '欣臣4月新人专区'

    img = 'http://image.ykd365.cn/act/202004/01.jpg'
    color = '#ff6a6c'
    # for drugstoreId in ydList:
    
    try:
        for index in range(len(ydList)):
            drugstoreId = ydList[index]
            actId = actIds[index]
            addNewSku4JHSMS(tableName,'xr',drugstoreId)
            addPmActSale(tableName,drugstoreId,startTime,endTime)
            
            buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color)
            db.commit()
    except Exception as err:
        logging.error("Error %s for execute sql: %s" % (err, tableName))
        db.rollback()

def mqj(actName = '感恩母亲节',tableName ='as_test.202005_ty_mqj',ydList = [200],startTime='2020-05-01',endTime='2020-05-17',img = 'http://image.ykd365.cn/act/202005/mqj/02.jpg',color = '#e7e7e7'):
    ''' 五月母亲节活动'''
    # ydList = [200]
    # startTime='2020-05-01'
    # endTime='2020-05-17'
    # tableName ='as_test.202005_ty_mqj'

    # iAct = queryTableLastOne('am_act_info',field='act_id',where ='',order='act_id desc')
    # iActId = iAct['act_id']
    # actName = '感恩母亲节'

    # img = 'http://image.ykd365.cn/act/202005/mqj/02.jpg'
    # color = '#e7e7e7'
    # for drugstoreId in ydList:
    for index in range(len(ydList)):
        try:
            iAct = queryTableLastOne('am_act_info',field='act_id',where ='',order='act_id desc')
            iActId = iAct['act_id']
            drugstoreId = ydList[index]
            actId = iActId+1
            linkimg = 'http://image.ykd365.cn/act/202005/mqj/mqj_banner.jpg'
            linkurl = 'http://store.ykd365.com/medstore/actUserpage/muj_2005?pageSize=1000&dirId='
            linkView = ''
            windowimg= 'http://image.ykd365.cn/act/202005/mqj/mqj_tc.png'
            # 创建特价
            addPmActSale(tableName,drugstoreId,startTime,endTime)

            # 列表页走上角标志
            list =  querySkuIdByTable(  tableName,drugstoreId,where='1=1')
            logging.info(list)
            mqjskuIdList =[]
            lczskuIdList =[]
            for dic in list:
                list_logo = dic['list_logo']
                if list_logo =='感恩母亲节':
                    mqjskuIdList.append(dic['sku_id'])
                elif  list_logo =='疗程装':
                    lczskuIdList.append(dic['sku_id'])
            addPmLabelImage('母亲节','http://image.ykd365.cn/act/202005/mqj/mqj_logo.png','1',drugstoreId,skuIdList=mqjskuIdList)
            addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',drugstoreId,skuIdList=lczskuIdList)

            # 暂停疗程购
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=1')

            buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color,linkurl=linkurl,linkimg=linkimg,windowimg=windowimg)
        
            db.commit()
        except Exception as err:
            logging.error(err)
            db.rollback()
        
        # parentDirId = '1002763750'
        # addSmImageLink(drugstoreId,1,linkimg,linkurl,actName,parentDirId,startTime,endTime,linkView)
        # db.commit()

def xz(actId=0,actName = '感恩母亲节',tableName ='as_test.202005_ty_mqj',ydList = [200],startTime='2020-05-01',endTime='2020-05-17',img = 'http://image.ykd365.cn/act/202005/mqj/02.jpg',color = '#e7e7e7',linkimg = '',linkurl = '',linkView = '',windowimg= ''):
    ''' 夏至活动 '''
    if actId==0:
        iAct = queryTableLastOne('am_act_info',field='act_id',where ='',order='act_id desc')
        iActId = iAct['act_id']
        actId = iActId+1
    
    for index in range(len(ydList)):
        try:
            drugstoreId = ydList[index]
            # actId = iActId+1
            # linkimg = 'http://image.ykd365.cn/act/202005/xz/xz_banner.jpg'
            # linkurl = 'http://deve.ykd365.com/medstore/actUserpage/xiazhi_2005?dirId='
            # linkView = ''
            # windowimg= 'http://image.ykd365.cn/act/202005/xz/xz_tc.png'
            # 创建特价
            addPmActSale(tableName,drugstoreId,startTime,endTime)
            logging.info('创建价格------------')
            # # 列表页走上角标志
            list =  querySkuIdByTable(  tableName,drugstoreId,where='1=1')
            mqjskuIdList =[]
            lczskuIdList =[]
            hjjkskuIdList =[]
            for dic in list:
                list_logo = dic['list_logo']
                if list_logo =='感恩母亲节':
                    mqjskuIdList.append(dic['sku_id'])
                elif  list_logo =='疗程装':
                    lczskuIdList.append(dic['sku_id'])
                elif  list_logo =='换季健康':
                    hjjkskuIdList.append(dic['sku_id'])
            addPmLabelImage('母亲节','http://image.ykd365.cn/act/202005/mqj/mqj_logo.png','1',drugstoreId,skuIdList=mqjskuIdList)
            addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',drugstoreId,skuIdList=lczskuIdList)
            addPmLabelImage('换季健康','http://image.ykd365.cn/act/202005/xz/xz_logo.png','1',drugstoreId,skuIdList=hjjkskuIdList)
            logging.info('创建list logo------------')
            # 暂停疗程购
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=1')
            stopPacket(tableName,drugstoreId,where = 'list_logo="疗程装"',stop=1)
            logging.info('暂停疗程购------------')
            
            buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color,linkurl=linkurl,linkimg=linkimg,windowimg=windowimg)
            db.commit()
        except Exception as err:
            logging.error(err)
            db.rollback()
    return actId
        # 除此之外还需要 修改九宫格的图片 链接 ，删除第二件半价和2件92折3件88折的冲突，延期2件92折3件88折的活动到五月底
        

def xyx(actId=0,actName = '家庭必备小药箱',tableName ='as_test.202005_ty_xyx',ydList = [200],startTime='2020-05-22',endTime='2020-06-15',img = 'http://image.ykd365.cn/act/202005/xyx/02.jpg',color = '#c4cde6',linkimg = '',linkurl = '',linkView = '',windowimg= ''):
    ''' 家庭必备小药箱爆款清单 '''
    if actId==0:
        iAct = queryTableLastOne('am_act_info',field='act_id',where ='',order='act_id desc')
        iActId = iAct['act_id']
        actId = iActId+1
    
    for index in range(len(ydList)):
        try:
            drugstoreId = ydList[index]
            # 创建特价
            addPmActSale(tableName,drugstoreId,startTime,endTime)
            logging.info('创建价格------------')
            # # 列表页左上角标志
            list =  querySkuIdByTable(  tableName,drugstoreId,where='1=1')
            mqjskuIdList =[]
            lczskuIdList =[]
            hjjkskuIdList =[]
            jtcbskuIDList= []
            for dic in list:
                list_logo = dic['list_logo']
                sku_id=dic['sku_id']
                if list_logo =='感恩母亲节':
                    mqjskuIdList.append(dic['sku_id'])
                elif  list_logo =='疗程装':
                    lczskuIdList.append(dic['sku_id'])
                elif  list_logo =='换季健康':
                    hjjkskuIdList.append(dic['sku_id'])
                elif  list_logo =='家庭常备':
                    jtcbskuIDList.append(dic['sku_id'])
                # 限券
                if 'is_xq' in dic.keys() and dic['is_xq']!=None and dic['is_xq']==1:
                    copyAmStatInfoBySkuId( 78,sku_id)
                # huohao =  dic['pharmacy_huohao']
                # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)

            addPmLabelImage('母亲节','http://image.ykd365.cn/act/202005/mqj/mqj_logo.png','1',drugstoreId,skuIdList=mqjskuIdList)
            addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',drugstoreId,skuIdList=lczskuIdList)
            addPmLabelImage('换季健康','http://image.ykd365.cn/act/202005/xz/xz_logo.png','1',drugstoreId,skuIdList=hjjkskuIdList)
            addPmLabelImage('家庭常备','http://image.ykd365.cn/act/202005/xyx/list_jtbb.png','1',drugstoreId,skuIdList=jtcbskuIDList)
            logging.info('创建list logo------------')
            # 暂停疗程购
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=1')
            stopPacket(tableName,drugstoreId,where = 'list_logo="疗程装"',stop=1)
            logging.info('暂停疗程购------------')
            
            
            buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color,linkurl=linkurl,linkimg=linkimg,windowimg=windowimg)
            db.commit()
        except Exception as err:
            logging.error(err)
            db.rollback()
    return actId
# SELECT aa.* from am_stat_info  a,am_stat_info aa 
# WHERE 
# a.sku_id= aa.sku_id
# and a.item_name = '第二件半价' 
# and aa.item_name = '2件92折、3件88折'
# ORDER BY stat_id DESC;


def build292388(actId=0,actName = '2件92折、3件88折',tableName ='as_test.',ydList = [],startTime='',endTime='',img = '',color = '',linkimg = '',linkurl = '',linkView = '',windowimg= ''):
    ''' 2件92折、3件88折 重新配置，下掉之前的所有 2件92折3件88折活动，重新建一份'''
    if actId==0:
        iAct = queryTableLastOne('am_act_info',field='act_id',where ='',order='act_id desc')
        iActId = iAct['act_id']
        actId = iActId+1
    
    for index in range(len(ydList)):
        try:
            drugstoreId = ydList[index]
            # 创建特价
            # addPmActSale(tableName,drugstoreId,startTime,endTime)
            # logging.info('创建价格------------')
            # # 列表页左上角标志
            list =  querySkuIdByTable(  tableName,drugstoreId,where='1=1')
            xjxxzskuIdList =[]
            lczskuIdList =[]
            # hjjkskuIdList =[]
            # jtcbskuIDList= []
            for dic in list:
                list_logo = dic['list_logo']
                sku_id=dic['sku_id']
                if list_logo =='2件92折、3件88折':
                    xjxxzskuIdList.append(dic['sku_id'])
                elif  list_logo =='疗程装':
                    lczskuIdList.append(dic['sku_id'])
                # elif  list_logo =='换季健康':
                #     hjjkskuIdList.append(dic['sku_id'])
                # elif  list_logo =='家庭常备':
                #     jtcbskuIDList.append(dic['sku_id'])
                # 限券
                if 'is_xq' in dic.keys() and dic['is_xq']!=None and dic['is_xq']==1:
                    copyAmStatInfoBySkuId( 78,sku_id)
                # huohao =  dic['pharmacy_huohao']
                # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)

            addPmLabelImage('2件92折、3件88折','http://image.ykd365.cn/act/2002/notouch/list88.png','1',drugstoreId,skuIdList=xjxxzskuIdList)
            addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',drugstoreId,skuIdList=lczskuIdList)
            # addPmLabelImage('换季健康','http://image.ykd365.cn/act/202005/xz/xz_logo.png','1',drugstoreId,skuIdList=hjjkskuIdList)
            # addPmLabelImage('家庭常备','http://image.ykd365.cn/act/202005/xyx/list_jtbb.png','1',drugstoreId,skuIdList=jtcbskuIDList)
            logging.info('创建list logo------------')
            # 暂停疗程购
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=1')
            stopPacket(tableName,drugstoreId,where = 'list_logo="疗程装"',stop=1)
            logging.info('暂停疗程购------------')
            
            
            buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color,linkurl=linkurl,linkimg=linkimg,windowimg=windowimg)
            db.commit()
        except Exception as err:
            logging.error(err)
            db.rollback()
    return actId
def act618(actId=0,actName = '',tableName ='',ydList = [],startTime='',endTime='',img = '',color = '',linkimg = '',linkurl = '',linkView = '',windowimg= ''):
    '''  '''
    if actId==0:
        iAct = queryTableLastOne('am_act_info',field='act_id',where ='',order='act_id desc')
        iActId = iAct['act_id']
        actId = iActId+1
        # iAct = queryTableLastOne('am_act_info',field='*',where ='',order='act_id desc')
        # iActId = iAct['act_id']+1
        logging.info(f'活动id：{actId}')
        # queryTableLastOne(tableName,field='*',where ='',order='')
        # buildActInfoByTableWithChild(tableName,actId,actName,drugstoreId,startTime,endTime,img='',color='',linkurl='',linkimg='',linkView = '',windowimg='')

    
    for index in range(len(ydList)):
        try:
            drugstoreId = ydList[index]
            createDirByTable(actId=actId,drugstoreId=drugstoreId)
            # 创建特价
            addPmActSale(tableName,drugstoreId,startTime,endTime)
            logging.info('创建价格------------')
            # # 列表页左上角标志
            list =  querySkuIdByTable(  tableName,drugstoreId,where='1=1')
            mqjskuIdList =[]
            lczskuIdList =[]
            hjjkskuIdList =[]
            jtcbskuIDList= []
            for dic in list:
                list_logo = dic['list_logo']
                sku_id=dic['sku_id']
                if list_logo =='感恩母亲节':
                    mqjskuIdList.append(dic['sku_id'])
                elif  list_logo =='疗程装':
                    lczskuIdList.append(dic['sku_id'])
                elif  list_logo =='换季健康':
                    hjjkskuIdList.append(dic['sku_id'])
                elif  list_logo =='家庭常备':
                    jtcbskuIDList.append(dic['sku_id'])
                # 限券
                if 'is_xq' in dic.keys() and dic['is_xq']!=None and dic['is_xq']==1:
                    copyAmStatInfoBySkuId( 78,sku_id)
                # huohao =  dic['pharmacy_huohao']
                # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)

            addPmLabelImage('母亲节','http://image.ykd365.cn/act/202005/mqj/mqj_logo.png','1',drugstoreId,skuIdList=mqjskuIdList)
            addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',drugstoreId,skuIdList=lczskuIdList)
            addPmLabelImage('换季健康','http://image.ykd365.cn/act/202005/xz/xz_logo.png','1',drugstoreId,skuIdList=hjjkskuIdList)
            addPmLabelImage('家庭常备','http://image.ykd365.cn/act/202005/xyx/list_jtbb.png','1',drugstoreId,skuIdList=jtcbskuIDList)
            logging.info('创建list logo------------')
            # 暂停疗程购
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=1')
            stopPacket(tableName,drugstoreId,where = 'list_logo="疗程装"',stop=1)
            logging.info('暂停疗程购------------')
            
            
            buildActInfoByTableWithChild(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color,linkurl=linkurl,linkimg=linkimg,windowimg=windowimg)
            db.commit()
        except Exception as err:
            logging.error(err)
            db.rollback()
    return actId

def update9GG():
    ydIds=[200,1600,1601,1620,
    1621,
    1622,
    1627,
    1629,
    1631]
    # images=[
    #     'http://image.ykd365.cn/act/202005/天一母亲节.jpg',
    #     'http://image.ykd365.cn/act/202005/欣臣母亲节.jpg','http://image.ykd365.cn/act/202005/欣臣母亲节.jpg',
    #     'http://image.ykd365.cn/act/202005/北京母亲节.jpg','http://image.ykd365.cn/act/202005/北京母亲节.jpg','http://image.ykd365.cn/act/202005/北京母亲节.jpg','http://image.ykd365.cn/act/202005/北京母亲节.jpg','http://image.ykd365.cn/act/202005/北京母亲节.jpg','http://image.ykd365.cn/act/202005/北京母亲节.jpg'
    # ]
    images=[
        'http://image.ykd365.cn/act/202005/天一夏至.jpg',
        'http://image.ykd365.cn/act/202005/欣臣夏至.jpg','http://image.ykd365.cn/act/202005/欣臣夏至.jpg',
        'http://image.ykd365.cn/act/202005/北京夏至.jpg','http://image.ykd365.cn/act/202005/北京夏至.jpg','http://image.ykd365.cn/act/202005/北京夏至.jpg','http://image.ykd365.cn/act/202005/北京夏至.jpg','http://image.ykd365.cn/act/202005/北京夏至.jpg','http://image.ykd365.cn/act/202005/北京夏至.jpg'
    ]

    queryTable('pm_dir_info')
    start = '2020-05-05 00:00:00'
    end = '2020-05-31 23:59:59'
    toDirName='夏至·春未央'
    # url = 
    for i in range(len(ydIds)):
        # if i==0:
        updateAllEnssence(ydIds[i],images[i])
        updateEnssence(ydIds[i],5,start,end,toDirName=toDirName)
        # else:
        #     logging.info(i)
    db.commit()      

def updateHuodong():
    """更新基础活动表中的数据，填满"""
    dirkv=[{
      "id": "1",
      "act": "202006618",
      "name": "年中大促 抢618神券",
      "code": "",
      "img": "http://image.ykd365.cn/act/202006/618/02.jpg",
      "num": "2",
      "drugstore_ids": "1620,1621,1622,1627,1629,1631,1600,1601,200",
      "parent_id": "",
      "lvl": "2",
      "to_dir_id": ""
    },
    {
      "id": "2",
      "act": "202006618",
      "name": "应季爆款",
      "code": "yjbk",
      "img": "http://image.ykd365.cn/act/202006/618/yjbk.jpg",
      "num": "2",
      "drugstore_ids": "1620,1621,1622,1627,1629,1631,1600,1601,200",
      "parent_id": "1",
      "lvl": "3",
      "to_dir_id": ""
    },
    {
      "id": "3",
      "act": "202006618",
      "name": "儿童健康专场",
      "code": "et",
      "img": "http://image.ykd365.cn/act/202006/618/etjk.jpg",
      "num": "4",
      "drugstore_ids": "1620,1621,1622,1627,1629,1631,1600,1601,200",
      "parent_id": "1",
      "lvl": "3",
      "to_dir_id": "7"
    },
    {
      "id": "4",
      "act": "202006618",
      "name": "女性健康专场",
      "code": "nv",
      "img": "http://image.ykd365.cn/act/202006/618/nvxjk.jpg",
      "num": "6",
      "drugstore_ids": "1620,1621,1622,1627,1629,1631,1600,1601,200",
      "parent_id": "1",
      "lvl": "3",
      "to_dir_id": "8"
    },
    {
      "id": "5",
      "act": "202006618",
      "name": "男性健康专场",
      "code": "nan",
      "img": "http://image.ykd365.cn/act/202006/618/nanxjk.jpg",
      "num": "8",
      "drugstore_ids": "1620,1621,1622,1627,1629,1631,1600,1601,200",
      "parent_id": "1",
      "lvl": "3",
      "to_dir_id": "9"
    },
    {
      "id": "6",
      "act": "202006618",
      "name": "父母健康专场",
      "code": "fm",
      "img": "http://image.ykd365.cn/act/202006/618/fmjk.jpg",
      "num": "10",
      "drugstore_ids": "1620,1621,1622,1627,1629,1631,1600,1601,200",
      "parent_id": "1",
      "lvl": "3",
      "to_dir_id": "10"
    },
    {
      "id": "7",
      "act": "202006618",
      "name": "儿童健康专场",
      "code": "cet",
      "img": "http://image.ykd365.cn/act/202006/618/et_02.jpg",
      "num": "2",
      "drugstore_ids": "200",
      "parent_id": "",
      "lvl": "4",
      "to_dir_id": ""
    },
    {
      "id": "8",
      "act": "202006618",
      "name": "女性健康专场",
      "code": "cnv",
      "img": "http://image.ykd365.cn/act/202006/618/nv_02.jpg",
      "num": "2",
      "drugstore_ids": "",
      "parent_id": "",
      "lvl": "4",
      "to_dir_id": ""
    },
    {
      "id": "9",
      "act": "202006618",
      "name": "男性健康专场",
      "code": "cnan",
      "img": "http://image.ykd365.cn/act/202006/618/nan_02.jpg",
      "num": "2",
      "drugstore_ids": "",
      "parent_id": "",
      "lvl": "4",
      "to_dir_id": ""
    },
    {
      "id": "10",
      "act": "202006618",
      "name": "父母健康专场",
      "code": "cfm",
      "img": "http://image.ykd365.cn/act/202006/618/fm_02.jpg",
      "num": "2",
      "drugstore_ids": "",
      "parent_id": "",
      "lvl": "4",
      "to_dir_id": ""
    },
    {
      "id": "11",
      "act": "202006618",
      "name": "儿童感冒",
      "code": "etgm",
      "img": "http://image.ykd365.cn/act/202006/618/etgm.jpg",
      "num": "4",
      "drugstore_ids": "",
      "parent_id": "7",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "12",
      "act": "202006618",
      "name": "止咳化痰",
      "code": "zkht",
      "img": "http://image.ykd365.cn/act/202006/618/zkht.jpg",
      "num": "6",
      "drugstore_ids": "",
      "parent_id": "7",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "13",
      "act": "202006618",
      "name": "脾胃健康",
      "code": "pwjk",
      "img": "http://image.ykd365.cn/act/202006/618/pwjk.jpg",
      "num": "8",
      "drugstore_ids": "",
      "parent_id": "7",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "14",
      "act": "202006618",
      "name": "儿童营养",
      "code": "etyy",
      "img": "http://image.ykd365.cn/act/202006/618/etyy.jpg",
      "num": "10",
      "drugstore_ids": "",
      "parent_id": "7",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "15",
      "act": "202006618",
      "name": "美容减肥",
      "code": "mrjf",
      "img": "http://image.ykd365.cn/act/202006/618/mrjf.jpg",
      "num": "4",
      "drugstore_ids": "",
      "parent_id": "8",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "16",
      "act": "202006618",
      "name": "营养保健",
      "code": "yybj",
      "img": "http://image.ykd365.cn/act/202006/618/yybj.jpg",
      "num": "6",
      "drugstore_ids": "",
      "parent_id": "8",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "17",
      "act": "202006618",
      "name": "妇科用药",
      "code": "fkyy",
      "img": "http://image.ykd365.cn/act/202006/618/fkyy.jpg",
      "num": "8",
      "drugstore_ids": "",
      "parent_id": "8",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "18",
      "act": "202006618",
      "name": "避孕验孕",
      "code": "byyy",
      "img": "http://image.ykd365.cn/act/202006/618/byyy.jpg",
      "num": "10",
      "drugstore_ids": "",
      "parent_id": "8",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "19",
      "act": "202006618",
      "name": "补肾壮阳",
      "code": "bszy",
      "img": "http://image.ykd365.cn/act/202006/618/bszy.jpg",
      "num": "4",
      "drugstore_ids": "",
      "parent_id": "9",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "20",
      "act": "202006618",
      "name": "男科用药",
      "code": "nkyy",
      "img": "http://image.ykd365.cn/act/202006/618/nkyy.jpg",
      "num": "6",
      "drugstore_ids": "",
      "parent_id": "9",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "21",
      "act": "202006618",
      "name": "日常保健",
      "code": "rcbj",
      "img": "http://image.ykd365.cn/act/202006/618/rcbj.jpg",
      "num": "8",
      "drugstore_ids": "",
      "parent_id": "9",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "22",
      "act": "202006618",
      "name": "心血管",
      "code": "xxg",
      "img": "http://image.ykd365.cn/act/202006/618/xxg.jpg",
      "num": "4",
      "drugstore_ids": "",
      "parent_id": "10",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "23",
      "act": "202006618",
      "name": "糖尿病",
      "code": "tnb",
      "img": "http://image.ykd365.cn/act/202006/618/tnb.jpg",
      "num": "6",
      "drugstore_ids": "",
      "parent_id": "10",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "24",
      "act": "202006618",
      "name": "滋补营养",
      "code": "zbyy",
      "img": "http://image.ykd365.cn/act/202006/618/zbyy.jpg",
      "num": "8",
      "drugstore_ids": "",
      "parent_id": "10",
      "lvl": "5",
      "to_dir_id": ""
    },
    {
      "id": "25",
      "act": "202006618",
      "name": "增强免疫",
      "code": "zqmy",
      "img": "http://image.ykd365.cn/act/202006/618/zqmy.jpg",
      "num": "10",
      "drugstore_ids": "",
      "parent_id": "10",
      "lvl": "5",
      "to_dir_id": ""
    }]

    for dir in dirkv:
        updateActTable('as_test.202006_ty_618',set=f"""dir_code='{dir['code']}',dir_num='{dir['num']}',dir_img='{dir['img']}'""",where=f"dir_name='{dir['name']}'")
        updateActTable('as_test.202006_xc_618',set=f"""dir_code='{dir['code']}',dir_num='{dir['num']}',dir_img='{dir['img']}'""",where=f"dir_name='{dir['name']}'")
        db.commit()
        logging.info(f"更新基础表中的目录数据{dir['name']}")

    itemkv=[{'item_name': '特价', 'item_desc': '特价', 'item_code': 'tj'
            , 'item_img': 'http://image.ykd365.cn/act/202006/618/detail.png'
            , 'item_img_r': '420', 'num': 100, 'item_type': 'discount'
            , 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None
            , 'kc_day': None, 'act_name': '618'}
       ]
 
    for dir in itemkv:
        updateActTable('as_test.202006_ty_618',set=f"""item_code='{dir['item_code']}',item_desc='{dir['item_desc']}',item_type='{dir['item_type']}',item_img='{dir['item_img']}',item_img_r='{dir['item_img_r']}',details_value='{dir['details_value']}',rule_value='{dir['rule_value']}'""",where=f"item_name='{dir['item_name']}'")
        updateActTable('as_test.202006_xc_618',set=f"""item_code='{dir['item_code']}',item_desc='{dir['item_desc']}',item_type='{dir['item_type']}',item_img='{dir['item_img']}',item_img_r='{dir['item_img_r']}',details_value='{dir['details_value']}',rule_value='{dir['rule_value']}'""",where=f"item_name='{dir['item_name']}'")
        db.commit()
        logging.info(f"更新基础表中的活动数据{dir['item_name']}")

def test():
    logging.info('test---------')
    iDirId = checkTable('pm_dir_info',result='*',where ='',order='dir_id desc limit 20')
    iSkuId = checkTable('pm_prod_sku',result='*',where ='',order='sku_id desc limit 10')
    iSmId = checkTable('sm_image_link',result='*',where ='',order='link_id desc limit 30')
    iSmId2 = checkTable('sm_image_link_window',result='*',where ='',order='window_id desc limit 10')
    iPacketId = checkTable('pm_packet_info',result='*',where ='',order='packet_id desc limit 10')

    iActId = checkTable('am_act_info',result='*',where ='',order='act_id desc limit 10')
    iItemId = checkTable('am_act_item',result='*',where ='',order='item_id desc limit 10')
    iRangeId = checkTable('am_act_range',result='*',where ='',order='range_id desc limit 10')
    iDetailId = checkTable('am_item_details',result='*',where ='',order='details_id desc limit 10')
    iQuotaId = checkTable('am_quota_info',result='*',where ='',order='quota_id desc limit 10')
    iSgId = checkTable('am_stages_sale',result='*',where ='',order='sg_id desc limit 10')
# 创建多盒商品 createCombByHuohao('1007150',1601,331474,490,490,count=5)
# 添加商品到amstatinfo 和 pmskudir中 ，根据货号和itemid addSkuDirByItemId(huohao,1600,1590)
# 给商品添加首单免费 下单返券 当日达 标签 buildSkuBaseByHuohao(huohao,1601,itemId=0,quotaId=0)
# 根据表 创建全套的活动 buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime,endTime,img='',color='')
# 根据表 创建sku createNewSkuByTable(tableName)
# 根据货号 查skuid querySkuId(huohao,drugstoreId)
# 1620,1621,1622,1627,1629,1631    
# 1600,1601
# 200
if __name__ == "__main__":
    logging.info(f'开始！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   
    # actName = '年中大促 健康狂欢'
    # linkurl = 'http://deve.ykd365.com/medstore/actUserpage/xiazhi_2005?dirId=' 
    # start = '2020-06-10'
    # # linkurl = 'http://store.ykd365.com/medstore/actUserpage/medicineKit_2005?dirId=' 
    # # start = '2020-06-15'
    # end = '2020-06-22'
    # color = ''
    # linkimg = 'http://image.ykd365.cn/act/202006/618/lb.jpg'
    # windowimg = 'http://image.ykd365.cn/act/202006/618/tc.png'
    # # updateHuodong()

    # act618(actId=0,actName = actName,tableName ='as_test.202006_ty_618',ydList = [200]
    #     ,startTime=start,endTime=end,color = color,linkimg =linkimg,linkurl = linkurl,linkView = '',windowimg= windowimg)
    # act618(actId=0,actName = actName,tableName ='as_test.202006_xc_618',ydList = [1600,1601,1602,1603]
    #     ,startTime=start,endTime=end,color = color,linkimg =linkimg,linkurl = linkurl,linkView = '',windowimg= windowimg)
    # db.commit()

    
    
    dirId = 1002764370	
    dirCode = '618limitcoupon'
    sql = f"""INSERT INTO `medstore`.`pm_sku_dir` (  `dir_id`, `sku_id`, `dir_code`, `sku_order`, `update_time`) 
            SELECT '{dirId}',s.sku_id,'{dirCode}','100', now()
            from as_test.202006_ty_618_limitq a 
            left join pm_prod_sku s on a.huohao = s.pharmacy_huohao and s.drugstore_id = 200
            """
    res = insertSQL(sql)
    db.commit()

    
    # try:
    #     ydIds = [1600,1601,1602,1603]
    #     huohaos = ['1007312','1007256']
    #     prodIds = [331726,331727]
    #     for ydId in ydIds:
    #         for huohao in huohaos:
    #             skuId = querySkuId(f"10件装{huohao}",ydId)
    #             # createCombByHuohao(huohao,ydId,prodIds[huohaos.index(huohao)],2000,2000,count=10)
    #             # buildSkuBaseByHuohao(f"10件装{huohao}",ydId,itemId=0,quotaId=0,skuImage='30分钟',limitquan=False)
    #             dir =  queryTableLastOne('pm_dir_info',field='*',where =f'pharmacy_id={ydId} and dir_name like "%戴口罩%"',order='dir_id desc')
    #             logging.info('查询出的dir信息 %s',dir)
    #             dirId = dir['dir_id']
    #             dirCode = dir['dir_code']
    #             order = 1
    #             addPmSkuDir(skuId,dirId,dirCode,order=order)

    #             dir =  queryTableLastOne('pm_dir_info',field='*',where =f'pharmacy_id={ydId} and dir_name like "%首单优选推荐%" ',order='dir_id desc')
    #             logging.info('查询出的dir信息 %s',dir)
    #             dirId = dir['dir_id']
    #             dirCode = dir['dir_code']
    #             order = 1
    #             addPmSkuDir(skuId,dirId,dirCode,order=order)
    #     db.commit()
    # except Exception as err:
    #         logging.error(err)
    #         db.rollback()
    # hh=f"10件装1007312"
    # addSkuDirByItemId(hh,1600,1633)
    # addSkuDirByItemId(hh,1601,1634)
    # addSkuDirByItemId(hh,1602,1739)
    # addSkuDirByItemId(hh,1603,1756)

    # hh2=f"10件装1007256"
    # addSkuDirByItemId(hh2,1600,1633)
    # addSkuDirByItemId(hh2,1601,1634)
    # addSkuDirByItemId(hh2,1602,1739)
    # addSkuDirByItemId(hh2,1603,1756)
    # db.commit()

#     1756	1603
# 1739	1602
# 1634	1601
# 1633	1600

    # actName = '2件92折、3件88折'
    # start = '2020-05-30' # '2020-05-22'
    # end = '2020-06-15'
    # img = ''
    # color = ''
    # linkimg = ''
    # # linkurl = 'http://deve.ykd365.com/medstore/actUserpage/medicineKit_2005?dirId=' 

    # linkurl =  ''
    # windowimg = ''
    # # xyx(actId=0,actName = actName,tableName ='as_test.202005_ty_xyx',ydList = [200],startTime=start,endTime=end
    # #     ,img = img,color = color,linkimg = linkimg,linkurl = linkurl,linkView = '',windowimg= windowimg)
    # # build292388(actId=0,actName = actName,tableName ='as_test.202005_ty_292388',ydList = [200]
    # #     ,startTime=start,endTime=end,img = '',color = '',linkimg = '',linkurl = '',linkView = '',windowimg= '')
    # # build292388(actId=0,actName = actName,tableName ='as_test.202005_xc_292388',ydList = [1600,1601,1602,1603]
    # #     ,startTime=start,endTime=end,img = '',color = '',linkimg = '',linkurl = '',linkView = '',windowimg= '')
    # build292388(actId=0,actName = actName,tableName ='as_test.202005_bj_292388',ydList = [1620,1621,1622,1627,1629,1631]
    #     ,startTime=start,endTime=end,img = '',color = '',linkimg = '',linkurl = '',linkView = '',windowimg= '')
    
# http://image.ykd365.cn/act/1906/1906_list3.png
# http://image.ykd365.cn/act/1910/drug_list_2.png
# http://image.ykd365.cn/act/2002/notouch/list.png
# http://image.ykd365.cn/act/2002/notouch/list88.png
# http://image.ykd365.cn/act/202005/mqj/lcz_logo.png
# http://image.ykd365.cn/act/202005/mqj/mqj_logo.png
# http://image.ykd365.cn/act/202005/xyx/list_jtbb.png
# http://image.ykd365.cn/act/202005/xz/xz_logo.png
# http://image.ykd365.cn/drugstore/list.png
    # updateHuodong()
    # actName = '家庭必备小药箱'
    # start = '2020-05-26' # '2020-05-22'
    # end = '2020-06-15'
    # img = 'http://image.ykd365.cn/act/202005/xyx/02.jpg'
    # color = '#c4cde6'
    # linkimg = 'http://image.ykd365.cn/act/202005/xyx/xyx_lb.jpg'
    # # linkurl = 'http://deve.ykd365.com/medstore/actUserpage/medicineKit_2005?dirId=' 

    # linkurl =  'http://store.ykd365.com/medstore/actUserpage/medicineKit_2005?dirId='
    # windowimg = 'http://image.ykd365.cn/act/202005/xyx/xyx_tc.png'
    # xyx(actId=0,actName = actName,tableName ='as_test.202005_ty_xyx',ydList = [200],startTime=start,endTime=end
    #     ,img = img,color = color,linkimg = linkimg,linkurl = linkurl,linkView = '',windowimg= windowimg)
    # xyx(actId=0,actName = actName,tableName ='as_test.202005_xc_xyx',ydList = [1600,1601],startTime=start,endTime=end
    #     ,img = img,color = color,linkimg = linkimg,linkurl = linkurl,linkView = '',windowimg= windowimg)
    # xyx(actId=0,actName = actName,tableName ='as_test.202005_bj_xyx',ydList = [1620,1621,1622,1627,1629,1631],startTime=start,endTime=end
    #     ,img = img,color = color,linkimg = linkimg,linkurl = linkurl,linkView = '',windowimg= windowimg)
    


    # xyx()
    # xrzq2()
    # drugstoreIds=[1600,1601]
    # index=1
    # img='http://image.ykd365.cn/act/202005/xc/gd_tc.png'
    # url=''
    # name='关店'
    # dirId=''
    # start='2020-05-07'
    # end='2020-05-16'
    # type=''
    # for drugstoreId in drugstoreIds:
    #     addSmImageLinkWindow(drugstoreId,index,img,url,name,dirId,start,end,type)
    # db.commit()

    # res =  queryTable('pm_dir_info',result='*',where ='',order='dir_id desc limit 20')
    # logging.info(f"pm_dir_info====={res}")
    # updateHuodong()
   
    # actName ='夏至·春未央'
    # start = '2020-05-10'
    # end = '2020-05-31'
    # img = 'http://image.ykd365.cn/act/202005/xz/02.jpg'
    # color = '#e7e7e7'
    # actId = xz(actName = actName,tableName ='as_test.202005_ty_xz_all',ydList = [200],startTime=start,endTime=end,img =img,color = color)
    # xz(actId=actId,actName = actName,tableName ='as_test.202005_ty_xz',ydList = [200],startTime=start,endTime=end,img =img,color = color,linkimg = 'http://image.ykd365.cn/act/202005/xz/xz_banner.jpg',linkurl = 'http://deve.ykd365.com/medstore/actUserpage/xiazhi_2005?dirId=',linkView = '',windowimg= 'http://image.ykd365.cn/act/202005/xz/xz_tc.png')
    
    # xz(actName = actName,tableName ='as_test.202005_xc_xz',ydList = [1600,1601],startTime=start,endTime=end,img =img,color = color,linkimg = 'http://image.ykd365.cn/act/202005/xz/xz_banner.jpg',linkurl = 'http://deve.ykd365.com/medstore/actUserpage/xiazhi_2005?dirId=',linkView = '',windowimg= 'http://image.ykd365.cn/act/202005/xz/xz_tc.png')
    
    # bjactId = xz(actName = actName,tableName ='as_test.202005_bj_xz_all',ydList = [1620,1621,1622,1627,1629,1631],startTime=start,endTime=end,img =img,color = color)
    # xz(actId=bjactId,actName = actName,tableName ='as_test.202005_bj_xz',ydList = [1620,1621,1622,1627,1629,1631],startTime=start,endTime=end,img =img,color = color,linkimg = 'http://image.ykd365.cn/act/202005/xz/xz_banner.jpg',linkurl = 'http://store.ykd365.com/medstore/actUserpage/xiazhi_2005?dirId=',linkView = '',windowimg= 'http://image.ykd365.cn/act/202005/xz/xz_tc.png')
    
    # update9GG()
    # updateSQL("UPDATE pm_label_image SET label_status=0 WHERE label_url='http://image.ykd365.cn/act/2002/notouch/list.png'")





    # ydList = [1620,1621,1622,1627,1629,1631]
    # for ydId in ydList:
    #     # stopPacket('as_test.202005_bj_xz_all',ydId,where = 'stop_lcz=1')
    #     # stopPacket('as_test.202005_bj_xz',ydId,where = 'stop_lcz=1')
    #     # stopPacket('as_test.202005_bj_xz',ydId,where = 'list_logo="疗程装"',stop=1)
    #     # updateSQL("UPDATE pm_label_image SET label_status=0 WHERE label_url='http://image.ykd365.cn/act/2002/notouch/list.png'")

    #     # # 列表页走上角标志
    #     list =  querySkuIdByTable(  'as_test.202005_bj_xz',ydId,where='1=1')
    #     lczskuIdList =[]
    #     hjjkskuIdList =[]
    #     for dic in list:
    #         list_logo = dic['list_logo']
    #         if  list_logo =='疗程装':
    #             lczskuIdList.append(dic['sku_id'])
    #         elif  list_logo =='换季健康':
    #             hjjkskuIdList.append(dic['sku_id'])
    #     addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',ydId,skuIdList=lczskuIdList)
    #     addPmLabelImage('换季健康','http://image.ykd365.cn/act/202005/xz/xz_logo.png','1',ydId,skuIdList=hjjkskuIdList)


    # ydList = [200]
    # for ydId in ydList:
    #     stopPacket('as_test.202005_ty_xz_all',ydId,where = 'stop_lcz=1')
    #     stopPacket('as_test.202005_ty_xz',ydId,where = 'stop_lcz=1')
    #     # stopPacket('as_test.202005_ty_xz',ydId,where = 'list_logo="疗程装"',stop=1)
    #     # updateSQL("UPDATE pm_label_image SET label_status=0 WHERE label_url='http://image.ykd365.cn/act/2002/notouch/list.png'")

    #     # # 列表页走上角标志
    #     list =  querySkuIdByTable(  'as_test.202005_ty_xz',ydId,where='1=1')
    #     lczskuIdList =[]
    #     hjjkskuIdList =[]
    #     for dic in list:
    #         list_logo = dic['list_logo']
    #         if  list_logo =='疗程装':
    #             lczskuIdList.append(dic['sku_id'])
    #         elif  list_logo =='换季健康':
    #             hjjkskuIdList.append(dic['sku_id'])
    #     addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',ydId,skuIdList=lczskuIdList)
    #     addPmLabelImage('换季健康','http://image.ykd365.cn/act/202005/xz/xz_logo.png','1',ydId,skuIdList=hjjkskuIdList)

    # ydList = [1600,1601]
    # for ydId in ydList:
    #     list =  querySkuIdByTable(  'as_test.202005_xc_xz',ydId,where='1=1')
    #     lczskuIdList =[]
    #     hjjkskuIdList =[]
    #     for dic in list:
    #         list_logo = dic['list_logo']
    #         if  list_logo =='疗程装':
    #             lczskuIdList.append(dic['sku_id'])
    #         elif  list_logo =='换季健康':
    #             hjjkskuIdList.append(dic['sku_id'])
    #     addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',ydId,skuIdList=lczskuIdList)
    #     addPmLabelImage('换季健康','http://image.ykd365.cn/act/202005/xz/xz_logo.png','1',ydId,skuIdList=hjjkskuIdList)
    # db.commit()



    # actName = '感恩母亲节'
    # startTime='2020-05-07'
    # endTime='2020-05-17'
    # img = 'http://image.ykd365.cn/act/202005/mqj/02.jpg'
    # color = '#e7e7e7'
    # linkimg = 'http://image.ykd365.cn/act/202005/xz/xz_banner.jpg'
    # linkurl = 'http://deve.ykd365.com/medstore/actUserpage/muj_2005?dirId='
    # linkView = ''
    # windowimg= 'http://image.ykd365.cn/act/202005/xz/xz_tc.png'
    # mqj(actName = '感恩母亲节',tableName ='as_test.202005_ty_mqj',ydList = [200],startTime=startTime,endTime=endTime,img = 'http://image.ykd365.cn/act/202005/mqj/02.jpg',color = '#e7e7e7')
    # mqj(actName = '感恩母亲节',tableName ='as_test.202005_xc_mqj',ydList = [1600,1601],startTime=startTime,endTime=endTime,img = 'http://image.ykd365.cn/act/202005/mqj/02.jpg',color = '#e7e7e7')
    # mqj(actName = '感恩母亲节',tableName ='as_test.202005_bj_mqj',ydList = [1620,1621,1622,1627,1629,1631],startTime=startTime,endTime=endTime,img = 'http://image.ykd365.cn/act/202005/mqj/02.jpg',color = '#e7e7e7')
    
    # update9GG()

# SELECT  * 
# from as_test.202005_ty_xz a 
# LEFT JOIN pm_prod_sku s on a.huohao = s.pharmacy_huohao and s.drugstore_id=200
# LEFT JOIN am_stat_info ai on s.sku_id = ai.sku_id and ai.item_name = '2件92折3件88折'
# WHERE a.w = '新增'
# ; 删掉多余的amstatinfo ，下面会新加进去，但是type是drugtag ，要手动改成discount
    # logging.info(" 删掉多余的amstatinfo ，下面会新加进去，但是type是drugtag ，要手动改成discount")
    # drugstoreId = 200
    # itemId=1739
    # list =  queryTable('as_test.202005_ty_xz',result='*',where =f' w="新增"')
    # for dic in list:
    #     huohao = dic['huohao']
    #     addSkuDirByItemId(huohao,drugstoreId,itemId,skuTotal=0,maxTotal=0)
    # db.commit()

    # parentDirId = '1002763750'
    # addSmImageLink(1601,1,linkimg,linkurl,actName,parentDirId,startTime,endTime,linkView)
    # db.commit()
    
    # huohao = 18102376
    # ydId = 200
    # buildSkuBaseByHuohao(huohao,ydId,skuImage='30分钟')
    # dir =  queryTableLastOne('pm_dir_info',field='*',where =f'pharmacy_id={ydId} and dir_code like "%1000act226dkz"',order='dir_id desc')
    # logging.debug('查询出的dir信息 %s',dir)
    # dirId = dir['dir_id']
    # dirCode = dir['dir_code']
    # order = 120
    # skuId = querySkuId(huohao,ydId)
    # addPmSkuDir(skuId,dirId,dirCode,order=order)
    # db.commit()
    # try:
    #     huohaos = ['06100347','18102380']
    #     yds = [200]
    #     for ydId in yds:
    #         # for huohao in huohaos:
    #         for i in range(len(huohaos)):
    #             huohao = huohaos[i]
    #             buildSkuBaseByHuohao(huohao,ydId,skuImage='30分钟')
    #             skuId = querySkuId(huohao,ydId)
    #             # dirList =  queryTable('pm_dir_info',result='*',where =f'pharmacy_id={ydId} and dir_code like "%yxtj"')
    #             dir =  queryTableLastOne('pm_dir_info',field='*',where =f'pharmacy_id={ydId} and dir_code like "%1000act226dkz"',order='dir_id desc')
    #             logging.debug('查询出的dir信息 %s',dir)
    #             dirId = dir['dir_id']
    #             dirCode = dir['dir_code']
    #             order = 120
    #             addPmSkuDir(skuId,dirId,dirCode,order=order)

    #             dir =  queryTableLastOne('pm_dir_info',field='*',where =f'pharmacy_id={ydId} and dir_code like "%1000act226cxd"',order='dir_id desc')
    #             logging.debug('查询出的dir信息 %s',dir)
    #             dirId = dir['dir_id']
    #             dirCode = dir['dir_code']
    #             order = 120
    #             addPmSkuDir(skuId,dirId,dirCode,order=order)
    #     db.commit()
    # except Exception as err:
    #         logging.error("Error %s for execute sql: %s" % (err, sql))
    #         logging.debug('语句失败！！！')
    #         db.rollback()

    # huohao = '06100344'
    # ydId = 200
    # dirId= '1002763460'
    # dirCode='1000act226qxs'
    # order =10
    # buildSkuBaseByHuohao(huohao,ydId,skuImage='30分钟')
    # skuId = querySkuId(huohao,ydId)
    # addPmSkuDir(skuId,dirId,dirCode,order=order)

    # dirList =  queryTable('pm_dir_info',result='*',where =f'pharmacy_id={ydId} and dir_code like "%act228dkz" limit 1')
    # for dir in dirList:
    #     logging.debug(dir)
    #     dirId = dir['dir_id']
    #     dirCode = dir['dir_code']
    #     order = i+110
    #     addPmSkuDir(skuId,dirId,dirCode,order=order)


#  http://image.ykd365.cn/act/202006/618/02.jpg
# http://image.ykd365.cn/act/202006/618/yjbk.jpg
# http://image.ykd365.cn/act/202006/618/etjk.jpg
# http://image.ykd365.cn/act/202006/618/nvxjk.jpg
# http://image.ykd365.cn/act/202006/618/nanxjk.jpg
# http://image.ykd365.cn/act/202006/618/fmjk.jpg
# http://image.ykd365.cn/act/202006/618/et_02.jpg
# http://image.ykd365.cn/act/202006/618/nv_02.jpg
# http://image.ykd365.cn/act/202006/618/nan_02.jpg
# http://image.ykd365.cn/act/202006/618/fm_02.jpg
# http://image.ykd365.cn/act/202006/618/etgm.jpg
# http://image.ykd365.cn/act/202006/618/zkht.jpg
# http://image.ykd365.cn/act/202006/618/pwjk.jpg
# http://image.ykd365.cn/act/202006/618/etyy.jpg
# http://image.ykd365.cn/act/202006/618/mrjf.jpg
# http://image.ykd365.cn/act/202006/618/yybj.jpg
# http://image.ykd365.cn/act/202006/618/fkyy.jpg
# http://image.ykd365.cn/act/202006/618/byyy.jpg
# http://image.ykd365.cn/act/202006/618/bszy.jpg
# http://image.ykd365.cn/act/202006/618/nkyy.jpg
# http://image.ykd365.cn/act/202006/618/rcbj.jpg
# http://image.ykd365.cn/act/202006/618/xxg.jpg
# http://image.ykd365.cn/act/202006/618/tnb.jpg
# http://image.ykd365.cn/act/202006/618/zbjk.jpg
# http://image.ykd365.cn/act/202006/618/zqmy.jpg