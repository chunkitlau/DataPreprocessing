<div class="cover" style="page-break-after:always;font-family:方正公文仿宋;width:100%;height:100%;border:none;margin: 0 auto;text-align:center;">
    </br></br></br>
    <div style="width:70%;margin: 0 auto;height:0;padding-bottom:10%;">
        </br>
        <img src="buptname.png" alt="校名" style="width:100%;"/>
    </div>
    </br></br></br></br>
    <span style="font-family:华文黑体Bold;text-align:center;font-size:25pt;margin: 10pt auto;line-height:30pt;">实验报告</span>
    </br></br>
    <div style="width:20%;margin: 0 auto;height:0;padding-bottom:30%;">
        <img src="buptseal.png" alt="校徽" style="width:100%;"/>
	</div>
    </br>
    <table style="border:none;text-align:center;width:80%;font-family:仿宋;font-size:24px; margin: 0 auto;">
    <tbody style="font-family:方正公文仿宋;font-size:20pt;">
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">题　　目</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"> 数据预处理实验报告</td>     </tr>
    </tbody>              
    </table>
	</br></br></br>
    <table style="border:none;text-align:center;width:72%;font-family:仿宋;font-size:14px; margin: 0 auto;">
    <tbody style="font-family:方正公文仿宋;font-size:12pt;">
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">课程名称</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"> Python程序设计</td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">上课学期</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"> 2021春</td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">授课教师</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">杨亚 </td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">姓　　名</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"></td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">学　　号</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"></td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">日　　期</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">2021年12月1日</td>     </tr>
    </tbody>              
    </table>
	</br></br></br></br></br>
</div>

<!-- 注释语句：导出PDF时会在这里分页 -->

# 目录

[TOC]

## 通过爬虫爬取链家的新房数据，并进行预处理。

### 实验内容

　　通过爬虫爬取链家的新房数据，并进行预处理，目标网页：https://bj.fang.lianjia.com/loupan/

- 最终的 csv 文件，应包括以下字段：名称，地理位置（ 3 个字段分别存储），房型（只保留最小房型），面积（按照最小值），总价（万元，整数），均价（万元，保留小数点后 4 位）；
- 对于所有字符串字段，要求去掉所有的前后空格；
- 如果有缺失数据，不用填充。
- 找出总价最贵和最便宜的房子，以及总价的中位数
- 找出单价最贵和最便宜的房子，以及单价的中位数

### 实验步骤

#### 配置环境

​		使用 conda 创建一个 Python 3.8 环境并激活该环境。

​		在终端输入```conda install -c conda-forge scrapy```安装 scrapy 库。

​		使用 cd 命令进入项目根目录，在终端输入```scrapy startproject lianjia```创建链家爬虫项目。

#### 创建主运行文件

​		使用 Visual Studio Code 打开该项目，在该目录下创建一个 begin.py 文件（与 scrapy.cfg 在同一级目录下）内容如下：

```
from scrapy import cmdline
cmdline.execute("scrapy crawl lianjia".split())
# lianjia 为爬虫的名字，在 spider.py 中定义
```

#### 创建 Item 类

​		修改 items.py 文件：调用 scrapy.Field() 方法，从 scrapy 提取出 name、location1、location2、location3、type、 area、totalPrice和 avgPrice 八个参数作为 Item 类的成员变量。

```
import scrapy

class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    location1 = scrapy.Field()
    location2 = scrapy.Field()
    location3 = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    totalPrice = scrapy.Field()
    avgPrice = scrapy.Field()
    pass
```

#### 编写 Spider 爬虫类、请求和解析方法

​		新建一个 spider.py 文件（在 spider 目录下），设置允许的域名和目标 url 集合。

