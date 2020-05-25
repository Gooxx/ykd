from peewee import *

database = MySQLDatabase('medstore', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'rm-2ze7fnv9ydw78u07a7o.mysql.rds.aliyuncs.com', 'port': 3306, 'user': 'camore', 'password': 'camore'})

database_act = MySQLDatabase('as_test', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'rm-2ze7fnv9ydw78u07a7o.mysql.rds.aliyuncs.com', 'port': 3306, 'user': 'camore', 'password': 'camore'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database
    

class YkdActBase(BaseModel):
    base_huohao = CharField(null=True)
    comb_huohao = CharField(null=True)
    detail_logo = CharField(null=True)
    detail_value = CharField(null=True)
    dir_code = CharField(null=True)
    dir_img = CharField(null=True)
    dir_name = CharField(null=True)
    dir_num = CharField(null=True)
    fee = CharField(null=True)
    huohao = CharField(null=True)
    item_code = CharField(null=True)
    item_desc = CharField(null=True)
    item_img = CharField(null=True)
    item_img_r = CharField(null=True)
    item_name = CharField(null=True)
    item_type = CharField(null=True)
    kc_day = CharField(null=True)
    list_logo = CharField(null=True)
    price = CharField(null=True)
    quota_group = CharField(null=True)
    quota_rule = CharField(null=True)
    remark = CharField(null=True)
    rule = CharField(null=True)
    stop_lcz = CharField(null=True)
    xh = AutoField(null=True)
    is_xq = IntegerField(null=True)
    # 品牌名 = CharField(null=True)
    # 商品id = CharField(column_name='商品ID', null=True)
    # 商品列表页左上角打标 = CharField(null=True)
    # 商品列表页文字标 = CharField(null=True)
    # 多盒货号 = CharField(null=True)
    # 市场价 = CharField(null=True)
    # 活动促销 = CharField(null=True)
    # 活动页商品打标 = CharField(null=True)
    # 生产厂家 = CharField(null=True)
    # 规格 = CharField(null=True)
    # 通用名 = CharField(null=True)
    # 销售价 = CharField(null=True)

    class Meta:
        database = database_act
        table_name = 'ykd_act_base'


class YkdBaseDir(BaseModel):
    act = CharField(null=True)
    code = CharField(null=True)
    img = CharField(null=True)
    name = CharField(null=True)
    num = IntegerField(null=True)
    drugstore_ids = CharField(null=True)
    class Meta:
        database = database_act
        table_name = 'ykd_base_dir'

class YkdBaseItem(BaseModel):
    act = CharField(null=True)
    code = CharField(null=True)
    desc = CharField(null=True)
    detail_type = CharField(null=True)
    img = CharField(null=True)
    img_r = CharField(null=True)
    name = CharField(null=True)
    num = IntegerField(null=True)
    quota_group = CharField(null=True)
    quota_rule = CharField(null=True)
    rule_value = CharField(null=True)
    type = CharField(null=True)
    drugstore_ids = CharField(null=True)
    act_name = CharField(null=True)
    class Meta:
        database = database_act
        table_name = 'ykd_base_item'

class YkdBaseSku(BaseModel):
    act = CharField(null=True)
    sku_id = IntegerField(null=True)
    xh = IntegerField(null=True)
    dir = CharField(null=True)
    drugstore_id = CharField(null=True)
    huohao = CharField(null=True)
    is_lcz = IntegerField(null=True)
    is_xq = IntegerField(null=True)
    item = CharField(null=True)
    list_logo = CharField(null=True)
    name = CharField(null=True)
    comb_huohao = CharField(null=True) 
    fee = FloatField(null=True)
    price = FloatField(null=True)
    class Meta:
        database = database_act
        table_name = 'ykd_base_sku'


class T191016Export(BaseModel):
    下单时间 = CharField(null=True)
    下单月份 = CharField(null=True)
    优惠卷信息 = CharField(null=True)
    优惠卷金额 = CharField(null=True)
    备注 = CharField(null=True)
    实际交易金额 = CharField(null=True)
    手机号 = CharField(null=True)
    新老用户 = CharField(null=True)
    注册时间 = CharField(null=True)
    签收时间 = CharField(null=True)
    订单号 = AutoField()
    订单类型 = CharField(null=True)
    门店名称 = CharField(null=True)
    零售金额 = CharField(null=True)
    首单时间 = CharField(null=True)
    首单月份 = CharField(null=True)

    class Meta:
        table_name = '191016export'

class T190909Ty(BaseModel):
    coupon_id = IntegerField(null=True)
    优惠券金额 = CharField(null=True)
    优惠卷信息 = CharField(null=True)
    券来源 = CharField(null=True)
    原零售金额 = CharField(null=True)
    实际零售金额 = CharField(null=True)
    实际零售金额1 = CharField(null=True)
    手机号 = CharField(null=True)
    订单号 = AutoField()

    class Meta:
        table_name = '19_09_09_ty'

class T20181017(BaseModel):
    phone_num = CharField(column_name='phoneNum', null=True)

    class Meta:
        table_name = '20181017'

class T202005XcNew药品(BaseModel):
    不良反应 = CharField(null=True)
    临床试验 = CharField(null=True)
    作用类别 = CharField(null=True)
    储存条件 = CharField(null=True)
    儿童用药 = CharField(null=True)
    分子式 = CharField(null=True)
    分子量 = CharField(null=True)
    适应症 = CharField(column_name='功能主治/适应症', null=True)
    包装 = CharField(null=True)
    化学名称 = CharField(null=True)
    单位 = CharField(null=True)
    商品名 = CharField(null=True)
    商品名1 = CharField(null=True)
    商品条码 = CharField(null=True)
    商品类别 = CharField(null=True)
    图片1 = CharField(null=True)
    图片2 = CharField(null=True)
    图片3 = CharField(null=True)
    图片4 = CharField(null=True)
    孕妇及哺乳期妇女用药 = CharField(null=True)
    性状 = CharField(null=True)
    成份 = CharField(null=True)
    批准文号 = CharField(null=True)
    批准文号1 = CharField(null=True)
    注射剂辅料 = CharField(null=True)
    注意事项 = CharField(null=True)
    生产企业 = CharField(null=True)
    生产厂家 = CharField(null=True)
    用法用量 = CharField(null=True)
    禁忌 = CharField(null=True)
    老年用药 = CharField(null=True)
    自己药店货号 = CharField(null=True)
    英文名 = CharField(null=True)
    药代动力学 = CharField(null=True)
    药物相互作用 = CharField(null=True)
    药物过量 = CharField(null=True)
    药理毒理 = CharField(null=True)
    规格 = CharField(null=True)
    通用名 = CharField(null=True)
    通用名1 = CharField(null=True)
    零售价 = FloatField(null=True)

    class Meta:
        table_name = '202005_xc_new药品'
        primary_key = False

class T2TymType(BaseModel):
    prod_gen_name = CharField(index=True, null=True)
    prod_type = CharField(null=True)
    tymid = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = '2_tym_type'
        primary_key = False

class AmActInfo(BaseModel):
    act_content = CharField()
    act_create_time = DateTimeField(null=True)
    act_end_time = DateTimeField(null=True)
    act_id = AutoField()
    act_img = CharField(null=True)
    act_level = IntegerField()
    act_name = CharField()
    act_remark = CharField(null=True)
    act_start_time = DateTimeField(null=True)
    act_status = IntegerField()
    act_type = CharField()
    act_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    act_url = CharField(null=True)
    pharmacy_id = IntegerField(null=True)

    class Meta:
        table_name = 'am_act_info'

class AmActItem(BaseModel):
    act_id = IntegerField()
    activity_img = CharField(null=True)
    activity_img_ratio = CharField(null=True)
    item_attr = CharField()
    item_create_time = DateTimeField(null=True)
    item_desc = CharField(null=True)
    item_flag = CharField(null=True)
    item_id = AutoField()
    item_img = CharField(null=True)
    item_name = CharField()
    item_num = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    item_priority = IntegerField()
    item_remark = CharField(null=True)
    item_status = IntegerField()
    item_title = CharField(null=True)
    item_type = CharField()
    item_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    pharmacy_id = IntegerField(null=True)
    sales_goto_title = CharField(null=True)
    sales_goto_type = CharField(null=True)
    sales_goto_url = CharField(null=True)

    class Meta:
        table_name = 'am_act_item'

class AmActMenu(BaseModel):
    act_status = CharField(null=True)
    chanpindalei = CharField(null=True)
    chanpinxiaolei = CharField(null=True)
    dir_code = CharField(null=True)
    dir_id = IntegerField(null=True)
    dir_img_1 = CharField(null=True)
    dir_img_2 = CharField(null=True)
    dir_remark = CharField(null=True)
    drugstore_id = IntegerField(null=True)
    menu_id = AutoField()
    pharmacy_huohao = CharField(null=True)
    shangpinming = CharField(null=True)
    sku_fee = IntegerField(null=True)
    sku_id = CharField(null=True)
    sku_price = IntegerField(null=True)
    tongyongming = CharField(null=True)
    xuhao = CharField(null=True)
    zongshu = CharField(null=True)

    class Meta:
        table_name = 'am_act_menu'

class AmActPrize(BaseModel):
    act_prize_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    act_prize_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], null=True)
    act_prize_flag = IntegerField(null=True)
    act_prize_id = AutoField()
    act_prize_name = CharField(null=True)
    act_prize_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], null=True)
    act_prize_status = IntegerField(null=True)
    act_prize_type = IntegerField(null=True)
    act_prize_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'am_act_prize'

class AmActPrizeAddress(BaseModel):
    address_id = AutoField()
    departure_time = DateTimeField(null=True)
    iphone_num = IntegerField(null=True)
    prize_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    prize_id = IntegerField(null=True)
    prize_result_id = IntegerField(null=True)
    prize_status = CharField(null=True)
    prize_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_address = CharField(null=True)
    user_destination = CharField(null=True)
    user_id = IntegerField(null=True)
    user_idcard = CharField(null=True)
    user_name = CharField(null=True)
    user_sex = CharField(null=True)

    class Meta:
        table_name = 'am_act_prize_address'

class AmActPrizeInfo(BaseModel):
    act_prize_id = IntegerField(null=True)
    prize_code = CharField(null=True)
    prize_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    prize_flag = IntegerField(null=True)
    prize_id = AutoField()
    prize_image = CharField(null=True)
    prize_maxnum = IntegerField(null=True)
    prize_maxuser = IntegerField(null=True)
    prize_name = CharField(null=True)
    prize_order = IntegerField(null=True)
    prize_rate = IntegerField(null=True)
    prize_status = IntegerField(null=True)
    prize_type = IntegerField(null=True)
    prize_update_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])

    class Meta:
        table_name = 'am_act_prize_info'

class AmActPrizeOrder(BaseModel):
    get_count = IntegerField(null=True)
    order_id = IntegerField(null=True)
    po_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    po_id = AutoField()
    po_key = CharField(null=True)
    po_name = CharField(null=True)
    po_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    po_url = CharField(null=True)
    prize_id = IntegerField(null=True)

    class Meta:
        table_name = 'am_act_prize_order'

class AmActPrizeResult(BaseModel):
    order_id = IntegerField()
    phone_number = CharField(null=True)
    prize_id = IntegerField(null=True)
    prize_info_id = IntegerField(null=True)
    result_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    result_id = AutoField()
    result_price_describe = CharField(null=True)
    result_prize_name = CharField(null=True)
    result_remark = CharField(null=True)
    result_status = IntegerField(null=True)
    result_type = IntegerField(null=True)
    result_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    rusult_code = IntegerField(null=True)
    union_id = CharField(null=True)
    user_id = IntegerField()

    class Meta:
        table_name = 'am_act_prize_result'

