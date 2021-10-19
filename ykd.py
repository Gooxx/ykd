# from db2 import db,cursor,querySQL,updateSQL,insertSQL,selectBy,selectOneBy
# import time
# import datetime
# import json
# import logging
# import xlwt
from act import *
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

# def update9GG():
#     ydIds=[200,1600,1601,1602,1603]

#     images=[
#         'http://image.ykd365.cn/act/202008/kx/ty_9gg.jpg','http://image.ykd365.cn/act/202008/kx/xc_9gg.jpg','http://image.ykd365.cn/act/202008/kx/xc_9gg.jpg','http://image.ykd365.cn/act/202008/kx/xc_9gg.jpg','http://image.ykd365.cn/act/202008/kx/xc_9gg.jpg'
#     ]
#     queryTable('pm_dir_info')
#     start = '2020-08-29 00:00:00'
#     end = '2020-09-10 23:59:59'
#     toDirName='开学必备小药箱'
#     # url = 
#     for i in range(len(ydIds)):
#         # if i==0:
#         updateAllEnssence(ydIds[i],images[i])
#         updateEnssence(ydIds[i],5,start,end,toDirName=toDirName,link_view='')
#         # else:
#         #     logging.info(i)
#     db.commit()
    
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
    # pre_img,suf_img 图片的前后缀
def 自动补充目录信息(tableName,dirList,pre_img,suf_img='.jpg'):
    # dirList 中的map 格式为 {name:''}
    for index,dir in enumerate(dirList):
        wordList = pinyin(dir['name'], style=Style.FIRST_LETTER)
        name = dir['name']
        code =''
        num = index+1
        for item in wordList:
            code += ''.join(item)
        updateActTable(tableName,set=f"""dir_code='{code}',dir_num='{num}',dir_img='{pre_img}{num}{suf_img}'""",where=f"dir_name='{name}'")
        db.commit()
        logging.info(f"更新基础表中的目录数据{code}")
# 
def 自动补充活动信息(tableName,itemList,pre_img,suf_img='.jpg'):
    # {'item_name':'活动名','item_desc':'描述','item_type': 'discount','item_img':'中间那段就行','item_img_r': '宽高比', 'details_value': '92,88', 'rule_value': '2,3', 'quota_rule': None, 'quota_group': None}
            # , 'kc_day': None, 'act_name': ''}
            # {'item_name': '2件92折、3件88折', 'item_desc': '2件92折、3件88折', 'item_code': 'd292388'
            # , 'item_img': ''
            # , 'item_img_r': '', 'num': 100, 'item_type': 'discount'
            # , 'details_value': '92,88', 'rule_value': '2,3', 'quota_rule': None, 'quota_group': None
            # , 'kc_day': None, 'act_name': ''},
            # {'item_name': '3件85折', 'item_desc': '3件85折', 'item_code': 'd385'
            # , 'item_img': f'{pre_img}detail{suf_img}'
            # , 'item_img_r': '643', 'num': 100, 'item_type': 'discount'
            # , 'details_value': '85', 'rule_value': '3', 'quota_rule': None, 'quota_group': None
            # , 'kc_day': None, 'act_name': ''},
    #    ]
 
    for index,item in enumerate(itemList):
        wordList = pinyin(item['item_name'], style=Style.FIRST_LETTER)
        item_name = item['item_name']
        num = index
        item_img = item['item_img'] if 'item_img' in item else ''
        item_img_r=  item['item_img_r']
        item_desc = item['item_desc']
        item_type = item['item_type']
        rule_value=  item['rule_value']
        details_value = item['details_value']
        code =''
        image = ''
        for word in wordList:
            code += ''.join(word)
        # 
        image = '' if item_img =='' else  f'{pre_img}{item_img}{suf_img}'

        updateActTable(tableName,set=f"""item_code='{code}',item_desc='{item_desc}',item_type='{item_type}',item_img='{image}',item_img_r='{item_img_r}',details_value='{details_value}',rule_value='{rule_value}'""",where=f"item_name='{item_name}'")
        db.commit()
        logging.info(f"更新基础表中的目录数据{code}")
    # 以上 是对基础表的修改， 上生产的时候直接复制盘货表即可，无需再次执行上面的代码
    # 以下 是活动的正式内容 ，上生产的时候需要执行

