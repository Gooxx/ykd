# from db2 import db,cursor,querySQL,updateSQL,insertSQL,selectBy,selectOneBy
# import time
# import datetime
# import json
# import logging
# import xlwt
from  act import *
# import act
import logging
from pypinyin import pinyin, lazy_pinyin, Style

def 新商品打下单返券和30分钟必达的标():
    ydId =200
    huohaoList = ['07099611','20100008','20100009','21099636','39000397','39000398','39000399','39000400','39000396','20100007','21099635','20100006','06100356','22000781','04000990','08100124','08100130','08100123','08100122','08100126','08100121','08100127','06100325','18102355','08100125']
    for huohao in huohaoList:
        # buildSkuBaseByHuohao(huohao,ydId,skuImage='30分钟')
        addAmskuImage(huohao,ydId,img='http://image.ykd365.cn/icon/home/30minbd.png',radio='393',title='30分钟送达')
        db.commit()

def 给5月两件92折活动缺少列表页左上角标的商品加标():
    tableName = 'as_test.202005_ty_292388'
    drugstoreId=200
    list =  querySkuIdByTable(tableName,drugstoreId,where='1=1')
    logoList =[]
    # hjjkskuIdList =[]
    # jtcbskuIDList= []
    for dic in list:
        list_logo = dic['list_logo']
        sku_id=dic['sku_id']
        if list_logo !='2件92折、3件88折':
            logoList.append(dic['sku_id'])
    addPmLabelImage('2件92折、3件88折','http://image.ykd365.cn/act/2002/notouch/list88.png','1',drugstoreId,skuIdList=logoList)
    db.commit()



def updateact8月开学必备小药箱活动(tableName):
    """更新基础活动表中的数据，填满"""
    pre_img = 'http://image.ykd365.cn/act/202008/kx/'
    suf_img = '.jpg'
    dirkv=[{
      "name": "防疫消毒",
      "code": "fyxd",
      "num": "02",
    },{
     "name": "解暑消署",
      "code": "jsxs",
      "num": "04",
    },{
     "name": "感冒发烧",
      "code": "gmfs",
      "num": "06",
    },{
     "name": "胃肠消化",
      "code": "cwxh",
      "num": "08",
    },{
     "name": "消炎止痛",
      "code": "xyzt",
      "num": "10",
    },{
     "name": "止咳化痰",
      "code": "zkht",
      "num": "12",
    },{
     "name": "皮肤过敏",
      "code": "pfgm",
      "num": "14",
    },{
     "name": "调节免疫",
      "code": "tjmy",
      "num": "16",
    },{
     "name": "外用护理",
      "code": "wyhl",
      "num": "18",
    }]

    for dir in dirkv:
        updateActTable(tableName,set=f"""dir_code='{dir['code']}',dir_num='{dir['num']}',dir_img='{pre_img}{dir['code']}{suf_img}'""",where=f"dir_name='{dir['name']}'")
        db.commit()
        logging.info(f"更新基础表中的目录数据{dir['name']}")

    itemkv=[{'item_name': '特价', 'item_desc': '特价', 'item_code': 'tj'
            , 'item_img': ''
            , 'item_img_r': '', 'num': 100, 'item_type': 'discount'
            , 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None
            , 'kc_day': None, 'act_name': ''},
            {'item_name': '2件92折、3件88折', 'item_desc': '2件92折、3件88折', 'item_code': 'd292388'
            , 'item_img': ''
            , 'item_img_r': '', 'num': 100, 'item_type': 'discount'
            , 'details_value': '92,88', 'rule_value': '2,3', 'quota_rule': None, 'quota_group': None
            , 'kc_day': None, 'act_name': ''},
            {'item_name': '3件85折', 'item_desc': '3件85折', 'item_code': 'd385'
            , 'item_img': f'{pre_img}detail{suf_img}'
            , 'item_img_r': '643', 'num': 100, 'item_type': 'discount'
            , 'details_value': '85', 'rule_value': '3', 'quota_rule': None, 'quota_group': None
            , 'kc_day': None, 'act_name': ''}
       ]
 
    for dir in itemkv:
        updateActTable(tableName,set=f"""item_code='{dir['item_code']}',item_desc='{dir['item_desc']}',item_type='{dir['item_type']}',item_img='{dir['item_img']}',item_img_r='{dir['item_img_r']}',details_value='{dir['details_value']}',rule_value='{dir['rule_value']}'""",where=f"item_name='{dir['item_name']}'")
        db.commit()
        logging.info(f"更新基础表中的活动数据{dir['item_name']}")

def act8月开学必备小药箱活动(actId=0,actName = '',tableName ='',ydList = [],startTime='',endTime='',img = '',color = '',linkimg = '',linkurl = '',linkView = '',windowimg= ''):
    logging.debug('开学季活动')
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
            list =  querySkuIdByTable(tableName,drugstoreId,where='1=1')
            logoList= []
            for dic in list:
                list_logo = dic['list_logo']
                sku_id=dic['sku_id']
                if list_logo =='开学必备':
                    logoList.append(dic['sku_id'])
                    addPmLabelImage('开学必备','http://image.ykd365.cn/act/202008/kx/list_logo.png','1',drugstoreId,skuIdList=logoList)
                elif  list_logo =='疗程装':
                    logoList.append(dic['sku_id'])
                    addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',drugstoreId,skuIdList=logoList)
                # 限券
                if 'is_xq' in dic.keys() and dic['is_xq']!=None and dic['is_xq']==1:
                    copyAmStatInfoBySkuId( 78,sku_id)
                # huohao =  dic['pharmacy_huohao']
                # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)

            # addPmLabelImage('2件92折、3件88折','http://image.ykd365.cn/act/2002/notouch/list88.png','1',drugstoreId,skuIdList=xjxxzskuIdList)
            # addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',drugstoreId,skuIdList=lczskuIdList)
            # addPmLabelImage('换季健康','http://image.ykd365.cn/act/202005/xz/xz_logo.png','1',drugstoreId,skuIdList=hjjkskuIdList)
            # addPmLabelImage('家庭常备','http://image.ykd365.cn/act/202005/xyx/list_jtbb.png','1',drugstoreId,skuIdList=jtcbskuIDList)
            logging.info('创建list logo------------')
            # 暂停疗程购
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=1')
            stopPacket(tableName,drugstoreId,where = 'list_logo="疗程装"',stop=1)
            # 停掉一些疗程购， 标着疗程装的就上架打开
            logging.info('暂停疗程购------------')
            
            
            buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color,linkurl=linkurl,linkimg=linkimg,windowimg=windowimg)
            db.commit()
        except Exception as err:
            logging.error(err)
            db.rollback()

