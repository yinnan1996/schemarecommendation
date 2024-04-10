import re

def extract_chinese_words_from_quotes(file_path):
    chinese_words = set()  # 用集合来存储中文词，确保不重复

    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        # 使用正则表达式匹配引号中的中文词
        chinese_matches = re.findall(r'["“”](.*?)["“”]', data)
        # 提取中文词，并加入集合中
        for match in chinese_matches:
            chinese_words.add(match)

    return chinese_words

file_path = 'example.txt'  # 你的txt文件路径
chinese_words = extract_chinese_words_from_quotes(file_path)
print("提取的中文词：", chinese_words)