class AmActPrizeSource(BaseModel):
    phone_number = CharField(null=True)
    prize_id = IntegerField(null=True)
    source_already_num = IntegerField(null=True)
    source_already_pray = IntegerField(null=True)
    source_already_share = IntegerField(null=True)
    source_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    source_date = DateField(null=True)
    source_flag = CharField(null=True)
    source_id = AutoField()
    source_remark = CharField(null=True)
    source_sum_num = IntegerField(null=True)
    source_update_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    union_id = CharField(null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'am_act_prize_source'

class AmActPromotions(BaseModel):
    dir_code = CharField(null=True)
    dir_id = IntegerField(null=True)
    dir_name = CharField(null=True)
    drugstore_id = CharField(null=True)
    prom_create_time = DateTimeField(null=True)
    prom_end_time = DateTimeField(null=True)
    prom_image = CharField(constraints=[SQL("DEFAULT '0'")])
    prom_start_time = DateTimeField(null=True)
    prom_status = CharField(null=True)
    prom_type = CharField(null=True)
    prom_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    promotions_id = AutoField()

    class Meta:
        table_name = 'am_act_promotions'

class AmActPromotionsHis(BaseModel):
    dir_code = CharField(null=True)
    dir_id = IntegerField(null=True)
    dir_name = CharField(null=True)
    drugstore_id = CharField(null=True)
    prom_create_time = DateTimeField(null=True)
    prom_end_time = DateTimeField(null=True)
    prom_image = CharField(constraints=[SQL("DEFAULT '0'")])
    prom_start_time = DateTimeField(null=True)
    prom_status = CharField(null=True)
    prom_type = CharField(null=True)
    prom_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    promotions_id = AutoField()

    class Meta:
        table_name = 'am_act_promotions_his'

class AmActRange(BaseModel):
    range_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    range_id = AutoField()
    range_name = CharField(null=True)
    range_remark = CharField(null=True)
    range_status = IntegerField()
    range_type = CharField()
    range_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    range_value = CharField(null=True)

    class Meta:
        table_name = 'am_act_range'

class AmActRule(BaseModel):
    rule_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    rule_id = AutoField()
    rule_name = CharField()
    rule_remark = CharField(null=True)
    rule_type = CharField()
    rule_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    rule_value = CharField()
    rule_value_type = CharField()

    class Meta:
        table_name = 'am_act_rule'

class AmCodeActHistory(BaseModel):
    code_act = CharField(null=True)
    code_act_id = IntegerField(null=True)
    code_type = CharField(null=True)
    device_id = CharField(null=True)
    his_id = AutoField()
    other_info1 = CharField(null=True)
    other_info2 = CharField(null=True)
    owner_id = IntegerField(null=True)
    update_time = DateTimeField(null=True)
    use_time = DateTimeField(null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'am_code_act_history'
        indexes = (
            (('user_id', 'code_act', 'code_act_id'), False),
        )

class AmCodeActInfo(BaseModel):
    act_amount_fee = IntegerField(null=True)
    act_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    act_encourage = CharField(null=True)
    act_end_time = DateTimeField(null=True)
    act_max_count = IntegerField(null=True)
    act_name = CharField(null=True)
    act_per_code_used = IntegerField(null=True)
    act_per_code_user_used = IntegerField(null=True)
    act_per_user_used = IntegerField(null=True)
    act_priority = IntegerField(null=True)
    act_send_type = CharField(null=True)
    act_start_time = DateTimeField(null=True)
    act_type = CharField(null=True)
    act_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    act_user_type = IntegerField(null=True)
    code_act_id = AutoField()
    login_logout_show = CharField(null=True)
    other_one = CharField(null=True)
    other_two = CharField(null=True)
    pharmacy_id = IntegerField(null=True)

    class Meta:
        table_name = 'am_code_act_info'

class AmCodeActStat(BaseModel):
    act_code_id = AutoField()
    create_code_nums = IntegerField(null=True)
    create_coupon_fee = BigIntegerField(null=True)
    create_coupon_nums = IntegerField(null=True)
    create_time = DateTimeField(null=True)
    last_time = DateTimeField(null=True)
    other_info = CharField(null=True)
    use_code_nums = IntegerField(null=True)
    user_coupon_nums = IntegerField(null=True)

    class Meta:
        table_name = 'am_code_act_stat'

class AmCoupleTemplateInfo(BaseModel):
    activate_immed = IntegerField(null=True)
    code_act_id = IntegerField(null=True)
    cou_act_mutex = CharField(null=True)
    cou_color = CharField(null=True)
    cou_create_type = CharField(null=True)
    cou_delivery_fee = IntegerField(null=True)
    cou_desc = CharField(null=True)
    cou_nouse_cause = CharField(null=True)
    cou_num = IntegerField(constraints=[SQL("DEFAULT 1")])
    cou_other_str = CharField(null=True)
    cou_tem_for = CharField(null=True)
    cou_tem_id = AutoField()
    cou_tem_seq = IntegerField(null=True)
    cou_tem_threshold = IntegerField(null=True)
    cou_tem_type = CharField(null=True)
    cou_tem_value = IntegerField(null=True)
    cou_use_dir = CharField(null=True)
    cou_use_info = CharField(null=True)
    cou_use_type = IntegerField(null=True)
    count_max = IntegerField(null=True)
    has_next = IntegerField(null=True)
    invild_date = IntegerField(null=True)
    is_open_device_power = IntegerField(null=True)
    value_amount_fee = IntegerField(null=True)
    value_max = IntegerField(null=True)
    value_min = IntegerField(null=True)
    value_ratio = IntegerField(null=True)

    class Meta:
        table_name = 'am_couple_template_info'

class AmCoupleTemplateInfo191107新人券修改备份(BaseModel):
    activate_immed = IntegerField(null=True)
    code_act_id = IntegerField(null=True)
    cou_act_mutex = CharField(null=True)
    cou_color = CharField(null=True)
    cou_create_type = CharField(null=True)
    cou_delivery_fee = IntegerField(null=True)
    cou_desc = CharField(null=True)
    cou_nouse_cause = CharField(null=True)
    cou_num = IntegerField(constraints=[SQL("DEFAULT 1")])
    cou_other_str = CharField(null=True)
    cou_tem_for = CharField(null=True)
    cou_tem_id = AutoField()
    cou_tem_seq = IntegerField(null=True)
    cou_tem_threshold = IntegerField(null=True)
    cou_tem_type = CharField(null=True)
    cou_tem_value = IntegerField(null=True)
    cou_use_dir = CharField(null=True)
    cou_use_info = CharField(null=True)
    cou_use_type = IntegerField(null=True)
    count_max = IntegerField(null=True)
    has_next = IntegerField(null=True)
    invild_date = IntegerField(null=True)
    is_open_device_power = IntegerField(null=True)
    value_amount_fee = IntegerField(null=True)
    value_max = IntegerField(null=True)
    value_min = IntegerField(null=True)
    value_ratio = IntegerField(null=True)

    class Meta:
        table_name = 'am_couple_template_info_191107新人券修改备份'

class AmCoupleTemplateInfo191205(BaseModel):
    activate_immed = IntegerField(null=True)
    code_act_id = IntegerField(null=True)
    cou_act_mutex = CharField(null=True)
    cou_color = CharField(null=True)
    cou_create_type = CharField(null=True)
    cou_delivery_fee = IntegerField(null=True)
    cou_desc = CharField(null=True)
    cou_nouse_cause = CharField(null=True)
    cou_num = IntegerField(constraints=[SQL("DEFAULT 1")])
    cou_other_str = CharField(null=True)
    cou_tem_for = CharField(null=True)
    cou_tem_id = AutoField()
    cou_tem_seq = IntegerField(null=True)
    cou_tem_threshold = IntegerField(null=True)
    cou_tem_type = CharField(null=True)
    cou_tem_value = IntegerField(null=True)
    cou_use_dir = CharField(null=True)
    cou_use_info = CharField(null=True)
    cou_use_type = IntegerField(null=True)
    count_max = IntegerField(null=True)
    has_next = IntegerField(null=True)
    invild_date = IntegerField(null=True)
    is_open_device_power = IntegerField(null=True)
    value_amount_fee = IntegerField(null=True)
    value_max = IntegerField(null=True)
    value_min = IntegerField(null=True)
    value_ratio = IntegerField(null=True)

    class Meta:
        table_name = 'am_couple_template_info_191205'

class AmCouponActHis(BaseModel):
    act_create_time = DateTimeField(null=True)
    act_end_time = DateTimeField(null=True)
    act_start_time = DateTimeField(null=True)
    act_status = IntegerField(null=True)
    act_update_time = DateTimeField(null=True)
    code_act_id = IntegerField(null=True)
    from_user_id = IntegerField(null=True)
    happen_date = CharField(null=True)
    invite_code = CharField(null=True)
    phone_num = CharField(null=True)
    r_id = AutoField()
    remark = CharField(null=True)
    user_ip = CharField(null=True)

    class Meta:
        table_name = 'am_coupon_act_his'
        indexes = (
            (('phone_num', 'act_status', 'act_end_time'), False),
        )

class AmCouponInfo(BaseModel):
    cou_act_mutex = CharField(null=True)
    cou_delivery_fee = IntegerField(null=True)
    cou_other_str = CharField(null=True)
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_code = CharField(index=True, null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = AutoField()
    coupon_name = CharField()
    coupon_nouse_cause = CharField(null=True)
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField(index=True)
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_use_dir = CharField(null=True)
    coupon_use_info = CharField(null=True)
    coupon_use_type = IntegerField(null=True)
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    is_open_device_power = IntegerField(null=True)
    pharmacy_id = IntegerField(index=True, null=True)
    user_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'am_coupon_info'
        indexes = (
            (('coupon_create_time', 'coupon_code'), False),
            (('coupon_create_time', 'coupon_threshold'), False),
        )

class AmCouponInfo180718(BaseModel):
    cou_delivery_fee = IntegerField(null=True)
    cou_other_str = CharField(null=True)
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_code = CharField(index=True, null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = AutoField()
    coupon_name = CharField()
    coupon_nouse_cause = CharField(null=True)
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField(index=True)
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_use_dir = CharField(null=True)
    coupon_use_info = CharField(null=True)
    coupon_use_type = IntegerField(null=True)
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    is_open_device_power = IntegerField(null=True)
    pharmacy_id = IntegerField(index=True, null=True)
    user_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'am_coupon_info_180718'
        indexes = (
            (('coupon_create_time', 'coupon_code'), False),
            (('coupon_create_time', 'coupon_threshold'), False),
        )

class AmCouponInfo191022(BaseModel):
    cou_act_mutex = CharField(null=True)
    cou_delivery_fee = IntegerField(null=True)
    cou_other_str = CharField(null=True)
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_code = CharField(index=True, null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = AutoField()
    coupon_name = CharField()
    coupon_nouse_cause = CharField(null=True)
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField(index=True)
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_use_dir = CharField(null=True)
    coupon_use_info = CharField(null=True)
    coupon_use_type = IntegerField(null=True)
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    is_open_device_power = IntegerField(null=True)
    pharmacy_id = IntegerField(index=True, null=True)
    user_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'am_coupon_info_191022'
        indexes = (
            (('coupon_create_time', 'coupon_code'), False),
            (('coupon_create_time', 'coupon_threshold'), False),
        )

class AmCouponInfo191023(BaseModel):
    cou_act_mutex = CharField(null=True)
    cou_delivery_fee = IntegerField(null=True)
    cou_other_str = CharField(null=True)
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_code = CharField(index=True, null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = AutoField()
    coupon_name = CharField()
    coupon_nouse_cause = CharField(null=True)
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField(index=True)
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_use_dir = CharField(null=True)
    coupon_use_info = CharField(null=True)
    coupon_use_type = IntegerField(null=True)
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    is_open_device_power = IntegerField(null=True)
    pharmacy_id = IntegerField(index=True, null=True)
    user_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'am_coupon_info_191023'
        indexes = (
            (('coupon_create_time', 'coupon_code'), False),
            (('coupon_create_time', 'coupon_threshold'), False),
        )

class AmCouponInfo200308(BaseModel):
    cou_act_mutex = CharField(null=True)
    cou_delivery_fee = IntegerField(null=True)
    cou_other_str = CharField(null=True)
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_code = CharField(index=True, null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = AutoField()
    coupon_name = CharField()
    coupon_nouse_cause = CharField(null=True)
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField(index=True)
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_use_dir = CharField(null=True)
    coupon_use_info = CharField(null=True)
    coupon_use_type = IntegerField(null=True)
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    is_open_device_power = IntegerField(null=True)
    pharmacy_id = IntegerField(index=True, null=True)
    user_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'am_coupon_info_200308'
        indexes = (
            (('coupon_create_time', 'coupon_code'), False),
            (('coupon_create_time', 'coupon_threshold'), False),
        )

class AmCouponInfoDel(BaseModel):
    cou_act_mutex = CharField(null=True)
    cou_delivery_fee = IntegerField(null=True)
    cou_other_str = CharField(null=True)
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_code = CharField(index=True, null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = AutoField()
    coupon_name = CharField()
    coupon_nouse_cause = CharField(null=True)
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField(index=True)
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_use_dir = CharField(null=True)
    coupon_use_info = CharField(null=True)
    coupon_use_type = IntegerField(null=True)
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    is_open_device_power = IntegerField(null=True)
    pharmacy_id = IntegerField(index=True, null=True)
    user_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'am_coupon_info_del'
        indexes = (
            (('coupon_create_time', 'coupon_code'), False),
            (('coupon_create_time', 'coupon_threshold'), False),
        )

class AmCouponInfoDrugstore(BaseModel):
    coupon_id = IntegerField(null=True)
    drugstore_id = IntegerField(null=True)

    class Meta:
        table_name = 'am_coupon_info_drugstore'

class AmCouponInfoHis(BaseModel):
    cou_delivery_fee = IntegerField(null=True)
    cou_other_str = CharField(null=True)
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_code = CharField(index=True, null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = AutoField()
    coupon_name = CharField()
    coupon_nouse_cause = CharField(null=True)
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField(index=True)
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_use_dir = CharField(null=True)
    coupon_use_info = CharField(null=True)
    coupon_use_type = IntegerField(null=True)
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    is_open_device_power = IntegerField(null=True)
    pharmacy_id = IntegerField(index=True, null=True)
    user_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'am_coupon_info_his'
        indexes = (
            (('coupon_create_time', 'coupon_code'), False),
            (('coupon_create_time', 'coupon_threshold'), False),
        )

class AmDetailsRule(BaseModel):
    details_id = IntegerField()
    link_id = AutoField()
    rule_id = IntegerField()

    class Meta:
        table_name = 'am_details_rule'

class AmInviteCode(BaseModel):
    code_act_id = IntegerField(null=True)
    coupon_value = IntegerField()
    inivite_json = CharField(null=True)
    invite_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    invite_code = CharField(index=True)
    invite_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    invite_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    invite_from_id = IntegerField(null=True)
    invite_from_type = CharField(null=True)
    invite_id = AutoField()
    invite_remark = CharField(null=True)
    invite_status = IntegerField()
    invite_type = CharField()
    invite_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    invite_use_times = IntegerField(null=True)
    invite_user_id = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'am_invite_code'
        indexes = (
            (('user_id', 'invite_code'), False),
        )

class AmItemDetails(BaseModel):
    details_content = CharField(null=True)
    details_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    details_id = AutoField()
    details_level = IntegerField()
    details_remark = CharField(null=True)
    details_type = CharField()
    details_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    details_val_type = CharField(null=True)
    details_value = CharField(null=True)
    item_id = IntegerField()

    class Meta:
        table_name = 'am_item_details'

class AmItemRange(BaseModel):
    item_id = IntegerField()
    link_id = AutoField()
    range_id = IntegerField()

    class Meta:
        table_name = 'am_item_range'

class AmMonthCouponTp(BaseModel):
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_code = CharField(null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = AutoField()
    coupon_name = CharField()
    coupon_nouse_cause = CharField(null=True)
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField()
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_use_dir = CharField(null=True)
    coupon_use_info = CharField(null=True)
    coupon_use_type = IntegerField(null=True)
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    push_info = CharField(null=True)
    sms_info = CharField(null=True)

    class Meta:
        table_name = 'am_month_coupon_tp'

class AmMutexInfo(BaseModel):
    mutex_id = AutoField()
    mutex_remark = CharField(null=True)
    mutex_status = IntegerField()
    that_act_id = IntegerField()
    this_act_id = IntegerField()

    class Meta:
        table_name = 'am_mutex_info'

class AmQuotaInfo(BaseModel):
    item_id = IntegerField()
    quota_content = CharField(null=True)
    quota_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    quota_id = AutoField()
    quota_kind = CharField()
    quota_remark = CharField(null=True)
    quota_rule = CharField()
    quota_status = IntegerField()
    quota_total = IntegerField(null=True)
    quota_type = CharField()
    quota_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    qutoa_group = IntegerField(null=True)

    class Meta:
        table_name = 'am_quota_info'

class AmRangeExtend(BaseModel):
    extend_id = AutoField()
    extend_remark = CharField(null=True)
    extend_val = IntegerField()
    range_id = IntegerField()
    range_type = CharField(null=True)

    class Meta:
        table_name = 'am_range_extend'

class AmSkuImg(BaseModel):
    act_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    act_img_url = CharField()
    act_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    act_status = IntegerField()
    act_type = CharField(null=True)
    aspect_ratio = IntegerField(null=True)
    create_time = DateTimeField(null=True)
    link_id = AutoField()
    remark = CharField(null=True)
    sku_id = IntegerField()
    update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'am_sku_img'

class AmSkuImg200208(BaseModel):
    act_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    act_img_url = CharField()
    act_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    act_status = IntegerField()
    act_type = CharField(null=True)
    aspect_ratio = IntegerField(null=True)
    create_time = DateTimeField(null=True)
    link_id = AutoField()
    remark = CharField(null=True)
    sku_id = IntegerField()
    update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'am_sku_img_200208'

class AmSkuStat(BaseModel):
    device_id = CharField(null=True)
    item_id = IntegerField()
    opd_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    opd_extend = CharField(null=True)
    opd_id = AutoField()
    opd_remark = CharField(null=True)
    opd_status = IntegerField(null=True)
    opd_type = CharField(null=True)
    opd_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    quota_id = IntegerField()
    sku_amount = IntegerField()
    sku_date = CharField(null=True)
    sku_id = IntegerField()
    user_id = IntegerField()

    class Meta:
        table_name = 'am_sku_stat'
        indexes = (
            (('sku_id', 'item_id', 'quota_id', 'sku_amount'), False),
            (('user_id', 'device_id', 'item_id', 'quota_id'), False),
        )

class AmSkuStat20161220(BaseModel):
    device_id = CharField(null=True)
    item_id = IntegerField()
    opd_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    opd_extend = CharField(null=True)
    opd_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    opd_remark = CharField(null=True)
    opd_status = IntegerField(null=True)
    opd_type = CharField(null=True)
    opd_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    quota_id = IntegerField()
    sku_amount = IntegerField()
    sku_date = CharField(null=True)
    sku_id = IntegerField()
    user_id = IntegerField()

    class Meta:
        table_name = 'am_sku_stat_20161220'
        primary_key = False

class AmSkuStatDel(BaseModel):
    device_id = CharField(null=True)
    item_id = IntegerField()
    opd_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    opd_extend = CharField(null=True)
    opd_id = AutoField()
    opd_remark = CharField(null=True)
    opd_status = IntegerField(null=True)
    opd_type = CharField(null=True)
    opd_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    quota_id = IntegerField()
    sku_amount = IntegerField()
    sku_date = CharField(null=True)
    sku_id = IntegerField()
    user_id = IntegerField()

    class Meta:
        table_name = 'am_sku_stat_del'
        indexes = (
            (('user_id', 'device_id', 'item_id', 'quota_id'), False),
        )

class AmSkuStatHis(BaseModel):
    device_id = CharField(null=True)
    item_id = IntegerField()
    opd_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    opd_extend = CharField(null=True)
    opd_id = AutoField()
    opd_remark = CharField(null=True)
    opd_status = IntegerField(null=True)
    opd_type = CharField(null=True)
    opd_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    quota_id = IntegerField()
    sku_amount = IntegerField()
    sku_date = CharField(null=True)
    sku_id = IntegerField()
    user_id = IntegerField()

    class Meta:
        table_name = 'am_sku_stat_his'
        indexes = (
            (('user_id', 'device_id', 'item_id', 'quota_id'), False),
        )

class AmStagesSale(BaseModel):
    act_id = IntegerField(null=True)
    item_id = IntegerField(null=True)
    pharmacy_id = IntegerField()
    quota_id = IntegerField(null=True)
    sg_color = CharField(null=True)
    sg_create_time = DateTimeField(null=True)
    sg_end_time = DateTimeField(null=True)
    sg_id = AutoField()
    sg_json = CharField(null=True)
    sg_remark = CharField(null=True)
    sg_start_time = DateTimeField(null=True)
    sg_status = IntegerField()
    sg_title = CharField()
    sg_update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'am_stages_sale'
        indexes = (
            (('pharmacy_id', 'sg_status', 'sg_end_time', 'sg_start_time'), False),
        )

class AmStagesSaleDetail(BaseModel):
    act_id = IntegerField()
    dir_id = IntegerField()
    item_id = IntegerField()
    pharmacy_id = IntegerField()
    quota_id = IntegerField()
    sg_detail_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sg_detail_flag = IntegerField()
    sg_detail_id = AutoField()
    sg_detail_remark = CharField(null=True)
    sg_detail_type = CharField(null=True)
    sg_detail_update_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sg_id = IntegerField()

    class Meta:
        table_name = 'am_stages_sale_detail'
        indexes = (
            (('sg_id', 'dir_id'), False),
        )

class AmStatHis(BaseModel):
    act_id = IntegerField()
    batch_num = CharField()
    item_attr = CharField(null=True)
    item_effect_time = DateTimeField(null=True)
    item_expire_time = DateTimeField(null=True)
    item_flag = CharField(null=True)
    item_id = IntegerField()
    item_name = CharField(null=True)
    item_priority = IntegerField(null=True)
    item_remark = CharField(null=True)
    item_type = CharField()
    other_str1 = CharField(null=True)
    quota_id = IntegerField(null=True)
    sku_id = IntegerField()
    stat_create_time = DateTimeField(null=True)
    stat_id = AutoField()
    stat_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'am_stat_his'

class AmStatInfo(BaseModel):
    act_id = IntegerField()
    batch_num = CharField()
    item_attr = CharField(null=True)
    item_effect_time = DateTimeField(null=True)
    item_expire_time = DateTimeField(null=True)
    item_flag = CharField(null=True)
    item_id = IntegerField()
    item_name = CharField(null=True)
    item_priority = IntegerField(null=True)
    item_remark = CharField(null=True)
    item_type = CharField()
    other_str1 = CharField(null=True)
    quota_id = IntegerField(null=True)
    sku_id = IntegerField()
    stat_create_time = DateTimeField(null=True)
    stat_id = AutoField()
    stat_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'am_stat_info'
        indexes = (
            (('sku_id', 'batch_num', 'item_id', 'quota_id'), False),
            (('sku_id', 'item_effect_time', 'item_expire_time', 'item_type', 'item_id'), False),
        )

class AmStatInfo180810(BaseModel):
    act_id = IntegerField()
    batch_num = CharField()
    item_attr = CharField(null=True)
    item_effect_time = DateTimeField(null=True)
    item_expire_time = DateTimeField(null=True)
    item_flag = CharField(null=True)
    item_id = IntegerField()
    item_name = CharField(null=True)
    item_priority = IntegerField(null=True)
    item_remark = CharField(null=True)
    item_type = CharField()
    other_str1 = CharField(null=True)
    quota_id = IntegerField(null=True)
    sku_id = IntegerField()
    stat_create_time = DateTimeField(null=True)
    stat_id = AutoField()
    stat_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'am_stat_info_180810'
        indexes = (
            (('sku_id', 'batch_num', 'item_id', 'quota_id'), False),
        )

class AmStatInfo200304(BaseModel):
    act_id = IntegerField()
    batch_num = CharField()
    item_attr = CharField(null=True)
    item_effect_time = DateTimeField(null=True)
    item_expire_time = DateTimeField(null=True)
    item_flag = CharField(null=True)
    item_id = IntegerField()
    item_name = CharField(null=True)
    item_priority = IntegerField(null=True)
    item_remark = CharField(null=True)
    item_type = CharField()
    other_str1 = CharField(null=True)
    quota_id = IntegerField(null=True)
    sku_id = IntegerField()
    stat_create_time = DateTimeField(null=True)
    stat_id = AutoField()
    stat_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'am_stat_info_200304'
        indexes = (
            (('sku_id', 'batch_num', 'item_id', 'quota_id'), False),
        )

class AmStockLimit(BaseModel):
    as_id = AutoField()
    as_remark = CharField(null=True)
    item_id = IntegerField()
    max_total = IntegerField(null=True)
    quota_id = IntegerField(null=True)
    sku_id = IntegerField()
    sku_total = IntegerField()

    class Meta:
        table_name = 'am_stock_limit'

class AmStockLimitTemp(BaseModel):
    as_id = AutoField()
    as_remark = CharField(null=True)
    item_id = IntegerField()
    max_total = IntegerField(null=True)
    quota_id = IntegerField(null=True)
    sku_id = IntegerField()
    sku_total = IntegerField()

    class Meta:
        table_name = 'am_stock_limit_temp'

class AmStockLimitTempTemp(BaseModel):
    as_id = AutoField()
    as_remark = CharField(null=True)
    item_id = IntegerField()
    max_total = IntegerField(null=True)
    quota_id = IntegerField(null=True)
    sku_id = IntegerField()
    sku_total = IntegerField()

    class Meta:
        table_name = 'am_stock_limit_temp_temp'

class AmStockPday(BaseModel):
    act_id = IntegerField(null=True)
    huohao = CharField(null=True)
    item_id = IntegerField(null=True)
    kill_price = IntegerField(null=True)
    link_id = AutoField()
    pharmacy_id = IntegerField(null=True)
    prod_name = CharField(null=True)
    prod_spce = CharField(null=True)
    quota_id = IntegerField(null=True)
    remark = CharField(null=True)
    sku_fee = IntegerField(null=True)
    sku_id = IntegerField(null=True)
    sku_num = IntegerField(null=True)
    sku_order = IntegerField(null=True)
    sku_total = IntegerField(null=True)

    class Meta:
        table_name = 'am_stock_pday'

class BjpDrugDetail(BaseModel):
    bjp_id = AutoField()
    common_name = CharField(null=True)
    company_name = CharField(null=True)
    component = CharField(null=True)
    condition = CharField(null=True)
    contraindications = TextField(null=True)
    dosage = TextField(null=True)
    format = CharField(null=True)
    health_function = CharField(null=True)
    huohao = IntegerField()
    material = CharField(null=True)
    microorganism = CharField(null=True)
    number = CharField(null=True)
    other = TextField(null=True)
    packages = CharField(null=True)
    precautions = TextField(null=True)
    product_name = CharField(null=True)
    publish_date = CharField(null=True)
    suitable_for = CharField(null=True)
    unsuitable_for = CharField(null=True)

    class Meta:
        table_name = 'bjp_drug_detail'

class Calendar(BaseModel):
    datelist = DateField(null=True)

    class Meta:
        table_name = 'calendar'
        primary_key = False



class DrugCnInfo(BaseModel):
    di_fda = CharField(column_name='di_FDA', null=True)
    di_otc = CharField(column_name='di_OTC', null=True)
    di_administration = TextField(null=True)
    di_adverse_reactions = TextField(column_name='di_adverseReactions', null=True)
    di_approve_date = TextField(column_name='di_approveDate', null=True)
    di_cate_name = CharField(column_name='di_cateName', null=True)
    di_cautions = TextField(null=True)
    di_chemical = TextField(null=True)
    di_clinical_trial = TextField(column_name='di_clinicalTrial', null=True)
    di_cn_name = CharField(column_name='di_cnName', null=True)
    di_common_name = CharField(column_name='di_commonName', null=True)
    di_company_name = CharField(column_name='di_companyName', null=True)
    di_component = TextField(null=True)
    di_contraindications = TextField(null=True)
    di_description = TextField(null=True)
    di_dosage = TextField(null=True)
    di_drug_interactions = TextField(column_name='di_drugInteractions', null=True)
    di_eng_name = CharField(column_name='di_engName', null=True)
    di_forensic_classification = CharField(column_name='di_forensicClassification', null=True)
    di_form = TextField(null=True)
    di_indication = TextField(null=True)
    di_mechanism_action = TextField(column_name='di_mechanismAction', null=True)
    di_modify_date = CharField(column_name='di_modifyDate', null=True)
    di_number = CharField(null=True)
    di_overdosage = TextField(null=True)
    di_pack = TextField(null=True)
    di_period = CharField(null=True)
    di_pharmacokinetics = TextField(null=True)
    di_pic_path = TextField(column_name='di_picPath', null=True)
    di_poison = TextField(null=True)
    di_precautions = TextField(null=True)
    di_price = CharField(null=True)
    di_show_name = CharField(column_name='di_showName', null=True)
    di_standard = TextField(null=True)
    di_storage = TextField(null=True)
    di_use_in_children = TextField(column_name='di_useInChildren', null=True)
    di_use_in_elderly = TextField(column_name='di_useInElderly', null=True)
    di_use_in_preg_lact = TextField(column_name='di_useInPregLact', null=True)
    di_warnings = TextField(null=True)
    drug_id = IntegerField(column_name='drugId', null=True)

    class Meta:
        table_name = 'drug_cn_info'
        primary_key = False

class ExCourierOrder(BaseModel):
    courier_id = IntegerField()
    order_id = IntegerField()
    uo_id = AutoField()

    class Meta:
        table_name = 'ex_courier_order'

class ExFeedBack(BaseModel):
    age = IntegerField(null=True)
    back_type = CharField(null=True)
    feed_create_time = DateTimeField(null=True)
    feed_id = AutoField()
    feed_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    manner = IntegerField(null=True)
    order_id = IntegerField()
    pharmacy_id = IntegerField(null=True)
    remark = CharField(null=True)
    satisfaction = IntegerField(null=True)
    sex = IntegerField(null=True)
    user_id = IntegerField(null=True)
    user_phone = CharField(null=True)

    class Meta:
        table_name = 'ex_feed_back'

class ExUserInfo(BaseModel):
    employee_id = IntegerField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    pharmacy_id = IntegerField()
    phone_num = CharField()
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    remark = CharField(null=True)
    user_create_time = DateTimeField(null=True)
    user_id = AutoField()
    user_status = IntegerField(null=True)
    user_token = CharField(null=True)
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField()

    class Meta:
        table_name = 'ex_user_info'

class Haibin0104(BaseModel):
    chanpindalei = CharField(null=True)
    chanpinhuohao = CharField(null=True)
    chanpinxiaolei = CharField(null=True)
    dir_code = CharField(null=True)
    dir_id = IntegerField(null=True)
    shangpincuxiaojia = IntegerField(null=True)
    shangpinming = CharField(null=True)
    shangpinyuanjia = IntegerField(null=True)
    sku_id = CharField(null=True)
    tongyongming = CharField(null=True)
    xuhao = CharField(null=True)
    zongshu = CharField(null=True)

    class Meta:
        table_name = 'haibin_0104'

class Hj77Z(BaseModel):
    促销价 = FloatField(null=True)
    分类 = CharField(null=True)
    单位 = CharField(null=True)
    厂家 = CharField(null=True)
    原价 = FloatField(null=True)
    品牌 = CharField(null=True)
    商品名 = CharField(null=True)
    规格 = CharField(null=True)
    门店商品货号 = CharField(null=True)
    限订库存量 = FloatField(null=True)

    class Meta:
        table_name = 'hj_77z'
        primary_key = False

class Hj7Z(BaseModel):
    促销价_元_ = FloatField(column_name='促销价（元）', null=True)
    分类 = CharField(null=True)
    单位 = CharField(null=True)
    厂家 = CharField(null=True)
    原价_元_ = FloatField(column_name='原价（元）', null=True)
    品牌 = CharField(null=True)
    商品名 = CharField(null=True)
    规格 = CharField(null=True)
    货号 = CharField(null=True)
    限订库存量 = FloatField(null=True)

    class Meta:
        table_name = 'hj_7z'
        primary_key = False

class HmCustAgent(BaseModel):
    admin_id = IntegerField()
    agent_addr = CharField(null=True)
    agent_code = CharField()
    agent_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    agent_id = AutoField()
    agent_name = CharField(null=True)
    agent_remark = CharField(null=True)
    agent_status = IntegerField()
    agent_tel = CharField()
    agent_type = CharField(null=True)
    agent_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    employee_id = IntegerField()
    employee_name = CharField()
    pharmacy_id = IntegerField()

    class Meta:
        table_name = 'hm_cust_agent'

class HmServiceReq(BaseModel):
    agent_id = IntegerField()
    cust_d = IntegerField(null=True)
    cust_phone = CharField()
    next_admin_id = IntegerField(null=True)
    order_id = IntegerField(null=True)
    sr_admin_id = IntegerField(null=True)
    sr_agent_id = IntegerField(null=True)
    sr_content = CharField(null=True)
    sr_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sr_id = AutoField()
    sr_phone = CharField(null=True)
    sr_plan_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sr_point_sum = IntegerField(null=True)
    sr_remark = CharField(null=True)
    sr_result = CharField(null=True)
    sr_status = IntegerField()
    sr_type = CharField()
    sr_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'hm_service_req'

class HmSrTrack(BaseModel):
    admin_id = IntegerField()
    agent_id = IntegerField(null=True)
    cust_id = IntegerField()
    cust_phone = CharField()
    sr_id = IntegerField()
    sr_last_status = IntegerField()
    sr_status = IntegerField(null=True)
    track_content = CharField(null=True)
    track_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    track_id = AutoField()
    track_remark = CharField(null=True)
    track_type = CharField()
    track_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'hm_sr_track'

class InventCodeAll(BaseModel):
    drugstore_id = CharField(null=True)
    drugstore_name = CharField(null=True)
    person_name = CharField(null=True)
    phone_number = CharField(null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'invent_code_all'

class Kangfuyaodian1128(BaseModel):
    bieming = CharField(null=True)
    chandi = CharField(null=True)
    danwei = CharField(null=True)
    guige = CharField(null=True)
    huohao = CharField(null=True)
    lingshoujia = CharField(null=True)
    pinming = CharField(null=True)
    pizhunwenhao = CharField(null=True)
    sku_id = CharField(null=True)
    xitongid = CharField(null=True)

    class Meta:
        table_name = 'kangfuyaodian_1128'
        primary_key = False

class Kangzhongfu1123(BaseModel):
    dir_code = CharField(null=True)
    id = CharField(constraints=[SQL("DEFAULT ''")], primary_key=True)
    paixu = CharField(null=True)
    sku_id = CharField(null=True)

    class Meta:
        table_name = 'kangzhongfu_1123'

class Kangzhongfu112302(BaseModel):
    dir_code = CharField(index=True, null=True)
    id = CharField(constraints=[SQL("DEFAULT ''")], primary_key=True)
    paixu = CharField(null=True)
    sku_id = CharField(null=True)

    class Meta:
        table_name = 'kangzhongfu_112302'

class Kangzhongfu112303(BaseModel):
    dir_code = CharField(null=True)
    id = CharField(constraints=[SQL("DEFAULT ''")], primary_key=True)
    paixu = CharField(null=True)
    sku_id = CharField(null=True)

    class Meta:
        table_name = 'kangzhongfu_112303'

class Kangzhongfu1128(BaseModel):
    dir_code = CharField(null=True)
    sku_id = CharField(null=True)
    xuhao = CharField(null=True)

    class Meta:
        table_name = 'kangzhongfu_1128'

class Kangzhongfu112802(BaseModel):
    dir_code = CharField(null=True)
    sku_id = CharField(null=True)
    xuhao = CharField(null=True)

    class Meta:
        table_name = 'kangzhongfu_112802'

class Kangzhongfu112803(BaseModel):
    dir_code = CharField(null=True)
    price = IntegerField(null=True)
    sku_id = CharField(null=True)
    xuhao = CharField(null=True)

    class Meta:
        table_name = 'kangzhongfu_112803'

class KzfMulu83(BaseModel):
    dircode = CharField(null=True)
    dirid = IntegerField(null=True)
    huohao = CharField(constraints=[SQL("DEFAULT '0'")])
    skuid = IntegerField(null=True)

    class Meta:
        table_name = 'kzf_mulu_8_3'

class LmTemInstance(BaseModel):
    effect_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    ins_priority = IntegerField(null=True)
    ins_rule = CharField(null=True)
    invalid_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    other_info = CharField(null=True)
    pharmacy_id = IntegerField(null=True)
    tem_id = IntegerField(null=True)
    tem_ins_id = AutoField()

    class Meta:
        table_name = 'lm_tem_instance'

class LmTemItem(BaseModel):
    col_aspect_radio = IntegerField(null=True)
    col_seq = IntegerField(null=True)
    col_span = IntegerField(null=True)
    col_width = IntegerField(null=True)
    item_id = AutoField()
    item_seq = IntegerField(null=True)
    row_seq = IntegerField(null=True)
    row_span = IntegerField(null=True)
    tem_id = IntegerField(null=True)

    class Meta:
        table_name = 'lm_tem_item'

class LmTemItemIns(BaseModel):
    ins_desc = CharField(null=True)
    relation_id = IntegerField(null=True)
    relation_object = CharField(null=True)
    tem_ins_id = IntegerField(null=True)
    tem_item_id = IntegerField(null=True)
    tem_item_ins_id = AutoField()

    class Meta:
        table_name = 'lm_tem_item_ins'

class LmTemplate(BaseModel):
    tem_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    tem_desc = CharField(null=True)
    tem_id = AutoField()
    tem_name = CharField(null=True)
    tem_status = IntegerField(null=True)
    tem_update_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])

    class Meta:
        table_name = 'lm_template'

class MsBasePinyin(BaseModel):
    prod_id = AutoField()
    py = CharField(null=True)
    short_py = CharField(null=True)

    class Meta:
        table_name = 'ms_base_pinyin'

class NewCategory(BaseModel):
    category_code = CharField(null=True)
    category__id = IntegerField(column_name='category_⁯id', null=True)
    hb = CharField(null=True)
    一级目录 = CharField(null=True)
    三级目录 = CharField(null=True)
    二级目录 = CharField(null=True)
    修改项目 = CharField(null=True)
    合并1 = CharField(null=True)
    合并10 = CharField(null=True)
    合并11 = CharField(null=True)
    合并12 = CharField(null=True)
    合并13 = CharField(null=True)
    合并2 = CharField(null=True)
    合并3 = CharField(null=True)
    合并4 = CharField(null=True)
    合并5 = CharField(null=True)
    合并6 = CharField(null=True)
    合并7 = CharField(null=True)
    合并8 = CharField(null=True)
    合并9 = CharField(null=True)
    目录编码 = CharField(null=True)
    编码 = CharField(null=True)

    class Meta:
        table_name = 'new_category'

class OmActIns(BaseModel):
    act_item_id = IntegerField()
    details_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    details_id = IntegerField()
    details_ins_id = AutoField()
    details_level = IntegerField()
    details_remark = CharField(null=True)
    details_type = CharField()
    details_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    details_val_type = CharField()
    details_value = CharField()
    is_active = CharField(null=True)
    order_id = IntegerField()
    order_item_id = IntegerField()
    order_value = IntegerField(null=True)

    class Meta:
        table_name = 'om_act_ins'

class OmCartInfo(BaseModel):
    cart_create_time = DateTimeField(null=True)
    cart_id = AutoField()
    cart_remark = CharField(null=True)
    cart_sku_type = CharField(null=True)
    cart_type = CharField()
    cart_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    pharmacy_id = IntegerField()
    sku_amount = IntegerField()
    sku_id = IntegerField(index=True)
    sku_selected = CharField()
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = IntegerField(index=True)

    class Meta:
        table_name = 'om_cart_info'

class OmDeliverFee(BaseModel):
    date_range = CharField()
    deliver_fee = IntegerField()
    deliver_order2 = CharField(null=True)
    deliver_other = CharField(null=True)
    deliver_remark = CharField()
    deliver_sort = CharField()
    deliver_status = IntegerField()
    deliver_type = CharField()
    fee_id = AutoField()
    pharmacy_id = IntegerField()
    threshold_value = IntegerField()
    time_range = CharField()
    user_old_or_new = IntegerField(null=True)

    class Meta:
        table_name = 'om_deliver_fee'

class OmDeliveryInfo(BaseModel):
    addr = CharField(null=True)
    contact = CharField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_id = IntegerField()
    phone = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'om_delivery_info'

class OmLogistComp(BaseModel):
    cp_addr = CharField(null=True)
    cp_code = CharField()
    cp_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    cp_id = AutoField()
    cp_name = CharField()
    cp_remark = CharField(null=True)
    cp_type = CharField()
    cp_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'om_logist_comp'

class OmLogistTrack(BaseModel):
    lg_content = CharField(null=True)
    lg_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    lg_from_status = IntegerField()
    lg_his_id = AutoField()
    lg_his_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    lg_to_status = IntegerField()
    lg_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    logist_id = IntegerField()
    staff_id = IntegerField()

    class Meta:
        table_name = 'om_logist_track'

class OmOrderAddr(BaseModel):
    accept_name = CharField()
    accept_phone = CharField(index=True, null=True)
    addr_city = CharField(null=True)
    addr_create_time = DateTimeField(null=True)
    addr_dist = CharField(null=True)
    addr_id = AutoField()
    addr_info = CharField()
    addr_pos = CharField(null=True)
    addr_prov = CharField(null=True)
    addr_remark = CharField(null=True)
    addr_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    logisit_custom_time = DateTimeField(index=True, null=True)
    logist_arrival_minute = IntegerField(null=True)
    logist_arrival_time = DateTimeField(null=True)
    logist_comp = IntegerField(index=True, null=True)
    logist_end_time = DateTimeField(index=True, null=True)
    logist_fee = IntegerField(null=True)
    logist_start_time = DateTimeField(null=True)
    logist_status = CharField(null=True)
    logist_type = CharField(null=True)
    order_id = IntegerField(index=True)
    pharmacy_id = IntegerField(null=True)
    user_label = IntegerField(null=True)
    user_sex = IntegerField(null=True)
    zip_code = CharField(null=True)

    class Meta:
        table_name = 'om_order_addr'
        indexes = (
            (('addr_city', 'addr_dist', 'logist_status', 'addr_info'), False),
        )

class OmOrderCoupon(BaseModel):
    coupon_id = IntegerField()
    coupon_status = CharField(null=True)
    coupon_threshold = IntegerField(null=True)
    coupon_value = IntegerField()
    order_id = IntegerField(index=True)
    uc_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    uc_id = AutoField()
    uc_other1 = CharField(null=True)
    uc_remark = CharField(null=True)
    uc_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'om_order_coupon'

class OmOrderDel(BaseModel):
    order_create_time = DateTimeField(null=True)
    order_fee = IntegerField()
    order_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_mark = IntegerField()
    order_other1 = CharField(null=True)
    order_other2 = CharField(null=True)
    order_pay_fee = IntegerField()
    order_remark = CharField(null=True)
    order_status = IntegerField()
    order_type = CharField()
    order_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    paid_fee = IntegerField(null=True)
    pay_bank = CharField(null=True)
    pay_status = IntegerField()
    pay_type = CharField()
    pharmacy_id = IntegerField()
    user_id = IntegerField()

    class Meta:
        table_name = 'om_order_del'
        primary_key = False

class OmOrderFengniao(BaseModel):
    carrier_driver_name = CharField(null=True)
    carrier_driver_phone = CharField(null=True)
    create_time = DateTimeField(null=True)
    current_status = IntegerField(null=True)
    delivery_distance_meter = IntegerField(null=True)
    disabled = IntegerField(constraints=[SQL("DEFAULT 000")])
    drugstore_id = IntegerField(null=True)
    express_type = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    id = BigAutoField()
    order_id = IntegerField()
    status_desc = CharField(null=True)
    sys_order_id = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'om_order_fengniao'

class OmOrderFengniaoStatus(BaseModel):
    address = CharField(null=True)
    cancel_reason = IntegerField(null=True)
    carrier_driver_name = CharField(null=True)
    carrier_driver_phone = CharField(null=True)
    create_time = DateTimeField(null=True)
    description = CharField(null=True)
    error_code = CharField(null=True)
    id = BigAutoField()
    latitude = CharField(null=True)
    longitude = CharField(null=True)
    order_id = IntegerField()
    order_status = IntegerField(null=True)
    push_time = BigIntegerField(null=True)
    station_name = CharField(null=True)
    station_tel = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'om_order_fengniao_status'

class OmOrderInfo(BaseModel):
    is_coupon_timeout = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_first_print = IntegerField(constraints=[SQL("DEFAULT 000")], null=True)
    is_send_timeout = IntegerField(constraints=[SQL("DEFAULT 000")], null=True)
    obtain_type = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    order_create_time = DateTimeField(index=True, null=True)
    order_fee = IntegerField()
    order_id = AutoField()
    order_isreply = CharField(constraints=[SQL("DEFAULT 'false'")], null=True)
    order_json = CharField(null=True)
    order_mark = IntegerField()
    order_other1 = CharField(null=True)
    order_other2 = CharField(null=True)
    order_pay_fee = IntegerField()
    order_remark = CharField(null=True)
    order_reminder = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    order_status = IntegerField(index=True)
    order_type = CharField()
    order_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    paid_fee = IntegerField(null=True)
    pay_bank = CharField(null=True)
    pay_status = IntegerField()
    pay_type = CharField()
    pharmacy_id = IntegerField()
    picture_url = TextField(null=True)
    prebook_type = IntegerField(null=True)
    reply_read = IntegerField(null=True)
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    special_id = CharField(null=True)
    special_img = CharField(null=True)
    special_req = TextField(null=True)
    special_status = IntegerField(constraints=[SQL("DEFAULT 00000000000")])
    special_type = IntegerField(constraints=[SQL("DEFAULT 0000000000")])
    special_user_id = IntegerField(constraints=[SQL("DEFAULT 00000000000")])
    user_id = IntegerField(index=True)

    class Meta:
        table_name = 'om_order_info'
        indexes = (
            (('pharmacy_id', 'order_remark'), False),
        )

class OmOrderInfoHis(BaseModel):
    order_create_time = DateTimeField(index=True, null=True)
    order_fee = IntegerField()
    order_id = AutoField()
    order_isreply = CharField(constraints=[SQL("DEFAULT 'false'")], null=True)
    order_mark = IntegerField()
    order_other1 = CharField(null=True)
    order_other2 = CharField(null=True)
    order_pay_fee = IntegerField()
    order_remark = CharField(null=True)
    order_status = IntegerField(index=True)
    order_type = CharField()
    order_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    paid_fee = IntegerField(null=True)
    pay_bank = CharField(null=True)
    pay_status = IntegerField()
    pay_type = CharField()
    pharmacy_id = IntegerField(index=True)
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = IntegerField()

    class Meta:
        table_name = 'om_order_info_his'

class OmOrderItem(BaseModel):
    item_attr = CharField(null=True)
    item_cost = IntegerField()
    item_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    item_desc = CharField(null=True)
    item_extend = CharField(null=True)
    item_fee = IntegerField()
    item_id = AutoField()
    item_name = CharField(null=True)
    item_remark = CharField(null=True)
    item_type = CharField(null=True)
    item_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_id = IntegerField(index=True)
    other_id = IntegerField(null=True)

    class Meta:
        table_name = 'om_order_item'

class OmOrderLogist(BaseModel):
    logist_comp = IntegerField()
    logist_create_time = DateTimeField(null=True)
    logist_end_time = DateTimeField(null=True)
    logist_fee = IntegerField()
    logist_id = AutoField()
    logist_other1 = CharField(null=True)
    logist_other2 = CharField(null=True)
    logist_other3 = CharField(null=True)
    logist_remark = CharField(null=True)
    logist_start_time = DateTimeField(null=True)
    logist_status = IntegerField()
    logist_type = IntegerField()
    logist_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_id = IntegerField()

    class Meta:
        table_name = 'om_order_logist'

class OmOrderQrcode(BaseModel):
    app_id = CharField(null=True)
    captcha = CharField(null=True)
    create_time = DateTimeField(null=True)
    disabled = IntegerField(null=True)
    order_id = IntegerField(null=True)
    push_time = DateTimeField(null=True)
    qrcode_content = CharField(null=True)
    qrcode_status = IntegerField(null=True)
    qrcode_url = CharField(null=True)
    token = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'om_order_qrcode'

class OmOrderReply(BaseModel):
    delivery_comment = CharField(null=True)
    delivery_level = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    has_banword = IntegerField(constraints=[SQL("DEFAULT 0000000000")], null=True)
    order_id = IntegerField(index=True)
    reply_content = CharField()
    reply_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    reply_id = AutoField()
    reply_level = IntegerField(null=True)
    reply_manner = IntegerField()
    reply_remark = CharField(null=True)
    reply_speed = IntegerField()
    reply_synthesize = IntegerField()
    reply_title = CharField(null=True)
    reply_update_time = DateTimeField(null=True)
    user_id = IntegerField()

    class Meta:
        table_name = 'om_order_reply'

class OmOrderSpecialUser(BaseModel):
    drug_user_id = IntegerField(null=True)
    oredr_id = IntegerField(null=True)
    special_user_amh = CharField(null=True)
    special_user_birthdate = CharField(null=True)
    special_user_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    special_user_disease_list = CharField(null=True)
    special_user_fmh = CharField(null=True)
    special_user_id = AutoField()
    special_user_idcard = CharField(null=True)
    special_user_liver_desc = CharField(null=True)
    special_user_name = CharField(null=True)
    special_user_nurse_desc = CharField(null=True)
    special_user_phone = CharField(null=True)
    special_user_pmh = CharField(null=True)
    special_user_renal_desc = CharField(null=True)
    special_user_sex = CharField(null=True)
    special_user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    special_user_weight = CharField(null=True)

    class Meta:
        table_name = 'om_order_special_user'

class OmOrderTrack(BaseModel):
    order_id = IntegerField(index=True)
    order_status = IntegerField()
    track_arrival_time = DateTimeField(null=True)
    track_code = IntegerField()
    track_consum_time = IntegerField(null=True)
    track_content = CharField()
    track_create_time = DateTimeField(index=True, null=True)
    track_id = AutoField()
    track_name = CharField()
    track_remark = CharField(null=True)
    track_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'om_order_track'
        indexes = (
            (('order_id', 'track_code'), False),
        )

class OmPayBill(BaseModel):
    bank_no = CharField(null=True)
    bill_id = AutoField()
    bill_remark = CharField(null=True)
    bill_resp = CharField(null=True)
    deal_type = CharField(null=True)
    order_id = CharField(null=True)
    order_no = CharField(null=True)
    order_user = CharField(null=True)
    pay_date = DateTimeField(null=True)
    pay_fee = CharField(null=True)
    pay_serial = CharField(null=True)
    pay_type = CharField(null=True)
    product_name = CharField(null=True)
    refund_type = CharField(null=True)

    class Meta:
        table_name = 'om_pay_bill'

class OmPayInfo(BaseModel):
    order_id = CharField(index=True, null=True)
    pay_bank = CharField()
    pay_bill_confirm = IntegerField(null=True)
    pay_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    pay_fee = IntegerField()
    pay_id = AutoField()
    pay_other1 = CharField(null=True)
    pay_other2 = CharField(null=True)
    pay_remark = CharField(null=True)
    pay_req_data = CharField(null=True)
    pay_req_time = DateTimeField(null=True)
    pay_resp_data = CharField(null=True)
    pay_resp_time = DateTimeField(null=True)
    pay_result = CharField(null=True)
    pay_serial = CharField(null=True)
    pay_status = CharField(index=True)
    pay_type = CharField()
    pay_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'om_pay_info'

class OmPayOrder(BaseModel):
    link_id = AutoField()
    order_id = IntegerField()
    pay_id = IntegerField()

    class Meta:
        table_name = 'om_pay_order'
        indexes = (
            (('order_id', 'pay_id'), False),
        )

class OmPayVerify(BaseModel):
    batch_no = CharField(null=True)
    check_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], null=True)
    check_id = AutoField()
    check_remark = CharField(null=True)
    check_req = CharField(null=True)
    check_resp = CharField(null=True)
    check_result = CharField(null=True)
    check_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], null=True)
    check_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    order_id = IntegerField(null=True)
    pay_fee = CharField(null=True)
    pay_id = IntegerField(null=True)
    pay_serial = CharField(null=True)

    class Meta:
        table_name = 'om_pay_verify'

class OmPreOrder(BaseModel):
    addr_id = IntegerField(null=True)
    pharmacy_id = IntegerField()
    pre_addr = CharField(null=True)
    pre_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    pre_id = AutoField()
    pre_json = CharField(null=True)
    pre_phone = CharField(null=True)
    pre_remark = CharField(null=True)
    pre_rx = CharField(null=True)
    pre_status = CharField(null=True)
    pre_type = CharField(null=True)
    pre_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    pre_url = CharField(null=True)
    user_id = IntegerField(null=True)
    user_phone = CharField(null=True)

    class Meta:
        table_name = 'om_pre_order'

class OmPreSku(BaseModel):
    pcart_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    pcart_id = AutoField()
    pcart_json = CharField(null=True)
    pcart_selected = CharField()
    pcart_type = CharField(null=True)
    pcart_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    pharmacy_id = IntegerField()
    pre_id = IntegerField()
    sku_amount = IntegerField()
    sku_id = IntegerField()
    source_id = CharField(null=True)
    user_id = IntegerField()

    class Meta:
        table_name = 'om_pre_sku'

class OmPrescriptionBack(BaseModel):
    back_id = AutoField()
    back_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    back_url = CharField(null=True)
    create_time = DateTimeField(null=True)
    deal_desc = CharField(null=True)
    doctor_name = CharField(null=True)
    inquiry_id = CharField(null=True)
    msg_id = CharField(null=True)
    msg_type = CharField(null=True)
    out_order_id = CharField(null=True)
    pic_url = CharField(null=True)
    sign = CharField(null=True)
    status = IntegerField(null=True)

    class Meta:
        table_name = 'om_prescription_back'

class OmProdAttr(BaseModel):
    attr_id = AutoField()
    attr_name = CharField()
    attr_remark = CharField(null=True)
    attr_type = CharField()
    attr_value = CharField(null=True)
    ins_id = IntegerField()

    class Meta:
        table_name = 'om_prod_attr'

class OmProdIns(BaseModel):
    category_id = IntegerField(null=True)
    ins_amount = IntegerField()
    ins_create_time = DateTimeField(index=True, null=True)
    ins_expand = CharField(null=True)
    ins_id = AutoField()
    ins_order_price = IntegerField(null=True)
    ins_price = IntegerField()
    ins_remark = CharField(null=True)
    ins_type = CharField(null=True)
    ins_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_id = IntegerField(index=True)
    order_item_id = IntegerField(index=True)
    prod_id = IntegerField()
    prod_img = CharField(null=True)
    prod_name = CharField(null=True)
    sku_huohao = CharField(null=True)
    sku_id = IntegerField(index=True)
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    total_price = IntegerField()

    class Meta:
        table_name = 'om_prod_ins'

class OmPushMess(BaseModel):
    mess_content = CharField(null=True)
    mess_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    mess_id = AutoField()
    mess_phone = CharField(null=True)
    mess_push_time = DateTimeField(null=True)
    mess_remark = CharField(null=True)
    mess_status = IntegerField(null=True)
    mess_type = CharField(null=True)
    mess_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_id = IntegerField(null=True)
    push_status = IntegerField(null=True)
    push_time = DateTimeField(null=True)

    class Meta:
        table_name = 'om_push_mess'

class OmSkuIns(BaseModel):
    coupon_id = IntegerField(null=True)
    cpn_mutex = CharField(column_name='cpn_Mutex', null=True)
    cpn_price = IntegerField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    details_id = IntegerField(null=True)
    details_remark = CharField(null=True)
    item_desc = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    item_flag = CharField(null=True)
    item_id = IntegerField(null=True)
    item_price = IntegerField(null=True)
    item_type = CharField(null=True)
    order_id = IntegerField()
    price = IntegerField(constraints=[SQL("DEFAULT 00000000000")], null=True)
    sku_amount = IntegerField()
    sku_huohao = CharField(null=True)
    sku_id = IntegerField()
    sku_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    use_cpn = CharField(null=True)

    class Meta:
        table_name = 'om_sku_ins'

class OmStatusFlow(BaseModel):
    admin_id = IntegerField(null=True)
    current_status = IntegerField(index=True)
    flow_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    flow_id = AutoField()
    flow_message = CharField(null=True)
    flow_remark = CharField(null=True)
    flow_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    handler_type = CharField()
    order_id = IntegerField(index=True)
    prev_status = IntegerField(index=True)

    class Meta:
        table_name = 'om_status_flow'

class OmVoucherOrderInfo(BaseModel):
    is_first_print = IntegerField(constraints=[SQL("DEFAULT 000")], null=True)
    is_send_timeout = IntegerField(constraints=[SQL("DEFAULT 000")], null=True)
    obtain_type = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    order_create_time = DateTimeField(index=True, null=True)
    order_fee = IntegerField()
    order_id = AutoField()
    order_isreply = CharField(constraints=[SQL("DEFAULT 'false'")], null=True)
    order_json = CharField(null=True)
    order_mark = IntegerField()
    order_other1 = CharField(null=True)
    order_other2 = CharField(null=True)
    order_pay_fee = IntegerField()
    order_remark = CharField(null=True)
    order_reminder = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    order_status = IntegerField(index=True)
    order_type = CharField()
    order_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    paid_fee = IntegerField(null=True)
    pay_bank = CharField(null=True)
    pay_status = IntegerField()
    pay_type = CharField()
    pharmacy_id = IntegerField()
    prebook_type = IntegerField(null=True)
    reply_read = IntegerField(null=True)
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = IntegerField(index=True)
    voucher_id = IntegerField(null=True)

    class Meta:
        table_name = 'om_voucher_order_info'
        indexes = (
            (('pharmacy_id', 'order_remark'), False),
        )

class OmVoucherPayInfo(BaseModel):
    order_id = CharField(null=True)
    pay_bank = CharField()
    pay_bill_confirm = IntegerField(null=True)
    pay_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    pay_fee = IntegerField()
    pay_id = AutoField()
    pay_other1 = CharField(null=True)
    pay_other2 = CharField(null=True)
    pay_remark = CharField(null=True)
    pay_req_data = CharField(null=True)
    pay_req_time = DateTimeField(null=True)
    pay_resp_data = CharField(null=True)
    pay_resp_time = DateTimeField(null=True)
    pay_result = CharField(null=True)
    pay_serial = CharField(null=True)
    pay_status = CharField(index=True)
    pay_type = CharField()
    pay_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'om_voucher_pay_info'

class Paixu0301(BaseModel):
    huohao = CharField(null=True)
    sku_id_0 = CharField(null=True)
    sku_id_1 = CharField(null=True)
    sku_id_2 = CharField(null=True)
    sku_id_3 = CharField(null=True)
    xuhao = FloatField(null=True)
    中类 = CharField(null=True)
    商品名称 = CharField(null=True)
    小类 = CharField(null=True)
    规格 = CharField(null=True)
    零售价 = FloatField(null=True)

    class Meta:
        table_name = 'paixu_0301'
        primary_key = False

class Parent1211(BaseModel):
    dir_code = CharField(null=True)
    dir_id = AutoField()
    dir_name = CharField(null=True)
    parent_dir_id = IntegerField(null=True)

    class Meta:
        table_name = 'parent_1211'

class PhPharmacyEmpl(BaseModel):
    empl_code = CharField(null=True)
    empl_id = AutoField()
    empl_name = CharField(null=True)
    empl_phone = CharField(index=True, null=True)
    pharmacy_group = CharField(null=True)
    pharmacy_id = IntegerField(null=True)
    pharmacy_name = CharField(null=True)
    pharmacy_place = CharField(null=True)
    user_id = IntegerField(index=True, null=True)
    user_invite_code = CharField(null=True)

    class Meta:
        table_name = 'ph_pharmacy_empl'

class PhPharmacyEmplHis(BaseModel):
    empl_code = CharField(null=True)
    empl_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    empl_name = CharField(null=True)
    empl_phone = CharField(null=True)
    pharmacy_group = CharField(null=True)
    pharmacy_id = IntegerField(null=True)
    pharmacy_name = CharField(null=True)
    pharmacy_place = CharField(null=True)
    user_id = IntegerField(null=True)
    user_invite_code = CharField(null=True)

    class Meta:
        table_name = 'ph_pharmacy_empl_his'
        primary_key = False

class Phone0711(BaseModel):
    phone_number = CharField(null=True)
    user_id = CharField(null=True)

    class Meta:
        table_name = 'phone_0711'
        primary_key = False

class Phone2000920(BaseModel):
    dianhua = CharField(null=True)
    drugstore_id = CharField(null=True)
    xingming = CharField(null=True)
    yaodianming = CharField(null=True)

    class Meta:
        table_name = 'phone_200_0920'

class Pinpai1104(BaseModel):
    chanpindalei = CharField(null=True)
    chanpinxiaolei = CharField(null=True)
    dir_remark = CharField(null=True)
    dir_remark_200 = CharField(null=True)
    drugstore_id = CharField(null=True)

    class Meta:
        table_name = 'pinpai_1104'

class PmActskuCheck(BaseModel):
    check_admin_id = IntegerField(null=True)
    check_create_time = DateTimeField(null=True)
    check_id = AutoField()
    check_pihao = CharField(null=True)
    check_status = IntegerField(null=True)
    check_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    drugstore_id = IntegerField(null=True)
    remark = CharField(null=True)
    sku_act_change = IntegerField(null=True)
    sku_act_last = IntegerField(null=True)
    sku_id = IntegerField(null=True)
    submit_admin_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_actsku_check'

class PmActskuHis(BaseModel):
    check_admin_id = IntegerField(null=True)
    check_create_time = DateTimeField(null=True)
    check_status = IntegerField(null=True)
    check_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    drugstore_id = IntegerField(null=True)
    his_id = AutoField()
    his_pihao = CharField(null=True)
    remark = CharField(null=True)
    sku_act_change = IntegerField(null=True)
    sku_act_last = IntegerField(null=True)
    sku_id = IntegerField(null=True)
    submit_admin_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_actsku_his'

class PmAttrValue(BaseModel):
    attr_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    attr_id = IntegerField()
    attr_remark = CharField(null=True)
    attr_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    attr_value = CharField()
    attr_value_id = AutoField()
    attr_value_num = IntegerField()
    attr_value_type = CharField()
    prod_id = IntegerField()

    class Meta:
        table_name = 'pm_attr_value'

class PmCategoryInfo(BaseModel):
    category_all_name = CharField()
    category_code = CharField(index=True)
    category_create_time = DateTimeField(null=True)
    category_id = AutoField()
    category_img = CharField(null=True)
    category_level = IntegerField()
    category_name = CharField()
    category_num = IntegerField()
    category_remark = CharField(null=True)
    category_revalue = CharField(null=True)
    category_status = IntegerField()
    category_type = CharField(constraints=[SQL("DEFAULT 'dir'")])
    category_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    parent_category_id = IntegerField(index=True, null=True)
    prod_sum = IntegerField()

    class Meta:
        table_name = 'pm_category_info'

class PmChufangInfo(BaseModel):
    分类 = CharField(null=True)
    单位 = CharField(null=True)
    厂家 = CharField(null=True)
    商品id = CharField(null=True)
    商品名 = CharField(null=True)
    建议更改 = CharField(null=True)
    批准文号 = CharField(null=True)
    是否禁开 = CharField(null=True)
    是否高危 = CharField(null=True)
    条码 = CharField(null=True)
    规格 = CharField(null=True)
    通用名 = CharField(null=True)

    class Meta:
        table_name = 'pm_chufang_info'
        primary_key = False

class PmCommentImg(BaseModel):
    comment_id = IntegerField()
    img_id = IntegerField()
    link_id = AutoField()

    class Meta:
        table_name = 'pm_comment_img'

class PmCommentInfo(BaseModel):
    comment_content = CharField(null=True)
    comment_create_time = DateTimeField(null=True)
    comment_id = AutoField()
    comment_key = CharField(null=True)
    comment_other1 = CharField(null=True)
    comment_other2 = CharField(null=True)
    comment_remark = CharField(null=True)
    comment_score = IntegerField()
    comment_time = DateTimeField(null=True)
    comment_title = CharField(null=True)
    comment_type = CharField(null=True)
    comment_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    has_banword = IntegerField(constraints=[SQL("DEFAULT 0000000000")], null=True)
    order_id = IntegerField(null=True)
    prod_id = IntegerField()
    reply_id = IntegerField(null=True)
    user_id = IntegerField()

    class Meta:
        table_name = 'pm_comment_info'

class PmCompanyInfo(BaseModel):
    company_code = CharField(null=True)
    company_flag = CharField(null=True)
    company_id = AutoField()
    company_name = CharField(null=True)

    class Meta:
        table_name = 'pm_company_info'

class PmDirInfo(BaseModel):
    category_id = IntegerField(index=True, null=True)
    dir_all_name = CharField(null=True)
    dir_code = CharField(index=True)
    dir_create_time = DateTimeField(null=True)
    dir_gotocata = CharField(null=True)
    dir_id = AutoField()
    dir_img = CharField(null=True)
    dir_level = IntegerField()
    dir_main_show = IntegerField(null=True)
    dir_name = CharField()
    dir_num = IntegerField()
    dir_remark = CharField(null=True)
    dir_revalue = CharField(null=True)
    dir_status = IntegerField()
    dir_type = CharField(constraints=[SQL("DEFAULT 'dir'")])
    dir_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    parent_dir_id = IntegerField(index=True, null=True)
    pharmacy_id = IntegerField(null=True)
    prod_sum = IntegerField()

    class Meta:
        table_name = 'pm_dir_info'
        indexes = (
            (('parent_dir_id', 'dir_id'), False),
        )

class PmDirInfo0901(BaseModel):
    category_id = IntegerField(index=True, null=True)
    dir_all_name = CharField(null=True)
    dir_code = CharField(index=True)
    dir_create_time = DateTimeField(null=True)
    dir_gotocata = CharField(null=True)
    dir_id = AutoField()
    dir_img = CharField(null=True)
    dir_level = IntegerField()
    dir_name = CharField()
    dir_num = IntegerField()
    dir_remark = CharField(null=True)
    dir_revalue = CharField(null=True)
    dir_status = IntegerField()
    dir_type = CharField(constraints=[SQL("DEFAULT 'dir'")])
    dir_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    parent_dir_id = IntegerField(index=True, null=True)
    pharmacy_id = IntegerField(null=True)
    prod_sum = IntegerField()

    class Meta:
        table_name = 'pm_dir_info_0901'
        indexes = (
            (('parent_dir_id', 'dir_id'), False),
        )

class PmDirInfo0930(BaseModel):
    category_id = IntegerField(null=True)
    dir_all_name = CharField(null=True)
    dir_code = CharField(index=True)
    dir_create_time = DateTimeField(null=True)
    dir_id = AutoField()
    dir_img = CharField(null=True)
    dir_level = IntegerField()
    dir_name = CharField()
    dir_num = IntegerField()
    dir_remark = CharField(null=True)
    dir_revalue = CharField(null=True)
    dir_status = IntegerField()
    dir_type = CharField(constraints=[SQL("DEFAULT 'dir'")])
    dir_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    parent_dir_id = IntegerField(index=True, null=True)
    pharmacy_id = IntegerField(null=True)
    prod_sum = IntegerField()

    class Meta:
        table_name = 'pm_dir_info_0930'

class PmDirInfo170421(BaseModel):
    category_id = IntegerField(index=True, null=True)
    dir_all_name = CharField(null=True)
    dir_code = CharField(index=True)
    dir_create_time = DateTimeField(null=True)
    dir_gotocata = CharField(null=True)
    dir_id = AutoField()
    dir_img = CharField(null=True)
    dir_level = IntegerField()
    dir_name = CharField()
    dir_num = IntegerField()
    dir_remark = CharField(null=True)
    dir_revalue = CharField(null=True)
    dir_status = IntegerField()
    dir_type = CharField(constraints=[SQL("DEFAULT 'dir'")])
    dir_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    parent_dir_id = IntegerField(index=True, null=True)
    pharmacy_id = IntegerField(null=True)
    prod_sum = IntegerField()

    class Meta:
        table_name = 'pm_dir_info_170421'
        indexes = (
            (('parent_dir_id', 'dir_id'), False),
        )

class PmDirInfo180706(BaseModel):
    category_id = IntegerField(index=True, null=True)
    dir_all_name = CharField(null=True)
    dir_code = CharField(index=True)
    dir_create_time = DateTimeField(null=True)
    dir_gotocata = CharField(null=True)
    dir_id = AutoField()
    dir_img = CharField(null=True)
    dir_level = IntegerField()
    dir_main_show = IntegerField(null=True)
    dir_name = CharField()
    dir_num = IntegerField()
    dir_remark = CharField(null=True)
    dir_revalue = CharField(null=True)
    dir_status = IntegerField()
    dir_type = CharField(constraints=[SQL("DEFAULT 'dir'")])
    dir_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    parent_dir_id = IntegerField(index=True, null=True)
    pharmacy_id = IntegerField(null=True)
    prod_sum = IntegerField()

    class Meta:
        table_name = 'pm_dir_info_180706'
        indexes = (
            (('parent_dir_id', 'dir_id'), False),
        )

class PmDirInfo180725(BaseModel):
    category_id = IntegerField(index=True, null=True)
    dir_all_name = CharField(null=True)
    dir_code = CharField(index=True)
    dir_create_time = DateTimeField(null=True)
    dir_gotocata = CharField(null=True)
    dir_id = AutoField()
    dir_img = CharField(null=True)
    dir_level = IntegerField()
    dir_main_show = IntegerField(null=True)
    dir_name = CharField()
    dir_num = IntegerField()
    dir_remark = CharField(null=True)
    dir_revalue = CharField(null=True)
    dir_status = IntegerField()
    dir_type = CharField(constraints=[SQL("DEFAULT 'dir'")])
    dir_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    parent_dir_id = IntegerField(index=True, null=True)
    pharmacy_id = IntegerField(null=True)
    prod_sum = IntegerField()

    class Meta:
        table_name = 'pm_dir_info_180725'
        indexes = (
            (('parent_dir_id', 'dir_id'), False),
        )

class PmDirInfo190109(BaseModel):
    category_id = IntegerField(index=True, null=True)
    dir_all_name = CharField(null=True)
    dir_code = CharField(index=True)
    dir_create_time = DateTimeField(null=True)
    dir_gotocata = CharField(null=True)
    dir_id = AutoField()
    dir_img = CharField(null=True)
    dir_level = IntegerField()
    dir_main_show = IntegerField(null=True)
    dir_name = CharField()
    dir_num = IntegerField()
    dir_remark = CharField(null=True)
    dir_revalue = CharField(null=True)
    dir_status = IntegerField()
    dir_type = CharField(constraints=[SQL("DEFAULT 'dir'")])
    dir_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    parent_dir_id = IntegerField(index=True, null=True)
    pharmacy_id = IntegerField(null=True)
    prod_sum = IntegerField()

    class Meta:
        table_name = 'pm_dir_info_190109'
        indexes = (
            (('parent_dir_id', 'dir_id'), False),
        )

class PmDirInfoBak180606(BaseModel):
    category_id = IntegerField(index=True, null=True)
    dir_all_name = CharField(null=True)
    dir_code = CharField(index=True)
    dir_create_time = DateTimeField(null=True)
    dir_gotocata = CharField(null=True)
    dir_id = AutoField()
    dir_img = CharField(null=True)
    dir_level = IntegerField()
    dir_main_show = IntegerField(null=True)
    dir_name = CharField()
    dir_num = IntegerField()
    dir_remark = CharField(null=True)
    dir_revalue = CharField(null=True)
    dir_status = IntegerField()
    dir_type = CharField(constraints=[SQL("DEFAULT 'dir'")])
    dir_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    parent_dir_id = IntegerField(index=True, null=True)
    pharmacy_id = IntegerField(null=True)
    prod_sum = IntegerField()

    class Meta:
        table_name = 'pm_dir_info_bak_180606'
        indexes = (
            (('parent_dir_id', 'dir_id'), False),
        )

class PmDirInfoNewc(BaseModel):
    category_id = IntegerField(index=True, null=True)
    dir_all_name = CharField(null=True)
    dir_code = CharField(index=True)
    dir_create_time = DateTimeField(null=True)
    dir_gotocata = CharField(null=True)
    dir_id = AutoField()
    dir_img = CharField(null=True)
    dir_level = IntegerField()
    dir_main_show = IntegerField(null=True)
    dir_name = CharField()
    dir_num = IntegerField()
    dir_remark = CharField(null=True)
    dir_revalue = CharField(null=True)
    dir_status = IntegerField()
    dir_type = CharField(constraints=[SQL("DEFAULT 'dir'")])
    dir_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    old_c_id = IntegerField(null=True)
    parent_dir_id = IntegerField(index=True, null=True)
    pharmacy_id = IntegerField(null=True)
    prod_sum = IntegerField()

    class Meta:
        table_name = 'pm_dir_info_newc'
        indexes = (
            (('parent_dir_id', 'dir_id'), False),
        )

class PmDirInfoTemp1213(BaseModel):
    category_id = IntegerField(index=True, null=True)
    dir_all_name = CharField(null=True)
    dir_code = CharField(index=True)
    dir_create_time = DateTimeField(null=True)
    dir_gotocata = CharField(null=True)
    dir_id = AutoField()
    dir_img = CharField(null=True)
    dir_level = IntegerField()
    dir_main_show = IntegerField(null=True)
    dir_name = CharField()
    dir_num = IntegerField()
    dir_remark = CharField(null=True)
    dir_revalue = CharField(null=True)
    dir_status = IntegerField()
    dir_type = CharField(constraints=[SQL("DEFAULT 'dir'")])
    dir_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    parent_dir_id = IntegerField(index=True, null=True)
    pharmacy_id = IntegerField(null=True)
    prod_sum = IntegerField()

    class Meta:
        table_name = 'pm_dir_info_temp1213'
        indexes = (
            (('parent_dir_id', 'dir_id'), False),
        )

class PmDiseaseDic(BaseModel):
    disease_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    disease_icd = CharField(null=True)
    disease_id = AutoField()
    disease_name = CharField(null=True)
    disease_sex = IntegerField()
    disease_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'pm_disease_dic'

class PmDiseaseDicCopy(BaseModel):
    disease_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    disease_icd = CharField(null=True)
    disease_id = AutoField()
    disease_name = CharField(null=True)
    disease_sex = IntegerField()
    disease_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'pm_disease_dic_copy'

class PmImageInfo(BaseModel):
    img_create_time = DateTimeField(null=True)
    img_id = AutoField()
    img_name = CharField()
    img_other1 = CharField(null=True)
    img_other2 = CharField(null=True)
    img_remark = CharField(null=True)
    img_status = IntegerField()
    img_type = CharField()
    img_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    img_url = CharField()

    class Meta:
        table_name = 'pm_image_info'

class PmImageInfoCopy(BaseModel):
    img_create_time = DateTimeField(null=True)
    img_id = AutoField()
    img_name = CharField()
    img_other1 = CharField(null=True)
    img_other2 = CharField(null=True)
    img_remark = CharField(null=True)
    img_status = IntegerField()
    img_type = CharField()
    img_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    img_url = CharField()

    class Meta:
        table_name = 'pm_image_info_copy'

class PmImageStock(BaseModel):
    admin_id = IntegerField(null=True)
    admin_name = CharField(null=True)
    img_create_time = DateTimeField(null=True)
    img_name = CharField(null=True)
    img_remark = CharField(null=True)
    img_status = IntegerField()
    img_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    img_url = CharField()
    order_id = IntegerField()
    stock_id = AutoField()

    class Meta:
        table_name = 'pm_image_stock'

class PmLabelImage(BaseModel):
    label_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    label_flag = IntegerField(null=True)
    label_id = AutoField()
    label_name = CharField(null=True)
    label_status = IntegerField(null=True)
    label_type = CharField(null=True)
    label_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    label_url = CharField(null=True)
    label_url_double = CharField(null=True)
    pharmacy_id = IntegerField(null=True)
    sku_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_label_image'
        indexes = (
            (('sku_id', 'pharmacy_id', 'label_status', 'label_flag'), False),
        )

class PmLabelImage20200306(BaseModel):
    label_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    label_flag = IntegerField(null=True)
    label_id = AutoField()
    label_name = CharField(null=True)
    label_status = IntegerField(null=True)
    label_type = CharField(null=True)
    label_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    label_url = CharField(null=True)
    label_url_double = CharField(null=True)
    pharmacy_id = IntegerField(null=True)
    sku_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_label_image_20200306'

class PmMessageInfo(BaseModel):
    customer_id = IntegerField()
    fixation_phone = CharField(null=True)
    message_content = CharField()
    message_create_time = DateTimeField(null=True)
    message_id = AutoField()
    message_status = IntegerField(null=True)
    message_type = IntegerField()
    message_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    messager_addr = CharField(null=True)
    messager_email = CharField(null=True)
    messager_name = CharField()
    move_phone = CharField(null=True)

    class Meta:
        table_name = 'pm_message_info'

class PmPacketCategory(BaseModel):
    catefory_remark = CharField(null=True)
    category_all_name = CharField(null=True)
    category_code = CharField()
    category_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    category_id = AutoField()
    category_level = IntegerField(null=True)
    category_name = CharField()
    category_seq = IntegerField(null=True)
    category_status = IntegerField()
    category_type = CharField()
    category_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    parent_category_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_packet_category'

class PmPacketDir(BaseModel):
    dir_code = CharField(null=True)
    dir_id = IntegerField()
    link_id = AutoField()
    packet_id = IntegerField()
    packet_order = IntegerField(null=True)

    class Meta:
        table_name = 'pm_packet_dir'

class PmPacketInfo(BaseModel):
    drugstore_id = IntegerField(null=True)
    packet_category = IntegerField()
    packet_content = CharField(null=True)
    packet_coures = CharField(null=True)
    packet_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    packet_fee = IntegerField(null=True)
    packet_huohao = CharField(index=True, null=True)
    packet_id = AutoField()
    packet_img = CharField(null=True)
    packet_name = CharField(index=True)
    packet_price = IntegerField(null=True)
    packet_remark = CharField(null=True)
    packet_status = IntegerField()
    packet_stock = IntegerField(null=True)
    packet_title_formula = CharField(null=True)
    packet_type = CharField(null=True)
    packet_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    pre_prod_name = CharField(null=True)
    sku_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_packet_info'

class PmPacketInfoOld(BaseModel):
    drugstore_id = IntegerField(null=True)
    packet_content = CharField(null=True)
    packet_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    packet_id = AutoField()
    packet_name = CharField(index=True)
    packet_price = IntegerField()
    packet_remark = CharField(null=True)
    packet_status = IntegerField()
    packet_type = CharField(null=True)
    packet_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sku_id = IntegerField(index=True)

    class Meta:
        table_name = 'pm_packet_info_old'

class PmPacketSku(BaseModel):
    link_id = AutoField()
    link_remark = CharField(null=True)
    packet_id = IntegerField()
    packet_sku_id = IntegerField(null=True)
    packet_sku_price = IntegerField()
    prod_name = CharField(null=True)
    sku_amount = IntegerField(constraints=[SQL("DEFAULT 1")])
    sku_fee = IntegerField()
    sku_huohao = CharField(null=True)
    sku_id = IntegerField(index=True)
    sku_seq = IntegerField(null=True)
    total_price = IntegerField()

    class Meta:
        table_name = 'pm_packet_sku'

class PmPacketSkuOld(BaseModel):
    link_id = AutoField()
    link_remark = CharField(null=True)
    packet_id = IntegerField()
    packet_sku_id = IntegerField()
    packet_sku_price = IntegerField()
    sku_id = IntegerField()

    class Meta:
        table_name = 'pm_packet_sku_old'

class PmPharmacyDir(BaseModel):
    dir_id = IntegerField()
    dir_level = IntegerField(null=True)
    dir_type = CharField(null=True)
    link_id = AutoField()
    pharmacy_id = IntegerField()

    class Meta:
        table_name = 'pm_pharmacy_dir'

class PmPharmacyProd(BaseModel):
    drug_id = IntegerField(index=True, null=True)
    p_id = AutoField()
    pharmacy_id = IntegerField(null=True)
    prod_brand = CharField(null=True)
    prod_code = CharField(null=True)
    prod_create_time = DateTimeField(null=True)
    prod_firm = CharField(null=True)
    prod_gen_name = CharField(null=True)
    prod_id = IntegerField(null=True)
    prod_indication = TextField(null=True)
    prod_level = IntegerField(null=True)
    prod_logist = CharField(null=True)
    prod_name = CharField(null=True)
    prod_price = IntegerField(null=True)
    prod_remark = CharField(null=True)
    prod_sn = CharField(null=True)
    prod_spec = CharField(null=True)
    prod_status = IntegerField(null=True)
    prod_type = IntegerField(null=True)
    prod_unit = CharField(null=True)
    prod_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    succ_status = IntegerField(null=True)

    class Meta:
        table_name = 'pm_pharmacy_prod'

class PmProdAttr(BaseModel):
    attr_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    attr_desc = CharField()
    attr_display = CharField(null=True)
    attr_id = AutoField()
    attr_name = CharField()
    attr_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    attr_remark = CharField(null=True)
    attr_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    prod_id = IntegerField()

    class Meta:
        table_name = 'pm_prod_attr'

class PmProdCategory(BaseModel):
    category_code = CharField()
    category_id = IntegerField(index=True)
    link_id = AutoField()
    prod_id = IntegerField(index=True)
    prod_order = IntegerField()

    class Meta:
        table_name = 'pm_prod_category'

class PmProdDisease(BaseModel):
    disease_id = IntegerField(null=True)
    dp_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    dp_id = AutoField()
    dp_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    prod_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_prod_disease'

class PmProdDiseaseCopy(BaseModel):
    disease_id = IntegerField(null=True)
    dp_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    dp_id = AutoField()
    dp_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    prod_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_prod_disease_copy'

class PmProdDiseaseCopy1(BaseModel):
    disease_id = IntegerField(null=True)
    dp_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    dp_id = AutoField()
    dp_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    prod_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_prod_disease_copy1'

class PmProdImg(BaseModel):
    attr_id = IntegerField(null=True)
    attr_value_id = IntegerField(null=True)
    img_id = IntegerField(null=True)
    img_kind = CharField(null=True)
    img_name = CharField(null=True)
    link_id = AutoField()
    prod_id = IntegerField(index=True)

    class Meta:
        table_name = 'pm_prod_img'

class PmProdImgCopy(BaseModel):
    attr_id = IntegerField(null=True)
    attr_value_id = IntegerField(null=True)
    img_id = IntegerField(null=True)
    img_kind = CharField(null=True)
    img_name = CharField(null=True)
    link_id = AutoField()
    prod_id = IntegerField(index=True)

    class Meta:
        table_name = 'pm_prod_img_copy'

class PmProdInfo(BaseModel):
    drug_id = IntegerField(index=True, null=True)
    pre_prod_name = CharField(null=True)
    prod_brand = CharField()
    prod_code = CharField()
    prod_create_time = DateTimeField(null=True)
    prod_firm = CharField(null=True)
    prod_gen_name = CharField(null=True)
    prod_id = AutoField()
    prod_indication = TextField(null=True)
    prod_level = IntegerField()
    prod_logist = CharField(null=True)
    prod_name = CharField()
    prod_order = IntegerField(null=True)
    prod_price = IntegerField()
    prod_remark = CharField(null=True)
    prod_sn = CharField()
    prod_spec = CharField(null=True)
    prod_split_word = CharField(null=True)
    prod_status = IntegerField(index=True, null=True)
    prod_synonyms = CharField(null=True)
    prod_type = IntegerField(null=True)
    prod_unit = CharField(null=True)
    prod_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'pm_prod_info'

class PmProdInfoTemp(BaseModel):
    drug_id = IntegerField(null=True)
    prod_brand = CharField()
    prod_code = CharField()
    prod_create_time = DateTimeField(null=True)
    prod_firm = CharField(null=True)
    prod_gen_name = CharField(null=True)
    prod_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    prod_indication = TextField(null=True)
    prod_level = IntegerField()
    prod_logist = CharField(null=True)
    prod_name = CharField()
    prod_order = IntegerField(null=True)
    prod_price = IntegerField()
    prod_remark = CharField(null=True)
    prod_sn = CharField()
    prod_spec = CharField(null=True)
    prod_status = IntegerField(null=True)
    prod_type = IntegerField(null=True)
    prod_unit = CharField(null=True)
    prod_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")])

    class Meta:
        table_name = 'pm_prod_info_temp'
        primary_key = False

class PmProdSku(BaseModel):
    brand_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    dis_after_price = IntegerField(null=True)
    dis_before_price = IntegerField(null=True)
    discount_price = IntegerField(null=True)
    drugstore_id = IntegerField(index=True, null=True)
    is_danger = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_interrogation = IntegerField(constraints=[SQL("DEFAULT 0000000000")])
    is_prescription = IntegerField(constraints=[SQL("DEFAULT 0000000000")])
    is_set = IntegerField(null=True)
    pharmacy_huohao = CharField(null=True)
    pre_prod_name = CharField(null=True)
    prod_id = IntegerField(index=True)
    prod_name = CharField(null=True)
    sales_info = CharField(null=True)
    set_num = IntegerField(null=True)
    sku_activate = IntegerField(null=True)
    sku_attr = CharField(null=True)
    sku_create_time = DateTimeField(null=True)
    sku_fee = IntegerField()
    sku_hot_order = IntegerField(null=True)
    sku_id = AutoField()
    sku_img = CharField(null=True)
    sku_json = CharField(null=True)
    sku_logistics = CharField(null=True)
    sku_price = IntegerField()
    sku_rank = IntegerField(null=True)
    sku_remark = CharField(null=True)
    sku_sort = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sku_status = IntegerField(index=True)
    sku_sum = IntegerField(null=True)
    sku_sum_flag = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    sku_type = CharField(constraints=[SQL("DEFAULT 'normal'")], null=True)
    sku_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)
    special_buy = IntegerField(constraints=[SQL("DEFAULT 00000000000")])

    class Meta:
        table_name = 'pm_prod_sku'
 

class PmProdSku1712(BaseModel):
    brand_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    drugstore_id = IntegerField(index=True, null=True)
    pharmacy_huohao = CharField(null=True)
    prod_id = IntegerField(index=True)
    prod_name = CharField(null=True)
    sku_attr = CharField(null=True)
    sku_create_time = DateTimeField(null=True)
    sku_fee = IntegerField()
    sku_id = AutoField()
    sku_img = CharField(null=True)
    sku_json = CharField(null=True)
    sku_logistics = CharField(null=True)
    sku_price = IntegerField()
    sku_remark = CharField(null=True)
    sku_status = IntegerField(index=True)
    sku_sum = IntegerField(null=True)
    sku_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)

    class Meta:
        table_name = 'pm_prod_sku_1712'

class PmProdSku190624(BaseModel):
    brand_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    dis_after_price = IntegerField(null=True)
    dis_before_price = IntegerField(null=True)
    discount_price = IntegerField(null=True)
    drugstore_id = IntegerField(index=True, null=True)
    is_set = IntegerField(null=True)
    pharmacy_huohao = CharField(null=True)
    pre_prod_name = CharField(null=True)
    prod_id = IntegerField(index=True)
    prod_name = CharField(null=True)
    sales_info = CharField(null=True)
    set_num = IntegerField(null=True)
    sku_activate = IntegerField(null=True)
    sku_attr = CharField(null=True)
    sku_create_time = DateTimeField(null=True)
    sku_fee = IntegerField()
    sku_hot_order = IntegerField(null=True)
    sku_id = AutoField()
    sku_img = CharField(null=True)
    sku_json = CharField(null=True)
    sku_logistics = CharField(null=True)
    sku_price = IntegerField()
    sku_rank = IntegerField(null=True)
    sku_remark = CharField(null=True)
    sku_sort = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sku_status = IntegerField(index=True)
    sku_sum = IntegerField(null=True)
    sku_sum_flag = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    sku_type = CharField(constraints=[SQL("DEFAULT 'normal'")], null=True)
    sku_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)

    class Meta:
        table_name = 'pm_prod_sku_190624'

class PmProdSku200403(BaseModel):
    brand_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    dis_after_price = IntegerField(null=True)
    dis_before_price = IntegerField(null=True)
    discount_price = IntegerField(null=True)
    drugstore_id = IntegerField(index=True, null=True)
    is_interrogation = IntegerField()
    is_prescription = IntegerField()
    is_set = IntegerField(null=True)
    pharmacy_huohao = CharField(null=True)
    pre_prod_name = CharField(null=True)
    prod_id = IntegerField(index=True)
    prod_name = CharField(null=True)
    sales_info = CharField(null=True)
    set_num = IntegerField(null=True)
    sku_activate = IntegerField(null=True)
    sku_attr = CharField(null=True)
    sku_create_time = DateTimeField(null=True)
    sku_fee = IntegerField()
    sku_hot_order = IntegerField(null=True)
    sku_id = AutoField()
    sku_img = CharField(null=True)
    sku_json = CharField(null=True)
    sku_logistics = CharField(null=True)
    sku_price = IntegerField()
    sku_rank = IntegerField(null=True)
    sku_remark = CharField(null=True)
    sku_sort = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sku_status = IntegerField(index=True)
    sku_sum = IntegerField(null=True)
    sku_sum_flag = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    sku_type = CharField(constraints=[SQL("DEFAULT 'normal'")], null=True)
    sku_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)
    special_buy = IntegerField()

    class Meta:
        table_name = 'pm_prod_sku_200403'

class PmProdSkuCopy(BaseModel):
    brand_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    dis_after_price = IntegerField(null=True)
    dis_before_price = IntegerField(null=True)
    discount_price = IntegerField(null=True)
    drugstore_id = IntegerField(index=True, null=True)
    is_danger = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_interrogation = IntegerField(constraints=[SQL("DEFAULT 0000000000")])
    is_prescription = IntegerField(constraints=[SQL("DEFAULT 0000000000")])
    is_set = IntegerField(null=True)
    pharmacy_huohao = CharField(null=True)
    pre_prod_name = CharField(null=True)
    prod_id = IntegerField(index=True)
    prod_name = CharField(null=True)
    sales_info = CharField(null=True)
    set_num = IntegerField(null=True)
    sku_activate = IntegerField(null=True)
    sku_attr = CharField(null=True)
    sku_create_time = DateTimeField(null=True)
    sku_fee = IntegerField()
    sku_hot_order = IntegerField(null=True)
    sku_id = AutoField()
    sku_img = CharField(null=True)
    sku_json = CharField(null=True)
    sku_logistics = CharField(null=True)
    sku_price = IntegerField()
    sku_rank = IntegerField(null=True)
    sku_remark = CharField(null=True)
    sku_sort = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sku_status = IntegerField(index=True)
    sku_sum = IntegerField(null=True)
    sku_sum_flag = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    sku_type = CharField(constraints=[SQL("DEFAULT 'normal'")], null=True)
    sku_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)
    special_buy = IntegerField(constraints=[SQL("DEFAULT 00000000000")])

    class Meta:
        table_name = 'pm_prod_sku_copy'