def update9GG():
    ydIds=[200,1600,1601,1602,1603]

    images=[
        'http://image.ykd365.cn/act/202008/kx/ty_9gg.jpg','http://image.ykd365.cn/act/202008/kx/xc_9gg.jpg','http://image.ykd365.cn/act/202008/kx/xc_9gg.jpg','http://image.ykd365.cn/act/202008/kx/xc_9gg.jpg','http://image.ykd365.cn/act/202008/kx/xc_9gg.jpg'
    ]
    queryTable('pm_dir_info')
    start = '2020-08-29 00:00:00'
    end = '2020-09-10 23:59:59'
    toDirName='开学必备小药箱'
    # url = 
    for i in range(len(ydIds)):
        # if i==0:
        updateAllEnssence(ydIds[i],images[i])
        updateEnssence(ydIds[i],5,start,end,toDirName=toDirName,link_view='')
        # else:
        #     logging.info(i)
    db.commit()
    
def 忘记特价价格了():
    logging.info(' 忘记特价价格了--------')
    start = '2020-08-25 00:00:00'
    end = '2020-09-10 23:59:59'

    tableName ='as_test.202008_ty_kx'
    ydList = [200]
    for index in range(len(ydList)):
        drugstoreId = ydList[index]
        # 创建特价
        addPmActSale(tableName,drugstoreId,start,end)
        logging.info('创建价格------------')
    db.commit()

    tableName ='as_test.202008_xc_kx'
    ydList = [1600,1601,1602,1603]
    for index in range(len(ydList)):
        drugstoreId = ydList[index]
        # 创建特价
        addPmActSale(tableName,drugstoreId,start,end)
        logging.info('创建价格------------')
    db.commit()

def 中秋国庆(actId=0,actName = '',tableName ='',ydList = [],startTime='',endTime='',img = '',color = '',linkimg = '',linkurl = '',linkView = '',windowimg= ''):
    tableName = "as_test.202009_ty_zq"
    # pre_img = 'http://image.ykd365.cn/act/202009/zq/'
    # suf_img = '.png'
    # dirkv=[{
    #   "name": "送礼首选",
    #   "num": "02",
    # },{
    #  "name": "出行必备",
    #   "num": "04",
    # },{
    #  "name": "关爱父母",
    #   "num": "06",
    # },{
    #  "name": "儿童健康",
    #   "num": "08",
    # },{
    #  "name": "呵护自己",
    #   "num": "10",
    # }]

    # for dir in dirkv:
    #     wordList = pinyin(dir['name'], style=Style.FIRST_LETTER)
    #     code =''
    #     for item in wordList:
    #         code += ''.join(item)
    #     updateActTable(tableName,set=f"""dir_code='{code}',dir_num='{dir['num']}',dir_img='{pre_img}{code}{suf_img}'""",where=f"dir_name='{dir['name']}'")
    #     db.commit()
    #     logging.info(f"更新基础表中的目录数据{code}")

    # itemkv=[
    #         {'item_name': '2件92折、3件88折', 'item_desc': '2件92折、3件88折', 'item_code': 'd292388'
    #         , 'item_img': ''
    #         , 'item_img_r': '', 'num': 100, 'item_type': 'discount'
    #         , 'details_value': '92,88', 'rule_value': '2,3', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''},
    #         {'item_name': '3件85折', 'item_desc': '3件85折', 'item_code': 'd385'
    #         , 'item_img': f'{pre_img}detail{suf_img}'
    #         , 'item_img_r': '643', 'num': 100, 'item_type': 'discount'
    #         , 'details_value': '85', 'rule_value': '3', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''},
    #         {'item_name': '特价', 'item_desc': '特价' 
    #         ,'item_img':''
    #         , 'item_img_r': '', 'num': 100, 'item_type': 'discount'
    #         , 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''},
    #         {'item_name': '第二件半价', 'item_desc': '第二件半价'
    #         ,'item_img':'1'
    #         , 'item_img_r': '643', 'num': 100, 'item_type': 'discount'
    #         , 'details_value': '75', 'rule_value': '2', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''}
    #    ]
 
    # for dir in itemkv:
    #     wordList = pinyin(dir['item_name'], style=Style.FIRST_LETTER)
    #     code =''
    #     image = ''
    #     for item in wordList:
    #         code += ''.join(item)
        
    #     image = '' if dir['item_img'] =='' else  f'{pre_img}{code}{suf_img}'
    #     updateActTable(tableName,set=f"""item_code='{code}',item_desc='{dir['item_desc']}',item_type='{dir['item_type']}',item_img='{image}',item_img_r='{dir['item_img_r']}',details_value='{dir['details_value']}',rule_value='{dir['rule_value']}'""",where=f"item_name='{dir['item_name']}'")
    #     db.commit()
    #     logging.info(f"更新基础表中的目录数据{code}")
    # 以上 是对基础表的修改， 上生产的时候直接复制盘货表即可，无需再次执行上面的代码
    # 以下 是活动的正式内容 ，上生产的时候需要执行

    logging.debug('中秋 国庆')
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
            list =  querySkuIdByTable(tableName,drugstoreId,where='1=1')
            logoList= []
            for dic in list:
                list_logo = dic['list_logo']
                sku_id=dic['sku_id']
                if list_logo =='嗨购季':
                    logoList.append(dic['sku_id'])
            
                # elif  list_logo =='疗程装':
                #     logoList.append(dic['sku_id'])
                #     addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',drugstoreId,skuIdList=logoList)
                # 限券
                if 'is_xq' in dic.keys() and dic['is_xq']!=None and dic['is_xq']==1:
                    copyAmStatInfoBySkuId( 78,sku_id)
                # huohao =  dic['pharmacy_huohao']
                # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)
            addPmLabelImage('嗨购季','http://image.ykd365.cn/act/202009/zq/list.png','1',drugstoreId,skuIdList=logoList)
            logging.info('创建list logo------------')
            # 暂停疗程购
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=1')
            stopPacket(tableName,drugstoreId,where = 'list_logo="疗程装"',stop=1)
            # 停掉一些疗程购， 标着疗程装的就上架打开
            logging.info('暂停疗程购------------')
            
            
            buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color,linkurl=linkurl,linkimg=linkimg,windowimg=windowimg)
            db.commit()
        except Exception as err:
            logging.error(err)
            db.rollback()
        logging.info('上完活动 记得执行下面的sql，解决本次特价和第二件半价活动商品，还有老2件92折活动的问题------------')
