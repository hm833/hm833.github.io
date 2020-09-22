1. `from aip import AipFace`
2. `from picamera import PiCamera`
3. `import urllib.request`
4. `import RPi.GPIO as GPIO`
5. `import base64`
6. `import time`
7. `#百度人脸识别API账号信息`
8. `APP_ID = '18333248'`
9. `API_KEY = 'HrfpWmTASGVQTGQ2UQO29IGY'`
10. `SECRET_KEY ='7x8m9vuKWH5XeVV8GeLkly8OkqUpzfPz'`
11. `client = AipFace(APP_ID, API_KEY, SECRET_KEY)#创建一个客户端用以访问百度云`
12. `#图像编码方式`
13. `IMAGE_TYPE='BASE64'`
14. `camera = PiCamera()#定义一个摄像头对象`
15. `#用户组`
16. `GROUP = 'yusheng01'`
17. 
18. `#照相函数`
19. `def getimage():`
20. `camera.resolution = (1024,768)#摄像界面为1024*768`
21. `camera.start_preview()#开始摄像`
22. `time.sleep(2)`
23. `camera.capture('faceimage.jpg')#拍照并保存`
24. `time.sleep(2)`
25. `#对图片的格式进行转换`
26. `def transimage():`
27. `f = open('faceimage.jpg','rb')`
28. `img = base64.b64encode(f.read())`
29. `return img`
30. `#上传到百度api进行人脸检测`
31. `def go_api(image):`
32. `result = client.search(str(image, 'utf-8'), IMAGE_TYPE, GROUP);#在百度云人脸库中寻找有没有匹配的人脸`
33. `if result['error_msg'] == 'SUCCESS':#如果成功了`
34. `name = result['result']['user_list'][0]['user_id']#获取名字`
35. `score = result['result']['user_list'][0]['score']#获取相似度`
36. `if score > 80:#如果相似度大于80`
37. `if name == 'yusheng_02':`
38. 
39. `print("欢迎%s !" % name)`
40. `time.sleep(3)`
41. `if name == 'xiaoming':`
42. `print("欢迎%s !" % name)`
43. `time.sleep(3)`
44. `if name == "xiaoyu":`
45. `print("欢迎%s !" % name)`
46. `else:`
47. `print("对不起，我不认识你！")`
48. `name = 'Unknow'`
49. `return 0`
50. `curren_time = time.asctime(time.localtime(time.time()))#获取当前时间`
51. 
52. `#将人员出入的记录保存到Log.txt中`
53. `f = open('Log.txt','a')`
54. `f.write("Person: " + name + "     " + "Time:" + str(curren_time)+'\n')`
55. `f.close()`
56. `return 1`
57. `if result['error_msg'] == 'pic not has face':`
58. `print('检测不到人脸')`
59. `time.sleep(2)`
60. `return 0`
61. `else:`
62. `print(result['error_code']+' ' + result['error_code'])`
63. `return 0`
64. `#主函数`
65. `if __name__ == '__main__':`
66. `while True:`
67. `print('准备')`
68. `if True:`
69. `getimage()#拍照`
70. `img = transimage()#转换照片格式`
71. `res = go_api(img)#将转换了格式的图片上传到百度云`
72. `if(res == 1):#是人脸库中的人`
73. `print("开门")`
74. `else:`
75. `print("关门")`
76. `print('稍等三秒进入下一个')`
77. `time.sleep(3)`