class PmProdSkuCopy1(BaseModel):
    brand_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    dis_after_price = IntegerField(null=True)
    dis_before_price = IntegerField(null=True)
    discount_price = IntegerField(null=True)
    drugstore_id = IntegerField(index=True, null=True)
    is_danger = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_interrogation = IntegerField(constraints=[SQL("DEFAULT 0000000000")])
    is_prescription = IntegerField(constraints=[SQL("DEFAULT 0000000000")])
    is_set = IntegerField(null=True)
    pharmacy_huohao = CharField(null=True)
    pre_prod_name = CharField(null=True)
    prod_id = IntegerField(index=True)
    prod_name = CharField(null=True)
    sales_info = CharField(null=True)
    set_num = IntegerField(null=True)
    sku_activate = IntegerField(null=True)
    sku_attr = CharField(null=True)
    sku_create_time = DateTimeField(null=True)
    sku_fee = IntegerField()
    sku_hot_order = IntegerField(null=True)
    sku_id = AutoField()
    sku_img = CharField(null=True)
    sku_json = CharField(null=True)
    sku_logistics = CharField(null=True)
    sku_price = IntegerField()
    sku_rank = IntegerField(null=True)
    sku_remark = CharField(null=True)
    sku_sort = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sku_status = IntegerField(index=True)
    sku_sum = IntegerField(null=True)
    sku_sum_flag = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    sku_type = CharField(constraints=[SQL("DEFAULT 'normal'")], null=True)
    sku_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)
    special_buy = IntegerField(constraints=[SQL("DEFAULT 00000000000")])

    class Meta:
        table_name = 'pm_prod_sku_copy1'