def 标准单会场活动(actId=0,actName = '',tableName ='',ydList = [],startTime='',endTime='',img = '',color = '',linkimg = '',linkurl = '',linkView = '',windowimg= '',listimg='',detailJump=False):
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
                # if list_logo =='年终盛典':
                #     logoList.append(dic['sku_id'])
                if list_logo !='':
                    logoList.append(dic['sku_id'])
                # elif  list_logo =='疗程装':
                #     logoList.append(dic['sku_id'])
                # 限券
                if 'is_xq' in dic.keys() and dic['is_xq']!=None and dic['is_xq']==1:
                    copyAmStatInfoBySkuId( 78,sku_id)
                # huohao =  dic['pharmacy_huohao']
                # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)
            addPmLabelImage(list_logo,listimg,'1',drugstoreId,skuIdList=logoList,start=startTime,end=endTime)
            logging.info('创建list logo------------')
            # 暂停疗程购
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=1') # 要下架
            stopPacket(tableName,drugstoreId,where = 'list_logo="疗程装"',stop=1) # 打标的上架一下
            stopPacket(tableName,drugstoreId,where = 'stop_lcz=2',stop=1) # 要上架
            # 停掉一些疗程购， 标着疗程装的就上架打开
            logging.info('暂停疗程购------------')
            
            
            buildActInfoByTable(tableName,actId,actName,drugstoreId,startTime=startTime,endTime=endTime,img=img,color=color,linkurl=linkurl,linkimg=linkimg,windowimg=windowimg,detailJump=detailJump)
            db.commit()
        except Exception as err:
            logging.error(err)
            db.rollback()
        logging.info('上完活动 记得执行下面的sql------------')

if __name__ == "__main__":
    logging.info(' 测试 药快到专用工具--------')
    # 2021.10.10-2021.11.15
    tableName = 'as_test.202110_ty_qdhj'
    actId = 0
    actName = '秋冬换季 家庭常用药清单'
    start = '2021-10-09 00:00:00'  #s 生产要改
    end = '2021-11-15 23:59:59' 

    linkurl = 'http://store.ykd365.com/html-activity/page/familyCommonly/index.html?type=15&actId=881&dirId='  # 生产要改

    color = '#f91549'
    imagePre = 'http://image.ykd365.cn/act/2021/10/qiudong/'
    headimg = f"{imagePre}head.jpg"
    linkimg = f'{imagePre}lb.jpg'
    windowimg = f'{imagePre}tc.png' 
# http://image.ykd365.cn/act/2021/9/101/9gg.png
    allimg = f'{imagePre}9gg.jpg' 

    listimg = f'{imagePre}list.png'
    # 自动补充目录信息(tableName,[{'name':'感冒咳嗽'},{'name':'慢性支气管炎'},{'name':'哮喘'},{'name':'心脑血管'},{'name':'消化系统'},{'name':'小儿秋季腹泻'},{'name':'鼻炎'}],imagePre,suf_img='.jpg')

    # 自动补充活动信息(tableName,[{'item_name':'2件92折、3件88折','item_desc':'任意2件92折、3件88折','item_type': 'discount','item_img':'detail','item_img_r': '391', 'details_value': '92,88', 'rule_value': '2,3', 'quota_rule': None, 'quota_group': None}],imagePre,suf_img='.png')
    
    标准单会场活动(actId=actId,actName = actName,tableName =tableName,ydList = [200]
        ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
        ,linkurl = linkurl
        ,linkView = '',windowimg= windowimg
        ,listimg=listimg,detailJump=True)
    update9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)

    logging.info(' over --------')
# // 有老的2件xx折, 把开始时间放到 11-15 这样本次活动结束的时候,正常活动继续
"""
UPDATE  as_test.202110_ty_qdhj a LEFT JOIN pm_prod_sku s on a.huohao = s.pharmacy_huohao
LEFT JOIN am_stat_info stat on s.sku_id = stat.sku_id 
SET stat.item_effect_time = '2021-11-15 23:59:59'
WHERE s.drugstore_id = 200
and stat.item_remark like '2件92折、3件88折'
and stat.item_expire_time > now()
;

INSERT INTO `medstore`.`sm_image_link`(  `drugstore_id`, `seq_num`, `image_url`, `link_url`, `link_type`, `link_name`, `link_param`, `link_status`, `link_update_time`, `link_create_time`, `link_remark`, `link_start_time`, `link_end_time`, `link_view`, `link_version`, `link_button_type`) VALUES (  200, 1, 'http://image.ykd365.cn/act/2021/10/qiudong/tl.jpg', 'http://deve.ykd365.com/html-activity/page/familyCommonly/index.html?type=15&actId=881&dirId=1002765294', 'web2', '秋冬换季 家庭常用药清单', 1002765294, 1, '2021-10-09 10:32:47', '2021-10-09 10:29:12', '{\"aspect_ratio\":431,\"having_line\":0,\"image_seat\":1}', '2020-10-10 00:00:00', '2021-11-15 23:59:59', 'activity', 1, NULL);

"""








    # 2021.9.10-2021.10.10
#     tableName = 'as_test.202109_ty_101'
#     actId = 0
#     actName = '中秋&国庆 团圆健康礼'
#     start = '2021-09-10 21:00:00'  #s 生产要改
#     end = '2021-10-10 23:59:59' 