# update am_stat_info a LEFT JOIN am_stat_info a2 on a.sku_id = a2.sku_id
# set a2.item_expire_time = '2010-12-31 23:59:59'
# where a2.item_name = '2件92折、3件88折'
# and a.item_id = 1857
# ;

# update am_stat_info a LEFT JOIN am_stat_info a2 on a.sku_id = a2.sku_id
# set a2.item_expire_time = '2010-12-31 23:59:59'
# where a2.item_name = '2件92折、3件88折'
# and a.item_id = 1856
# ;


def update国庆中秋9GG( toDirName ='',ydIds = [],allImags=[],images=[],startTime='',endTime=''):
    # ydIds=[200]

    # images=[
    #     'http://image.ykd365.cn/act/202008/kx/ty_9gg.jpg','http://image.ykd365.cn/act/202008/kx/xc_9gg.jpg','http://image.ykd365.cn/act/202008/kx/xc_9gg.jpg','http://image.ykd365.cn/act/202008/kx/xc_9gg.jpg','http://image.ykd365.cn/act/202008/kx/xc_9gg.jpg'
    # ]
    # queryTable('pm_dir_info')
    # start = '2020-08-29 00:00:00'
    # end = '2020-09-10 23:59:59'
    # toDirName='开学必备小药箱'
    # url = 
    actName = '健康好礼嗨购季'
    # start = '2010-09-25 00:00:00'
    # end = '2020-10-11 23:59:59'
    parentDirId = '1002764884'
    # linkurl = 'http://store.ykd365.com/medstore/actUserpage/medicineKit_2008?pageSize=1000&dirId='
    linkurl = 'http://store.ykd365.com/medstore/actUserpage/moon_2010?pageSize=1000&dirId='

    color = '#deedef'
    headimg = 'http://image.ykd365.cn/act/202009/zq/02.png'
    linkimg = 'http://image.ykd365.cn/act/202009/zq/lb.jpg'
    windowimg = 'http://image.ykd365.cn/act/202009/zq/tc.png'
    for i in range(len(ydIds)):
        drugstoreId = ydIds[i]
        # addSmImageLink(drugstoreId,1,linkimg,linkurl,actName,parentDirId,startTime,endTime,link_view='')
        # addSmImageLinkWindow(drugstoreId,1,windowimg,linkurl,actName,parentDirId,startTime,endTime)
        # if i==0:
        updateAllEnssence(ydIds[i],allImags[i])
        updateEnssence(ydIds[i],5,startTime,endTime,toDirName=toDirName,link_view='')
        # else:
        #     logging.info(i)
    db.commit()
    