class PmProdSkuImage(BaseModel):
    brand_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    dis_after_price = IntegerField(null=True)
    dis_before_price = IntegerField(null=True)
    discount_price = IntegerField(null=True)
    drugstore_id = IntegerField(index=True, null=True)
    is_set = IntegerField(null=True)
    pharmacy_huohao = CharField(null=True)
    prod_id = IntegerField(index=True)
    prod_name = CharField(null=True)
    sales_info = CharField(null=True)
    set_num = IntegerField(null=True)
    sku_activate = IntegerField(null=True)
    sku_attr = CharField(null=True)
    sku_create_time = DateTimeField(null=True)
    sku_fee = IntegerField()
    sku_hot_order = IntegerField(null=True)
    sku_id = AutoField()
    sku_img = CharField(null=True)
    sku_json = CharField(null=True)
    sku_logistics = CharField(null=True)
    sku_price = IntegerField()
    sku_rank = IntegerField(null=True)
    sku_remark = CharField(null=True)
    sku_sort = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sku_status = IntegerField(index=True)
    sku_sum = IntegerField(null=True)
    sku_sum_flag = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    sku_type = CharField(constraints=[SQL("DEFAULT 'normal'")], null=True)
    sku_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)

    class Meta:
        table_name = 'pm_prod_sku_image'