#     linkurl = 'http://store.ykd365.com/html-activity/page/midFestival/index.html?type=15&actId=881&dirId='  # 生产要改

#     color = '#f91549'
#     imagePre = 'http://image.ykd365.cn/act/2021/9/101/'
#     headimg = f"{imagePre}head.jpg"
#     linkimg = f'{imagePre}lb.jpg'
#     windowimg = f'{imagePre}tc.png' 
# # http://image.ykd365.cn/act/2021/9/101/9gg.png
#     allimg = f'{imagePre}9gg.png' 

#     listimg = f'{imagePre}list.png'
#     # 自动补充目录信息(tableName,[{'name':'健康礼首选'},{'name':'初秋滋补'},{'name':'儿童营养'},{'name':'调节三高'},{'name':'维生素钙'}],imagePre,suf_img='.jpg')

#     # 自动补充活动信息(tableName,[{'item_name':'满99减50,满199减100','item_desc':'团圆健康礼 满99减50,团圆健康礼 满199减100','item_type': 'discount','item_img':'detail','item_img_r': '444', 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None},{'item_name':'团圆健康礼','item_desc':'团圆健康礼','item_type': 'drugtag','item_img':'detail','item_img_r': '444', 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None}],imagePre,suf_img='.png')
    
#     # 标准单会场活动(actId=actId,actName = actName,tableName =tableName,ydList = [200]
#     #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
#     #     ,linkurl = linkurl
#     #     ,linkView = '',windowimg= windowimg
#     #     ,listimg=listimg,detailJump=True)
#     update9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)


# 1.配置通栏
# 2.把满99减50 的优先级顺序改为 201, 慢199减100改为200 item_priority







    # tableName = 'as_test.202106_ty_xyx'
    # actId = 0
    # actName = '家庭必备小药箱'
    # start = '2021-06-29 00:00:00'  #s 生产要改
    # end = '2021-08-15 23:59:59'

    # # html-activity\page\summerMed
    # linkurl = 'http://store.ykd365.com/html-activity/page/summerMed/index.html?type=15&actId=878&dirId='  # 生产要改

    # color = '#f91549'
    # imagePre = 'http://image.ykd365.cn/act/2021/6/xyx/'
    # headimg = f"{imagePre}head.jpg"
    # linkimg = f'{imagePre}lb.jpg'
    # windowimg = f'{imagePre}tc.png'

    # allimg = f'{imagePre}9gg.jpg' 

    # listimg = f'{imagePre}list.png'


 

    # # 自动补充目录信息(tableName,[{'name':'清热解暑'},{'name':'蚊虫叮咬'},{'name':'夏季感冒'},{'name':'肠胃用药'},{'name':'日常防护'}],imagePre,suf_img='.jpg')

    # # 自动补充活动信息(tableName,[{'item_name':'2件92折，3件88折','item_desc':'2件92折，3件88折','item_type': 'discount','item_img':'detail','item_img_r': '391', 'details_value': '92,88', 'rule_value': '2,3', 'quota_rule': None, 'quota_group': None},{'item_name':'清凉一夏','item_desc':'清凉一夏','item_type': 'drugtag','item_img':'detail','item_img_r': '391', 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None}],imagePre,suf_img='.png')
    
    # 标准单会场活动(actId=actId,actName = actName,tableName =tableName,ydList = [200]
    #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
    #     ,linkurl = linkurl
    #     ,linkView = '',windowimg= windowimg
    #     ,listimg=listimg,detailJump=True)
    # update9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)




#            6月10日-6月15日 品牌日  大牌价到 满99减50
# 6月16日-6月18日  爆品特价 限量开抢
# 6月19-6月25日  返场特惠 满98减18
    # tableName = 'as_test.202106_ty_618p3'
    # actId = 0
    # actName = '618年中大促'
    # start = '2021-06-18 20:00:00'  #s 生产要改
    # end = '2021-06-25 23:59:59'

    
    # linkurl = 'http://store.ykd365.com/html-activity/page/618/index_e.html?type=15&actId=878&dirId='  # 生产要改

    # color = '#f91549'
    # imagePre = 'http://image.ykd365.cn/act/2021/6/618/3/'
    # headimg = f"{imagePre}head.jpg"
    # linkimg = f'{imagePre}lb.jpg'
    # windowimg = f'{imagePre}tc.png'

    # allimg = f'{imagePre}9gg.jpg' 

    # listimg = f'{imagePre}list.png'


 

    # # 自动补充目录信息(tableName,[{'name':'精选推荐'},{'name':'家庭必备'},{'name':'慢病健康'},{'name':'女性健康'},{'name':'男性健康'},{'name':'儿童健康'}],imagePre,suf_img='.jpg')

    # # 自动补充活动信息(tableName,[{'item_name':'满98减18','item_desc':'领券满98减18','item_type': 'discount','item_img':'detail','item_img_r': '373', 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None},{'item_name':'618','item_desc':'618年中大促','item_type': 'drugtag','item_img':'detail','item_img_r': '373', 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None}],imagePre,suf_img='.png')
    
    # 标准单会场活动(actId=actId,actName = actName,tableName =tableName,ydList = [200]
    #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
    #     ,linkurl = linkurl
    #     ,linkView = '',windowimg= windowimg
    #     ,listimg=listimg,detailJump=True)