def 秋季小药箱(actId=0,actName = '',tableName ='',ydList = [],startTime='',endTime='',img = '',color = '',linkimg = '',linkurl = '',linkView = '',windowimg= ''):
    # tableName = "as_test.202009_ty_xyx"
    # pre_img = 'http://image.ykd365.cn/act/202009/xyx/'
    # suf_img = '.jpg' # 主要是会场的楼层图
    # dirkv=[{
    #   "name": "感冒咳嗽",
    #   "num": "02",
    # },{
    #  "name": "解热镇痛",
    #   "num": "04",
    # },{
    #  "name": "胃肠用药",
    #   "num": "06",
    # },{
    #  "name": "小儿用药",
    #   "num": "08",
    # },{
    #  "name": "女性健康",
    #   "num": "10",
    # },{
    #  "name": "男性健康",
    #   "num": "12",
    # },{
    #  "name": "慢病用药",
    #   "num": "14",
    # }]

    # for dir in dirkv:
    #     wordList = pinyin(dir['name'], style=Style.FIRST_LETTER)
    #     code =''
    #     for item in wordList:
    #         code += ''.join(item)
    #     updateActTable(tableName,set=f"""dir_code='{code}',dir_num='{dir['num']}',dir_img='{pre_img}{code}{suf_img}'""",where=f"dir_name='{dir['name']}'")
    #     db.commit()
    #     logging.info(f"更新基础表中的目录数据{code}")

    # itemkv=[
    #         {'item_name': '2件92折、3件88折', 'item_desc': '2件92折、3件88折', 'item_code': 'd292388'
    #         , 'item_img': ''
    #         , 'item_img_r': '', 'num': 100, 'item_type': 'discount'
    #         , 'details_value': '92,88', 'rule_value': '2,3', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''},
    #         {'item_name': '3件85折', 'item_desc': '3件85折', 'item_code': 'd385'
    #         , 'item_img': f'{pre_img}detail{suf_img}'
    #         , 'item_img_r': '643', 'num': 100, 'item_type': 'discount'
    #         , 'details_value': '85', 'rule_value': '3', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''},
    #         {'item_name': '特价', 'item_desc': '特价' 
    #         ,'item_img':''
    #         , 'item_img_r': '', 'num': 100, 'item_type': 'discount'
    #         , 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''},
    #         {'item_name': '第二件半价', 'item_desc': '第二件半价'
    #         ,'item_img':'1'
    #         , 'item_img_r': '643', 'num': 100, 'item_type': 'discount'
    #         , 'details_value': '75', 'rule_value': '2', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''}
    #    ]
 
    # for dir in itemkv:
    #     wordList = pinyin(dir['item_name'], style=Style.FIRST_LETTER)
    #     code =''
    #     image = ''
    #     for item in wordList:
    #         code += ''.join(item)
        
    #     image = '' if dir['item_img'] =='' else  f'{pre_img}{code}{suf_img}'
    #     updateActTable(tableName,set=f"""item_code='{code}',item_desc='{dir['item_desc']}',item_type='{dir['item_type']}',item_img='{image}',item_img_r='{dir['item_img_r']}',details_value='{dir['details_value']}',rule_value='{dir['rule_value']}'""",where=f"item_name='{dir['item_name']}'")
    #     db.commit()
    #     logging.info(f"更新基础表中的目录数据{code}")
    # 以上 是对基础表的修改， 上生产的时候直接复制盘货表即可，无需再次执行上面的代码
    # 以下 是活动的正式内容 ，上生产的时候需要执行

    logging.debug('秋季小药箱----------')
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
            list =  querySkuIdByTable(tableName,drugstoreId,where='1=1')
            logoList= []
            for dic in list:
                list_logo = dic['list_logo']
                sku_id=dic['sku_id']
                if list_logo =='家庭必备':
                    logoList.append(dic['sku_id'])
            
                # elif  list_logo =='疗程装':
                #     logoList.append(dic['sku_id'])
                #     addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',drugstoreId,skuIdList=logoList)
                # 限券
                if 'is_xq' in dic.keys() and dic['is_xq']!=None and dic['is_xq']==1:
                    copyAmStatInfoBySkuId( 78,sku_id)
                # huohao =  dic['pharmacy_huohao']
                # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)
            addPmLabelImage('家庭必备','http://image.ykd365.cn/act/202009/xyx/list.png','1',drugstoreId,skuIdList=logoList)
            logging.info('创建list logo------------')
            # 暂停疗程购
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=1') # 要下架
            stopPacket(tableName,drugstoreId,where = 'list_logo="疗程装"',stop=1) # 打标的上架一下
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=2',stop=1) # 要上架
            # 停掉一些疗程购， 标着疗程装的就上架打开
            logging.info('暂停疗程购------------')
            
            
            buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color,linkurl=linkurl,linkimg=linkimg,windowimg=windowimg)
            db.commit()
        except Exception as err:
            logging.error(err)
            db.rollback()
        logging.info('上完活动 记得执行下面的sql，解决本次特价和第二件半价活动商品，还有老2件92折活动的问题------------')


"""
SELECT a2.* from  am_stat_info a 
LEFT JOIN am_stat_info a2 
on a.sku_id = a2.sku_id 
-- and a.item_name = '特价'
where a.act_id =291
-- and a2.item_name = '2件92折、3件88折';
and a2.item_name = '第二件半价';
"""


def updateDate(tableName ='',pre_img = '',suf_img='',dirkv=[],itemkv = []):
    for dir in dirkv:
        wordList = pinyin(dir['name'], style=Style.FIRST_LETTER)
        code =''
        for item in wordList:
            code += ''.join(item)
        updateActTable(tableName,set=f"""dir_code='{code}'
                                ,dir_num='{dir['num']}'
                                ,dir_img='{pre_img}{code}{suf_img}'"""
                                ,where=f"dir_name='{dir['name']}'")
        db.commit()
        logging.info(f"更新基础表中的目录数据{code}")

    for dir in itemkv:
        wordList = pinyin(dir['item_name'], style=Style.FIRST_LETTER)
        code =''
        image = ''
        for item in wordList:
            code += ''.join(item)
        
        image = '' if dir['item_img'] =='' else  f'{pre_img}{code}{suf_img}'
        updateActTable(tableName
                    ,set=f"""item_code='{code}'
                    ,item_desc='{dir['item_desc']}'
                    ,item_type='{dir['item_type']}'
                    ,item_img='{image}'
                    ,item_img_r='{dir['item_img_r']}'
                    ,details_value='{dir['details_value']}'
                    ,rule_value='{dir['rule_value']}'"""
                        ,where=f"item_name='{dir['item_name']}'")
        db.commit()
        logging.info(f"更新基础表中的目录数据{code}")
    # 以上 是对基础表的修改， 上生产的时候直接复制盘货表即可，无需再次执行上面的代码

def update9GG( toDirName ='',ydIds = [],allImags=[],images=[],startTime='',endTime=''):
    for i in range(len(ydIds)):
        drugstoreId = ydIds[i]
        updateAllEnssence(ydIds[i],allImags[i])
        updateEnssence(ydIds[i],5,startTime,endTime,toDirName=toDirName,link_view='')
    db.commit()


def act1111(actId=0,actName = '',tableName ='',ydList = [],startTime='',endTime='',img = '',color = '',linkimg = '',linkurl = '',linkView = '',windowimg= ''):
    ''' 1.会场所有商品都加上详情页横图
        2. 满100-30  50 的活动在分别的盘货表中配置，主会场不用单独配 '''
    #  http://image.ykd365.cn/act/202011/1111/detail.jpg
