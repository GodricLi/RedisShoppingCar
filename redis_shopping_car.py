# _*_ coding=utf-8 _*_
import json
import redis, json
from redistest.redis_pool import POOL

conn = redis.Redis(connection_pool=POOL)
"""
结构：
# shopping_car_用户id_商品id作为key
{
	"shopping_car_6_11":{
        "title":"从入门到放弃",
        "price":666,
	    },
	"shopping_car_6_12":{
	    "title":"从入门到放弃",
	    "price":666,},
}

"""
# conn.flushall()  # 清空
# redis_key = "shopping_car_%s_%s" % (10, 15)
# data_produce = json.dumps({"title": "21天入门到放弃", "price": 99, })
# print(type(data_produce))
# 添加商品
# conn.hmset(redis_key, data_produce)

# 删除商品
# conn.delete("shopping_car_6_13")

# 修改商品
# conn.hset("shopping_car_6_15", "price", 66)
# print(conn.hget("shopping_car_6_15", "price"))

# 查看所有商品
# print(conn.keys("shopping_car_6_*"))
# for item in conn.scan_iter("shopping_car_6_*", count=10):
#     course = conn.hgetall(item)
#     print(type(course))
# print(conn.keys())

# 查看商品信息
# data = conn.hget(redis_key, 'title')
# data = conn.hgetall(redis_key)

# data = conn.hgetall("Payment_1_1")
# print(data)
