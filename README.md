# 对外接口（写操作） 
 
### 创建预约: Post /reservations/take

参数说明 

* passenger_id: 乘客号（非空）  
* bus_number_id: 车次号（非空）


测试程序 python create_reservation.py  5  3
五号乘客预约3号车次

返回值：

* {result：200} 调用成功
* {result：400} 调用失败



### 签到: Post /takes/doctors

参数说明 

* passenger_id: 乘客号（非空）  
* bus_number_id: 车次号（非空）


测试程序 python create_takes.py  5  3
五号乘客登上3号车次

返回值：

* {result：200} 调用成功
* {result：400} 调用失败

