# from peewee import MySQLDatabase,Model,IntegerField,CharField,DateTimeField
from ykdmodel import *
import datetime
import logging
import uuid
logger = logging.getLogger()
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my-58.log', level=logging.DEBUG, format=LOG_FORMAT)
#  创建一个handler，用于将日志输出到控制台
# log = logging.StreamHandler()
# log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)
logging.info('peewee-----------------')
db = MySQLDatabase('medstore', host='rm-2ze7fnv9ydw78u07a7o.mysql.rds.aliyuncs.com', user='camore', passwd='camore', charset='utf8', port=3306)
# db = pymysql.connect('rm-2ze7fnv9ydw78u07a7o.mysql.rds.aliyuncs.com',user = "camore",passwd = "camore",db = "medstore")
db.connect()

class XyxTY(YkdActBase):
# class XyxTY(BaseModel):
    class Meta:
        database = database
        table_name = '202005_ty_xyx'


def createSku(drugstoreIds,sku_status=1):
    '''根据药品盘活表,创建 说明书 image prod sku'''
    xcList = T202005XcNew药品.select().execute()
    for info in xcList:
        drug_id = YjjDrugDetail.insert(yjj_id=str(uuid.uuid1()).replace('-','')
                        ,common_name=info.通用名,product_name=f'{info.商品名} {info.通用名}'
                        ,product_name_en=info.英文名,product_name_chem=info.化学名称
                        ,structural_formula=info.分子式,molecular_weight=info.分子量
                        ,component=info.成份,trait=info.性状
                        ,assist_matreial=info.注射剂辅料,indication=info.适应症
                        ,role_category=info.作用类别,dosage=info.用法用量
                        ,adverse_reactions=info.不良反应,precautions=info.注意事项

                        ,contraindications=info.禁忌,format=info.规格
                        ,package=info.包装,over_dosage=info.药物过量
                        ,pharmacokinetics=info.药代动力学,use_in_elderly=info.老年用药
                        ,use_in_children=info.儿童用药,user_in_preglact=info.孕妇及哺乳期妇女用药
                        ,mechanism_action=info.药理毒理,drug_interactions=info.药物相互作用

                        ,number=info.批准文号,company_name=info.生产企业
                        ,clinical_trial=info.临床试验
                        ).execute()
        logging.info(f'1 YjjDrugDetail      {drug_id}  {info.商品名} {info.通用名} {info.自己药店货号}')
        # logging.info(f'drug_id {drug_id}')
        prodTypeDic = {
            'OTC':1,
            'RX':3
        }
        # CASE f.`prod_type` WHEN 1 THEN '药品OTC' WHEN 2 THEN '医疗器械' WHEN 3 THEN '处方药'  WHEN 5 THEN '保健品' WHEN 6 THEN '非药品'
        prod = PmProdInfo.create(drug_id=drug_id
                        ,prod_brand=info.商品名,prod_name=f'{info.商品名} {info.通用名}',prod_gen_name=info.通用名
                        ,prod_status=1,prod_code=info.商品条码
                        ,prod_sn=info.批准文号,prod_price=info.零售价*100
                        ,prod_level=5,prod_firm=info.生产厂家
                        ,prod_type=prodTypeDic[info.商品类别],prod_spec=info.规格
                        ,prod_unit=info.单位,prod_indication=info.适应症
                                    )
        prod_id = prod.prod_id
        logging.info(f'2 PmProdInfo          {prod_id}  {prod.prod_name}')
        imageList = [info.图片1,info.图片2,info.图片3,info.图片4]
        for imageUrl in imageList:
            if imageUrl!='':
                image_id = PmImageInfo.insert(
                            img_name=info.自己药店货号,img_url=f'http://image.ykd365.cn/tongchuan/xc/{imageUrl}.JPG'
                            ,img_type='jpg',img_status=1
                                ).execute()
                logging.info(f'3 PmImageInfo    {image_id}  http://image.ykd365.cn/tongchuan/xc/{imageUrl}.JPG')
                PmProdImg.insert(
                            img_id=image_id,prod_id=prod_id
                            ,img_kind='prodImage',img_name=f'http://image.ykd365.cn/tongchuan/xc/{imageUrl}.JPG'
                                ).execute()
                logging.info(f'4 PmProdImg      {image_id}  {prod_id}')
        for drugstoreId in drugstoreIds:
            sku_id = PmProdSku.insert(
                            prod_id=prod_id,sku_status=sku_status
                            ,sku_price=prod.prod_price,sku_fee=prod.prod_price
                            ,drugstore_id = drugstoreId,prod_name=prod.prod_name
                            ,pharmacy_huohao=info.自己药店货号,sku_json=f'{{"prod_spec":"{prod.prod_spec}"}}'
            ).execute()
        logging.info(f'5 PmProdSku      {sku_id}  name:{prod.prod_name} huohao:{info.自己药店货号}  prod_id：{prod_id}')


if __name__ == "__main__":
    logging.info('peewee-----------------')
    YkdBaseSku.delete().execute()
    actName = '202005xyx'
    with db.atomic():
        # list = XyxTY.select()
        # list = XyxTY.select().join(PmProdSku).where((XyxTY.huohao==PmProdSku.pharmacy_huohao) & (PmProdSku.pharmacy_id == 200)).execute()
        list = XyxTY.select(XyxTY,PmProdSku).join(PmProdSku,on=(XyxTY.huohao==PmProdSku.pharmacy_huohao)).where((PmProdSku.drugstore_id == 200)).execute()
        for xyx in list:
            logging.info(f"{xyx.xh}-{xyx.huohao}--{xyx.dir_name}--{xyx.item_name}--{xyx.pmprodsku.prod_name}")
            # YkdBaseSku.insert(xh=xyx.xh,sku_id=xyx.pmprodsku.sku_id,
                            # act=actName,name=xyx.pmprodsku.prod_name,huohao=xyx.pmprodsku.pharmacy_huohao
                            # ,drugstore_id=xyx.pmprodsku.drugstore_id
                            # ,item=xyx.item_name,dir=xyx.dir_name
                            # ,list_logo=xyx.list_logo,is_lcz=xyx.stop_lcz,is_xq=xyx.is_xq
                            # ,comb_huohao= xyx.comb_huohao,fee=xyx.fee,price=xyx.price).execute()



    # with db.atomic():
    #     createSku([1602,1603])
        # createSku([1600,1601])
  