# 然后需要 第二期的活动从 stat中结束掉
# sm_image_link_window
# sm_image_link



    # tableName = 'as_test.202106_ty_618p2'
    # actId = 0
    # actName = '618年中大促'
    # start = '2021-06-15 18:00:00'  #s 生产要改
    # end = '2021-06-18 23:59:59'

    
    # linkurl = 'http://store.ykd365.com/html-activity/page/618/index_c.html?type=15&actId=876&dirId='  # 生产要改

    # color = '#f91549'
    # imagePre = 'http://image.ykd365.cn/act/2021/6/618/2/'
    # headimg = f"{imagePre}head.jpg"
    # linkimg = f'{imagePre}lb.jpg'
    # windowimg = f'{imagePre}tc.png'

    # allimg = f'{imagePre}9gg.jpg' 

    # listimg = f'{imagePre}list.png'


    # imagePre2 = 'http://image.ykd365.cn/act/2021/6/618/2/'
    # # 爆品开抢和家庭必备 
    # # 自动补充目录信息(tableName,[{'name':'爆品开抢'},{'name':'家庭必备'},{'name':'慢病健康'},{'name':'女性健康'},{'name':'男性健康'},{'name':'儿童健康'}],imagePre2,suf_img='.jpg')

    # # 自动补充活动信息(tableName,[{'item_name':'特价','item_desc':'618嗨购，爆品特价限量抢','item_type': 'quota','item_img':'detail','item_img_r': '373', 'details_value': '', 'rule_value': '', 'quota_rule': '1:2:6', 'quota_group': '0'},
    # # {'item_name':'2件5折','item_desc':'同品2件5折','item_type': 'discount','item_img':'detail','item_img_r': '373', 'details_value': '50', 'rule_value': '2', 'quota_rule': None, 'quota_group': None},
    # # {'item_name':'2件8折','item_desc':'同品2件8折','item_type': 'discount','item_img':'detail','item_img_r': '373', 'details_value': '80', 'rule_value': '2', 'quota_rule': None, 'quota_group': None}
    # # ,{'item_name':'2件9折','item_desc':'同品2件9折','item_type': 'discount','item_img':'detail','item_img_r': '373', 'details_value': '90', 'rule_value': '2', 'quota_rule': None, 'quota_group': None}],imagePre,suf_img='.png')
    
    # 标准单会场活动(actId=actId,actName = actName,tableName =tableName,ydList = [200]
    #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
    #     ,linkurl = linkurl
    #     ,linkView = '',windowimg= windowimg
    #     ,listimg=listimg,detailJump=True)
    # # update9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)





    # tableName = 'as_test.202106_ty_618'
    # actId = 0
    # actName = '618年中大促'
    # start = '2021-06-09 17:00:00'  #s 生产要改
    # end = '2021-06-14 23:59:59'
 

    
    # linkurl = 'http://store.ykd365.com/html-activity/page/618/index.html?type=15&actId=876&dirId='  # 生产要改

    # color = '#f91549'
    # imagePre = 'http://image.ykd365.cn/act/2021/6/618/'
    # headimg = f"{imagePre}head.jpg"
    # linkimg = f'{imagePre}lb.jpg'
    # windowimg = f'{imagePre}tc.png'

    # allimg = f'{imagePre}9gg.jpg' 

    # listimg = f'{imagePre}list.png'

    # # 自动补充目录信息(tableName,[{'name':'同仁堂'},{'name':'汤臣倍健'},{'name':'九芝堂'},{'name':'云南白药'},{'name':'修正'},{'name':'白云山'},{'name':'步长'},{'name':'葵花'},{'name':'仁和'},{'name':'太极'}],imagePre,suf_img='.jpg')
    # # 自动补充活动信息(tableName,[{'item_name':'满99减50,满199减100','item_desc':'618嗨购领券满99减50,618嗨购领券满199减100','item_type': 'discount','item_img':'detail','item_img_r': '373', 'details_value': '', 'rule_value': '', 'quota_rule': None, 'quota_group': None}],imagePre,suf_img='.png')
    
    # 标准单会场活动(actId=actId,actName = actName,tableName =tableName,ydList = [200]
    #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
    #     ,linkurl = linkurl
    #     ,linkView = '',windowimg= windowimg
    #     ,listimg=listimg,detailJump=True)
    # update9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)
