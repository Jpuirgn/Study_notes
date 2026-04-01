'''
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储
商品数据，通过控制台菜单与用户交互。具体功能如下：
'''
goods_dict = {}

#1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
def add_goods():
    name = input("输入商品名称：")
    price = float(input("输入商品价格："))
    counts = int(input("输入商品数量："))
    if name in goods_dict:
        print("商品已存在，请重新选择")
    else:
        goods_info = (price, counts)
        goods_dict[name] = goods_info
    print("商品添加完成！")
    print(goods_dict)

#2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
def change_goods():
    change_name = input("输入要修改的购物车商品名称：")
    if change_name not in goods_dict:
        print("商品不存在，请重新选择")
    else:
        change_price = float(input("输入要修改的购物车商品价格："))
        change_counts = float(input("输入要修改的购物车商品数量："))
        goods_info = (change_price, change_counts)
        goods_dict[change_name] = goods_info
        print("信息修改完成！")
        print(goods_dict)
#3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
def delete_goods():
    del_name = input("要删除的商品名称：")
    if del_name not in goods_dict:
        print("商品不存在，请重新选择")
    else:
        goods_dict.pop(del_name)
    print("商品删除完成！")
    print(goods_dict)
#4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxxx, 商品价格：xxxx, 商品数量：xx"。
def search_goods():
    for key, value in goods_dict.items():
        print(f"商品名称: {key}\t商品价格: {value[0]}\t商品数量: {value[1]}")

#5.退出购物车。
def quit_goods():
    exit()

running = True
while running:
    print("1.添加商品")
    print("2.修改商品价格和数量")
    print("3.删除商品")
    print("4.查询商品")
    print("5.退出购物车")
    print()
    option = int(input("选择功能: "))
    print()
    if option == 1:
        add_goods()
    elif option == 2:
        change_goods()
    elif option == 3:
        delete_goods()
    elif option == 4:
        search_goods()
    elif option == 5:
        quit_goods()