class PmProdSkuKzf(BaseModel):
    brand_id = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    drugstore_id = IntegerField(index=True, null=True)
    pharmacy_huohao = CharField(null=True)
    prod_id = IntegerField(index=True)
    prod_name = CharField(null=True)
    sku_attr = CharField(null=True)
    sku_create_time = DateTimeField(null=True)
    sku_fee = IntegerField()
    sku_id = AutoField()
    sku_json = CharField(null=True)
    sku_logistics = CharField(null=True)
    sku_price = IntegerField()
    sku_remark = CharField(null=True)
    sku_status = IntegerField(index=True)
    sku_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)

    class Meta:
        table_name = 'pm_prod_sku_kzf'

class PmProdSource(BaseModel):
    source_create_time = DateTimeField(null=True)
    source_id = AutoField()
    source_name = CharField(null=True)
    source_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'pm_prod_source'

class PmProdStats(BaseModel):
    prod_id = IntegerField(index=True)
    prod_other1 = IntegerField(null=True)
    prod_other2 = IntegerField(null=True)
    prod_sales = IntegerField(null=True)
    prod_standard = IntegerField(null=True)
    stats_create_time = DateTimeField(null=True)
    stats_id = AutoField()
    stats_remark = CharField(null=True)
    stats_status = IntegerField(index=True)
    stats_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'pm_prod_stats'

class PmRecomProd(BaseModel):
    due_sku_id = IntegerField()
    recom_prod_id = AutoField()
    rp_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    rp_end_time = DateTimeField(null=True)
    rp_level = IntegerField()
    rp_remark = CharField(null=True)
    rp_start_time = DateTimeField(null=True)
    rp_type = CharField()
    rp_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sku_id = IntegerField()

    class Meta:
        table_name = 'pm_recom_prod'

class PmRecomSys(BaseModel):
    pharmacy_id = IntegerField(null=True)
    recom_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    recom_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    recom_level = IntegerField()
    recom_remark = CharField(null=True)
    recom_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    recom_status = IntegerField()
    recom_sys_id = AutoField()
    recom_type = CharField()
    recom_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sku_id = IntegerField()

    class Meta:
        table_name = 'pm_recom_sys'

class PmRecomUser(BaseModel):
    pharmacy_id = IntegerField(null=True)
    recom_prod_id = AutoField()
    rp_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    rp_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    rp_level = IntegerField()
    rp_remark = CharField(null=True)
    rp_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    rp_type = CharField()
    rp_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sku_id = IntegerField()
    user_id = IntegerField()

    class Meta:
        table_name = 'pm_recom_user'

class PmSkuAttr(BaseModel):
    attr_id = IntegerField()
    attr_value_id = IntegerField()
    sku_id = IntegerField()
    val_id = AutoField()

    class Meta:
        table_name = 'pm_sku_attr'

