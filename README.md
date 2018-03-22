# Bilibili 爬虫相关

## 参考资料

- [B站API收集整理及开发](https://github.com/Vespa314/bilibili-api)
- [Bilibili API (For thrid-party) Documents 哔哩哔哩开放接口第三方文档](https://github.com/fython/BilibiliAPIDocs)

## 可用 Web API

### 1. 视频搜索

```python
base_url = 'https://s.search.bilibili.com/cate/search'
params = {
        'main_ver': 'v3',
        'search_type': 'video',
        'view_type': 'hot_rank',
        'order': 'click',
        'copy_right': -1,
        'cate_id': 25,
        'page': page,
        'pagesize': pagesize,
        'time_from': 20171218,
        'time_to': 20180321
}
```

### 2. 单个视频信息

```python
base_url = 'http://api.bilibili.com/archive_stat/stat'
params = {
    'aid': '20987509'
}
```

response example:

```json
{
    "code": 0,
    "data": {
        "aid": 20987509,
        "view": 143963,
        "danmaku": 806,
        "reply": 777,
        "favorite": 5969,
        "coin": 12564,
        "share": 2365,
        "now_rank": 0,
        "his_rank": 49,
        "like": 3870,
        "no_reprint": 1,
        "copyright": 1
    },
    "message": "0",
    "ttl": 1
}
```

### 3. 单个视频tag信息

```python
base_url = 'https://api.bilibili.com/x/tag/archive/tags'
params = {
    'aid': '20987509'
}
```

### 4. 单个视频描述

```python
base_url = 'https://api.bilibili.com/x/web-interface/archive/desc'
params = {
    'aid': '20987509'
}
```

response example:

```json
{
    "code": 0,
    "message": "0",
    "ttl": 1,
    "data": "视频类型: 其他\n相关题材: 紫罗兰永恒花园 & 魔法少女小圆\n简介: 自制\n当JOJO 和 京紫 和 魔圆 三部番剧产生碰撞会怎么样？\n哈哈哈哈~"
}
```

### 5. 第三方的单个视频信息

```url
http://www.bilibilijj.com/Api/AvToCid/{Av}/{P}
```

example：[http://www.bilibilijj.com/Api/AvToCid/10086](http://www.bilibilijj.com/Api/AvToCid/10086)