#  646
   
    # 以下 是活动的正式内容 ，上生产的时候需要执行

    if actId==0:
        iAct = queryTableLastOne('am_act_info',field='act_id',where ='',order='act_id desc')
        iActId = iAct['act_id']
        actId = iActId+1
        logging.info(f'活动id：{actId}')
    
    for index in range(len(ydList)):
        try:
            drugstoreId = ydList[index]
            createDirByTable(actId=actId,drugstoreId=drugstoreId,act='双11狂欢')
            # 创建特价
            addPmActSale(tableName,drugstoreId,startTime,endTime)
            logging.info('创建价格------------')
            # # 列表页左上角标志
            list =  querySkuIdByTable(  tableName,drugstoreId,where='1=1')
            logoList =[]
          
            for dic in list:
                list_logo = dic['list_logo']
                sku_id=dic['sku_id']
                if list_logo =='双11狂欢购':
                    logoList.append(dic['sku_id'])
                # elif  list_logo =='疗程装':
                #     lczskuIdList.append(dic['sku_id'])
                
                # 限券
                if 'is_xq' in dic.keys() and dic['is_xq']!=None and dic['is_xq']==1:
                    copyAmStatInfoBySkuId( 78,sku_id)
                # huohao =  dic['pharmacy_huohao']
                # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)

            addPmLabelImage('双11狂欢购','http://image.ykd365.cn/act/202011/1111/list.png','1',drugstoreId,skuIdList=logoList)
           
            logging.info('创建list logo------------')
            # 暂停疗程购
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=1')
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=2',stop=1) # 代表如果有疗程购 则把疗程购多品上架
            logging.info('暂停疗程购-开启疗程购-----------')
            
            buildActInfoByTableWithChild(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color,linkurl=linkurl,linkimg=linkimg,windowimg=windowimg)
            db.commit()
        except Exception as err:
            logging.error(err)
            db.rollback()
    return actId



def 标准单会场活动(actId=0,actName = '',tableName ='',ydList = [],startTime='',endTime='',img = '',color = '',linkimg = '',linkurl = '',linkView = '',windowimg= ''):
    logging.debug('开始配置活动----------')
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
            list =  querySkuIdByTable(tableName,drugstoreId,where='1=1')
            logoList= []
            for dic in list:
                list_logo = dic['list_logo']
                sku_id=dic['sku_id']
                if list_logo =='1212':
                    logoList.append(dic['sku_id'])
            
                # elif  list_logo =='疗程装':
                #     logoList.append(dic['sku_id'])
                # 限券
                if 'is_xq' in dic.keys() and dic['is_xq']!=None and dic['is_xq']==1:
                    copyAmStatInfoBySkuId( 78,sku_id)
                # huohao =  dic['pharmacy_huohao']
                # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)
            addPmLabelImage(list_logo,'http://image.ykd365.cn/act/202012/1212/list.png','1',drugstoreId,skuIdList=logoList)
            logging.info('创建list logo------------')
            # 暂停疗程购
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=1') # 要下架
            stopPacket(tableName,drugstoreId,where = 'list_logo="疗程装"',stop=1) # 打标的上架一下
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=2',stop=1) # 要上架
            # 停掉一些疗程购， 标着疗程装的就上架打开
            logging.info('暂停疗程购------------')
            
            
            buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color,linkurl=linkurl,linkimg=linkimg,windowimg=windowimg)
            db.commit()
        except Exception as err:
            logging.error(err)
            db.rollback()
        logging.info('上完活动 记得执行下面的sql------------')

if __name__ == "__main__":
    # 手动把2件xx折活动商品的开始时间调整到双12活动的结束时间上
    logging.info(' 测试 药快到专用工具--------')
    tableName = 'as_test.202012_ty_1212'
    actName = '12·12 家庭备药一站购齐'
    start = '2010-12-04 00:00:00'  # 生产要改
    end = '2020-12-15 23:59:59'

    linkurl = 'http://deve.ykd365.com/html-activity/page/eleven/index.html?type=15&actId=865&dirId='  # 生产要改

    color = '#f44430'
    headimg = 'http://image.ykd365.cn/act/202012/1212/main.jpg'
    linkimg = 'http://image.ykd365.cn/act/202012/1212/lb.jpg'
    windowimg = 'http://image.ykd365.cn/act/202012/1212/tc.png'

    allimg = 'http://image.ykd365.cn/act/202011/1111/9gg.jpg'

    标准单会场活动(actId=0,actName = actName,tableName =tableName,ydList = [200]
        ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
        ,linkurl = linkurl
        ,linkView = '',windowimg= windowimg)


    # updateDate(tableName ='感恩季 滋补节',pre_img ='http://image.ykd365.cn/act/202011/gej/',suf_img='.jpg',dirkv=[{
    #   "name": "滋补爆品",
    #   "num": "02",
    # },{
    #  "name": "长辈专区",
    #   "num": "04",
    # },{
    #  "name": "男士专区",
    #   "num": "06",
    # },{
    #  "name": "女士专区",
    #   "num": "08",
    #   "code":"nvszq"
    # },{
    #  "name": "儿童专区",
    #   "num": "10",
    # }],itemkv = [
    #         {'item_name': '2件92折、3件88折', 'item_desc': '2件92折、3件88折', 'item_code': 'd292388'
    #         , 'item_img': ''
    #         , 'item_img_r': '', 'num': 100, 'item_type': 'discount'
    #         , 'details_value': '92,88', 'rule_value': '2,3', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''},
            
    #         {'item_name': '满199减100', 'item_desc': '满199减100' 
    #         ,'item_img':'http://image.ykd365.cn/act/202011/gej/detail.jpg'
    #         , 'item_img_r': '642', 'num': 100, 'item_type': 'discount'
    #         , 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''},
    #         {'item_name': '满99减50', 'item_desc': '满99减50' 
    #         ,'item_img':'http://image.ykd365.cn/act/202011/gej/detail.jpg'
    #         , 'item_img_r': '642', 'num': 100, 'item_type': 'cut'
    #         , 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''}
            
    #    ])



    
    # tableName = 'as_test.202011_ty_1111'
    # actName = '双11狂欢购'
    # start = '2020-11-10 00:00:00'  # 生产要改
    # end = '2020-11-20 23:59:59'

    # linkurl = 'http://store.ykd365.com/html-activity/page/eleven/index.html?type=15&actId=865&dirId='  # 生产要改

    # color = ''
    # headimg = 'http://image.ykd365.cn/act/202011/1111/24.jpg'
    # linkimg = 'http://image.ykd365.cn/act/202011/1111/lb.jpg'
    # windowimg = 'http://image.ykd365.cn/act/202011/1111/tc.png'

    # allimg = 'http://image.ykd365.cn/act/202011/1111/9gg.jpg'

    # itemkv=[
    #         {'item_name': '2件92折，3件88折', 'item_desc': '2件92折，3件88折', 'item_code': 'd292388'
    #         , 'item_img': ''
    #         , 'item_img_r': '', 'num': 100, 'item_type': 'discount'
    #         , 'details_value': '92,88', 'rule_value': '2,3', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''},
        
    #         {'item_name': '特价', 'item_desc': '特价' ,'item_code': 'tj'
    #         ,'item_img':''
    #         , 'item_img_r': '', 'num': 100, 'item_type': 'discount'
    #         , 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None
    #         , 'kc_day': None, 'act_name': ''}
             
            
    #    ]

    # for dir in itemkv:
    #     updateActTable(tableName,set=f"""item_code='{dir['item_code']}',item_desc='{dir['item_desc']}',item_type='{dir['item_type']}',item_img='{dir['item_img']}',item_img_r='{dir['item_img_r']}',details_value='{dir['details_value']}',rule_value='{dir['rule_value']}'""",where=f"item_name='{dir['item_name']}'")
    # db.commit()

    # act1111(actId=0,actName = actName,tableName =tableName,ydList = [200]
    #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
    #     ,linkurl = linkurl
    #     ,linkView = '',windowimg= windowimg)
    # update9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)

    #  三件事没做，两个满100减xx的盘货表没处理，所以需要把盘货表里的商品加到对应目录下
    # 给满100减xx的商品 加上列表页角标 （主会场和分会场的已经加过了）
    # 给满100减xx的商品加上详情页的横图 （追会场和分会场已经加过了）