# 
# -- 儿童节活动结束掉，给618活动让路 
# -- UPDATE am_stat_info a LEFT JOIN am_stat_info b on a.sku_id = b.sku_id 
# set b.item_expire_time = '2020-06-14 23:59:59'
# where a.act_id = 313
# and b.act_id = 310;

# SELECT * from am_stat_info a LEFT JOIN am_stat_info b on a.sku_id = b.sku_id 
# where a.act_id = 313
# and b.act_id = 310;

# -- 2件92折、3件88折 活动暂时停掉，等到618活动结束再恢复
# -- UPDATE am_stat_info a LEFT JOIN am_stat_info b on a.sku_id = b.sku_id 
# set b.item_effect_time = '2021-06-26 00:00:00'
# where a.act_id = 313
# and b.item_name = '2件92折、3件88折' 
# and b.item_effect_time < NOW()
# and b.item_expire_time>NOW();


# SELECT * from am_stat_info a LEFT JOIN am_stat_info b on a.sku_id = b.sku_id 
# where a.act_id = 313
# and b.item_name = '2件92折、3件88折' 
# and b.item_effect_time < NOW()
# and b.item_expire_time>NOW();

    # tableName = 'as_test.202105_ty_61'
    # actId = 0
    # actName = '儿童健康专题'
    # start = '2021-05-31 17:00:00'  #s 生产要改
    # end = '2021-06-14 23:59:59'
    
    # linkurl = 'http://store.ykd365.com/html-activity/page/childrens/index.html?type=15&actId=876&dirId='  # 生产要改

    # color = '#f91549'
    # imagePre = 'http://image.ykd365.cn/act/2021/5/61/'
    # headimg = f"{imagePre}head.jpg"
    # linkimg = f'{imagePre}lb.jpg'
    # windowimg = f'{imagePre}tc.png'

    # allimg = f'{imagePre}9gg.jpg' 

    # listimg = f'{imagePre}list.png'
    
    # 标准单会场活动(actId=actId,actName = actName,tableName =tableName,ydList = [200]
    #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
    #     ,linkurl = linkurl
    #     ,linkView = '',windowimg= windowimg
    #     ,listimg=listimg,detailJump=True)
    # update9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)

# 2.按照excel要求下掉部分疗程装和x件xx折
# -- UPDATE as_test.202105_ty_61 a JOIN pm_prod_sku s on a.huohao = s.pharmacy_huohao and s.drugstore_id = 200
# join am_stat_info ai on s.sku_id= ai.sku_id
# and ai.item_remark = '2件92折、3件88折' and ai.item_effect_time<NOW()
# set ai.item_effect_time = '2021-06-15 00:00:00'
# ;


# SELECT * from as_test.202105_ty_61 a JOIN pm_prod_sku s on a.huohao = s.pharmacy_huohao and s.drugstore_id = 200
# join am_stat_info ai on s.sku_id= ai.sku_id
# and ai.item_remark = '2件92折、3件88折' and ai.item_effect_time<NOW()
# ;
# 3.让价格马上生效





#     tableName = 'as_test.202105_ty_mqj'
#     actId = 0
#     actName = '女性健康爆品直降'
#     start = '2021-05-07 17:20:00'  #s 生产要改
#     end = '2021-05-31 23:59:59'
    
#     linkurl = 'http://store.ykd365.com/html-activity/page/motherDay/index.html?type=15&dirId='  # 生产要改

#     color = '#f91549'
#     imagePre = 'http://image.ykd365.cn/act/2021/5/mqj/'
#     headimg = f"{imagePre}head.jpg"
#     linkimg = f'{imagePre}lb.jpg'
#     windowimg = f'{imagePre}tc.png'

#     allimg = f'{imagePre}9gg.jpg' 

#     listimg = f'{imagePre}list.png'
    
#     标准单会场活动(actId=actId,actName = actName,tableName =tableName,ydList = [200]
#         ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
#         ,linkurl = linkurl
#         ,linkView = '',windowimg= windowimg
#         ,listimg=listimg,detailJump=True)
#     update9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)
# # 1.增加通栏
# # 2.按照excel要求下掉部分疗程装和x件xx折
# # 3.让价格马上生效


# # 1.INSERT INTO `medstore`.`sm_image_link` (  `drugstore_id`, `seq_num`, `image_url`, `link_url`, `link_type`, `link_name`, `link_param`, `link_status`, `link_update_time`, `link_create_time`, `link_remark`, `link_start_time`, `link_end_time`, `link_view`, `link_version`) 
# VALUES (  '200', '0', 'http://image.ykd365.cn/act/2021/5/mqj/tl.jpg', 'http://deve.ykd365.com/html-activity/page/laborDay/index.html?type=15&dirId=1002765081&actId=875', 'web2', '母亲节主题月 关爱女性健康', '1002765073', '1', '2021-04-25 14:23:29', '2021-04-23 11:57:37', '{\"aspect_ratio\":448,\"having_line\":0,\"image_seat\":1}', '2020-05-08 00:00:00', '2021-05-31 23:59:59', 'activity', '1');

