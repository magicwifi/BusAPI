# 司机侧


### 车辆运行: Post /api/update_driver

参数说明 

* name: 司机姓名（非空）  
* lat: 维度（非空）
* lng: 经度（非空）


测试程序 python update_driver.py James 50 50

返回值：

* {result：200} 调用成功
* {result：400} 调用失败



# 乘客侧 
 
### 创建预约: Post /reservations/register

参数说明 

* passenger_id: 乘客号（非空）  
* bus_number_id: 车次号（非空）
* site_id: 车站号（非空）


测试程序 python create_reservation.py  5  3  8

返回值：

* {result：200} 调用成功
* {result：400} 调用失败



### 签到: Post /takes/register

参数说明 

* passenger_id: 乘客号（非空）  
* bus_number_id: 车次号（非空）
* site_id: 车站号（非空）


测试程序 python create_takes.py  5  3 8

返回值：

* {result：200} 调用成功
* {result：400} 调用失败

### 获取车次位置信息: Get /fetchgps/:bus_number_id.json


参数说明 

* bus_number_id: 车次号（非空）



返回说明：
```javascript
{"code":"200", #返回成功
"result":{"lat":50.0, #纬度
"lng":50.0, #经度
"running":ture #该车的司机正在行驶
}
}
```
---


### 获取全部车次信息: Get /show_bus_all.json


返回说明：
```javascript
{"code":"200",
"bus_numbers":[ #线路信息
{"id":1,
"name":"线路七第一班", #名称
"bus_route_id":1,
"start_time":17, #发车时间
"created_at":"2016-04-16T11:15:50.000+08:00","updated_at":"2016-04-16T11:15:50.000+08:00",
"capacity":60} #容量

...

"drivers":[ #司机信息
{"lat":40.1345,
"lng":116.432,
"running":false,
"name":"huangzhe",
"bus_number_id":1},
...

"routes": #各站点信息
[{"bus_number_id":1,
"sites":["北京市芍药居地铁站","北京市望京西地铁站","北京市昌平区未来科技城鲁疃西路"]}
...

```
---

### 获取独立车次信息: Get /show_bus_detail/3.json

参数说明 

* bus_number_id: 车次号（非空）



返回说明：
```javascript
{"code":"200", #返回成功
,"bus_number": #车次信息
{"id":3,
"name":"线路五第一班",
"bus_route_id":2,
"start_time":17, #发车时间
"created_at":"2016-04-16T11:31:56.000+08:00",
"updated_at":"2016-04-16T11:31:56.000+08:00",
"capacity":60}," #可载客
driver": #司机信息
{"lat":50.0,"lng":50.0, #位置信息
"running":false,
"name":"James", #司机姓名
"bus_number_id":3},
"route": #路线信息
{"bus_number_id":3,
"sites": #各站信息
["北京市天通苑北地铁站","中国北京市昌平区七北路北七家王府街1号","北京市昌平区未来科技城鲁疃西路"]}

}
}
```
---




