# iConference 模板版 v10

题目：Mapping Technological Knowledge Evolution in Chinese Universities

## 使用哪个文件

- `main.tex` / `main.pdf`：会议篇幅主稿，22 页，包含全部七个主体章节、6 幅图位、5 张结果表和 58 条参考文献。
- `extended.tex` / `extended.pdf`：完整扩展稿，36 页，保留 v9 的详细论证、数学定义、验证设计，以及附录 A–C。扩展稿超过会议字数上限，供研究修改和补充材料整理使用。
- `complete.tex`：完整扩展稿的合并源码，正文、图表和 BibTeX 数据均在一个文件中；仍须使用本包的 `Font/` 和 `Images/` 目录。
- `references.bib`：两版共用的 58 条参考文献；采用 biblatex-apa 与 Biber。
- `main_body.tex`、`extended_body.tex`：两版正文；`figures/` 和 `tables/`：共享图表源码。
- `REFERENCE_CHECK.md`：沿用上一版文献元数据核验记录。

## 编译

将 ZIP 整体上传至 Overleaf，编译器选择 **XeLaTeX**，主文件选择 `main.tex`；查看完整稿时改为 `extended.tex`。请保留字体和图片目录。

本地需安装 XeLaTeX、Biber、biblatex-apa 和常用 LaTeX 宏包。运行 `python build.py` 可依次编译主稿与扩展稿。也可对每个主文件执行：

```sh
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

本次实际验证使用 XeLaTeX、biblatex 3.22、biblatex-apa 与 Biber 2.22。不要用 BibTeX 替代 Biber。包内 PDF 已编译，无需安装环境即可阅读。编译脚本仅生成论文 PDF，不是专利数据分析程序。

## 模板依据和调整

依据 iConference 官方 Full Research Papers 页面提供的 Information Research LaTeX 模板：
https://www.ischools.org/full-papers

官方下载包：
https://www.ischools.org/_files/archives/39c5e8_db71948077e449feba92a4c85d51ec0e.zip

- A4 单栏，12 磅 Lora，四周 1 英寸、底部 35 毫米。
- 深绿色、无编号章节标题；保留官方页脚、刊期和 DOI 待编辑占位。
- 结构化摘要使用 Introduction、Method、Analysis、Results、Conclusion；正文 159 词，不含五个标签。
- 初次匿名稿不放作者姓名和单位。
- 图注、表注和表格正文为 9 磅，图表标题置于下方；主文表格使用黑色表头。
- 参考文献改为 APA 7，保留引文及 DOI/URL 链接。
- 论文标题压缩为两行；删除模板教学示例、作者说明和红色模板使用说明。未改变官方字体、行距和页脚。原始模板另存于 `official_template_original.tex`。

最终主稿从首页至参考文献之前，连同图表、图注和数学符号附近文本，按 PDF 英文词元估计约 5,100 词；这个较宽口径也低于 6,000 词。投稿系统的分词口径可能略有差异。扩展稿不用于代替限字主稿。

## 数据状态

当前收到的材料没有可运行的高校专利原始数据库或经核验的实证输出。因此 Table 1–5 中的数值仍为 TBD；Figure 3–6 是明确标记的分析展示规格，不是已计算的实证图。Figure 1–2 为可编辑 TikZ 框架图。不得将这些占位内容解释为研究发现。

本次工作完成格式转换与篇幅整理，不代表稿件已经满足投稿的实证和内容要求。官方关于 AI 使用的要求见上述指南；最终投稿内容与声明应由作者核查。