```
from sys import exec_prefix
import scrapy
from lianjia.items import MyItem # 从 items.py 中引入 MyItem 对象

class mySpider(scrapy.spiders.Spider):
    name = "lianjia" # 爬虫的名字是 lianjia
    allowed_domains = ["bj.lianjia.com/"] # 允许爬取的网站域名
    url_format = "https://bj.fang.lianjia.com/loupan/pg{}/" # URL 格式 ，即爬虫爬取的 URL 格式
    start_urls = []
    for page in range(1, 23):
        start_urls.append(url_format.format(page))
```

​		在 spider.py 文件中的 calss mySpider 中，添加 parse 函数，从响应中提取出楼盘的名称、位置、房型、面积、均价和总价，将提取出的信息形成一个 Item 类返回。对于所有字符串字段，使用 strip 函数去掉所有的前后空格，对于缺失数据，不用填充。如果给出均价则计算总价，如果给出总价则计算均价。

```
	def parse(self, response):
        item = MyItem()
        for each in response.xpath("/html/body/div[3]/ul[2]/li"):
            if each.xpath("div/div[1]/a/text()"):
                item['name'] = each.xpath("div/div[1]/a/text()").extract()[0].strip() # 名称
            if each.xpath("div/div[2]/span[1]/text()"):
                item['location1'] = each.xpath("div/div[2]/span[1]/text()").extract()[0].strip() # 位置1
            if each.xpath("div/div[2]/span[2]/text()"):
                item['location2'] = each.xpath("div/div[2]/span[2]/text()").extract()[0].strip() # 位置2
            if each.xpath("div/div[2]/a/text()"):
                item['location3'] = each.xpath("div/div[2]/a/text()").extract()[0].strip() # 位置3
            if each.xpath("div/a/span[1]/text()"):
                item['type'] = each.xpath("div/a/span[1]/text()").extract()[0].strip() # 房型
            if each.xpath("div/div[3]/span/text()"):
                item['area'] = each.xpath("div/div[3]/span/text()").extract()[0].split(' ')[1] # 面积
                if item['area'].find('-') != -1:
                    item['area'] = int(item['area'].split('-')[0])
                else:
                    item['area'] = int(item['area'].split('㎡')[0])
            if each.xpath("div/div[6]/div[1]/span[1]/text()"):
                if each.xpath("div/div[6]/div[1]/span[2]/text()").extract()[0].find('均价') != -1:
                    item['avgPrice'] = "%.4f" % (int(each.xpath("div/div[6]/div[1]/span[1]/text()").extract()[0]) / 10000.0) # 均价
                    item['totalPrice'] = "%.4f" % (item['area'] * float(item['avgPrice'])) # 总价
                if each.xpath("div/div[6]/div[1]/span[2]/text()").extract()[0].find('总价') != -1:
                    item['totalPrice'] = each.xpath("div/div[6]/div[1]/span[1]/text()").extract()[0]
                    if item['totalPrice'].find('-') == -1:
                        item['totalPrice'] = "%.4f" % (int(item['totalPrice'])) # 均价
                    else:
                        item['totalPrice'] = "%.4f" % (int(item['totalPrice'].split('-')[0])) # 均价
                    item['avgPrice'] = "%.4f" % (float(item['totalPrice']) / item['area']) # 总价
            yield(item)
```

#### 编写 Pipeline 类、数据保存方法

​		修改 pipelines.py，使用 UTF-8 格式以写模式打开 csv 文件并设置不换行，创建写字典类实例来将字典写到 csv 文件，处理数据时使用写字典类实例方法来将数据项写到文件中。

```
from itemadapter import ItemAdapter
import csv

class MyPipeline(object):
    labels = ['name', 'location1', 'location2', 'location3', 'type', 'area', 'avgPrice', 'totalPrice']
    
    def open_spider(self, spider):
        try: # 打开 csv 文件
            self.file = open('MyData.csv', "w", encoding="utf-8", newline='')
            self.writer = csv.DictWriter(self.file, fieldnames=self.labels)
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        self.writer.writerow(item) # 将条目写入到文件中
        return item

    def close_spider(self, spider):
        self.file.close() # 关闭文件
```

