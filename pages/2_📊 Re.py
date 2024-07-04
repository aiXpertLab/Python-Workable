import streamlit as st, re
from utils import st_def, tab_db, tab_re
st_def.st_logo(title = "👋 Regular Expression")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["General", "extract email", "mySQL-Oracle", "Mongo", "PostgreQL"])

with tab1:  tab_re.db_general()

with tab1:
    st.image('images/re1.png', use_column_width=True)

    st.markdown('''
    In the mid-1960s, computer science pioneer Ken Thompson, one of the original designers of Unix, implemented pattern matching in the QED text editor using Kleene’s notation. Since then, regexes have appeared in many programming languages, editors, and other tools as a means of determining whether a string matches a specified pattern. Python, Java, and Perl all support regex functionality, as do most Unix tools and many text editors.''')
    st.image('images/re2.png', use_column_width=True)

    st.code("""
            验证输入用户名和QQ号是否有效并给出对应的提示信息
            要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
            
            def main():
                username = input('请输入用户名: ')
                qq = input('请输入QQ号: ')
                # match函数的第一个参数是正则表达式字符串或正则表达式对象
                # 第二个参数是要跟正则表达式做匹配的字符串对象
                m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
                if not m1:
                    print('请输入有效的用户名.')
                m2 = re.match(r'^[1-9]\d{4,11}$', qq)
                if not m2:
                    print('请输入有效的QQ号.')
                if m1 and m2:
                    print('你输入的信息是有效的!')
            
        """)

    st.code("""
            
            例子2：从一段文字中提取出国内手机号码。
    def main():
        # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
        pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
        sentence = '''
        重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
        不是15600998765，也是110或119，王大锤的手机号才是15600998765。
        '''
        # 查找所有匹配并保存到一个列表中
        mylist = re.findall(pattern, sentence)
        print(mylist)
        print('--------华丽的分隔线--------')
        # 通过迭代器取出匹配对象并获得匹配的内容
        for temp in pattern.finditer(sentence):
            print(temp.group())
        print('--------华丽的分隔线--------')
        # 通过search函数指定搜索位置找出所有匹配
        m = pattern.search(sentence)
        while m:
            print(m.group())
            m = pattern.search(sentence, m.end())
    
    
    def main():
        sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
        purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                        '*', sentence, flags=re.IGNORECASE)
        print(purified)  # 你丫是*吗? 我*你大爷的. * you.
    
    
    
    def main():
        poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
        sentence_list = re.split(r'[，。, .]', poem)
        while '' in sentence_list:
            sentence_list.remove('')
        print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
    
    
    pattern = re.compile(r"[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)")
    
    strs = '我的私人邮箱是zhuwjwh@outlook.com，公司邮箱是123456@qq.org，麻烦登记一下？'
    result = pattern.findall(strs)
    
    print(result)
    ['zhuwjwh@outlook.com', '123456@qq.org']


    pattern = re.compile(r"[1-9]\d{5}(?:18|19|(?:[23]\d))\d{2}(?:(?:0[1-9])|(?:10|11|12))(?:(?:[0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]")
    
    strs = '小明的身份证号码是342623198910235163，手机号是13987692110'
    result = pattern.findall(strs)
    
    print(result)
    ['342623198910235163']



    pattern = re.compile(r"(?:(?:http:\/\/)|(?:https:\/\/))?(?:[\w](?:[\w\-]{0,61}[\w])?\.)+[a-zA-Z]{2,6}(?:\/)")
    
    strs = 'Python官网的网址是https://www.python.org/'
    result = pattern.findall(strs)
    
    print(result)
    ['https://www.python.org/']



    验证数字：^[0-9]*$
    验证n位的数字：^\d{n}$
    验证至少n位数字：^\d{n,}$
    验证m-n位的数字：^\d{m,n}$
    验证零和非零开头的数字：^(0|[1-9][0-9]*)$
    验证有两位小数的正实数：^[0-9]+(.[0-9]{2})?$
    验证有1-3位小数的正实数：^[0-9]+(.[0-9]{1,3})?$
    验证非零的正整数：^\+?[1-9][0-9]*$
    验证非零的负整数：^\-[1-9][0-9]*$
    验证非负整数（正整数 + 0） ^\d+$
    验证非正整数（负整数 + 0） ^((-\d+)|(0+))$
    整数：^-?\d+$
    非负浮点数（正浮点数 + 0）：^\d+(\.\d+)?$
    正浮点数 ^(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*))$
    非正浮点数（负浮点数 + 0） ^((-\d+(\.\d+)?)|(0+(\.0+)?))$
    负浮点数 ^(-(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*)))$
    浮点数 ^(-?\d+)(\.\d+)?$



    英文和数字：^[A-Za-z0-9]+$ 或 ^[A-Za-z0-9]{4,40}$
    长度为3-20的所有字符：^.{3,20}$
    由26个英文字母组成的字符串：^[A-Za-z]+$
    由26个大写英文字母组成的字符串：^[A-Z]+$
    由26个小写英文字母组成的字符串：^[a-z]+$
    由数字和26个英文字母组成的字符串：^[A-Za-z0-9]+$
    由数字、26个英文字母或者下划线组成的字符串：^\w+$ 或 ^\w{3,20}$
    中文、英文、数字包括下划线：^[\u4E00-\u9FA5A-Za-z0-9_]+$
    中文、英文、数字但不包括下划线等符号：^[\u4E00-\u9FA5A-Za-z0-9]+$ 或 ^[\u4E00-\u9FA5A-Za-z0-9]{2,20}$
    可以输入含有^%&',;=?$\”等字符：`[^%&',;=?$\x22]+`
    禁止输入含有~的字符：[^~\x22]+
        
                
            """)