
    欧氏距离
    标准化欧氏距离
    马氏距离
    夹角余弦距离
    汉明距离
    曼哈顿(Manhattan)距离






汉明距离是两个等长字符串之间的汉明距离是两个字符串对应位置的不同字符的个数。比如：
1011101 与 1001001 为 2
2143896 与 2233796 是 3
可以把它看做将一个字符串变换成另外一个字符串所需要替换的字符个数。
此外，汉明重量是字符串相对于同样长度的零字符串的汉明距离，如：
11101 的汉明重量是 4。
所以两者间的汉明距离等于它们汉明重量的差a-b


补充】协方差矩阵的逆Σ−1
Σ−1的求法：

先将Σ
Σ进行SVD分解(由于协方差矩阵是对称矩阵，因此此处严格说来是特征值分解EVD)。