​		修改 setting.py，添加反反爬虫设置。

```
BOT_NAME = 'lianjia'
SPIDER_MODULES = ['lianjia.spiders']
NEWSPIDER_MODULE = 'lianjia.spiders'
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 60
COOKIES_ENABLED = False
ITEM_PIPELINES = {
    'lianjia.pipelines.MyPipeline': 300,
}
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
```

​		运行 begin.py

​		或者运行 spider.py ，并将其运行时的 Script path 配置项修改为 begin.py

### 获取的 CSV 文件：MyData.csv

​		获取到 173 条课程信息，其中前 50 条信息如下：

```
和光悦府,朝阳,朝阳其它,南皋路和光悦府,4室,120,8.8000,1056.0000
水岸壹号,房山,良乡,良乡大学城西站地铁南侧800米，刺猬河旁,3室,185,5.8000,1073.0000
观唐云鼎,密云,溪翁庄镇,溪翁庄镇密溪路39号院（云佛山度假村对面）,3室,172,3.0000,516.0000
运河铭著,通州,北关,商通大道与榆东一街交叉口，温榆河森林公园东500米,2室,100,4.9000,490.0000
万年广阳郡九号,房山,长阳,长阳清苑南街与汇商东路交汇处西北角,3室,166,5.0000,830.0000
首开璞瑅公馆,丰台,方庄,紫芳园五区,3室,203,10.6000,2151.8000
华远裘马四季,门头沟,大峪,增产路16号院,3室,156,5.5000,858.0000
御汤山熙园,昌平,昌平其它,北京市昌平区小汤山镇顺沙路99号院,4室,300,4.0000,1200.0000
华远和墅,大兴,南中轴机场商务区,南六环磁各庄桥沿南中轴向南2公里,5室,295,5.4000,1593.0000
天资华府,房山,长阳,房山区CSD政务大厅5号门,3室,115,3.8000,437.0000
檀香府,门头沟,门头沟其它,京潭大街与潭柘十街交叉口,3室,208,4.5000,936.0000
韩建·观山源墅,房山,良乡,阳光北大街与多宝路交汇处西南（理工大学北校区西侧）,3室,290,4.0000,1160.0000
首城汇景墅,平谷,平谷其它,"金河北街6号院, 金河北街8号院",3室,360,2.5000,900.0000
中国铁建花语金郡,大兴,瀛海,南海子公园西侧(南五环旧忠桥向南第二个红绿灯西300米),3室,150,7.0000,1050.0000
北辰墅院1900,顺义,马坡,顺兴街11号院望尊园,4室,251,4.2000,1054.2000
首创天阅西山,海淀,海淀北部新区,海淀区丰秀东路9号院，永丰路与北清路交汇处东北角，中关村壹号北侧,4室,175,8.0000,1400.0000
翡翠公园,昌平,北七家,北七家京承高速北七家出口向西3公里，七星路与七北路交汇处,4室,98,6.1000,597.8000
北科建泰禾丽春湖院子,昌平,沙河,中关村北延新核心，沙河水库边（地铁昌平线沙河站向南800米）,4室,379,5.0000,1895.0000
绿地海珀云翡,大兴,大兴其它,兴亦路京开高速东侧（黄村镇第一中心小学对面）,2室,102,6.5000,663.0000
都丽华府,平谷,平谷其它,新平南路与林荫南街交汇处向西100米,2室,94,2.9000,272.6000
中粮京西祥云,房山,长阳,地铁稻田站北800米，西邻京深路,4室,115,5.8000,667.0000
燕西华府,丰台,丰台其它,"王佐镇青龙湖公园东1500米,",4室,60,4.2000,252.0000
水岸壹号,房山,良乡,良乡大学城西站地铁南侧800米，刺猬河旁,3室,122,4.3000,524.6000
紫辰院,丰台,岳各庄,岳各庄北桥东北角200米处,5室,266,12.8000,3404.8000
鲁能格拉斯小镇,通州,通州其它,北京市通州区宋庄镇格拉斯小镇营销中心,3室,246,6.0000,1476.0000
兴创荣墅,大兴,大兴新机场洋房别墅区,北京市大兴区育胜街,3室,240,2.3000,552.0000
温哥华森林,昌平,北七家,"北五环外紧邻立汤路，北七家建材城向北第一个路口200米路东, 枫树家园6区, 枫树家园五区",4室,460,4.3478,1999.9880
润泽御府,朝阳,北苑,北京市朝阳区北五环顾家庄桥向北约2.6公里,4室,540,11.0000,5940.0000
中骏西山天璟,门头沟,城子,西山永定楼北300米,4室,117,6.5000,760.5000
炫立方,顺义,顺义其它,金关北二路2号院,4室,117,3.0000,351.0000
国瑞熙墅,昌平,北七家,北七家镇岭上西路与定泗路交汇处东南角,3室,314,4.8000,1507.2000
中冶德贤公馆,大兴,旧宫,德贤东路6号院（南四环榴乡桥东南角800米）,0室,134,7.7000,1031.8000
燕西华府,丰台,丰台其它,"王佐镇青龙湖公园东1500米, 泉湖西路1号院（七区）, 泉湖西路1号院（六区）",0室,195,5.2000,1014.0000
京西悦府,房山,阎村,燕房线阎村地铁站东南角约189米,3室,120,3.3000,396.0000
首创伊林郡,房山,良乡,京港澳高速22B良乡机场出口即到，行宫西街1号院,2室,81,3.6500,295.6500
K2十里春风,通州,通州其它,永乐店镇漷小路百菜玛工业园对面,2室,74,2.4500,181.3000
K2十里春风,通州,通州其它,永乐店镇漷小路百菜玛工业园对面,2室,155,2.8000,434.0000
奥园雲水院,密云,溪翁庄镇,溪翁庄镇,3室,120,2.5000,300.0000
北京城建·龙樾西山,门头沟,冯村,长安街西延线南约300米,4室,118,4.8000,566.4000
远洋新天地,门头沟,上岸地铁,长安街西延线与滨河路南延交汇处（东南侧）,1室,1118,2.5000,2795.0000
长海御墅,房山,房山其它,长沟国家湿地公园南侧,3室,224,2.3000,515.2000
棠颂璟庐,亦庄开发区,亦庄开发区其它,鹿华路7号院（南海子公园北侧500米）,4室,250,7.5000,1875.0000
金隅上城郡,昌平,北七家,北亚花园东路50米,4室,212,4.5000,954.0000
万科弗农小镇,密云,溪翁庄镇,密关路西侧（密云水库南岸2公里）,3室,140,2.5000,350.0000
首开保利欢乐大都汇,门头沟,冯村,石门营环岛北50米,3室,140,6.5000,910.0000
中铁华侨城和园,大兴,瀛海,南五环南海子公园西侧约500米,3室,154,6.0000,924.0000
顺鑫颐和天璟,顺义,顺义其它,新城右堤路与昌金路交汇处向北200米,3室,110,3.3000,363.0000
誉天下盛寓,顺义,中央别墅区,中央别墅区榆阳路与林荫路交叉口,3室,120,6.0000,720.0000
泰禾金府大院,丰台,西红门,南四环地铁新宫站南800米,2室,175,8.2000,1435.0000
奥园雲水院,密云,溪翁庄镇,密云区Y753(走石路),3室,111,2.2000,244.2000

```

