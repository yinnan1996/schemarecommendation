class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class MaterialTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def display(self):
        self._display_recursive(self.root, "")

    def _display_recursive(self, node, word):
        if node.is_end_of_word:
            print(word)

        for char, child_node in node.children.items():
            self._display_recursive(child_node, word + char)

# 创建Trie字典树
material_trie = MaterialTrie()

# 定义模式片段
patterns = [
    "材料分类",
    "材料基本信息",
    "化学式", "材料宏观形态", "材料制备方法", "实验得到", "参考文献",
    "结构", "晶体结构", "基本信息", "压强", "温度", "空间群", "群序号", "参考文献", "cif文件",
    "晶体结构相变", "a-T", "T", "a", "b-T", "T", "b", "c/sqrt2-T", "T", "c/sqrt2", "c",
    "V-T", "T", "V",
    "磁性", "变温磁化强度/磁化率/磁矩曲线", "磁结构转变", "奈耳温度/居里温度", "奈耳温度", "居里温度",
    "相变原理", "M-T/χ-T/m-T", "M-T", "T", "M", "M的单位", "X（当选择μB/(X site)时）", "晶向（各向异性）",
    "χ-T", "T", "χ", "χ的单位", "X（当选择μB/(X site)时）", "晶向（各向异性）", "m-T", "T", "m", "晶向（各向异性）",
    "实验条件（备注）", "测量方法", "参考文献",
    "磁化强度-磁场强度曲线", "M-H", "H", "M", "H的单位", "M的单位", "X（当选择μB/(X site)时）", "温度", "晶向（各向异性）",
    "实验条件（备注）", "测量方法", "参考文献",
    "光学特性", "热致变色", "透射率/反射率", "透射率-λ", "λ", "透射率", "温度",
    "反射率-λ", "λ", "反射率", "温度",
    "实验条件（备注）", "测量方法", "参考文献",
    "红外伪装", "发射率-λ", "λ", "发射率", "温度",
    "实验条件（备注）", "测量方法", "参考文献"
]

# 插入模式片段到Trie树中
for pattern in patterns:
    material_trie.insert(pattern)

material_trie.display()

# 输出Trie树构建完成
print("Trie字典树构建完成！")
print(material_trie)

pattern_to_search = "基本信息"
result = material_trie.search(pattern_to_search)

if result:
    print(f"模式片段 '{pattern_to_search}' 存在于MaterialTrie中。")
else:
    print(f"模式片段 '{pattern_to_search}' 不存在于MaterialTrie中。")