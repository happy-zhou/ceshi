from selenium import webdriver   #相当于使用selenium库里面的一个模块


driver=webdriver.chrome(r'F:\chrom\chromedriver_win32\chromedriver.exe')      
#告知浏览器驱动的地址,dirver是webdriver的实例对象，这个对象类似于一个遥控器
driver.get('http://www.51job.com')   #打开51job网站
    #driver.input('python')，这种输入的话无法知道是在哪里输入，因为有很多输入框

ele=driver.find_element_by_id('jcnjdsmsdlv')    
#告诉浏览器寻找ID为jcnjdsmsdlv的元素，在HTML中，每一个搜索框都是对应的元素,再赋值给具体的对象ele
ele.send_keys('python')    #发送搜索的关键字Python

ele=driver.find_element_by_id('work_position_input')    
#告诉浏览器寻找ID为work_position_input的元素，即工作地点,再赋值给具体的对象ele
ele.click('') 