### 分析爬取到的数据

- 找出总价最贵和最便宜的房子，以及总价的中位数
- 找出单价最贵和最便宜的房子，以及单价的中位数

​		使用 pandas 库，读入 CSV 文件称 dataframe 类，使用索引和 idxmax 与 idmin 方法找到最大值和最小值所在的房子，使用索引和 median 找出中位数。最后将统计结果输出。

​		可以发现总价最高为 8755.6 万，最低为 105.0 万，中位数为 554.4 万。均价最高为 16.7 万每平米，最低为 1.5 万每平米，中位数为 4.6 万每平米。

```
Max Total Price: 
name                        北京壹号总部
location1                       大兴
location2                       亦庄
location3     台湖镇光机电一体化产业基地科创东二街5号
type                            1室
area                          3127
avgPrice                       2.8
totalPrice                  8755.6
Name: 138, dtype: object
Min Total Price:
name                长海御墅
location1             房山
location2           房山其它
location3     长沟国家湿地公园南侧
type                  1室
area                  70
avgPrice             1.5
totalPrice         105.0
Name: 147, dtype: object
Median Total Price:
554.4
Max Avg Price:
name                     北京庄园
location1                  顺义
location2                顺义其它
location3     京承高速第11出口往东800米
type                       4室
area                      460
avgPrice                 16.7
totalPrice             7682.0
Name: 129, dtype: object
Min Avg Price:
name                长海御墅
location1             房山
location2           房山其它
location3     长沟国家湿地公园南侧
type                  1室
area                  70
avgPrice             1.5
totalPrice         105.0
Name: 147, dtype: object
Median Avg Price:
4.6
```