# INSERT INTO `medstore`.`pm_sku_dir` (  `dir_id`, `sku_id`, `dir_code`, `sku_order`, `update_time`, `is_show`) 
# SELECT '1002764938',s.sku_id,'1000act2935030',100,NOW(),0 from as_test.202011_ty_满100减50所有商品 a ,pm_prod_sku s where a.货号 = s.pharmacy_huohao and s.drugstore_id =200;

# INSERT INTO `medstore`.`pm_sku_dir` (  `dir_id`, `sku_id`, `dir_code`, `sku_order`, `update_time`, `is_show`) 
# SELECT '1002764938',s.sku_id,'1000act2935030',100,NOW(),0 from as_test.202011_ty_满100减30所有商品 a ,pm_prod_sku s where a.货号 = s.pharmacy_huohao and s.drugstore_id =200;

# INSERT INTO `medstore`.`pm_sku_dir` (  `dir_id`, `sku_id`, `dir_code`, `sku_order`, `update_time`, `is_show`) 
# SELECT '1002764939',s.sku_id,'1000act29310050',100,NOW(),0 from as_test.202011_ty_满100减50所有商品 a ,pm_prod_sku s where a.货号 = s.pharmacy_huohao and s.drugstore_id =200;

#  INSERT INTO `medstore`.`pm_sku_dir` (  `dir_id`, `sku_id`, `dir_code`, `sku_order`, `update_time`, `is_show`) 
# SELECT '1002764940',s.sku_id,'1000act29310030',100,NOW(),0 from as_test.202011_ty_满100减30所有商品 a ,pm_prod_sku s where a.货号 = s.pharmacy_huohao and s.drugstore_id =200;

## 上面是将满100减50和满100减30的所有商品放到对应目录 
# 下面是将满100减50和满100减30的所有商品 添加列表页角标

# -- INSERT INTO `medstore`.`pm_label_image` ( `label_name`, `label_url`, `label_url_double`, `label_type`, `label_status`, `label_create_time`, `label_update_time`, `pharmacy_id`, `label_flag`, `sku_id`, `label_start_time`, `label_end_time`) 
# SELECT '双11狂欢购', 'http://image.ykd365.cn/act/202011/1111/list.png', 'http://image.ykd365.cn/act/202011/1111/list.png',
#  '1', '1', NOW(), NOW(), '200', '0', sku_id,'2020-11-03 00:00:00','2020-11-15 23:59:59'
#  from as_test.202011_ty_满100减50所有商品 a ,pm_prod_sku s where a.货号 = s.pharmacy_huohao and s.drugstore_id =200;

# -- INSERT INTO `medstore`.`pm_label_image` ( `label_name`, `label_url`, `label_url_double`, `label_type`, `label_status`, `label_create_time`, `label_update_time`, `pharmacy_id`, `label_flag`, `sku_id`, `label_start_time`, `label_end_time`) 
# SELECT '双11狂欢购', 'http://image.ykd365.cn/act/202011/1111/list.png', 'http://image.ykd365.cn/act/202011/1111/list.png',
#  '1', '1', NOW(), NOW(), '200', '0', sku_id,'2020-11-03 00:00:00','2020-11-15 23:59:59'
#  from as_test.202011_ty_满100减30所有商品 a ,pm_prod_sku s where a.货号 = s.pharmacy_huohao and s.drugstore_id =200;

#  下面是给所有商品加上详情页的横图



