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
                    addPmLabelImage('嗨购季','http://image.ykd365.cn/act/202009/zq/list.png','1',drugstoreId,skuIdList=logoList)
                elif  list_logo =='疗程装':
                    logoList.append(dic['sku_id'])
                    addPmLabelImage('疗程装','http://image.ykd365.cn/act/202005/mqj/lcz_logo.png','1',drugstoreId,skuIdList=logoList)
                # 限券
                if 'is_xq' in dic.keys() and dic['is_xq']!=None and dic['is_xq']==1:
                    copyAmStatInfoBySkuId( 78,sku_id)
                # huohao =  dic['pharmacy_huohao']
                # copyAmStatInfoByHuohao( '78',huohao,drugstoreId)
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
    linkurl = 'http://deve.ykd365.com/medstore/actUserpage/moon_2010?pageSize=1000&dirId='

    color = '#deedef'
    headimg = 'http://image.ykd365.cn/act/202009/zq/02.png'
    linkimg = 'http://image.ykd365.cn/act/202009/zq/lb.jpg'
    windowimg = 'http://image.ykd365.cn/act/202009/zq/tc.png'
    for i in range(len(ydIds)):
        drugstoreId = ydIds[i]
        addSmImageLink(drugstoreId,1,linkimg,linkurl,actName,parentDirId,startTime,endTime,link_view='')
        addSmImageLinkWindow(drugstoreId,1,windowimg,linkurl,actName,parentDirId,startTime,endTime)
        # if i==0:
        updateAllEnssence(ydIds[i],allImags[i])
        updateEnssence(ydIds[i],5,startTime,endTime,toDirName=toDirName,link_view='')
        # else:
        #     logging.info(i)
    db.commit()
    

if __name__ == "__main__":
    logging.info(' 测试 药快到专用工具--------')
    actName = '健康好礼嗨购季'
    start = '2010-09-25 00:00:00'
    end = '2020-10-11 23:59:59'

    # linkurl = 'http://store.ykd365.com/medstore/actUserpage/medicineKit_2008?pageSize=1000&dirId='
    linkurl = ''

    color = '#deedef'
    headimg = 'http://image.ykd365.cn/act/202009/zq/02.png'
    linkimg = 'http://image.ykd365.cn/act/202009/zq/lb.jpg'
    windowimg = 'http://image.ykd365.cn/act/202009/zq/tc.png'

    allimg = 'http://image.ykd365.cn/act/202009/zq/ty_9gg.jpg'


    # 中秋国庆(actId=0,actName = actName,tableName ='as_test.202009_ty_zq',ydList = [200]
    #     ,startTime=start,endTime=end,img = headimg,color = color,linkimg =linkimg
    #     ,linkurl = linkurl
    #     ,linkView = '',windowimg= windowimg)
    update国庆中秋9GG( toDirName =actName,ydIds = [200],allImags=[allimg],images=[linkimg],startTime=start,endTime=end)

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