### 源程序

#### begin.py

```
from scrapy import cmdline
cmdline.execute("scrapy crawl lianjia".split())
# lianjia 为爬虫的名字，在 spider.py 中定义
```

#### spider.py

```
from sys import exec_prefix
import scrapy
from lianjia.items import MyItem # 从 items.py 中引入 MyItem 对象

class mySpider(scrapy.spiders.Spider):
    name = "lianjia" # 爬虫的名字是 lianjia
    allowed_domains = ["bj.lianjia.com/"] # 允许爬取的网站域名
    url_format = "https://bj.fang.lianjia.com/loupan/pg{}/" # URL 格式 ，即爬虫爬取的 URL 格式
    start_urls = []
    for page in range(1, 23):
        start_urls.append(url_format.format(page))

    def parse(self, response):
        item = MyItem()
        for each in response.xpath("/html/body/div[3]/ul[2]/li"):
            if each.xpath("div/div[1]/a/text()"):
                item['name'] = each.xpath("div/div[1]/a/text()").extract()[0].strip() # 名称
            if each.xpath("div/div[2]/span[1]/text()"):
                item['location1'] = each.xpath("div/div[2]/span[1]/text()").extract()[0].strip() # 位置1
            if each.xpath("div/div[2]/span[2]/text()"):
                item['location2'] = each.xpath("div/div[2]/span[2]/text()").extract()[0].strip() # 位置2
            if each.xpath("div/div[2]/a/text()"):
                item['location3'] = each.xpath("div/div[2]/a/text()").extract()[0].strip() # 位置3
            if each.xpath("div/a/span[1]/text()"):
                item['type'] = each.xpath("div/a/span[1]/text()").extract()[0].strip() # 房型
            if each.xpath("div/div[3]/span/text()"):
                item['area'] = each.xpath("div/div[3]/span/text()").extract()[0].split(' ')[1] # 面积
                if item['area'].find('-') != -1:
                    item['area'] = int(item['area'].split('-')[0])
                else:
                    item['area'] = int(item['area'].split('㎡')[0])
            if each.xpath("div/div[6]/div[1]/span[1]/text()"):
                if each.xpath("div/div[6]/div[1]/span[2]/text()").extract()[0].find('均价') != -1:
                    item['avgPrice'] = "%.4f" % (int(each.xpath("div/div[6]/div[1]/span[1]/text()").extract()[0]) / 10000.0) # 均价
                    item['totalPrice'] = "%.4f" % (item['area'] * float(item['avgPrice'])) # 总价
                if each.xpath("div/div[6]/div[1]/span[2]/text()").extract()[0].find('总价') != -1:
                    item['totalPrice'] = each.xpath("div/div[6]/div[1]/span[1]/text()").extract()[0]
                    if item['totalPrice'].find('-') == -1:
                        item['totalPrice'] = "%.4f" % (int(item['totalPrice'])) # 均价
                    else:
                        item['totalPrice'] = "%.4f" % (int(item['totalPrice'].split('-')[0])) # 均价
                    item['avgPrice'] = "%.4f" % (float(item['totalPrice']) / item['area']) # 总价
            yield(item)
```