# INSERT INTO am_stat_info(  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark`, `item_name`, `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`, `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`, `is_show`) 
# -- VALUES ('37674943', '20200305224320', '100329', '194', '1438', NULL, '疗程购', 'single', '2020-03-05 22:52:50', '2020-03-05 22:52:50', '2019-05-01 00:00:00', '2020-12-30 23:59:59', 'drugtag', '{\"itemImageR\":\"436\"}', NULL, NULL, '100', '0');
# SELECT '20200305224320', s.sku_id, '292', '1864', NULL, '双11', 'single', NOW(), NOW()
# , '2020-11-10 00:00:00', '2020-11-20 23:59:59', 'drugtag'
# , '{"itemImageR":"646","itemImage":"http://image.ykd365.cn/act/202011/1111/detail.jpg"}', NULL, NULL, '100', '0'
# from as_test.202011_ty_满100减50所有商品 a ,pm_prod_sku s where a.货号 = s.pharmacy_huohao and s.drugstore_id =200
# and s.sku_id not in (
#   select sku_id from  am_stat_info where act_id =292 and item_id =1864
# );


# INSERT INTO am_stat_info(  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark`, `item_name`, `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`, `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`, `is_show`) 
# -- VALUES ('37674943', '20200305224320', '100329', '194', '1438', NULL, '疗程购', 'single', '2020-03-05 22:52:50', '2020-03-05 22:52:50', '2019-05-01 00:00:00', '2020-12-30 23:59:59', 'drugtag', '{\"itemImageR\":\"436\"}', NULL, NULL, '100', '0');
# SELECT '20200305224320', s.sku_id, '292', '1864', NULL, '双11', 'single', NOW(), NOW()
# , '2020-11-10 00:00:00', '2020-11-20 23:59:59', 'drugtag'
# , '{"itemImageR":"646","itemImage":"http://image.ykd365.cn/act/202011/1111/detail.jpg"}', NULL, NULL, '100', '0'
# from as_test.202011_ty_满100减30所有商品 a ,pm_prod_sku s where a.货号 = s.pharmacy_huohao and s.drugstore_id =200
# and s.sku_id not in (
#   select sku_id from  am_stat_info where act_id =292 and item_id =1864
# );




# INSERT INTO am_stat_info(  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark`, `item_name`, `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`, `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`, `is_show`) 
# -- VALUES ('37674943', '20200305224320', '100329', '194', '1438', NULL, '疗程购', 'single', '2020-03-05 22:52:50', '2020-03-05 22:52:50', '2019-05-01 00:00:00', '2020-12-30 23:59:59', 'drugtag', '{\"itemImageR\":\"436\"}', NULL, NULL, '100', '0');
# SELECT '20200305224320', s.sku_id, '292', '1864', NULL, '双11', 'single', NOW(), NOW()
# , '2020-11-10 00:00:00', '2020-11-20 23:59:59', 'drugtag'
# , '{"itemImageR":"646","itemImage":"http://image.ykd365.cn/act/202011/1111/detail.jpg"}', NULL, NULL, '100', '0'
# from as_test.202011_ty_1111 a ,pm_prod_sku s where a.huohao = s.pharmacy_huohao and s.drugstore_id =200
# and s.sku_id not in (
#   select sku_id from  am_stat_info where act_id =292 and item_id =1864
# );


# INSERT INTO am_stat_info(  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark`, `item_name`, `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`, `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`, `is_show`) 
# -- VALUES ('37674943', '20200305224320', '100329', '194', '1438', NULL, '疗程购', 'single', '2020-03-05 22:52:50', '2020-03-05 22:52:50', '2019-05-01 00:00:00', '2020-12-30 23:59:59', 'drugtag', '{\"itemImageR\":\"436\"}', NULL, NULL, '100', '0');
# SELECT '20200305224320', s.sku_id, '293', '1864', NULL, '双11', 'single', NOW(), NOW()
# , '2020-11-05 00:00:00', '2020-11-15 23:59:59', 'drugtag'
# , '{"itemImageR":"646","itemImage":"http://image.ykd365.cn/act/202011/1111/detail.jpg"}', NULL, NULL, '100', '0'
# -- SELECT *
# from as_test.202011_ty_1111 a ,pm_prod_sku s where a.huohao = s.pharmacy_huohao and s.drugstore_id =200
# and a.xh《400;



# INSERT INTO am_stat_info(  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark`, `item_name`, `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`, `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`, `is_show`) 
# -- VALUES ('37674943', '20200305224320', '100329', '194', '1438', NULL, '疗程购', 'single', '2020-03-05 22:52:50', '2020-03-05 22:52:50', '2019-05-01 00:00:00', '2020-12-30 23:59:59', 'drugtag', '{\"itemImageR\":\"436\"}', NULL, NULL, '100', '0');
# SELECT '20200305224320', s.sku_id, '293', '1864', NULL, '双11', 'single', NOW(), NOW()
# , '2020-11-05 00:00:00', '2020-11-15 23:59:59', 'drugtag'
# , '{"itemImageR":"646","itemImage":"http://image.ykd365.cn/act/202011/1111/detail.jpg"}', NULL, NULL, '100', '0'
# from as_test.202011_ty_满100减50所有商品 a ,pm_prod_sku s where a.货号 = s.pharmacy_huohao and s.drugstore_id =200;

