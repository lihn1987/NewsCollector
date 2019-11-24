
import jieba
import mysql.connector
import db_base
from pyquery import PyQuery as pq
#初始化数据库
db_base.init_db("localhost", "root", "", "coin")


#初始化需要屏蔽的词
del_word_list = set(
    ['','的',' ','，',', ',',','<','>','p','/','\u3000','\t','。','和','、','；',';','"', '-', ':', '=','\n',
    '&','.','&#',"“","”","：",'\xa0','(','（',')','）',
    '在','是','了',
    's', 'g','br','span','quot','style','px','font','t','com','http','https','align','alt',
    'png','PNG','JPG','jpg']+
    ['将', '这', 
    '也', '有', '中', '一个', '会', '可以', '上', '对', '为', 
    '我们', '都', '不', '与',  '就', 
    'color', 'img', '%', '并', 'b', 'left', 'rgb', 'size', 
    '但', '年', '月', 'src', '可能', '到', '而', 
    '其', '更', '进行', '你', '我', '等', '或', '被',
    'margin', '_', '没有',  '多', '它', '日', '从', '？', '需要', 
    '来', '他们', '人', '通过', '该', 'height', 'box', 'letter', 'spacing', 
    '以', '这个', '这些', 
    'li', '如果','使用', '新', '目前', '已经', 
    '大', '就是', '还',  '提供', '去',  '于', 
    '一种', '表示', '很', '下', 'Emoji', '一', '他', 
    'h2', '—', '让', '个', '能', '其他',  
    '要', '因为', '说', '时','a', '!', 
    '高', '自己',  'cdn', '认为','center', '后', '一些', 
    '任何', 'sans', 'serif', '向', 'important',  
    '开始', 'sp', '很多', 'white', '由', '以及','所有', 'Sans', '做', 
    '获得', '不是', 
    '但是', '最', '方式', '这种', 'blockquote', '这样', 'S',  
    '区', '?', 'UI', 'class', '给', '成为', '能够', '现在']+
    ['#',
   'normal',
    'Arial',
     '情况', '地', '至', '主要', '作为', '用', 'border', 'sizing', '可', 'div', 
    '那么', 'e', '什么', '非常', '包括',   'article', '因此', '方面', '者', 'jpeg', '未来', '同时', 
    '对于', '所以', '正在', '不同', 
    'em',  'word', '由于',  '前', '其中', '基于', '重要', '所', '矿', 'F', '还是', 
    '如何', '存在', '不会', '解决', '则',  '之间',  '2em', 'Color', 
    'Symbols', 'Font', 'Symbol', '作者', '建议','right', '像', '较',  '继续', 
    '把', '已', '比',  '或者', '内',  '《', '》', '根据', '建立', '比如', 
    'wrap', 'book', '本文', 'wp', '人们', '线', '当', '整个', 
    '带来', '之后', '相关', '万', 'images', '及', 'title', '产生', '好', 
    '·', 'break', '应该', '时候', '着',  '无法', '具有', '观点', '小', 
    'webkit', '力', '一直', '机', '完全', '使','占', '来说', '「', 
    'x', 'inherit', '据', '」', '看', '直接', '选择', 'href', '每个', 
     '算', '那', '随着', '再', '构成', '进入', '其实', '之前', '低', '发生', '一样', '又', 
     '必须', '达到', '\r\n', '发现', '过','为了', '下降', '而且', '希望', 
         '运行', '称', '是否', '功能', '超过', '它们', 'cn', '当前', '还有', 'YaHei', '知道', 
         '并且', '原因',  '拥有',  '里', '出', '一定', '看到', '过程', 
         '亿', '甚至', '虽然', '网', '许多', '今日', 'lianxiangfiles', 'beijing', 'aliyuncs', 
         '要求', 'standard', 'width','方', '小时', '利用', '即', 'newsdetail', '之一', 
         'upload', 'A', '意味着',  '来看', '导致', '只', '想',
          '最大',  '越来越', '大量', '增长', 'background', 'ur', '公', '报告', '亦', 
          '最终', '形成', '支撑',  '自', '亿美元', '完成', '上线', '显示', '意见', '万美元', 'overflow', '持续', 
          '仍', '例如', '呢', '如', '单', 'ul', 'image3', '采用', '得到',
          '之', '大家', '+', '太', '更加', '才', '且', 'content', '过去', 'uploads', '不断',  '最近', '今年', 
          '化',  '进一步',  '每', '只是', '然而', '立场', '方法', '部分', '池', '了解', '公开',
           '处于', '绝不', '只有',  '以来',  '考虑', '不能',  '昨日', 
            '然后','允许',  '能力',  '两个', '越', '转发', 
            '1em',  '总', '核心', '投稿', '尽管', '位', '结果', 
            '从而',  '空', 'C',  '仍然', '！', '吗', '明显',  '安',  'amp', 
            '真正', '整体', '帮助', '钱', '微', '不过', '来自', '信', '类似', '量',
            '减少', '仓', '另', '用于', '比较', '程度', '预计', '有效', '关于', 'B', 'w', 
            '仅', 'editorimg', 'imageView2', 'q', 'system', '处理', '接受', '确保', '附近', '此外', 
            'www', '激励', '同样', '才能', '容易', '表现', 
            '受', '今天', '相对', '圈', '点', '本身', '那些', '除了', 
            '当然', '09', '一旦', '最后', '觉得',  '近', '上升', '使得', '性', '形式', '数', 
            '通', '实际上', '本', '一次', '周', '变得', '启动', '天', '表明', 
            '提出', '指出', '三', '得', '现有', 
            '起来', '约', '而是', '足够', '云', '证', '本周', '平均', '75em', 
            '一份', '先','跟', '以上', '们', '似乎', '大多数', 
            'bottom', '造成',  '正', '位置', '黑', '价', '跌', '一下', '却', '有关', '巨大', '首先', '此', 
            '受到', '流入',  '一点', '在于', '移动', '最高', 

            '推', '增大', 'gt', '面临', '难', '保证', '上周', '合成', '更好', '走', '按照', '一项','通常', '盘', 'PingFang',
              '只要', 'medium', '24H', '块', '发送', '谁', '张', '微软', 'Bi', 'image', '资本', '均', 
             '东西', '特别', '想要', '…', 'apple', 'G', '以下', '主', '多个', '即使', '很大', '属于', '限制',  
             'full', 'lt', '几个', '万元', '相比', '水平', '各', '依然', '共同', '更新', '知识', '第一', '而言', '类',  
             '％', '作用', '您', '解释', '没', '各种',  '未', '等待', '长期', '大幅', 
             '试图', '上方', '几乎', '相信', '广泛',
              '雅', '满足', '月份', '零', '具体', '值', '是因为', '此前','一家', 
               '锁', '无需', '涉及', '确实', '一部分', 'D', '做出', '大部分', '成立', 
               '尤其', '特定', '率', '一起', '图', '如此', '强', '分别', 'target', '这里', '左右', 
               '为主', '的话', '非', '多少'])
for i in range(10000):
    del_word_list.add(str(i))
#初始化需要定制的词语
add_word_list=set(['区块链', '矿池','DeFi','联盟链','NetCloth','交易所','数字交易所'])
db_coin_list = db_base.get_all_coin()
for db_coin_row in db_coin_list:
    for db_coin_item in db_coin_row:
        add_word_list.add(db_coin_item.upper())
add_word_list.remove('')


#获取所有文章内容
content_list = db_base.get_all_content()

for word in add_word_list:
    jieba.add_word(word.upper())
word_anylse = {}
#for i in range(len(content_list)):
for i in range(len(content_list)):
    word_list = jieba.cut(content_list[i][0], cut_all=False, HMM=False)
    for word in list(word_list):
        if word not in word_anylse:
            word_anylse[word.upper()] = 1
        else:
            word_anylse[word.upper()] +=1

    for word in del_word_list:
        try:
            del word_anylse[word.upper()]
        except :
            pass
    print(str(i)+"/"+str(len(content_list)))
#print(word_anylse)
a = sorted(word_anylse.items(), key=lambda x: x[1], reverse=True)
for_show = []
for x in range(10000):
    for_show.append(a[x][0])
    if a[x][1] < 100:
        break
print(for_show)
print(a[:200])
