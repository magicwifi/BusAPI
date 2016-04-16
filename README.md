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