# INSERT INTO am_stat_info(  `batch_num`, `sku_id`, `act_id`, `item_id`, `item_remark`, `item_name`, `item_attr`, `stat_update_time`, `stat_create_time`, `item_effect_time`, `item_expire_time`, `item_type`, `other_str1`, `quota_id`, `item_flag`, `item_priority`, `is_show`) 
# -- VALUES ('37674943', '20200305224320', '100329', '194', '1438', NULL, '疗程购', 'single', '2020-03-05 22:52:50', '2020-03-05 22:52:50', '2019-05-01 00:00:00', '2020-12-30 23:59:59', 'drugtag', '{\"itemImageR\":\"436\"}', NULL, NULL, '100', '0');
# SELECT '20200305224320', s.sku_id, '293', '1864', NULL, '双11', 'single', NOW(), NOW()
# , '2020-11-05 00:00:00', '2020-11-15 23:59:59', 'drugtag'
# , '{"itemImageR":"646","itemImage":"http://image.ykd365.cn/act/202011/1111/detail.jpg"}', NULL, NULL, '100', '0'
# from as_test.202011_ty_满100减30所有商品 a ,pm_prod_sku s where a.货号 = s.pharmacy_huohao and s.drugstore_id =200;


    # actName = '家庭必备小药箱'
    # start = '2020-10-12 00:00:00'
    # end = '2020-11-06 23:59:59'

    # linkurl = 'http://store.ykd365.com/medstore/actUserpage/medicineKit_2010?pageSize=1000&dirId='

    # color = '#deedef'
    # headimg = 'http://image.ykd365.cn/act/202009/xyx/02.jpg'
    # linkimg = 'http://image.ykd365.cn/act/202009/xyx/lb.jpg'
    # windowimg = 'http://image.ykd365.cn/act/202009/xyx/tc.png'

    # allimg = 'http://image.ykd365.cn/act/202009/xyx/9gg.jpg'



    # # 秋季小药箱(actId=0,actName = actName,tableName ='as_test.202009_ty_xyx',ydList = [200]
    # #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
    # #     ,linkurl = linkurl
    # #     ,linkView = '',windowimg= windowimg)
    # update9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)

#  需要把盘货表里标记疗程转的给上架一下多盒装
    # stopPacket('as_test.202009_ty_xyx',200,where = 'stop_lcz=2',stop=1) # 要上架
    # db.commit()

    # actName = '健康好礼嗨购季'
    # start = '2020-09-25 00:00:00'
    # end = '2020-10-11 23:59:59'

    # # linkurl = 'http://store.ykd365.com/medstore/actUserpage/medicineKit_2008?pageSize=1000&dirId='
    # linkurl = 'http://store.ykd365.com/medstore/actUserpage/moon_2010?pageSize=1000&dirId='

    # color = '#deedef'
    # headimg = 'http://image.ykd365.cn/act/202009/zq/02.png'
    # linkimg = 'http://image.ykd365.cn/act/202009/zq/lb.jpg'
    # windowimg = 'http://image.ykd365.cn/act/202009/zq/tc.png'

    # allimg = 'http://image.ykd365.cn/act/202009/zq/ty_9gg.jpg'



    # # 中秋国庆(actId=0,actName = actName,tableName ='as_test.202009_ty_zq',ydList = [200]
    # #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
    # #     ,linkurl = linkurl
    # #     ,linkView = '',windowimg= windowimg)
    # update国庆中秋9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)

    # 新商品打下单返券和30分钟必达的标()


    # actName = '开学必备小药箱'
    # linkurl = 'http://store.ykd365.com/medstore/actUserpage/medicineKit_2008?pageSize=1000&dirId='
    # start = '2020-08-29 00:00:00'
    # end = '2020-09-10 23:59:59'
    # # linkurl = '' 
    # # start = '2020-06-15 21:00:00'

    
    # color = '#deedef'
    # headimg = 'http://image.ykd365.cn/act/202008/kx/02.jpg'
    # linkimg = 'http://image.ykd365.cn/act/202008/kx/lb.jpg'
    # windowimg = 'http://image.ykd365.cn/act/202008/kx/tc.png'
    # # updateact8月开学必备小药箱活动('as_test.202008_ty_kx')
    # # updateact8月开学必备小药箱活动('as_test.202008_xc_kx')
    
    # act8月开学必备小药箱活动(actId=0,actName = actName,tableName ='as_test.202008_ty_kx',ydList = [200]
    #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
    #     ,linkurl = linkurl
    #     ,linkView = '',windowimg= windowimg)

    # act8月开学必备小药箱活动(actId=0,actName = actName,tableName ='as_test.202008_xc_kx',ydList = [1600,1601,1602,1603]
    #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
    #     ,linkurl = linkurl
    #     ,linkView = '',windowimg= windowimg)

    # 忘记特价价格了()
    # update9GG()

#     UPDATE  am_stat_info   a1 ,  am_stat_info   a2
# set a2.item_expire_time = '2010-12-31 23:59:59'
# where a1.sku_id = a2.sku_id 
# and a1.item_name like '%3件85%'
# and a2.item_name like '%3件88%'
# ; 
    logging.info(' over --------')

# http://image.ykd365.cn/act/202005/lcg_list.png
# http://image.ykd365.cn/act/1906/1906_list3.png
# http://image.ykd365.cn/act/1910/drug_list_2.png
# http://image.ykd365.cn/act/202005/mqj/lcz_logo.png


# http://image.ykd365.cn/act/1906/1906_list3.png
# http://image.ykd365.cn/act/1910/drug_list_2.png
# http://image.ykd365.cn/act/2002/notouch/list88.png
# http://image.ykd365.cn/act/202005/lcg_list.png
# http://image.ykd365.cn/act/202005/mqj/lcz_logo.png
# http://image.ykd365.cn/act/202006/fqj/bkzj.png
# http://image.ykd365.cn/act/202008/kx/list_logo.png
# http://image.ykd365.cn/act/202009/zq/list.png
# http://image.ykd365.cn/drugstore/list.png


# http://image.ykd365.cn/act/1906/1906_list3.png
# http://image.ykd365.cn/act/1910/drug_list_2.png
# http://image.ykd365.cn/act/2002/notouch/list.png
# http://image.ykd365.cn/act/2002/notouch/list88.png
# http://image.ykd365.cn/act/202005/lcg_list.png
# http://image.ykd365.cn/act/202005/mqj/lcz_logo.png
# http://image.ykd365.cn/act/202005/mqj/mqj_logo.png
# http://image.ykd365.cn/act/202005/xyx/list_jtbb.png
# http://image.ykd365.cn/act/202005/xz/xz_logo.png
# http://image.ykd365.cn/act/202006/fqj/bkzj.png
# http://image.ykd365.cn/act/202008/kx/list_logo.png
# http://image.ykd365.cn/act/202009/zq/list.png
# http://image.ykd365.cn/drugstore/list.png 