# INSERT INTO `medstore`.`sm_image_link` ( `drugstore_id`, `seq_num`, `image_url`, `link_url`, `link_type`, `link_name`, `link_param`, `link_status`, `link_update_time`, `link_create_time`, `link_remark`, `link_start_time`, `link_end_time`, `link_view`, `link_version`)
#  VALUES ( '200', '0', 'http://image.ykd365.cn/act/2021/5/mqj/tl.jpg', 'http://store.ykd365.com/html-activity/page/motherDay/index.html?type=15&dirId=1002765081', 'web2', '女性健康爆品直降', '1002765073', '1', '2021-05-07 17:20:08', '2021-04-23 11:57:37', '{\"aspect_ratio\":448,\"having_line\":0,\"image_seat\":1}', '2020-05-07 00:00:00', '2021-05-31 23:59:59', 'activity', '1');


#2.   update as_test.202105_ty_mqj a join pm_prod_sku s on a.huohao = s.pharmacy_huohao and s.drugstore_id=200 join am_stat_info aa on s.sku_id = aa.sku_id and aa.item_name ='2件92折、3件88折'
# set aa.item_effect_time = '2021-06-01 00:00:00'
# where a.remark='暂时取消x件x折';

# 3. SELECT * from pm_sku_sale ORDER BY sale_id desc limit 1000;



# INSERT INTO `medstore`.`sm_image_link` (`link_id`, `drugstore_id`, `seq_num`, `image_url`, `link_url`, `link_type`, `link_name`, `link_param`, `link_status`, `link_update_time`, `link_create_time`, `link_remark`, `link_start_time`, `link_end_time`, `link_view`, `link_version`) VALUES ('7352', '200', '1', 'http://image.ykd365.cn/act/2021/5/1/lb.jpg', 'http://store.ykd365.com/html-activity/page/laborDay/index.html?type=15&dirId=1002765073&actId=875', 'url', '踏青出游  健康先行', '1002765073', '1', '2021-04-23 18:32:22', '2021-04-23 11:57:37', '', '2021-04-25 00:00:00', '2021-05-10 23:59:59', '', '1');



#     tableName = 'as_test.202105_ty_51'
#     actId = 0
#     actName = '踏青出游  健康先行'
#     start = '2021-04-25 00:00:00'  #s 生产要改
#     end = '2021-05-10 23:59:59'
    
#     linkurl = 'http://store.ykd365.com/html-activity/page/laborDay/index.html?type=15&actId=875&dirId='  # 生产要改

#     color = '#f91549'
#     imagePre = 'http://image.ykd365.cn/act/2021/5/1/'
#     headimg = f"{imagePre}head.jpg"
#     linkimg = f'{imagePre}lb.jpg'
#     windowimg = f'{imagePre}tc.png'

#     allimg = f'{imagePre}9gg.jpg' 

#     listimg = f'{imagePre}list.png'
    
#     标准单会场活动(actId=actId,actName = actName,tableName =tableName,ydList = [200]
#         ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
#         ,linkurl = linkurl
#         ,linkView = '',windowimg= windowimg
#         ,listimg=listimg,detailJump=True)
#     update9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)

# # INSERT INTO `medstore`.`sm_image_link` (`link_id`, `drugstore_id`, `seq_num`, `image_url`, `link_url`, `link_type`, `link_name`, `link_param`, `link_status`, `link_update_time`, `link_create_time`, `link_remark`, `link_start_time`, `link_end_time`, `link_view`, `link_version`) VALUES ('7352', '200', '1', 'http://image.ykd365.cn/act/2021/5/1/lb.jpg', 'http://store.ykd365.com/html-activity/page/laborDay/index.html?type=15&dirId=1002765073&actId=875', 'url', '踏青出游  健康先行', '1002765073', '1', '2021-04-23 18:32:22', '2021-04-23 11:57:37', '', '2021-04-25 00:00:00', '2021-05-10 23:59:59', '', '1');





    # 注意把第二件0元的活动目录的parent_dir_id 改成 和其他目录一样， 为了多一个第二件0元的楼层
    # logging.info(' 测试 药快到专用工具--------')
    # tableName = 'as_test.202103_ty_spring'
    # actId = 0
    # actName = '家庭必备小药箱'
    # start = '2021-03-16 18:40:00'  #s 生产要改
    # end = '2021-04-30 23:59:59'
    
    # linkurl = 'http://store.ykd365.com/html-activity/page/springbox/index.html?type=15&dirId='  # 生产要改

    # color = '#f91549'
    # imagePre = 'http://image.ykd365.cn/act/2021/3/springbox/'
    # headimg = f"{imagePre}head.jpg"
    # linkimg = f'{imagePre}lb.jpg'
    # windowimg = f'{imagePre}tc.png'

    # allimg = f'{imagePre}9gg.jpg' 

    # listimg = f'{imagePre}list.png'
    
    # 标准单会场活动(actId=actId,actName = actName,tableName =tableName,ydList = [200]
    #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
    #     ,linkurl = linkurl
    #     ,linkView = '',windowimg= windowimg
    #     ,listimg=listimg,detailJump=True)
    # update9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)


