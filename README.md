# 人人影视网爬虫

采集人人影视网和字幕库所有的数据，采集的数据可以建一个影视资源站。

使用scrapy-redis组件实现了Scrapy分布式架构,Redis作为消息队列,MongoDB储存数据,防止服务器宕机,增加了MongoDB群集功能。

数据流向:

- 调度器向Redis消息队列请求第一个Request,然后传给下载器

- 下载器将获取到的Response传给爬虫,爬虫对其进行解析,将数据打包为Item传给RedisPipeline,将新的Request传给Redis消息队列

- RedisPipeline将Item传给pipelines,pipelines对数据进行清洗,储存

# Linux系统安装项目过程

开发环境:

Ubuntu:16.04 LST

Redis:4.0.2

MongoDB:3.2.17

### 安装Redis

```
$ wget http://download.redis.io/releases/redis-4.0.2.tar.gz
$ tar xzf redis-3.2.5.tar.gz
$ cd redis-3.2.5
$ make
$ sudo make install
```

### 启动Redis服务

```
$ redis-server
```

### 安装MongoDB

```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
$ echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
```

### 启动MongoDB集群服务

```
# 用两个终端窗口启动两个MongoDB服务
$ mongod --dbpath ~/mongodb/master/data --replSet repset
$ mongod --dbpath ~/mongodb/slave/data --port 27018 --replSet repset

# 再打开一个窗口启动MongoDB群集服务
$ mongo
$ use admin
$ config = { _id:"repset", members:[
  {_id:0,host:" 127.0.0.1:27017"},
  {_id:1,host:" 127.0.0.1:27018"},]
  }
$ rs.initiate(config)
# 查看节点信息
$ rs.status()
```

# 配置settings.py文件，如果上传到服务器使用，请修改文件中以下配置

### Redis数据库的连接信息

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

### 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复
SCHEDULER_PERSIST = True

### 使用本地scrapy-redis-bloomfilter去重方式的去重队列信息，Redis数据库的连接信息
FILTER_URL = None
FILTER_HOST = 'localhost'
FILTER_PORT = 6379
FILTER_DB = 0
SCHEDULER_QUEUE_CLASS = 'renrenyingshi.scrapy_redis.queue.SpiderPriorityQueue'

### 阿布云隧道代理的账号密码，启用随机代理中间件才有效
PROXY_USER_PASSWOED = 'HP1II6G9LCCN6PMD:F1D1F5D43E06B603'

#### MongoDB数据库配置
MONGO_URI = 'mongodb://127.0.0.1:27017,127.0.0.1:27018'
MONGO_DATABASE='renren'
REPLICASET = 'repset'

# TO-DO

- 完成对影视信息的采集功能 [√]

- 完成对影视下载链接的采集功能 []

- 使用HTTP隧道代替普通代理IP [√]

- 增加字幕库网的字幕采集功能 [√]