#### items.py

```
import scrapy

class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    location1 = scrapy.Field()
    location2 = scrapy.Field()
    location3 = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    totalPrice = scrapy.Field()
    avgPrice = scrapy.Field()
    pass
```

#### pipeline.py

```
from itemadapter import ItemAdapter
import csv

class MyPipeline(object):
    labels = ['name', 'location1', 'location2', 'location3', 'type', 'area', 'avgPrice', 'totalPrice']
    
    def open_spider(self, spider):
        try: # 打开 csv 文件
            self.file = open('MyData.csv', "w", encoding="utf-8", newline='')
            self.writer = csv.DictWriter(self.file, fieldnames=self.labels)
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        self.writer.writerow(item) # 将条目写入到文件中
        return item

    def close_spider(self, spider):
        self.file.close() # 关闭文件
```

#### settings.py

```python
BOT_NAME = 'lianjia'

SPIDER_MODULES = ['lianjia.spiders']
NEWSPIDER_MODULE = 'lianjia.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lianjia (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 60
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lianjia.middlewares.LianjiaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lianjia.middlewares.LianjiaDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'lianjia.pipelines.MyPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

```

#### statistics.py

```
import pandas as pd
df = pd.read_csv('MyData.csv')

maxTotalPriceId = df["totalPrice"].idxmax()
maxTotalPriceRow = df.iloc[maxTotalPriceId,:]

minTotalPriceId = df["totalPrice"].idxmin()
minTotalPriceRow = df.iloc[minTotalPriceId,:]

medianTotalPrice = df["totalPrice"].median()

maxAvgPriceId = df["avgPrice"].idxmax()
maxAvgPriceRow = df.iloc[maxAvgPriceId,:]

minAvgPriceId = df["avgPrice"].idxmin()
minAvgPriceRow = df.iloc[minAvgPriceId,:]

medianAvgPrice = df["avgPrice"].median()

print("Max Total Price: ")
print(maxTotalPriceRow)
print("Min Total Price: ")
print(minTotalPriceRow)
print("Median Total Price: ")
print(medianTotalPrice)
print("Max Avg Price: ")
print(maxAvgPriceRow)
print("Min Avg Price: ")
print(minAvgPriceRow)
print("Median Avg Price: ")
print(medianAvgPrice)
```

## 计算北京空气质量数据

### 实验内容

　　计算北京空气质量数据，目标网页：保存到 csv 文件中。

#### 汇总计算 PM 指数年平均值的变化情况

#### 汇总计算 10 - 15 年 PM 指数和温度月平均数据的变化情况

- No: 行号
- year: 年份
- month: 月份
- day: 日期
- hour: 小时
- season: 季节
- PM: PM2.5 浓度 (ug/m^3)
- DEWP: 露点 ( 摄氏温度 ) 指在固定气压之下，空气中所含的气态水达到饱和而凝结成液态水所需要降至的温度。
- TEMP: Temperature ( 摄氏温度 )
- HUMI: 湿度 ( % )
- PRES: 气压 ( hPa )c
- cbwd : 组合风向
- Iws : 累计风速 (m/s)
- precipitation: 降水量/时 (mm)
- Iprec : 累计降水量 (mm) mm

### 实验步骤

#### 配置环境

​		使用 conda 创建一个 Python 3.8 环境并激活该环境。

​		在终端输入```conda install pandas```安装 pandas 库。

​		在终端输入```conda install -c conda-forge matplotlib```安装 matplotlib 库。

#### 导入库和文件