#   tableName = 'as_test.202102_ty_38'
#     actId = 0
#     actName = '女神节 宠自己'
#     start = '2021-03-02 00:00:00'  #s 生产要改
#     end = '2021-03-17 23:59:59'
    
#     linkurl = 'http://deve.ykd365.com/html-activity/page/springbox/index.html?type=15&dirId='  # 生产要改

#     color = '#f91549'
#     imagePre = 'http://image.ykd365.cn/act/2021/3/springbox/'

# tableName = 'as_test.202102_ty_2y'
#     actId = 0
#     actName = '开年福利 约惠健康'
#     start = '2021-02-18 00:00:00'  #s 生产要改
#     end = '2021-02-28 23:59:59'
    
#     linkurl = 'http://store.ykd365.com/html-activity/page/startWelfare/index.html?type=15&dirId='  # 生产要改

#     color = '#f91549'
#     imagePre = 'http://image.ykd365.cn/act/2021/2/kn/'
#     headimg = f"{imagePre}head.jpg"
#     linkimg = f'{imagePre}lb.jpg'
#     windowimg = f'{imagePre}tc.png'

#     allimg = f'{imagePre}9gg.jpg' 

#     listimg = f'{imagePre}list.png'
    

#    tableName = 'as_test.202101_ty_nhj'
#     actId = 0
#     actName = '滋补年货节'
#     start = '2021-02-01 00:00:00'  #s 生产要改
#     end = '2021-02-18 23:59:59'

#     linkurl = 'http://deve.ykd365.com/html-activity/page/epidemic/index.html?dirId='  # 生产要改

#     color = '#f91549'
#     imagePre = 'http://image.ykd365.cn/act/2021/2/nh/'
#     headimg = f"{imagePre}head.jpg"
#     linkimg = f'{imagePre}lb.jpg'
#     windowimg = f'{imagePre}tc.png'

#     # allimg = f'{imagePre}9gg.jpg' // 年货节活动不需要九宫格

#     listimg = f'{imagePre}list.png'


#  tableName = 'as_test.202101_ty_fy'
#     actId = 0
#     actName = '疫情反复 做好防护 防疫用品精选专题（口罩低至x元/只）'
#     start = '2021-01-11 00:00:00'  #s 生产要改
#     end = '2021-02-28 23:59:59'

#     linkurl = 'http://store.ykd365.com/html-activity/page/epidemic/index.html?type=15&dirId='  # 生产要改

#     color = '#f91549'
#     imagePre = 'http://image.ykd365.cn/act/2021/1/fy/'
#     headimg = f"{imagePre}head.jpg"
#     linkimg = f'{imagePre}lb.jpg'
#     windowimg = f'{imagePre}tc.png'

#     allimg = f'{imagePre}9gg.jpg'

#     listimg = f'{imagePre}list.png'

# http://image.ykd365.cn/act/2021/2/nh/1.jpg
# http://image.ykd365.cn/act/2021/2/nh/2.jpg
# http://image.ykd365.cn/act/2021/2/nh/3.jpg
# http://image.ykd365.cn/act/2021/2/nh/4.jpg
# http://image.ykd365.cn/act/2021/2/nh/5.jpg
# http://image.ykd365.cn/act/2021/2/nh/6.jpg
# http://image.ykd365.cn/act/2021/2/nh/7.jpg
# http://image.ykd365.cn/act/2021/2/nh/8.jpg


# http://image.ykd365.cn/act/191213/tcbj1.png	2020-02-06 20:16:47	双旦礼遇·健康狂欢
# http://image.ykd365.cn/act/191213/tcbj2.png	2020-02-06 20:28:07	跨年福利
# http://image.ykd365.cn/act/2001/tc_1.png	2020-02-06 20:28:07	药快到健康年货节
# http://image.ykd365.cn/act/2001/kgtc.png	2020-02-07 13:58:25	开工福袋
# http://image.ykd365.cn/act/2002/tc14.png	2020-02-14 15:48:53	天一关店
# http://image.ykd365.cn/act/2002/tcty.png	2020-05-11 14:27:49	疫情阻击战
# http://image.ykd365.cn/act/202003/tc_ty_kz.png	2020-05-13 10:29:42	防疫物资
# http://image.ykd365.cn/act/202003/tc325.png	2020-04-02 15:11:16	