class PmSkuDir(BaseModel):
    dir_code = CharField(index=True)
    dir_id = IntegerField(index=True)
    link_id = AutoField()
    sku_id = IntegerField(index=True)
    sku_order = IntegerField(constraints=[SQL("DEFAULT 1000")], null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'pm_sku_dir'
        indexes = (
            (('sku_id', 'dir_id'), False),
        )

class PmSkuDir180706(BaseModel):
    dir_code = CharField(index=True)
    dir_id = IntegerField(index=True)
    link_id = AutoField()
    sku_id = IntegerField(index=True)
    sku_order = IntegerField(constraints=[SQL("DEFAULT 1000")], null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'pm_sku_dir_180706'

class PmSkuDir20161026(BaseModel):
    dir_code = CharField()
    dir_id = IntegerField()
    link_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    sku_id = IntegerField()
    sku_order = IntegerField(null=True)

    class Meta:
        table_name = 'pm_sku_dir_20161026'
        primary_key = False

class PmSkuDir20161126(BaseModel):
    dir_code = CharField()
    dir_id = IntegerField()
    link_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    sku_id = IntegerField()
    sku_order = IntegerField(constraints=[SQL("DEFAULT 1000")], null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'pm_sku_dir_20161126'
        primary_key = False

class PmSkuDir20200229(BaseModel):
    dir_code = CharField(index=True)
    dir_id = IntegerField(index=True)
    link_id = AutoField()
    sku_id = IntegerField(index=True)
    sku_order = IntegerField(constraints=[SQL("DEFAULT 1000")], null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'pm_sku_dir_20200229'

class PmSkuDirBak180606(BaseModel):
    dir_code = CharField(index=True)
    dir_id = IntegerField(index=True)
    link_id = AutoField()
    sku_id = IntegerField(index=True)
    sku_order = IntegerField(constraints=[SQL("DEFAULT 1000")], null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'pm_sku_dir_bak_180606'

class PmSkuDirBak180607(BaseModel):
    dir_code = CharField(index=True)
    dir_id = IntegerField(index=True)
    link_id = AutoField()
    sku_id = IntegerField(index=True)
    sku_order = IntegerField(constraints=[SQL("DEFAULT 1000")], null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'pm_sku_dir_bak_180607'

class PmSkuDirFlzyback180731(BaseModel):
    dir_code = CharField(index=True)
    dir_id = IntegerField(index=True)
    link_id = AutoField()
    sku_id = IntegerField(index=True)
    sku_order = IntegerField(constraints=[SQL("DEFAULT 1000")], null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'pm_sku_dir_flzyback_180731'

class PmSkuDirKzf(BaseModel):
    dir_code = CharField(index=True)
    dir_id = IntegerField(index=True)
    link_id = AutoField()
    sku_id = IntegerField(index=True)
    sku_order = IntegerField(constraints=[SQL("DEFAULT 1000")], null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'pm_sku_dir_kzf'

class PmSkuHis(BaseModel):
    brand_id = IntegerField(null=True)
    drugstore_id = IntegerField(null=True)
    his_id = AutoField()
    operator_type = CharField(null=True)
    pharmacy_huohao = CharField(null=True)
    prod_id = IntegerField(null=True)
    prod_name = CharField(null=True)
    sku_create_time = DateTimeField(null=True)
    sku_fee = IntegerField(null=True)
    sku_id = IntegerField(null=True)
    sku_logistics = CharField(null=True)
    sku_price = IntegerField(null=True)
    sku_remark = CharField(null=True)
    sku_status = IntegerField(null=True)
    sku_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'pm_sku_his'

class PmSkuOnoff(BaseModel):
    column_10 = CharField(column_name='Column_10', null=True)
    action_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    action_id = AutoField()
    action_other1 = CharField(null=True)
    action_other2 = CharField(null=True)
    action_remark = CharField(null=True)
    action_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    action_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sku_action = CharField()
    sku_id = IntegerField()

    class Meta:
        table_name = 'pm_sku_onoff'

class PmSkuPricehis(BaseModel):
    from_price = IntegerField()
    price_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    price_id = AutoField()
    price_reason = CharField(null=True)
    price_remark = CharField(null=True)
    price_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sku_id = IntegerField()
    to_price = IntegerField()
    transf_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])

    class Meta:
        table_name = 'pm_sku_pricehis'

class PmSkuSale(BaseModel):
    sale_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    sale_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sale_fee = IntegerField(null=True)
    sale_id = AutoField()
    sale_price = IntegerField(null=True)
    sale_remark = CharField(null=True)
    sale_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sale_status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sale_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sku_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'pm_sku_sale'
        indexes = (
            (('sale_end_time', 'sale_start_time'), False),
        )

class PmSkuSale1208(BaseModel):
    sale_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    sale_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sale_fee = IntegerField(null=True)
    sale_id = AutoField()
    sale_price = IntegerField(null=True)
    sale_remark = CharField(null=True)
    sale_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sale_status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sale_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sku_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'pm_sku_sale_1208'

class PmSkuSale191017(BaseModel):
    sale_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    sale_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sale_fee = IntegerField(null=True)
    sale_id = AutoField()
    sale_price = IntegerField(null=True)
    sale_remark = CharField(null=True)
    sale_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sale_status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sale_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sku_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'pm_sku_sale_191017'

class PmSkuSale191118(BaseModel):
    sale_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    sale_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sale_fee = IntegerField(null=True)
    sale_id = AutoField()
    sale_price = IntegerField(null=True)
    sale_remark = CharField(null=True)
    sale_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sale_status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sale_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sku_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'pm_sku_sale_191118'

class PmSkuSaleHis(BaseModel):
    sale_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    sale_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sale_fee = CharField(null=True)
    sale_id = IntegerField(index=True)
    sale_price = CharField(null=True)
    sale_remark = CharField(null=True)
    sale_start_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sale_status = IntegerField(null=True)
    sale_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sku_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_sku_sale_his'
        primary_key = False

class PmSkuStock(BaseModel):
    sku_id = IntegerField()
    stock_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    stock_id = AutoField()
    stock_remark = CharField(null=True)
    stock_status = IntegerField()
    stock_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    stock_val = IntegerField()

    class Meta:
        table_name = 'pm_sku_stock'

class PmStatsInfo(BaseModel):
    prod_id = IntegerField(index=True)
    prod_sum = IntegerField()
    stats_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    stats_id = AutoField()
    stats_other1 = CharField(null=True)
    stats_other2 = CharField(null=True)
    stats_remark = CharField(null=True)
    stats_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    stats_type = CharField()
    stats_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'pm_stats_info'

class PmStockNote(BaseModel):
    emp_id = IntegerField(null=True)
    note_append = CharField(null=True)
    note_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    note_hand = CharField()
    note_id = AutoField()
    note_reason = CharField(null=True)
    note_remark = CharField(null=True)
    note_status = IntegerField(null=True)
    note_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    note_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    prod_sum = IntegerField()
    stock_id = IntegerField()

    class Meta:
        table_name = 'pm_stock_note'

class PmTattrValue(BaseModel):
    prod_id = IntegerField()
    tattr_id = IntegerField()
    tattr_value = CharField()
    tattr_value_id = AutoField()
    tattr_value_num = IntegerField()
    tattr_value_type = CharField()
    tav_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    tav_remark = CharField(null=True)
    tav_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'pm_tattr_value'

class PmTypeAttr(BaseModel):
    tattr_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    tattr_desc = CharField()
    tattr_display = CharField(null=True)
    tattr_name = CharField()
    tattr_num = IntegerField()
    tattr_remark = CharField(null=True)
    tattr_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    type_attr_id = AutoField()
    type_id = IntegerField()

    class Meta:
        table_name = 'pm_type_attr'

class PmTypeInfo(BaseModel):
    parent_type_id = IntegerField(null=True)
    type_code = CharField()
    type_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    type_desc = CharField()
    type_id = AutoField()
    type_level = IntegerField()
    type_name = CharField()
    type_remark = CharField(null=True)
    type_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'pm_type_info'

class PmUserIntent(BaseModel):
    addr_info = CharField(null=True)
    intent_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    intent_id = AutoField()
    intent_json = CharField(null=True)
    intent_remark = CharField(null=True)
    intent_time = CharField(null=True)
    intent_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    pharmacy_id = IntegerField()
    phone_num = CharField()
    sku_id = IntegerField()
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_user_intent'

class PmVoucherCode(BaseModel):
    cou_tem_id = IntegerField(null=True)
    cou_tem_num = IntegerField(null=True)
    voucher_code_id = AutoField()
    voucher_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_voucher_code'

class PmVoucherImage(BaseModel):
    image_create_time = DateTimeField(null=True)
    image_name = CharField(null=True)
    image_state = IntegerField(null=True)
    image_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    image_url = CharField(null=True)
    link_id = AutoField()
    voucher_id = IntegerField(null=True)

    class Meta:
        table_name = 'pm_voucher_image'

class PmVoucherInfo(BaseModel):
    code_act_id = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    voucher_create_time = DateTimeField(null=True)
    voucher_describe = CharField(null=True)
    voucher_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    voucher_fee = IntegerField(null=True)
    voucher_id = AutoField()
    voucher_imge = CharField(null=True)
    voucher_json = CharField(null=True)
    voucher_name = CharField(null=True)
    voucher_order = IntegerField(null=True)
    voucher_price = IntegerField(null=True)
    voucher_remark = CharField(null=True)
    voucher_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    voucher_state = IntegerField(null=True)
    voucher_tittle = CharField(null=True)
    voucher_type = IntegerField(null=True)
    voucher_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'pm_voucher_info'

class Prodid匹配货号价格(BaseModel):
    商品名 = CharField(null=True)
    康佰馨市场价 = CharField(null=True)
    康佰馨货号 = CharField(null=True)
    正济堂市场价 = CharField(null=True)
    正济堂货号 = CharField(null=True)
    药快到id = CharField(column_name='药快到ID', null=True)
    规格 = CharField(null=True)
    通用名称 = CharField(null=True)

    class Meta:
        table_name = 'prodid匹配货号价格'
        primary_key = False

class Sheet1(BaseModel):
    一级分类 = CharField(null=True)
    三级分类 = CharField(null=True)
    二级分类 = CharField(null=True)
    品牌名 = CharField(null=True)
    四级分类 = CharField(null=True)
    序号 = CharField(primary_key=True)
    康佰馨货号 = CharField(null=True)
    正济堂货号 = CharField(null=True)
    生产企业 = CharField(null=True)
    药快到id = CharField(column_name='药快到ID', null=True)
    规格 = CharField(null=True)
    通用名称 = CharField(null=True)

    class Meta:
        table_name = 'sheet1'


class SmAdminInfo(BaseModel):
    admin_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    admin_email = CharField(null=True)
    admin_id = AutoField()
    admin_image = CharField(null=True)
    admin_label = CharField(null=True)
    admin_name = CharField()
    admin_new_track = CharField(null=True)
    admin_online = CharField(null=True)
    admin_pass = CharField()
    admin_phone = CharField()
    admin_position = CharField(null=True)
    admin_remark = CharField(null=True)
    admin_status = IntegerField()
    admin_type = CharField(index=True, null=True)
    admin_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    admin_work = CharField(null=True)
    app_login_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    app_token = CharField(null=True)
    employee_id = IntegerField(null=True)
    operator = IntegerField(null=True)
    pharmacy_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'sm_admin_info'

class SmAdminRole(BaseModel):
    admin_id = IntegerField()
    rm_id = AutoField()
    role_id = IntegerField()

    class Meta:
        table_name = 'sm_admin_role'

class SmAdminTrack(BaseModel):
    admin_id = IntegerField()
    track_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    track_id = AutoField()
    track_lat = CharField(null=True)
    track_local = CharField(null=True)
    track_lon = CharField(null=True)
    track_pos = CharField(null=True)
    track_remark = CharField(null=True)
    track_status = IntegerField()
    track_type = CharField(null=True)
    track_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'sm_admin_track'

class SmAppLog(BaseModel):
    log_create_time = DateTimeField(null=True)
    log_id = AutoField()
    log_remark = CharField(null=True)
    log_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    req_body = CharField(null=True)
    req_param = CharField(null=True)
    req_time = DateTimeField(null=True)
    req_url = CharField()
    resp_body = TextField(null=True)
    resp_excep = TextField(null=True)
    resp_param = CharField(null=True)
    resp_result = CharField(null=True)
    resp_time = DateTimeField(null=True)
    total_time = IntegerField(null=True)

    class Meta:
        table_name = 'sm_app_log'

class SmAppleToken(BaseModel):
    access_token = CharField(null=True)
    create_time = DateTimeField()
    disabled = IntegerField(null=True)
    expires_in = IntegerField(null=True)
    id = BigAutoField()
    id_token = CharField(null=True)
    refresh_token = CharField(null=True)
    token_type = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'sm_apple_token'

class SmAreaCity(BaseModel):
    area_id = AutoField()
    area_prov = CharField(null=True)
    area_prov_value = CharField(null=True)
    area_remark = CharField(null=True)
    area_status = IntegerField(null=True)
    city_code = CharField(null=True)
    city_name = CharField(null=True)
    city_name_value = CharField(null=True)
    county_name = CharField(null=True)
    county_name_value = CharField(null=True)

    class Meta:
        table_name = 'sm_area_city'

class SmBrandImg(BaseModel):
    brand_id = IntegerField()
    img_id = IntegerField()
    img_type = CharField(null=True)
    link_id = AutoField()

    class Meta:
        table_name = 'sm_brand_img'

class SmBrandInfo(BaseModel):
    brand_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    brand_id = AutoField()
    brand_img = CharField(null=True)
    brand_number = CharField(null=True)
    brand_remark = CharField(null=True)
    brand_sn = CharField(null=True)
    brand_type = IntegerField()
    brand_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    brandname = CharField()
    operator = IntegerField(null=True)

    class Meta:
        table_name = 'sm_brand_info'

class SmConfig(BaseModel):
    config_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    config_id = AutoField()
    config_key = CharField()
    config_remark = CharField(null=True)
    config_status = IntegerField(null=True)
    config_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    config_value = TextField()
    value_type = CharField()

    class Meta:
        table_name = 'sm_config'

class SmConfigBak180608(BaseModel):
    config_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    config_id = AutoField()
    config_key = CharField()
    config_remark = CharField(null=True)
    config_status = IntegerField(null=True)
    config_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    config_value = CharField()
    value_type = CharField()

    class Meta:
        table_name = 'sm_config_bak_180608'

class SmDrugHeaderView(BaseModel):
    aspect_ratio = CharField()
    create_time = DateTimeField()
    disabled = IntegerField()
    image_drug_id = IntegerField()
    image_go_name = CharField()
    image_go_url = CharField()
    image_type = IntegerField()
    image_url = CharField()
    pharmacy_id = IntegerField()

    class Meta:
        table_name = 'sm_drug_header_view'

class SmDrugSalesInfo(BaseModel):
    create_time = DateTimeField()
    disabled = IntegerField()
    drug_id = IntegerField()
    pharmacy_id = IntegerField()
    sales_goto_title = CharField()
    sales_goto_type = IntegerField()
    sales_goto_url = CharField()
    sales_info = CharField()
    sales_info_new = CharField()

    class Meta:
        table_name = 'sm_drug_sales_info'

class SmDrugstoreAddr(BaseModel):
    deliver_time = IntegerField(null=True)
    drugstore_address = CharField(null=True)
    drugstore_area = CharField(null=True)
    drugstore_busi = CharField(null=True)
    drugstore_code = CharField(null=True)
    drugstore_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    drugstore_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    drugstore_level = IntegerField(null=True)
    drugstore_model = IntegerField(null=True)
    drugstore_name = CharField()
    drugstore_phone = CharField()
    drugstore_position = CharField(null=True)
    drugstore_range = CharField(null=True)
    drugstore_rect = CharField(null=True)
    drugstore_remark = CharField(null=True)
    drugstore_sid = CharField(null=True)
    drugstore_smqid = CharField(null=True)
    drugstore_time = CharField(null=True)
    drugstore_type = IntegerField()
    drugstore_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    drugstore_url = CharField(null=True)
    operator = IntegerField(null=True)
    parent_id = IntegerField(null=True)

    class Meta:
        table_name = 'sm_drugstore_addr'
        primary_key = False

class SmDrugstoreAudit(BaseModel):
    audit_create_time = DateTimeField(null=True)
    audit_message = CharField(null=True)
    audit_remark = CharField(null=True)
    audit_status = IntegerField(null=True)
    audit_update_time = DateTimeField(null=True)
    drugstore_id = IntegerField(null=True)

    class Meta:
        table_name = 'sm_drugstore_audit'

class SmDrugstoreBrand(BaseModel):
    brand_id = IntegerField()
    drugstore_id = IntegerField()
    link_id = AutoField()

    class Meta:
        table_name = 'sm_drugstore_brand'

class SmDrugstoreImg(BaseModel):
    drugstore_id = IntegerField(index=True)
    img_id = IntegerField()
    img_type = CharField(null=True)
    img_url = CharField(null=True)
    link_id = AutoField()

    class Meta:
        table_name = 'sm_drugstore_img'

class SmDrugstoreInfo(BaseModel):
    addonitem_goname = CharField(null=True)
    addonitem_subtitle = CharField(null=True)
    addonitem_title = CharField(null=True)
    addonitem_webname = CharField(null=True)
    addonitem_weburl = CharField(null=True)
    authority_tip_content = CharField(null=True)
    authority_tip_title = CharField(null=True)
    deliver_time = IntegerField(null=True)
    drugstore_address = CharField(null=True)
    drugstore_area = CharField(null=True)
    drugstore_busi = CharField(null=True)
    drugstore_certificate = CharField(null=True)
    drugstore_code = CharField(index=True, null=True)
    drugstore_contact = CharField(null=True)
    drugstore_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    drugstore_deliver_desc = CharField(null=True)
    drugstore_deliver_way = CharField(null=True)
    drugstore_home_ratio = CharField(null=True)
    drugstore_home_url = CharField(null=True)
    drugstore_id = AutoField()
    drugstore_level = IntegerField(null=True)
    drugstore_model = IntegerField(null=True)
    drugstore_model_new = IntegerField(null=True)
    drugstore_name = CharField()
    drugstore_notice = CharField(null=True)
    drugstore_phone = CharField()
    drugstore_position = CharField(null=True)
    drugstore_prin_phone = CharField(null=True)
    drugstore_principal = CharField(null=True)
    drugstore_purchase = CharField(null=True)
    drugstore_range = CharField(null=True)
    drugstore_rect = CharField(null=True)
    drugstore_remark = CharField(null=True)
    drugstore_show = CharField(null=True)
    drugstore_sid = CharField(null=True)
    drugstore_smqid = CharField(null=True)
    drugstore_time = CharField(null=True)
    drugstore_type = IntegerField()
    drugstore_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    drugstore_url = CharField(null=True)
    drugstore_wel_word = CharField(null=True)
    drugstore_wel_word_open = IntegerField(null=True)
    drugstore_wel_word_title = CharField(null=True)
    drugstore_wel_word_url = CharField(null=True)
    enable_3rdlogist = IntegerField(null=True)
    enable_sflogist = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    fn_time_range = CharField(null=True)
    lack_state_pic = CharField(null=True)
    lack_title = CharField(null=True)
    lack_webtitle = CharField(null=True)
    lack_weburl = CharField(null=True)
    operator = IntegerField(null=True)
    parent_id = IntegerField(null=True)
    share_alert_image = CharField(null=True)
    share_btn_image = CharField(null=True)
    share_btn_image_ratio = CharField(null=True)
    submit_order_remind = CharField(null=True)
    submit_order_remind_title = CharField(null=True)
    support_collect = CharField(constraints=[SQL("DEFAULT '0'")], null=True)

    class Meta:
        table_name = 'sm_drugstore_info'

class SmDrugstoreInfo18226(BaseModel):
    deliver_time = IntegerField(null=True)
    drugstore_address = CharField(null=True)
    drugstore_area = CharField(null=True)
    drugstore_busi = CharField(null=True)
    drugstore_certificate = CharField(null=True)
    drugstore_code = CharField(index=True, null=True)
    drugstore_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    drugstore_id = AutoField()
    drugstore_level = IntegerField(null=True)
    drugstore_model = IntegerField(null=True)
    drugstore_name = CharField()
    drugstore_notice = CharField(null=True)
    drugstore_phone = CharField()
    drugstore_position = CharField(null=True)
    drugstore_prin_phone = CharField(null=True)
    drugstore_principal = CharField(null=True)
    drugstore_purchase = CharField(null=True)
    drugstore_range = CharField(null=True)
    drugstore_rect = CharField(null=True)
    drugstore_remark = CharField(null=True)
    drugstore_show = CharField(null=True)
    drugstore_sid = CharField(null=True)
    drugstore_smqid = CharField(null=True)
    drugstore_time = CharField(null=True)
    drugstore_type = IntegerField()
    drugstore_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    drugstore_url = CharField(null=True)
    drugstore_wel_word = CharField(null=True)
    drugstore_wel_word_open = IntegerField(null=True)
    drugstore_wel_word_title = CharField(null=True)
    drugstore_wel_word_url = CharField(null=True)
    operator = IntegerField(null=True)
    parent_id = IntegerField(null=True)

    class Meta:
        table_name = 'sm_drugstore_info_18.2.26'

class SmDrugstoreQual(BaseModel):
    drugstore_id = IntegerField()
    qual_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    qual_deal = CharField(null=True)
    qual_end_time = DateTimeField(null=True)
    qual_no = CharField(null=True)
    qual_scope = CharField(null=True)
    qual_type = IntegerField(null=True)
    qual_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    qual_url = CharField(null=True)

    class Meta:
        table_name = 'sm_drugstore_qual'

class SmEmployeeInfo(BaseModel):
    employee_age = IntegerField(null=True)
    employee_create_time = DateTimeField(null=True)
    employee_email = CharField(null=True)
    employee_gender = CharField(null=True)
    employee_id = AutoField()
    employee_name = CharField()
    employee_part = IntegerField(null=True)
    employee_phone = CharField(null=True)
    employee_remark = CharField(null=True)
    employee_status = IntegerField(null=True)
    employee_type = CharField(null=True)
    employee_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    employeef_tel = CharField(null=True)
    operator = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)

    class Meta:
        table_name = 'sm_employee_info'

class SmFaqReply(BaseModel):
    admin_id = IntegerField()
    faq_id = IntegerField()
    reply_content = CharField(null=True)
    reply_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    reply_id = AutoField()
    reply_remark = CharField(null=True)
    reply_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    reply_title = CharField()
    reply_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'sm_faq_reply'

class SmFeedbackInfo(BaseModel):
    back_content = CharField()
    back_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    back_id = AutoField()
    back_remark = CharField(null=True)
    back_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    back_type = CharField()
    back_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    drugstore_id = IntegerField(null=True)
    user_id = IntegerField()

    class Meta:
        table_name = 'sm_feedback_info'

class SmGoWebImage(BaseModel):
    activity_type = IntegerField()
    aspect_ratio = CharField()
    create_time = DateTimeField()
    disabled = IntegerField()
    image_url = CharField()
    page_name = CharField()
    page_url = CharField()

    class Meta:
        table_name = 'sm_go_web_image'

class SmGoWebPage(BaseModel):
    activity_type = IntegerField()
    alert_click_type = IntegerField(null=True)
    alert_content = CharField()
    alert_title = CharField()
    alert_type = IntegerField()
    cancle_type = IntegerField()
    create_time = DateTimeField()
    disabled = IntegerField()
    image_url = CharField()
    share_describe = CharField(null=True)
    share_image = CharField(null=True)
    web_name = CharField()
    web_url = CharField()

    class Meta:
        table_name = 'sm_go_web_page'

class SmGoWebShare(BaseModel):
    alert_click_type = CharField(null=True)
    go_web_name = CharField(null=True)
    go_web_share_describe = CharField(null=True)
    go_web_share_image = CharField(null=True)
    go_web_url = CharField(null=True)
    image_url = CharField(null=True)
    page_id = IntegerField(null=True)
    paharmacy_ids = CharField(null=True)
    share_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    share_flag = IntegerField(null=True)
    share_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'sm_go_web_share'

class SmImageLink(BaseModel):
    drugstore_id = IntegerField()
    image_url = CharField()
    link_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    link_end_time = DateTimeField(null=True)
    link_id = AutoField()
    link_name = CharField(null=True)
    link_param = IntegerField(constraints=[SQL("DEFAULT 1")])
    link_remark = CharField(null=True)
    link_start_time = DateTimeField(null=True)
    link_status = IntegerField(null=True)
    link_type = CharField()
    link_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    link_url = CharField(null=True)
    link_version = IntegerField()
    link_view = CharField(null=True)
    seq_num = IntegerField(null=True)

    class Meta:
        table_name = 'sm_image_link'

class SmImageLink1013(BaseModel):
    drugstore_id = IntegerField()
    image_url = CharField()
    link_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    link_end_time = DateTimeField(null=True)
    link_id = AutoField()
    link_name = CharField(null=True)
    link_param = IntegerField(constraints=[SQL("DEFAULT 1")])
    link_remark = CharField(null=True)
    link_start_time = DateTimeField(null=True)
    link_status = IntegerField(null=True)
    link_type = CharField()
    link_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    link_url = CharField(null=True)
    link_view = CharField(null=True)
    seq_num = IntegerField(null=True)

    class Meta:
        table_name = 'sm_image_link_1013'

class SmImageLink191021(BaseModel):
    drugstore_id = IntegerField()
    image_url = CharField()
    link_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    link_end_time = DateTimeField(null=True)
    link_id = AutoField()
    link_name = CharField(null=True)
    link_param = IntegerField(constraints=[SQL("DEFAULT 1")])
    link_remark = CharField(null=True)
    link_start_time = DateTimeField(null=True)
    link_status = IntegerField(null=True)
    link_type = CharField()
    link_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    link_url = CharField(null=True)
    link_version = IntegerField()
    link_view = CharField(null=True)
    seq_num = IntegerField(null=True)

    class Meta:
        table_name = 'sm_image_link_191021'

class SmImageLinkError(BaseModel):
    drugstore_id = IntegerField()
    image_url = CharField()
    link_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    link_end_time = DateTimeField(null=True)
    link_id = AutoField()
    link_name = CharField(null=True)
    link_param = IntegerField(constraints=[SQL("DEFAULT 1")])
    link_remark = CharField(null=True)
    link_start_time = DateTimeField(null=True)
    link_status = IntegerField(null=True)
    link_type = CharField()
    link_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    link_url = CharField(null=True)
    link_version = IntegerField()
    link_view = CharField(null=True)
    seq_num = IntegerField(null=True)

    class Meta:
        table_name = 'sm_image_link_error'

class SmImageLinkHis(BaseModel):
    drugstore_id = IntegerField()
    image_url = CharField()
    link_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    link_end_time = DateTimeField(null=True)
    link_id = AutoField()
    link_name = CharField(null=True)
    link_param = IntegerField(null=True)
    link_remark = CharField(null=True)
    link_start_time = DateTimeField(null=True)
    link_status = IntegerField(null=True)
    link_type = CharField()
    link_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    link_url = CharField(null=True)
    link_view = CharField(null=True)
    seq_num = IntegerField(null=True)

    class Meta:
        table_name = 'sm_image_link_his'

class SmImageLinkWindow(BaseModel):
    drugstore_id = IntegerField(index=True)
    image_url = CharField()
    seq_num = IntegerField(null=True)
    window_create_time = DateTimeField(null=True)
    window_end_time = DateTimeField(null=True)
    window_go_type = IntegerField(null=True)
    window_id = AutoField()
    window_name = CharField(null=True)
    window_param = IntegerField(null=True)
    window_remark = CharField(null=True)
    window_start_time = DateTimeField(null=True)
    window_status = IntegerField(null=True)
    window_type = CharField()
    window_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    window_url = CharField(null=True)
    window_view = CharField(null=True)

    class Meta:
        table_name = 'sm_image_link_window'

class SmImageLogoWindow(BaseModel):
    drugstore_id = IntegerField(index=True)
    seq_num = IntegerField(null=True)
    window_create_time = DateTimeField(null=True)
    window_end_time = DateTimeField(null=True)
    window_id = AutoField()
    window_image_and = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    window_image_ip4 = CharField(null=True)
    window_image_ipp = CharField(null=True)
    window_image_ipx = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    window_remark = CharField(null=True)
    window_start_time = DateTimeField(null=True)
    window_status = IntegerField(null=True)
    window_title = CharField(null=True)
    window_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    window_url = CharField(null=True)

    class Meta:
        table_name = 'sm_image_logo_window'

class SmImageMarket(BaseModel):
    drugstore_id = IntegerField(index=True)
    image_url = CharField()
    market_create_time = DateTimeField(null=True)
    market_date_title = CharField(null=True)
    market_group = IntegerField(null=True)
    market_id = AutoField()
    market_name = CharField(null=True)
    market_num = IntegerField(null=True)
    market_remark = CharField(null=True)
    market_status = IntegerField(null=True)
    market_title = CharField(null=True)
    market_type = CharField(null=True)
    market_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    market_url = CharField()

    class Meta:
        table_name = 'sm_image_market'

class SmIp(BaseModel):
    count = IntegerField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    flag = IntegerField(null=True)
    ip = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'sm_ip'

class SmLog(BaseModel):
    log_class = CharField(null=True)
    log_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    log_details = TextField(null=True)
    log_id = AutoField()
    log_level = CharField(null=True)
    log_method = CharField(null=True)
    log_msg = CharField(null=True)
    log_remark = CharField(null=True)

    class Meta:
        table_name = 'sm_log'

class SmModuleInfo(BaseModel):
    module_create_time = DateTimeField(null=True)
    module_id = AutoField()
    module_index = IntegerField(null=True)
    module_name = CharField()
    module_pindex = IntegerField(null=True)
    module_pname = CharField(null=True)
    module_ptype = CharField(null=True)
    module_remark = CharField(null=True)
    module_status = IntegerField()
    module_type = CharField()
    module_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    module_uri = CharField()
    module_uri_type = CharField(null=True)

    class Meta:
        table_name = 'sm_module_info'

class SmModuleOperat(BaseModel):
    module_code = CharField(null=True)
    module_create_time = DateTimeField(null=True)
    module_id = AutoField()
    module_index = IntegerField(null=True)
    module_level = IntegerField()
    module_name = CharField()
    module_pid = IntegerField(null=True)
    module_pname = CharField(null=True)
    module_ptype = CharField(null=True)
    module_remark = CharField(null=True)
    module_status = IntegerField()
    module_type = CharField(null=True)
    module_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    module_uri = CharField()
    module_uri_type = CharField(null=True)

    class Meta:
        table_name = 'sm_module_operat'

class SmModuleOperatBak(BaseModel):
    module_code = CharField(null=True)
    module_create_time = DateTimeField(null=True)
    module_id = AutoField()
    module_index = IntegerField(null=True)
    module_level = IntegerField()
    module_name = CharField()
    module_pid = IntegerField(null=True)
    module_pname = CharField(null=True)
    module_ptype = CharField(null=True)
    module_remark = CharField(null=True)
    module_status = IntegerField()
    module_type = CharField(null=True)
    module_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    module_uri = CharField()
    module_uri_type = CharField(null=True)

    class Meta:
        table_name = 'sm_module_operat_bak'

class SmModuleOperatCopy(BaseModel):
    module_code = CharField(null=True)
    module_create_time = DateTimeField(null=True)
    module_id = AutoField()
    module_index = IntegerField(null=True)
    module_level = IntegerField()
    module_name = CharField()
    module_pid = IntegerField(null=True)
    module_pname = CharField(null=True)
    module_ptype = CharField(null=True)
    module_remark = CharField(null=True)
    module_status = IntegerField()
    module_type = CharField(null=True)
    module_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    module_uri = CharField()
    module_uri_type = CharField(null=True)

    class Meta:
        table_name = 'sm_module_operat_copy'

class SmRcardFlow(BaseModel):
    admin_id = IntegerField(null=True)
    admin_type = CharField(null=True)
    card_id = IntegerField()
    employee_id = IntegerField(null=True)
    flow_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    flow_id = AutoField()
    flow_last_status = IntegerField()
    flow_message = CharField(null=True)
    flow_prev_status = IntegerField()
    flow_remark = CharField(null=True)
    flow_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'sm_rcard_flow'

class SmRechargeCard(BaseModel):
    bal_serial = CharField(null=True)
    card_account = CharField()
    card_amount = IntegerField()
    card_batch_num = CharField(null=True)
    card_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    card_expires_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    card_flow_status = IntegerField()
    card_id = AutoField()
    card_name = CharField()
    card_pass = CharField()
    card_remark = IntegerField(null=True)
    card_status = IntegerField()
    card_type = CharField()
    card_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    employee_id = IntegerField(null=True)
    employee_name = CharField(null=True)

    class Meta:
        table_name = 'sm_recharge_card'

class SmReqHis(BaseModel):
    admin_id = IntegerField()
    his_id = AutoField()
    his_remark = CharField(null=True)
    is_success = IntegerField(null=True)
    operate_desc = CharField(null=True)
    operate_module = CharField(null=True)
    operator_name = CharField(null=True)
    operator_phone = CharField(null=True)
    req_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    req_param = TextField(null=True)
    req_update_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    req_url = CharField()

    class Meta:
        table_name = 'sm_req_his'

class SmRoleInfo(BaseModel):
    operator = IntegerField(null=True)
    role_code = CharField()
    role_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    role_id = AutoField()
    role_name = CharField()
    role_remark = CharField(null=True)
    role_status = IntegerField()
    role_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'sm_role_info'

class SmRoleModule(BaseModel):
    module_id = IntegerField()
    rm_id = AutoField()
    role_id = IntegerField()

    class Meta:
        table_name = 'sm_role_module'

class SmSeckillingRemind(BaseModel):
    pharmacy_id = IntegerField(null=True)
    phone_num = CharField(null=True)
    sg_id = IntegerField(null=True)
    sku_id = IntegerField(null=True)
    sr_context = CharField(null=True)
    sr_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sr_id = AutoField()
    sr_name = CharField(null=True)
    sr_remark = CharField(null=True)
    sr_remind = IntegerField(null=True)
    sr_status = IntegerField(null=True)
    sr_type = IntegerField(null=True)
    sr_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'sm_seckilling_remind'

class SmSeckillingShare(BaseModel):
    pharmacy_id = IntegerField(null=True)
    seckilling_share_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    seckilling_share_describe = CharField(null=True)
    seckilling_share_end_time = DateTimeField(null=True)
    seckilling_share_flag = IntegerField()
    seckilling_share_id = AutoField()
    seckilling_share_image = CharField(null=True)
    seckilling_share_remark = CharField(null=True)
    seckilling_share_start_time = DateTimeField(null=True)
    seckilling_share_status = IntegerField()
    seckilling_share_title = CharField(null=True)
    seckilling_share_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    seckilling_share_url = CharField(null=True)

    class Meta:
        table_name = 'sm_seckilling_share'

class SmSendHis(BaseModel):
    his_id = AutoField()
    other_info = CharField(null=True)
    send_content = CharField()
    send_phone = CharField()
    send_status = IntegerField()
    send_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    send_type = CharField()

    class Meta:
        table_name = 'sm_send_his'

class SmServiceFaq(BaseModel):
    faq_content = CharField(null=True)
    faq_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    faq_id = AutoField()
    faq_remark = CharField(null=True)
    faq_status = IntegerField()
    faq_title = CharField()
    faq_type = CharField()
    faq_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = IntegerField()

    class Meta:
        table_name = 'sm_service_faq'

class SmSharedInfo(BaseModel):
    pharmacy_id = IntegerField()
    share_go_can = CharField(null=True)
    share_go_data = CharField(null=True)
    share_go_title = CharField(null=True)
    share_go_type = CharField(null=True)
    shared_content = CharField()
    shared_create_time = DateTimeField(null=True)
    shared_id = AutoField()
    shared_img_url = CharField(null=True)
    shared_remark = CharField(null=True)
    shared_status = IntegerField(null=True)
    shared_title = CharField(null=True)
    shared_type = IntegerField()
    shared_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    shared_url = CharField(null=True)

    class Meta:
        table_name = 'sm_shared_info'

class SmSharedInfo1712(BaseModel):
    pharmacy_id = IntegerField()
    share_go_can = CharField(null=True)
    share_go_data = CharField(null=True)
    share_go_title = CharField(null=True)
    share_go_type = CharField(null=True)
    shared_content = CharField()
    shared_create_time = DateTimeField(null=True)
    shared_id = AutoField()
    shared_img_url = CharField(null=True)
    shared_remark = CharField(null=True)
    shared_status = IntegerField(null=True)
    shared_title = CharField(null=True)
    shared_type = IntegerField()
    shared_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    shared_url = CharField(null=True)

    class Meta:
        table_name = 'sm_shared_info_1712'

class SmSharedInfo180719(BaseModel):
    pharmacy_id = IntegerField()
    share_go_can = CharField(null=True)
    share_go_data = CharField(null=True)
    share_go_title = CharField(null=True)
    share_go_type = CharField(null=True)
    shared_content = CharField()
    shared_create_time = DateTimeField(null=True)
    shared_id = AutoField()
    shared_img_url = CharField(null=True)
    shared_remark = CharField(null=True)
    shared_status = IntegerField(null=True)
    shared_title = CharField(null=True)
    shared_type = IntegerField()
    shared_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    shared_url = CharField(null=True)

    class Meta:
        table_name = 'sm_shared_info_180719'

class SmSharedInfoBak(BaseModel):
    pharmacy_id = IntegerField()
    shared_content = CharField()
    shared_create_time = DateTimeField(null=True)
    shared_id = AutoField()
    shared_img_url = CharField(null=True)
    shared_remark = CharField(null=True)
    shared_status = IntegerField(null=True)
    shared_title = CharField(null=True)
    shared_type = IntegerField()
    shared_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    shared_url = CharField(null=True)

    class Meta:
        table_name = 'sm_shared_info_bak'

class SmSharedInfoBak2(BaseModel):
    pharmacy_id = IntegerField()
    shared_content = CharField()
    shared_create_time = DateTimeField(null=True)
    shared_id = AutoField()
    shared_img_url = CharField(null=True)
    shared_remark = CharField(null=True)
    shared_status = IntegerField(null=True)
    shared_title = CharField(null=True)
    shared_type = IntegerField()
    shared_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    shared_url = CharField(null=True)

    class Meta:
        table_name = 'sm_shared_info_bak2'

class SmSkipInfo(BaseModel):
    drugstore_id = IntegerField(null=True)
    skip_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    skip_flag = CharField(null=True)
    skip_id = AutoField()
    skip_image_height = CharField(null=True)
    skip_image_url = CharField(null=True)
    skip_image_width = CharField(null=True)
    skip_name = CharField(null=True)
    skip_type = CharField(null=True)
    skip_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    skip_web_tittle = CharField(null=True)
    skip_web_url = CharField(null=True)

    class Meta:
        table_name = 'sm_skip_info'

class SmUserBanner(BaseModel):
    banner_attr = CharField(null=True)
    banner_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    banner_flag = IntegerField(null=True)
    banner_id = AutoField()
    banner_image = CharField(null=True)
    banner_name = CharField(null=True)
    banner_param = IntegerField(null=True)
    banner_priority = IntegerField(null=True)
    banner_ratio = CharField(null=True)
    banner_remark = CharField(null=True)
    banner_type = CharField(null=True)
    banner_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    banner_url = CharField(null=True)
    pharmacy_id = IntegerField(null=True)

    class Meta:
        table_name = 'sm_user_banner'

class SmWindbirdInvokeLog(BaseModel):
    code = CharField(null=True)
    err = CharField(null=True)
    id = BigAutoField()
    invoke_time = BigIntegerField(null=True)
    json_data = CharField(null=True)
    method_name = CharField(null=True)
    param = CharField(null=True)
    succ = IntegerField(null=True)
    token = CharField(null=True)
    type = IntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'sm_windbird_invoke_log'

class SmWindbirdToken(BaseModel):
    disabled = IntegerField(null=True)
    expire_time = BigIntegerField(null=True)
    id = BigAutoField()
    token = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'sm_windbird_token'

class SmWxToken(BaseModel):
    access_token = CharField(null=True)
    create_time = DateTimeField()
    disabled = IntegerField()
    expires_in = IntegerField(null=True)
    id = BigAutoField()
    openid = CharField(null=True)
    refresh_token = CharField(null=True)
    scope = CharField(null=True)
    session_key = CharField(null=True)
    unionid = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    wx_type = IntegerField(constraints=[SQL("DEFAULT 2")], null=True)

    class Meta:
        table_name = 'sm_wx_token'

class SmsRecallUser(BaseModel):
    recall_create_time = DateTimeField(null=True)
    recall_id = AutoField()
    recall_status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    recall_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    user_phone = CharField(constraints=[SQL("DEFAULT '0'")], null=True)

    class Meta:
        table_name = 'sms_recall_user'

class StAnalysisCate(BaseModel):
    cate_id = AutoField()
    category_icon_url = CharField(null=True)
    category_id = IntegerField(null=True)
    category_name = CharField(null=True)
    category_order = IntegerField(null=True)
    category_state = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)

    class Meta:
        table_name = 'st_analysis_cate'

class StAnalysisResult(BaseModel):
    hot_main_show = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    st_create_time = DateTimeField(null=True)
    st_id = AutoField()
    st_name = CharField(null=True)
    st_remark = CharField(null=True)
    st_status = IntegerField(null=True)
    st_type = CharField(null=True)
    st_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'st_analysis_result'

class StAreaDay(BaseModel):
    ad_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    ad_date = DateTimeField(null=True)
    ad_id = AutoField()
    ad_remark = CharField(null=True)
    ad_time = CharField(null=True)
    ad_type = CharField(null=True)
    ad_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    all_count = IntegerField(null=True)
    city_name = CharField(null=True)
    county_name = CharField(null=True)
    open_count = IntegerField(null=True)
    order_count = IntegerField(null=True)
    order_fee = IntegerField(null=True)
    order_pay_fee = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_order_count = IntegerField(null=True)

    class Meta:
        table_name = 'st_area_day'
        indexes = (
            (('ad_time', 'pharmacy_id'), False),
        )

class StAreaDay0810(BaseModel):
    ad_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    ad_date = DateTimeField(null=True)
    ad_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    ad_remark = CharField(null=True)
    ad_time = CharField(null=True)
    ad_type = CharField(null=True)
    ad_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    all_count = IntegerField(null=True)
    city_name = CharField(null=True)
    county_name = CharField(null=True)
    open_count = IntegerField(null=True)
    order_count = IntegerField(null=True)
    order_fee = IntegerField(null=True)
    order_pay_fee = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_order_count = IntegerField(null=True)

    class Meta:
        table_name = 'st_area_day_0810'
        primary_key = False

class StAreaMonth(BaseModel):
    all_count = IntegerField(null=True)
    am_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    am_date = DateTimeField(null=True)
    am_id = AutoField()
    am_remark = CharField(null=True)
    am_time = CharField(null=True)
    am_type = CharField(null=True)
    am_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    city_name = CharField(null=True)
    county_name = CharField(null=True)
    open_count = IntegerField(null=True)
    order_count = IntegerField(null=True)
    order_fee = IntegerField(null=True)
    order_pay_fee = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_order_count = IntegerField(null=True)

    class Meta:
        table_name = 'st_area_month'

class StConsumeDay(BaseModel):
    all_count = IntegerField(null=True)
    cd_create_time = DateTimeField(null=True)
    cd_date = DateTimeField(null=True)
    cd_id = AutoField()
    cd_remark = CharField(null=True)
    cd_time = CharField(null=True)
    cd_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    open_count = IntegerField(null=True)
    order_count = IntegerField(null=True)
    order_fee = IntegerField(null=True)
    order_pay_fee = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)

    class Meta:
        table_name = 'st_consume_day'

class StConsumeMonth(BaseModel):
    all_count = IntegerField(null=True)
    cm_create_time = DateTimeField(null=True)
    cm_date = DateTimeField(null=True)
    cm_id = AutoField()
    cm_remark = CharField(null=True)
    cm_time = CharField(null=True)
    cm_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    open_count = IntegerField(null=True)
    order_count = IntegerField(null=True)
    order_fee = IntegerField(null=True)
    order_pay_fee = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)

    class Meta:
        table_name = 'st_consume_month'

class StSearchLog(BaseModel):
    pharmacy_id = IntegerField(null=True)
    phone_num = CharField(null=True)
    search_create_time = DateTimeField(index=True, null=True)
    search_id = AutoField()
    search_keywords = CharField(null=True)
    search_remark = CharField(null=True)
    search_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'st_search_log'
        indexes = (
            (('pharmacy_id', 'search_keywords', 'search_id'), False),
        )

class StShareInfo(BaseModel):
    app_system = CharField(null=True)
    app_verison = CharField(null=True)
    create_time = DateTimeField(null=True)
    pharmacy_id = IntegerField(null=True)
    share_act_id = IntegerField(null=True)
    share_act_type = CharField(null=True)
    share_id = AutoField()
    share_method = CharField(null=True)
    share_status = IntegerField(null=True)
    share_type = CharField(null=True)
    share_url = CharField(null=True)
    update_time = DateTimeField(null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'st_share_info'

class StSkuHitsInfo(BaseModel):
    hits_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    hits_id = AutoField()
    hits_remark = CharField(null=True)
    hits_type = CharField(null=True)
    hits_update_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    pharmacy_id = IntegerField(index=True, null=True)
    prod_id = IntegerField(null=True)
    sku_id = IntegerField(index=True, null=True)
    user_id = IntegerField(index=True, null=True)
    user_phone = CharField(null=True)

    class Meta:
        table_name = 'st_sku_hits_info'

class StTaskRecord(BaseModel):
    msg_body = CharField(null=True)
    msg_id = CharField(null=True)
    msg_key = CharField(null=True)
    msg_retimes = IntegerField(null=True)
    msg_tag = CharField(null=True)
    msg_topic = CharField(null=True)
    phone_num = CharField(null=True)
    task_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True, null=True)
    task_id = AutoField()
    task_remark = CharField(null=True)
    task_status = IntegerField(null=True)
    task_type = CharField(null=True)
    task_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'st_task_record'

class StTempUserOrder(BaseModel):
    odate = DateField(null=True)
    user_id = IntegerField(index=True)

    class Meta:
        table_name = 'st_temp_user_order'
        primary_key = False

class StUserCount(BaseModel):
    pharmacy_id = IntegerField(null=True)
    st_count = IntegerField()
    st_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    st_date = DateTimeField(null=True)
    st_end_type = CharField(null=True)
    st_id = AutoField()
    st_order_count = IntegerField(null=True)
    st_parent_type = CharField(null=True)
    st_sub_type = CharField(null=True)

    class Meta:
        table_name = 'st_user_count'

class StUserDay(BaseModel):
    hy_consume_45 = IntegerField(null=True)
    hy_open_45 = IntegerField(null=True)
    lc_consume_30 = IntegerField(null=True)
    lc_consume_60 = IntegerField(null=True)
    lc_consume_90 = IntegerField(null=True)
    lc_open_30 = IntegerField(null=True)
    lc_open_60 = IntegerField(null=True)
    lc_open_90 = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    tj_user_count = IntegerField(null=True)
    ud_create_time = DateTimeField(null=True)
    ud_date = DateTimeField(null=True)
    ud_id = AutoField()
    ud_remark = CharField(null=True)
    ud_time = CharField(null=True)
    ud_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    user_count = IntegerField(null=True)
    user_from = CharField(null=True)
    zm_user_count = IntegerField(null=True)

    class Meta:
        table_name = 'st_user_day'

class StUserKeep(BaseModel):
    keep_30 = IntegerField(null=True)
    keep_60 = IntegerField(null=True)
    keep_90 = IntegerField(null=True)
    keep_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    keep_happen = CharField()
    keep_happen_time = DateTimeField(constraints=[SQL("DEFAULT 2015-01-01 08:00:00")], index=True)
    keep_id = AutoField()
    keep_remark = CharField(null=True)
    keep_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    order_30 = IntegerField(null=True)
    order_60 = IntegerField(null=True)
    order_90 = IntegerField(null=True)
    pharmacy_id = IntegerField(index=True)
    phone_num = CharField(null=True)
    regist_type = CharField(null=True)
    user_id = IntegerField()

    class Meta:
        table_name = 'st_user_keep'
        indexes = (
            (('keep_happen_time', 'phone_num'), False),
            (('keep_happen_time', 'phone_num', 'keep_30'), False),
        )

class StUserLog(BaseModel):
    log_create_time = DateTimeField(null=True)
    log_happen_time = DateTimeField(null=True)
    log_id = AutoField()
    log_remark = CharField(null=True)
    log_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    message_name = CharField()
    pharmacy_id = IntegerField()
    phone_num = CharField()
    user_id = IntegerField()

    class Meta:
        table_name = 'st_user_log'
        indexes = (
            (('user_id', 'pharmacy_id'), False),
        )

class StUserMonth(BaseModel):
    hy_consume_45 = IntegerField(null=True)
    hy_open_45 = IntegerField(null=True)
    lc_consume_30 = IntegerField(null=True)
    lc_consume_60 = IntegerField(null=True)
    lc_consume_90 = IntegerField(null=True)
    lc_open_30 = IntegerField(null=True)
    lc_open_60 = IntegerField(null=True)
    lc_open_90 = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    tj_user_count = IntegerField(null=True)
    um_create_time = DateTimeField(null=True)
    um_date = DateTimeField(null=True)
    um_id = AutoField()
    um_remark = CharField(null=True)
    um_time = CharField(null=True)
    um_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    user_count = IntegerField(null=True)
    user_from = CharField(null=True)
    zm_user_count = IntegerField(null=True)

    class Meta:
        table_name = 'st_user_month'

class StUserVisit(BaseModel):
    pharmacy_id = IntegerField(null=True)
    phone_num = CharField(null=True)
    user_id = IntegerField(null=True)
    visit_create_time = DateTimeField(null=True)
    visit_happen = CharField(null=True)
    visit_id = AutoField()
    visit_remark = CharField(null=True)
    visit_type = CharField(null=True)
    visit_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'st_user_visit'
        indexes = (
            (('user_id', 'visit_happen'), False),
        )

class StUsertisInfo(BaseModel):
    action_name = CharField(index=True, null=True)
    action_time = DateTimeField(index=True, null=True)
    action_type = CharField(null=True)
    action_word = CharField(null=True)
    action_word_type = CharField(null=True)
    page_name = CharField(index=True, null=True)
    page_type = CharField(index=True, null=True)
    pharmacy_id = IntegerField(index=True, null=True)
    phone_num = CharField(index=True, null=True)
    time_type = CharField(null=True)
    tis_create_time = DateTimeField(index=True, null=True)
    tis_happen_time = DateTimeField(null=True)
    tis_id = AutoField()
    tis_remark = CharField(null=True)
    tis_update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'st_usertis_info'

class StUsertisInfo201707201804(BaseModel):
    action_name = CharField(index=True, null=True)
    action_time = DateTimeField(index=True, null=True)
    action_type = CharField(null=True)
    action_word = CharField(null=True)
    action_word_type = CharField(null=True)
    page_name = CharField(index=True, null=True)
    page_type = CharField(index=True, null=True)
    pharmacy_id = IntegerField(index=True, null=True)
    phone_num = CharField(index=True, null=True)
    time_type = CharField(null=True)
    tis_create_time = DateTimeField(index=True, null=True)
    tis_happen_time = DateTimeField(null=True)
    tis_id = AutoField()
    tis_remark = CharField(null=True)
    tis_update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'st_usertis_info_201707_201804'

class StWindowLog(BaseModel):
    device_id = CharField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(null=True)
    window_create_time = DateTimeField(null=True)
    window_happen = CharField(null=True)
    window_happen_time = DateTimeField(null=True)
    window_id = IntegerField(null=True)
    window_remark = CharField(null=True)
    window_status = IntegerField(null=True)
    window_type = CharField(null=True)
    window_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    wl_id = AutoField()

    class Meta:
        table_name = 'st_window_log'
        indexes = (
            (('user_id', 'pharmacy_id', 'window_happen'), False),
        )

class StWindowLog20160831(BaseModel):
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(null=True)
    window_create_time = DateTimeField(null=True)
    window_happen = CharField(null=True)
    window_happen_time = DateTimeField(null=True)
    window_remark = CharField(null=True)
    window_status = IntegerField(null=True)
    window_type = CharField(null=True)
    window_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    wl_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'st_window_log_20160831'
        primary_key = False

class StWindowLogBak200201(BaseModel):
    device_id = CharField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(null=True)
    window_create_time = DateTimeField(null=True)
    window_happen = CharField(null=True)
    window_happen_time = DateTimeField(null=True)
    window_id = IntegerField(null=True)
    window_remark = CharField(null=True)
    window_status = IntegerField(null=True)
    window_type = CharField(null=True)
    window_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    wl_id = AutoField()

    class Meta:
        table_name = 'st_window_log_bak200201'
        indexes = (
            (('user_id', 'pharmacy_id', 'window_happen'), False),
        )

class StWindowLogDel(BaseModel):
    device_id = CharField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(null=True)
    window_create_time = DateTimeField(null=True)
    window_happen = CharField(null=True)
    window_happen_time = DateTimeField(null=True)
    window_id = IntegerField(null=True)
    window_remark = CharField(null=True)
    window_status = IntegerField(null=True)
    window_type = CharField(null=True)
    window_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    wl_id = AutoField()

    class Meta:
        table_name = 'st_window_log_del'
        indexes = (
            (('user_id', 'pharmacy_id', 'window_happen'), False),
        )

class TaAjam93CjSource(BaseModel):
    cource_update_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    phone_number = CharField(null=True)
    source_already_num = IntegerField(null=True)
    source_already_pray = IntegerField(null=True)
    source_already_share = IntegerField(null=True)
    source_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    source_date = DateField(null=True)
    source_id = AutoField()
    source_remark = CharField(null=True)
    source_sum_num = IntegerField(null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'ta_ajam93_cj_source'

class TaAjam93Prayer(BaseModel):
    phone_number = CharField(null=True)
    pray_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    pray_id = AutoField()
    pray_info = CharField(null=True)
    pray_remark = CharField(null=True)
    pray_update_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'ta_ajam93_prayer'

class TaAjam93Result(BaseModel):
    phone_number = CharField(null=True)
    result_choujiang_timel = DateField(null=True)
    result_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    result_id = AutoField()
    result_price_describ = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    result_prize_name = CharField()
    result_remark = CharField(null=True)
    result_status = IntegerField(null=True)
    result_update_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    rusult_resu = IntegerField(null=True)
    user_id = IntegerField()

    class Meta:
        table_name = 'ta_ajam93_result'

class TaAjam93Share(BaseModel):
    phone_number = CharField(null=True)
    share_content = CharField(null=True)
    share_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    share_id = AutoField()
    share_remark = CharField(null=True)
    share_update_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'ta_ajam93_share'

class TaChristmasWork(BaseModel):
    nickname = CharField(null=True)
    openid = CharField()
    phone_num = CharField(null=True)
    user_id = IntegerField(null=True)
    work_blessing = CharField(null=True)
    work_createtime = DateTimeField(null=True)
    work_id = AutoField()
    work_remark = CharField(null=True)
    work_template_img = CharField()
    work_template_music = CharField()
    work_updatetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    work_user_img = CharField(null=True)

    class Meta:
        table_name = 'ta_christmas_work'

class TaGetcoupInfo(BaseModel):
    act_id = IntegerField(null=True)
    coupon_desc = CharField(null=True)
    coupon_id = IntegerField(null=True)
    coupon_threshold = IntegerField(null=True)
    coupon_value = IntegerField(null=True)
    from_user_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    gcp_createtime = DateTimeField(null=True)
    gcp_id = AutoField()
    gcp_remark = CharField(null=True)
    gcp_updatetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    headimgurl = CharField(null=True)
    invite_code = CharField(index=True)
    nickname = CharField(null=True)
    openid = CharField(null=True)
    phone_num = CharField()
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ta_getcoup_info'

class TaGrantInfo(BaseModel):
    city = CharField(null=True)
    country = CharField(null=True)
    createtime = DateTimeField(null=True)
    grant_id = AutoField()
    headimgurl = CharField(null=True)
    last_grant_time = DateTimeField(null=True)
    nickname = CharField(null=True)
    openid = CharField(index=True)
    phone_num = CharField(null=True)
    province = CharField(null=True)
    remark = CharField(null=True)
    sex = CharField(null=True)
    updatetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'ta_grant_info'

class TaLetterGame(BaseModel):
    game_createtime = DateTimeField(null=True)
    game_id = AutoField()
    game_letter = CharField()
    game_remark = CharField(null=True)
    game_to = CharField(null=True)
    game_updatetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    imgurl = CharField(null=True)
    nickname = CharField(null=True)
    openid = CharField()

    class Meta:
        table_name = 'ta_letter_game'

class TaLetterParticipant(BaseModel):
    game_id = IntegerField()
    imgurl = CharField(null=True)
    nickname = CharField(null=True)
    openid = CharField()
    ptcp_createtime = DateTimeField(null=True)
    ptcp_guessletter = CharField(null=True)
    ptcp_id = AutoField()
    ptcp_percent = CharField(null=True)
    ptcp_remark = CharField(null=True)
    ptcp_updatetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ta_letter_participant'

class TaMoonFestivalAward(BaseModel):
    admin_id = IntegerField(null=True)
    award_code = CharField()
    award_create_time = DateTimeField(null=True)
    award_get_time = DateTimeField(null=True)
    award_id = AutoField()
    award_status = CharField()
    award_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    gamer_id = IntegerField()
    user_id = IntegerField(null=True)
    user_phone = CharField(null=True)

    class Meta:
        table_name = 'ta_moon_festival_award'

class TaMoonFestivalGamer(BaseModel):
    game_continue = CharField(null=True)
    gamer_cake_num = IntegerField(column_name='gamer_cakeNum', constraints=[SQL("DEFAULT 0")], null=True)
    gamer_city = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    gamer_country = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    gamer_create_time = DateTimeField(null=True)
    gamer_from_id = IntegerField(null=True)
    gamer_get_cake_time = DateTimeField(column_name='gamer_getCake_time', constraints=[SQL("DEFAULT 2015-09-20 00:00:00")], null=True)
    gamer_headimgurl = CharField(null=True)
    gamer_id = AutoField()
    gamer_nickname = CharField(constraints=[SQL("DEFAULT '0'")])
    gamer_openid = CharField(constraints=[SQL("DEFAULT '0'")])
    gamer_phone = CharField(null=True)
    gamer_province = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    gamer_sex = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    gamer_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    gamer_userid = IntegerField(null=True)

    class Meta:
        table_name = 'ta_moon_festival_gamer'

class TaMoonFestivalOperate(BaseModel):
    gamer_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    operate_cake_sum = IntegerField(column_name='operate_cakeSum')
    operate_cake_increase = IntegerField(constraints=[SQL("DEFAULT 0")])
    operate_create_time = DateTimeField(null=True)
    operate_helper_id = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    operate_helper_nickname = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    operate_helper_url = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    operate_id = AutoField()
    operate_operate_time = DateTimeField(null=True)
    operate_remark = CharField(null=True)
    operate_status_code = CharField(constraints=[SQL("DEFAULT '0'")])
    operate_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'ta_moon_festival_operate'

class TaMoonFestivalReward(BaseModel):
    gamer_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    reward_create_time = DateTimeField(null=True)
    reward_gamer_openid = CharField(constraints=[SQL("DEFAULT '0'")])
    reward_id = AutoField()
    reward_type = CharField(constraints=[SQL("DEFAULT '0'")])
    reward_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    reward_value = CharField(constraints=[SQL("DEFAULT '0'")])

    class Meta:
        table_name = 'ta_moon_festival_reward'

class TaTeacher910Gamer(BaseModel):
    create_time = DateTimeField(null=True)
    gamer_id = AutoField()
    nick_name = CharField()
    phone_num = CharField(null=True)
    score = IntegerField(null=True)
    session_id = CharField()
    start_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'ta_teacher910_gamer'

class TaTeacher910Question(BaseModel):
    question_answer = CharField(null=True)
    question_content = CharField(null=True)
    question_id = AutoField()

    class Meta:
        table_name = 'ta_teacher910_question'

class Taoyuan0104(BaseModel):
    chanpindalei = CharField(null=True)
    chanpinhuohao = CharField(null=True)
    chanpinxiaolei = CharField(null=True)
    dir_code = CharField(null=True)
    dir_id = IntegerField(null=True)
    shangpincuxiaojia = IntegerField(null=True)
    shangpinming = CharField(null=True)
    shangpinyuanjia = IntegerField(null=True)
    sku_id = CharField(null=True)
    tongyongming = CharField(null=True)
    xuhao = CharField(null=True)
    zongshu = CharField(null=True)

    class Meta:
        table_name = 'taoyuan_0104'

class TemDir20171214(BaseModel):
    dir_code = CharField(null=True)
    dir_name = CharField(null=True)
    drugstore_id = IntegerField(null=True)
    prod_id = IntegerField(null=True)
    prod_name = CharField(null=True)
    sku_id = IntegerField(null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'tem_dir_20171214'

class Temp0413(BaseModel):
    dir_code = CharField(null=True)
    dir_id = IntegerField(null=True)
    prod_id = IntegerField(null=True)
    prod_name = CharField(null=True)
    sku_id = IntegerField(null=True)
    sku_order = CharField(null=True)
    sku_status = CharField(null=True)
    temp_id = AutoField()

    class Meta:
        table_name = 'temp_0413'

class Temp1127(BaseModel):
    bianhao = CharField(null=True)
    chanpinhuohao = CharField(null=True)
    code = CharField(null=True)
    dir_id = IntegerField(null=True)
    shangpincuxiaojia = CharField(null=True)
    shangpinyuanjia = CharField(null=True)
    sku_id = IntegerField(null=True)
    xuhao = CharField(null=True)

    class Meta:
        table_name = 'temp_1127'
        primary_key = False

class Temp1130(BaseModel):
    bianhao = CharField(null=True)
    cuxiaojia = CharField(null=True)
    cuxiaoma = CharField(null=True)
    dir_id = IntegerField(null=True)
    huohao = CharField(null=True)
    lingshoujia = CharField(null=True)
    sku_id = IntegerField(null=True)
    xuhao = CharField(null=True)

    class Meta:
        table_name = 'temp_1130'
        primary_key = False

class TempCategoryDrug(BaseModel):
    dir_id = IntegerField(null=True)
    drug_name = CharField(null=True)
    id = BigAutoField()
    name = CharField(null=True)
    prod_id = IntegerField(null=True)

    class Meta:
        table_name = 'temp_category_drug'

class TempCategoryDrug2(BaseModel):
    dir_id = IntegerField(null=True)
    drug_name = CharField(null=True)
    id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(null=True)
    prod_id = IntegerField(null=True)

    class Meta:
        table_name = 'temp_category_drug_2'
        primary_key = False

class TempInfo(BaseModel):
    品牌名 = CharField(null=True)
    序号 = AutoField()
    康佰馨货号 = CharField(null=True)
    正济堂货号 = CharField(null=True)
    生产企业 = CharField(null=True)
    药快到id = CharField(column_name='药快到ID', null=True)
    规格 = CharField(null=True)
    通用名称 = CharField(null=True)

    class Meta:
        table_name = 'temp_info'

class TempInfo2(BaseModel):
    dir_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    一级分类 = CharField(null=True)
    三级分类 = CharField(null=True)
    二级分类 = CharField(null=True)
    品牌名 = CharField(null=True)
    四级分类 = CharField(null=True)
    序号 = IntegerField()
    康佰馨货号 = CharField(null=True)
    正济堂货号 = CharField(null=True)
    生产企业 = CharField(null=True)
    药快到id = CharField(column_name='药快到ID', null=True)
    规格 = CharField(null=True)
    通用名称 = CharField(null=True)

    class Meta:
        table_name = 'temp_info2'
        primary_key = False

class TempProd(BaseModel):
    dir_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    prod_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    康佰馨货号 = CharField(null=True)
    正济堂货号 = CharField(null=True)

    class Meta:
        table_name = 'temp_prod'

class TempSkuDirPrice(BaseModel):
    dir_code = CharField()
    dir_id = IntegerField()
    link_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    sku_id = IntegerField()

    class Meta:
        table_name = 'temp_sku_dir_price'
        primary_key = False

class TempSkuPrice(BaseModel):
    sku_fee = IntegerField()
    sku_id = IntegerField()
    sku_price = IntegerField()

    class Meta:
        table_name = 'temp_sku_price'

class TempTjx0329(BaseModel):
    channel = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    phone_num = CharField()
    regist_date = DateTimeField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'temp_tjx_0329'
        primary_key = False

class TempTjx0330(BaseModel):
    order_create_time = DateTimeField(null=True)
    order_fee = IntegerField()
    order_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_other1 = CharField(null=True)
    order_pay_fee = IntegerField()
    user_id = IntegerField()

    class Meta:
        table_name = 'temp_tjx_0330'
        primary_key = False

class TempTjx033001(BaseModel):
    order_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'temp_tjx_0330_01'
        primary_key = False

class TempTjx0504(BaseModel):
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'temp_tjx_0504'
        primary_key = False

class TempTjx0506(BaseModel):
    o_order_fee_o_order_pay_fee_ = BigIntegerField(column_name='o.`order_fee` -o.`order_pay_fee`', constraints=[SQL("DEFAULT 0")])
    order_create_time = DateTimeField(null=True)
    order_fee = IntegerField()
    order_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_pay_fee = IntegerField()
    phone_num = CharField(null=True)
    user_from = CharField(index=True, null=True)
    user_id = IntegerField()

    class Meta:
        table_name = 'temp_tjx_0506'
        primary_key = False

class Tianyi0817(BaseModel):
    beizhu = TextField(null=True)
    chanpindalei = CharField(null=True)
    chanpinxiaolei = CharField(null=True)
    dir_code = CharField(null=True)
    dir_id = IntegerField(null=True)
    dir_remark = CharField(null=True)
    drugstore_id = CharField(null=True)
    huohao = CharField(null=True)
    miaoshu = CharField(null=True)
    newsku_id = CharField(null=True)
    pizhunwenhao = CharField(null=True)
    shangpincuxiaojia = CharField(null=True)
    shangpinming = CharField(null=True)
    shangpinyuanjia = CharField(null=True)
    tiaoma = CharField(null=True)
    tongyongming = CharField(null=True)
    xuhao = CharField(null=True)
    zongshu = CharField(null=True)

    class Meta:
        table_name = 'tianyi_0817'
        primary_key = False

class Tianyi081702(BaseModel):
    beizhu = TextField(null=True)
    chanpindalei = CharField(null=True)
    chanpinxiaolei = CharField(null=True)
    dir_code = CharField(null=True)
    dir_id = IntegerField(null=True)
    dir_remark = CharField(null=True)
    drugstore_id = CharField(null=True)
    huohao = CharField(null=True)
    miaoshu = CharField(null=True)
    pizhunwenhao = CharField(null=True)
    shangpincuxiaojia = CharField(null=True)
    shangpinming = CharField(null=True)
    shangpinyuanjia = CharField(null=True)
    sku_id = CharField(null=True)
    tiaoma = CharField(null=True)
    tongyongming = CharField(null=True)
    xuhao = CharField(null=True)
    zongshu = CharField(null=True)

    class Meta:
        table_name = 'tianyi_081702'
        primary_key = False

class TjBzspx(BaseModel):
    class1 = CharField(null=True)
    class2 = CharField(null=True)
    class3 = CharField(null=True)
    prod_brand = CharField(null=True)
    prod_firm = CharField(null=True)
    prod_id = CharField(null=True)
    prod_name = CharField(null=True)
    prod_spec = CharField(null=True)
    xh = CharField(null=True)

    class Meta:
        table_name = 'tj_bzspx'
        primary_key = False

class TjFlhz(BaseModel):
    class2 = CharField(null=True)
    prod_code = CharField(null=True)
    prod_firm = CharField(null=True)
    prod_gen_name = CharField(null=True)
    prod_id = CharField(null=True)
    prod_indication = CharField(null=True)
    prod_name = CharField(null=True)
    prod_sn = CharField(null=True)
    prod_spec = CharField(null=True)

    class Meta:
        table_name = 'tj_flhz'
        primary_key = False

class Tmp0728(BaseModel):
    css = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    dir_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'tmp_0728'
        primary_key = False

class Tmp12201(BaseModel):
    sku_id = IntegerField(null=True)
    skubat = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'tmp_1220_1'
        primary_key = False

class Tmp12202(BaseModel):
    sale_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    sale_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sale_fee = IntegerField(null=True)
    sale_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    sale_price = IntegerField(null=True)
    sale_remark = CharField(null=True)
    sale_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    sale_status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sale_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sku_id = IntegerField(null=True)

    class Meta:
        table_name = 'tmp_1220_2'
        primary_key = False

class Tmp1223(BaseModel):
    cat_link_id = IntegerField(index=True, null=True)
    category_id = IntegerField(null=True)
    dir_name = CharField()
    link_id = AutoField()
    prod_id = IntegerField(null=True)
    prod_name = CharField(null=True)

    class Meta:
        table_name = 'tmp_1223'

class TmpBrandCategory(BaseModel):
    category_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    category_name = CharField()
    prod_brand = CharField()

    class Meta:
        table_name = 'tmp_brand_category'
        primary_key = False

class TmpBrandInfo(BaseModel):
    category_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    category_name = CharField()
    prod_brand = CharField()
    prod_firm = CharField(null=True)

    class Meta:
        table_name = 'tmp_brand_info'
        primary_key = False

class TmpKscProd(BaseModel):
    prod_id = IntegerField()

    class Meta:
        table_name = 'tmp_ksc_prod'
        primary_key = False


class TmpUser(BaseModel):
    cur_status = IntegerField()
    email = CharField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    phone_num = CharField()
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_create_time = DateTimeField(null=True)
    user_credit = IntegerField(null=True)
    user_device = CharField(null=True)
    user_from = CharField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    user_max_points = IntegerField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_token = CharField(null=True)
    user_type = CharField()
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField()

    class Meta:
        table_name = 'tmp_user'
        primary_key = False

class TongxinImg(BaseModel):
    attr_id = IntegerField(null=True)
    attr_value_id = IntegerField(null=True)
    img_id = IntegerField(null=True)
    img_kind = CharField(null=True)
    img_name = CharField(null=True)
    link_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    prod_id = IntegerField()

    class Meta:
        table_name = 'tongxin_img'
        primary_key = False

class TtUserNerver(BaseModel):
    cur_status = IntegerField()
    email = CharField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    phone_num = CharField()
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_create_time = DateTimeField(null=True)
    user_credit = IntegerField(null=True)
    user_device = CharField(null=True)
    user_from = CharField(null=True)
    user_id = AutoField()
    user_max_points = IntegerField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_token = CharField(null=True)
    user_type = CharField()
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField()

    class Meta:
        table_name = 'tt_user_nerver'

class TtUserNerver60(BaseModel):
    cur_status = IntegerField()
    email = CharField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    phone_num = CharField()
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_create_time = DateTimeField(null=True)
    user_credit = IntegerField(null=True)
    user_device = CharField(null=True)
    user_from = CharField(null=True)
    user_id = AutoField()
    user_max_points = IntegerField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_token = CharField(null=True)
    user_type = CharField()
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField()

    class Meta:
        table_name = 'tt_user_nerver_60'

class TtUserOnly1(BaseModel):
    cur_status = IntegerField()
    email = CharField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    phone_num = CharField()
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_create_time = DateTimeField(null=True)
    user_credit = IntegerField(null=True)
    user_device = CharField(null=True)
    user_from = CharField(null=True)
    user_id = AutoField()
    user_max_points = IntegerField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_token = CharField(null=True)
    user_type = CharField()
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField()

    class Meta:
        table_name = 'tt_user_only_1'

class TtUserOther(BaseModel):
    cur_status = IntegerField()
    email = CharField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    phone_num = CharField()
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_create_time = DateTimeField(null=True)
    user_credit = IntegerField(null=True)
    user_device = CharField(null=True)
    user_from = CharField(null=True)
    user_id = AutoField()
    user_max_points = IntegerField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_token = CharField(null=True)
    user_type = CharField()
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField()

    class Meta:
        table_name = 'tt_user_other'

class TttCoupon1280(BaseModel):
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_code = CharField(null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_name = CharField()
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField()
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ttt_coupon_12_80'
        primary_key = False

class TttCoupon60(BaseModel):
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_code = CharField(null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_name = CharField()
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField()
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ttt_coupon_60'
        primary_key = False

class TttCoupon90(BaseModel):
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_code = CharField(null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_name = CharField()
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField()
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ttt_coupon_90'
        primary_key = False

class TttCouponNever(BaseModel):
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_code = CharField(null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_name = CharField()
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField()
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ttt_coupon_never'
        primary_key = False

class TttCouponOther(BaseModel):
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_code = CharField(null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_name = CharField()
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField()
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ttt_coupon_other'
        primary_key = False

class TttTest1(BaseModel):
    phone_num = CharField()
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ttt_test1'
        primary_key = False

class TttTest2(BaseModel):
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ttt_test2'
        primary_key = False

class TttTest3(BaseModel):
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_code = CharField(null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = AutoField()
    coupon_name = CharField()
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField()
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'ttt_test3'

class TttTyProdir(BaseModel):
    dir_code = CharField(null=True)
    high_dname = CharField(null=True)
    huohao = CharField(null=True)
    low_dir_id = BigIntegerField(column_name='low_dirId', null=True)
    max_code = CharField(null=True)
    max_dname = CharField(null=True)
    mid_code = CharField(null=True)
    mid_dname = CharField(null=True)
    min_dname = CharField(null=True)
    prod_id = IntegerField()
    sku_id = AutoField()

    class Meta:
        table_name = 'ttt_ty_prodir'

class TttUserNever(BaseModel):
    cur_status = IntegerField()
    email = CharField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    phone_num = CharField()
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_create_time = DateTimeField(null=True)
    user_credit = IntegerField(null=True)
    user_device = CharField(null=True)
    user_from = CharField(null=True)
    user_id = AutoField()
    user_max_points = IntegerField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_token = CharField(null=True)
    user_type = CharField()
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField()

    class Meta:
        table_name = 'ttt_user_never'

class TttUserNever60(BaseModel):
    cur_status = IntegerField()
    email = CharField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    phone_num = CharField()
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_create_time = DateTimeField(null=True)
    user_credit = IntegerField(null=True)
    user_device = CharField(null=True)
    user_from = CharField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    user_max_points = IntegerField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_token = CharField(null=True)
    user_type = CharField()
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField()

    class Meta:
        table_name = 'ttt_user_never_60'
        primary_key = False

class TttUserOnly1(BaseModel):
    cur_status = IntegerField()
    email = CharField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    phone_num = CharField()
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_create_time = DateTimeField(null=True)
    user_credit = IntegerField(null=True)
    user_device = CharField(null=True)
    user_from = CharField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    user_max_points = IntegerField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_token = CharField(null=True)
    user_type = CharField()
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField()

    class Meta:
        table_name = 'ttt_user_only_1'
        primary_key = False

class TttUserOrder(BaseModel):
    cur_status = IntegerField()
    email = CharField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    phone_num = CharField()
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_create_time = DateTimeField(null=True)
    user_credit = IntegerField(null=True)
    user_device = CharField(null=True)
    user_from = CharField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    user_max_points = IntegerField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_token = CharField(null=True)
    user_type = CharField()
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField()

    class Meta:
        table_name = 'ttt_user_order'
        primary_key = False

class TtttTtt(BaseModel):
    coupon_activate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_code = CharField(null=True)
    coupon_color = CharField(null=True)
    coupon_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_deactivate_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    coupon_desc = CharField(null=True)
    coupon_from_id = IntegerField(null=True)
    coupon_from_type = CharField(null=True)
    coupon_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_name = CharField()
    coupon_nouse_cause = CharField(null=True)
    coupon_read = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    coupon_remark = CharField(null=True)
    coupon_status = IntegerField()
    coupon_tem_id = IntegerField(null=True)
    coupon_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = CharField()
    coupon_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_use_dir = CharField(null=True)
    coupon_use_info = CharField(null=True)
    coupon_use_type = IntegerField(null=True)
    coupon_value = IntegerField()
    invite_id = IntegerField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'tttt_ttt'
        primary_key = False

class Ttttt1Tmp(BaseModel):
    dir_code = CharField(null=True)
    high_dname = CharField(null=True)
    huohao = CharField(null=True)
    low_dir_id = BigIntegerField(column_name='low_dirId', null=True)
    max_code = CharField(null=True)
    max_dname = CharField(null=True)
    mid_code = CharField(null=True)
    mid_dname = CharField(null=True)
    min_dname = CharField(null=True)
    prod_id = IntegerField()
    sku_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ttttt_1_tmp'
        primary_key = False

class UmAppleUser(BaseModel):
    apple_id = CharField(primary_key=True)
    create_time = DateTimeField(null=True)
    email = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    email_verified = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    ykd_phone = CharField(null=True)

    class Meta:
        table_name = 'um_apple_user'

class UmBalanceList(BaseModel):
    bal_amount = IntegerField(null=True)
    bal_create_time = DateTimeField(null=True)
    bal_do = IntegerField(null=True)
    bal_id = AutoField()
    bal_last_total = IntegerField(null=True)
    bal_type = IntegerField(null=True)
    bal_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_id = IntegerField(null=True)
    points_remark = CharField(null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'um_balance_list'

class UmDrugInfo(BaseModel):
    drug_user_allergy_history = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    drug_user_birthday = CharField(null=True)
    drug_user_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    drug_user_default = IntegerField(constraints=[SQL("DEFAULT 00000000000")])
    drug_user_describe = CharField(null=True)
    drug_user_disease_history = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    drug_user_eat = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    drug_user_family_disease_history = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    drug_user_flag = CharField(constraints=[SQL("DEFAULT '0'")])
    drug_user_id = AutoField()
    drug_user_idcard = CharField(null=True)
    drug_user_kidney = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    drug_user_liver = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    drug_user_name = CharField(null=True)
    drug_user_phone = CharField(null=True)
    drug_user_pregnancy = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    drug_user_reactions = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    drug_user_remark = CharField(null=True)
    drug_user_sex = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    drug_user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    drug_user_weight = CharField(null=True)
    user_id = CharField(null=True)

    class Meta:
        table_name = 'um_drug_info'

class UmInviteHistory(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    his_id = AutoField()
    invite_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    new_phone = CharField()
    new_uid = IntegerField()
    uid = IntegerField()
    user_phone = CharField()

    class Meta:
        table_name = 'um_invite_history'

class UmMessageInfo(BaseModel):
    msg_content = CharField()
    msg_create_time = DateTimeField(null=True)
    msg_from = IntegerField(null=True)
    msg_id = AutoField()
    msg_image = CharField(null=True)
    msg_link_data = CharField(null=True)
    msg_link_type = CharField(null=True)
    msg_recept_time = DateTimeField(null=True)
    msg_remark = CharField(null=True)
    msg_status = IntegerField()
    msg_title = CharField()
    msg_type = CharField()
    msg_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = IntegerField()

    class Meta:
        table_name = 'um_message_info'

class UmOpenUser(BaseModel):
    open_create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    open_id = AutoField()
    open_login_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    open_name = CharField()
    open_remark = CharField(null=True)
    open_result = CharField(null=True)
    open_status = IntegerField(null=True)
    open_uuid = CharField()
    user_id = IntegerField()

    class Meta:
        table_name = 'um_open_user'

class UmPointsList(BaseModel):
    list_id = AutoField()
    order_id = IntegerField(null=True)
    points_remark = CharField(null=True)
    pts_amount = IntegerField(null=True)
    pts_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    pts_do = IntegerField()
    pts_last_total = IntegerField(null=True)
    pts_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = IntegerField()

    class Meta:
        table_name = 'um_points_list'

class UmPosTrack(BaseModel):
    track_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    track_id = AutoField()
    track_lat = CharField()
    track_local = CharField(null=True)
    track_lon = CharField()
    track_remark = CharField(null=True)
    track_status = IntegerField()
    track_type = CharField(null=True)
    track_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = IntegerField()

    class Meta:
        table_name = 'um_pos_track'

class UmPushMsg(BaseModel):
    msg_content = CharField()
    msg_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    msg_id = AutoField()
    msg_phone_type = CharField(null=True)
    msg_recept_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    msg_remark = CharField(null=True)
    msg_status = IntegerField()
    msg_type = CharField(null=True)
    msg_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'um_push_msg'

class UmRoleInfo(BaseModel):
    operator = IntegerField(null=True)
    role_code = CharField()
    role_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    role_id = AutoField()
    role_level = IntegerField()
    role_name = CharField()
    role_parent = IntegerField(null=True)
    role_remark = CharField(null=True)
    role_status = IntegerField()
    role_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'um_role_info'

class UmSmsCode(BaseModel):
    code_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    code_id = AutoField()
    code_status = IntegerField(index=True)
    code_type = CharField()
    code_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    phone_code = CharField()
    phone_num = CharField(index=True)

    class Meta:
        table_name = 'um_sms_code'
        indexes = (
            (('phone_num', 'code_status'), False),
        )

class UmUserAddr(BaseModel):
    accept_name = CharField()
    accept_phone = CharField()
    addr_area = CharField(null=True)
    addr_city = CharField(null=True)
    addr_create_time = DateTimeField(null=True)
    addr_dist = CharField(null=True)
    addr_id = AutoField()
    addr_info = CharField()
    addr_position = CharField(null=True)
    addr_prov = CharField(null=True)
    addr_remark = CharField(null=True)
    addr_status = CharField(null=True)
    addr_type = CharField(null=True)
    addr_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    house_number = CharField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField()
    user_label = IntegerField(null=True)
    user_lable = IntegerField(null=True)
    user_sex = IntegerField(null=True)
    zip_code = CharField(null=True)

    class Meta:
        table_name = 'um_user_addr'
        indexes = (
            (('user_id', 'pharmacy_id'), False),
        )

class UmUserCard(BaseModel):
    user__name = CharField()
    user_address = CharField(null=True)
    user_birthday = CharField(null=True)
    user_card_id = CharField(primary_key=True)
    user_sex = CharField(null=True)

    class Meta:
        table_name = 'um_user_card'

class UmUserDetails(BaseModel):
    cust_id = AutoField()
    email = CharField(null=True)
    gender = CharField(null=True)
    phone_num = CharField()
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    user_credit = IntegerField(null=True)
    user_from = CharField(null=True)
    user_id = IntegerField()
    user_json = CharField(null=True)
    user_logo = CharField(null=True)
    user_max_points = IntegerField(null=True)
    user_nick = CharField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'um_user_details'

class UmUserDevice(BaseModel):
    app_system = CharField()
    dev_create_time = DateTimeField(null=True)
    dev_id = AutoField()
    dev_remark = CharField(null=True)
    dev_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    device_num = CharField()
    phone_num = CharField()
    user_id = IntegerField(index=True)

    class Meta:
        table_name = 'um_user_device'

class UmUserDeviceNow(BaseModel):
    d_type = CharField(null=True)
    d_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    device_num = CharField(null=True)
    user_id = AutoField()

    class Meta:
        table_name = 'um_user_device_now'

class UmUserDrugstore(BaseModel):
    drugstore_id = IntegerField()
    link_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    link_id = AutoField()
    link_remark = CharField(null=True)
    link_type = CharField()
    link_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = IntegerField()

    class Meta:
        table_name = 'um_user_drugstore'

class UmUserInfo(BaseModel):
    company_id = IntegerField(null=True)
    cur_status = IntegerField()
    email = CharField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    phone_num = CharField(index=True)
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_birthday = DateField(null=True)
    user_create_time = DateTimeField(null=True)
    user_credit = IntegerField(null=True)
    user_device = CharField(null=True)
    user_device2 = CharField(null=True)
    user_from = CharField(index=True, null=True)
    user_head = IntegerField(null=True)
    user_id = AutoField()
    user_img = CharField(null=True)
    user_location = CharField(null=True)
    user_max_points = IntegerField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_sex = IntegerField(null=True)
    user_token = CharField(index=True, null=True)
    user_type = CharField()
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField(index=True)

    class Meta:
        table_name = 'um_user_info'
        indexes = (
            (('user_device', 'phone_num'), False),
        )

class UmUserInfoBak200305(BaseModel):
    company_id = IntegerField(null=True)
    cur_status = IntegerField()
    email = CharField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    phone_num = CharField(index=True)
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_birthday = DateField(null=True)
    user_create_time = DateTimeField(null=True)
    user_credit = IntegerField(null=True)
    user_device = CharField(null=True)
    user_device2 = CharField(null=True)
    user_from = CharField(index=True, null=True)
    user_head = IntegerField(null=True)
    user_id = AutoField()
    user_img = CharField(null=True)
    user_location = CharField(null=True)
    user_max_points = IntegerField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_sex = IntegerField(null=True)
    user_token = CharField(index=True, null=True)
    user_type = CharField()
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField(index=True)

    class Meta:
        table_name = 'um_user_info_bak200305'
        indexes = (
            (('user_device', 'phone_num'), False),
        )

class UmUserInfoExtend(BaseModel):
    from_channel = CharField(null=True)
    from_code = CharField(null=True)
    from_id = IntegerField(null=True)
    last_pharmacy_id = IntegerField(null=True)
    other1 = CharField(null=True)
    other2 = CharField(null=True)
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    user_position = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    userextend_id = AutoField()

    class Meta:
        table_name = 'um_user_info_extend'

class UmUserInfoXc(BaseModel):
    company_id = IntegerField(null=True)
    cur_status = IntegerField()
    email = CharField(null=True)
    gender = CharField(null=True)
    login_date = DateTimeField(null=True)
    password = CharField()
    phone_num = CharField(index=True)
    phone_num1 = CharField(null=True)
    phone_num2 = CharField(null=True)
    regist_date = DateTimeField(null=True)
    user_addr = IntegerField(null=True)
    user_area = CharField(null=True)
    user_bal = IntegerField(null=True)
    user_birthday = DateField(null=True)
    user_create_time = DateTimeField(null=True)
    user_credit = IntegerField(null=True)
    user_device = CharField(null=True)
    user_device2 = CharField(null=True)
    user_from = CharField(index=True, null=True)
    user_head = IntegerField(null=True)
    user_id = AutoField()
    user_img = CharField(null=True)
    user_location = CharField(null=True)
    user_max_points = IntegerField(null=True)
    user_points = IntegerField(null=True)
    user_remark = CharField(null=True)
    user_sex = IntegerField(null=True)
    user_token = CharField(index=True, null=True)
    user_type = CharField()
    user_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField(index=True)

    class Meta:
        table_name = 'um_user_info_xc'
        indexes = (
            (('user_device', 'phone_num'), False),
        )

class UmUserMark(BaseModel):
    mark_id = AutoField()
    mark_time = DateTimeField(null=True)
    mark_type = CharField()
    mk_create_time = DateTimeField(null=True)
    mk_remark = CharField(null=True)
    mk_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    pharmacy_id = IntegerField(null=True)
    user_id = IntegerField(index=True)
    value_id = IntegerField(index=True)

    class Meta:
        table_name = 'um_user_mark'

class UmUserStat(BaseModel):
    invite_act_id = IntegerField(null=True)
    invite_code = CharField(null=True)
    invite_pharmacy = IntegerField(null=True)
    invite_user = IntegerField(null=True)
    invite_user_type = CharField(null=True)
    remark = CharField(null=True)
    stat_create_time = DateTimeField(null=True)
    stat_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    user_from_channel = CharField(null=True)
    user_id = AutoField()
    user_login_time = DateTimeField(null=True)
    user_register_time = DateTimeField(null=True)
    user_register_type = CharField(null=True)

    class Meta:
        table_name = 'um_user_stat'

class UmUserStatPh(BaseModel):
    pharmacy_id = IntegerField()
    uph_id = AutoField()
    uph_link_time = DateTimeField(null=True)
    uph_type = CharField(null=True)
    user_id = IntegerField(index=True)

    class Meta:
        table_name = 'um_user_stat_ph'

class UmWechatBind(BaseModel):
    bind_create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    bind_id = AutoField()
    bind_remark = CharField(null=True)
    bind_status = IntegerField(null=True)
    bind_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    bind_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    pharmacy_id = IntegerField(null=True)
    pharmacy_uuid = CharField(null=True)
    user_phone = CharField()
    uuid = CharField()

    class Meta:
        table_name = 'um_wechat_bind'

class UmWxUser(BaseModel):
    city = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    country = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    create_time = DateTimeField(null=True)
    headimgurl = CharField(null=True)
    nickname = CharField(constraints=[SQL("DEFAULT '0'")])
    openid = CharField(constraints=[SQL("DEFAULT '0'")])
    phone = CharField(null=True)
    province = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    sex = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    unionid = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'um_wx_user'

class WxApplicationForm(BaseModel):
    city = CharField(null=True)
    create_time = DateTimeField(null=True)
    name = CharField(null=True)
    pharmacy = CharField(null=True)
    phone = CharField(null=True)
    province = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    wechat = CharField(null=True)

    class Meta:
        table_name = 'wx_application_form'

class Y1520(BaseModel):
    促销价_元_ = FloatField(column_name='促销价（元）', null=True)
    分类 = CharField(null=True)
    单位 = CharField(null=True)
    厂家 = CharField(null=True)
    原价_元_ = FloatField(column_name='原价（元）', null=True)
    品牌 = CharField(null=True)
    商品名 = CharField(null=True)
    数量 = FloatField(null=True)
    规格 = CharField(null=True)
    门店商品货号 = CharField(null=True)
    限订库存量 = FloatField(null=True)

    class Meta:
        table_name = 'y_1520'
        primary_key = False

class YjjDrugDetail(BaseModel):
    adverse_reactions = TextField(null=True)
    assist_matreial = CharField(null=True)
    clinical_trial = TextField(null=True)
    common_name = CharField(null=True)
    company_name = CharField(null=True)
    component = CharField(null=True)
    condition = CharField(null=True)
    contraindications = TextField(null=True)
    dosage = TextField(null=True)
    drug_id = AutoField()
    drug_interactions = TextField(null=True)
    format = CharField(null=True)
    indication = TextField(null=True)
    last_modify_time = DateTimeField(index=True, null=True)
    mechanism_action = TextField(null=True)
    molecular_weight = CharField(null=True)
    number = CharField(null=True)
    other = CharField(null=True)
    over_dosage = TextField(null=True)
    package = CharField(null=True)
    pharmacokinetics = TextField(null=True)
    precautions = TextField(null=True)
    prod_id = IntegerField(index=True, null=True)
    product_name = CharField(null=True)
    product_name_chem = CharField(null=True)
    product_name_en = CharField(null=True)
    product_name_py = CharField(null=True)
    publish_date = CharField(null=True)
    role_category = CharField(null=True)
    structural_formula = CharField(null=True)
    trait = CharField(null=True)
    use_in_children = TextField(null=True)
    use_in_elderly = TextField(null=True)
    user_in_preglact = TextField(null=True)
    yjj_id = CharField(unique=True)

    class Meta:
        table_name = 'yjj_drug_detail'

class ZztempPmProdSku(BaseModel):
    dir_code = CharField(null=True)
    dir_name = CharField(null=True)
    drugstore_id = IntegerField(index=True, null=True)
    prod_id = IntegerField(index=True, null=True)
    prod_name = CharField(null=True)
    sku_id = IntegerField(index=True)

    class Meta:
        table_name = 'zztemp_pm_prod_sku'
        primary_key = False