​		创建源代码文件 BeijingAirQuality.py，导入 pandas 库，打开输出文件，导入数据文件成为 dataframe 类。

```
import pandas as pd
log = open('log.txt','w')
df = pd.read_csv('BeijingPM20100101_20151231.csv')
```

#### 汇总计算 PM 指数年平均值的变化情况

​		使用 groupby 方法按年分组统计，使用 agg 方法统计每年的 PM 指数平均值，再使用 mean 方法统计各 PM 指数的平均值。将统计结果输出到终端和输出文件，并绘图可视化。

```
df_year_PM = df.groupby('year').agg({'PM_Dongsi':'mean','PM_Dongsihuan':'mean','PM_Nongzhanguan':'mean','PM_US Post':'mean'})
df_year_PM["PM_avg"] = df_year_PM.mean(axis=1)
print(df_year_PM["PM_avg"])
log.write(df_year_PM["PM_avg"].to_string())
df_year_PM[["PM_avg"]].plot()
```

​		总的来说 PM 指数年平均值呈下降趋势，结果如下：

![](C:\Users\chunk\Documents\Repositories\DataPreprocessing\output1.png)

```
year
2010    104.045730
2011     99.093240
2012     90.538768
2013     94.364640
2014     92.356073
2015     86.434236
```

#### 汇总计算 10 - 15 年 PM 指数月平均数据的变化情况

​		使用 groupby 方法按年月分组统计，使用 agg 方法统计每月的 PM 指数平均值，再使用 mean 方法统计各 PM 指数的平均值。将统计结果输出到终端和输出文件，并绘图可视化。

```
df_month_PM = df.groupby(['year','month']).agg({'PM_Dongsi':'mean','PM_Dongsihuan':'mean','PM_Nongzhanguan':'mean','PM_US Post':'mean'})
df_month_PM["PM_avg"] = df_month_PM.mean(axis=1)
print(df_month_PM["PM_avg"])
log.write(df_month_PM["PM_avg"].to_string())
df_month_PM[["PM_avg"]].plot()
```

​		总的来说 PM 指数月平均值在震荡过程中呈下降趋势，结果如下：

![](C:\Users\chunk\Documents\Repositories\DataPreprocessing\output2.png)

```
year  month
2010  1         90.403670
      2         97.239940
      3         94.046544
      4         80.072423
      5         87.071913
      6        109.038938
      7        123.426075
      8         97.683432
      9        122.792735
      10       118.784367
      11       138.384036
      12        97.115747
2011  1         44.873700
      2        150.290179
      3         57.991987
      4         91.720670
      5         65.108146
      6        108.794655
      7        107.386486
      8        103.733800
      9         94.969402
      10       145.556818
      11       109.434965
      12       108.721400
2012  1        118.922388
      2         84.442029
      3         96.474324
      4         87.835883
      5         90.966715
      6         96.634181
      7         80.649709
      8         81.165329
      9         59.952247
      10        94.951351
      11        87.436963
      12       109.187296
2013  1        187.363566
      2        113.895498
      3        117.536968
      4         62.803477
      5         88.818390
      6        111.131018
      7         75.244688
      8         67.162611
      9         84.690537
      10       102.012920
      11        85.184422
      12        91.702244
2014  1        108.653207
      2        151.672827
      3        102.682987
      4         91.947651
      5         64.607826
      6         59.322455
      7         92.509858
      8         65.671778
      9         68.471039
      10       134.600703
      11       104.125174
      12        72.926404
2015  1        110.467642
      2        104.543512
      3         95.153210
      4         79.101396
      5         61.303962
      6         60.158753
      7         60.597316
      8         50.459379
      9         51.686172
      10        66.984238
      11       114.448834
      12       167.646073
```

#### 汇总计算 10 - 15 年温度月平均数据的变化情况

​		使用 groupby 方法按年月分组统计，使用 agg 方法统计每月的温度平均值，将统计结果输出到终端和输出文件并绘图可视化。