# http://image.ykd365.cn/act/2021/1/fy/010.jpg
# http://image.ykd365.cn/act/2021/1/fy/008.jpg
# http://image.ykd365.cn/act/2021/1/fy/006.jpg
# http://image.ykd365.cn/act/2021/1/fy/004.jpg
# http://image.ykd365.cn/act/2021/1/fy/002.jpg
# http://image.ykd365.cn/act/2021/1/fy/head.jpg
#   tableName = 'as_test.202101_ty_1'
#     actId = 0
#     actName = '冬季常见病  好药一站购齐'
#     start = '2021-01-05 00:00:00'  #s 生产要改
#     end = '2021-01-31 23:59:59'

#     linkurl = 'http://store.ykd365.com/html-activity/page/winter/index.html?type=15&dirId='  # 生产要改

#     color = '#f91549'
#     headimg = 'http://image.ykd365.cn/act/2021/1/head.jpg'
#     linkimg = 'http://image.ykd365.cn/act/2021/1/lb.jpg'
#     windowimg = 'http://image.ykd365.cn/act/2021/1/tc.png'

#     allimg = 'http://image.ykd365.cn/act/2021/1/9gg.jpg'

#     listimg = 'http://image.ykd365.cn/act/2021/1/list.png'

#   logging.info(' 测试 药快到专用工具--------')
#     tableName = 'as_test.202012_ty_nz'
#     actId = 0
#     actName = '2020年终盛典  抽奖享全场8折优惠'
#     start = '2020-12-17 21:00:00'  #s 生产要改
#     end = '2021-01-03 23:59:59'

#     linkurl = 'http://store.ykd365.com/html-activity/page/yearEnd/index.html?type=15&dirId='  # 生产要改

#     color = '#f91549'
#     headimg = 'http://image.ykd365.cn/act/202012/nz/main.png'
#     linkimg = 'http://image.ykd365.cn/act/202012/nz/lb.jpg'
#     windowimg = 'http://image.ykd365.cn/act/202012/nz/tc.png'

#     allimg = 'http://image.ykd365.cn/act/202012/nz/9gg.jpg'


# 消掉双12的列表页角标
# UPDATE pm_label_image set label_status = 0  where label_name = "1212"

# #  # 执行以下sql 为了把要暂时结束2件xx折的商品，开始时间改为本次活动的结束时间，以便本活动结束以后，自动上线
    # sql = f"""
        # update as_test.202012_ty_1212 a ,pm_prod_sku s   ,am_stat_info aa 
        # set aa.item_effect_time = '2020-12-16 00:00:00'
        # -- SELECT * FROM as_test.202012_ty_1212 a ,pm_prod_sku s   ,am_stat_info aa
        # where
        # a.huohao= s.pharmacy_huohao and s.drugstore_id = 200
        # and stop_lcz = '暂停2件92折、3件88折'
        # and s.sku_id = aa.sku_id 
        # and aa.item_name = '2件92折、3件88折'
        # and aa.item_expire_time >NOW()
    # """
    # updateSQL(sql)
# 执行以下sql是为了，让所有商品都有横图 而且能够跳转到助力页面，注意修改 act——id
    # sql2 = 'UPDATE am_stat_info set other_str1 = \'{"itemImageR":"642","itemImage":"http://image.ykd365.cn/act/202012/1212/detail.png","itemUrl":"http://store.ykd365.com/html-activity/page/twelve/invite.html?prize_id=37", "itemTitle":"邀2人助力，领最高50元抵用金"}\' where act_id = 296;'
    # updateSQL(sql2)

    # db.commit()


#  tableName = 'as_test.202012_ty_1212'
#     actId = 296
#     actName = '12·12 家庭备药一站购齐'
#     start = '2020-12-04 22:00:00'  #s 生产要改
#     end = '2020-12-15 23:59:59'

#     linkurl = 'http://store.ykd365.com/html-activity/page/twelve/index.html?type=15&prize_id=37&dirId='  # 生产要改

#     color = '#f44430'
#     headimg = 'http://image.ykd365.cn/act/202012/1212/main.jpg'
#     linkimg = 'http://image.ykd365.cn/act/202012/1212/lb.jpg'
#     windowimg = 'http://image.ykd365.cn/act/202012/1212/tc.png'

#     allimg = 'http://image.ykd365.cn/act/202012/1212/9gg.jpg'


# ----------------------------------------
    # logging.info(' 测试 药快到专用工具--------')
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
    # logging.info(' over --------')

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

