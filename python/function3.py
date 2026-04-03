"""
定义一个函数，用于根据传入的一批信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
#优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价
#积分抵扣需要商品总金额满5000才能使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）
"""
#订单总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
def goods_info(*args, coupon, credit, express):
    good_price = [item[1] * item[2] for item in args]
    total_price = sum(good_price)
    if total_price >= 5000 and coupon <= total_price:
        total_price -= coupon
    if total_price >= 5000 and credit // 100 <= total_price:
        total_price -= credit // 100

    total_price += express

    return total_price

total = goods_info(("earpods", 699, 2), ("iPhone16", 5799, 1), coupon=1000, credit=2000, express=100)
print(total)