```
df_month_TEMP = df.groupby(['year','month']).agg({'TEMP':'mean'})
print(df_month_TEMP)
log.write(df_month_TEMP.to_string())
df_month_TEMP.plot()
```

​		总的来说温度月平均值呈周期上升下降趋势，结果如下：

![](C:\Users\chunk\Documents\Repositories\DataPreprocessing\output3.png)

```
TEMP
year month           
2010 1      -6.162634
     2      -1.922619
     3       3.293011
     4      10.806944
     5      20.831989
     6      24.434722
     7      27.729839
     8      25.611559
     9      20.213889
     10     12.299731
     11      3.609722
     12     -2.064516
2011 1      -5.553763
     2      -0.854167
     3       7.068548
     4      14.605556
     5      20.713710
     6      25.648611
     7      26.469086
     8      25.758065
     9      19.231944
     10     13.209677
     11      5.980556
     12     -2.302419
2012 1      -4.758065
     2      -2.511494
     3       5.072581
     4      15.473611
     5      21.896505
     6      24.337500
     7      26.657258
     8      25.373656
     9      20.088889
     10     13.317204
     11      3.641667
     12     -5.408602
2013 1      -5.377688
     2      -1.821429
     3       5.405914
     4      12.248611
     5      21.455645
     6      23.677778
     7      27.086022
     8      26.571237
     9      20.125000
     10     12.821237
     11      5.913889
     12     -0.293011
2014 1      -0.913978
     2      -0.702381
     3       9.564516
     4      16.844444
     5      21.612903
     6      24.833333
     7      28.044355
     8      25.801075
     9      20.504167
     10     13.341398
     11      5.676389
     12     -1.419355
2015 1      -1.326613
     2       0.941964
     3       8.265141
     4      15.538889
     5      21.493280
     6      24.674548
     7      26.567204
     8      25.829071
     9      20.408333
     10     13.827957
     11      2.897079
     12     -0.617766
```

#### 总结

​		 PM 指数年平均值呈下降趋势。

​		 PM 指数月平均值在震荡过程中呈下降趋势。

​		温度月平均值呈周期上升下降趋势。

### 源程序

#### BeijingAirQuality.py

```python
#%%
import pandas as pd
log = open('log.txt','w')
df = pd.read_csv('BeijingPM20100101_20151231.csv')
df_year_PM = df.groupby('year').agg({'PM_Dongsi':'mean','PM_Dongsihuan':'mean','PM_Nongzhanguan':'mean','PM_US Post':'mean'})
df_year_PM["PM_avg"] = df_year_PM.mean(axis=1)
print(df_year_PM["PM_avg"])
log.write(df_year_PM["PM_avg"].to_string())
df_year_PM[["PM_avg"]].plot()

df_month_PM = df.groupby(['year','month']).agg({'PM_Dongsi':'mean','PM_Dongsihuan':'mean','PM_Nongzhanguan':'mean','PM_US Post':'mean'})
df_month_PM["PM_avg"] = df_month_PM.mean(axis=1)
print(df_month_PM["PM_avg"])
log.write(df_month_PM["PM_avg"].to_string())
df_month_PM[["PM_avg"]].plot()

df_month_TEMP = df.groupby(['year','month']).agg({'TEMP':'mean'})
print(df_month_TEMP)
log.write(df_month_TEMP.to_string())
df_month_TEMP.plot()
# %%
```

## 结语

​		使用 Python 语言的 scrapy 库可以比较容易地从互联网上爬取我们需要的数据，爬取的过程中使用 xpath 对 html 标签进行定位和提取，最后将爬取到的数据保存在 CSV 文件中。爬取的时候，对于不同的数据我们需要使用判断语句对不同的情况进行处理，通过计算得到我们需要的值。使用 pandas 库可以比较容易地处理 CSV 文件，对数据进行分组统计并进行可视化。通过本次实验，初步掌握了多种数据预处理的方法。
