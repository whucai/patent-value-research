# 绘制中国高校技术知识演化图谱

**期刊**：Information Research - Vol. ?? No. ? (20??)

**DOI**：保持原样，将由期刊创建

---

## 摘要

**引言。** 专利产出相当的高校，其技术知识的来源、组合与传承方式可能截然不同。专利计数无法体现这种差异，而专利文献中记录的关系则可以。本研究提出一个框架，将中国高校专利视为带日期的关系性文献，并追踪制度性知识结构的变迁。

**方法。** 三类关系层——IPC 分类、标题—摘要文本和引用——保持分离。四个过程维度（获取、重组、涌现，以及在可观测引用者中的再利用）描述一个高校—时段画像，每个维度以其可被观测的时间窗标注日期。转型则独立评估，作为高校技术构成的持续性变化，并与一个高校内部的原假设（null）进行检验。

**分析。** 固定布局的技术图谱配合分时段叠加、经数量和领域调整的画像分布，以及有序轨迹配合转型检验，共同构成分析。该设计明确指出仅含高校的专利与引用语料库能够支持哪些测度，并将再利用深度和全经济范围的扩散排除在主要论断之外。

**结果。** 本文给出可操作化定义与报告设计；源数据库尚未分析，因此没有任何画像值、轨迹计数或转型事件作为发现被报告。

**结论。** 该框架将知识组织和专利图谱与纵向制度分析联系起来，同时使每一项推断都可追溯至支撑它的专利关系以及可用数据的边界。

---

## 引言

专利数量相同的两所高校，其专利可能源自不同的知识过程：一所依赖狭窄的外部知识来源并对一个既有核心加以精炼；另一所则连接那些很少同时出现的技术要素，并随后被自身领域之外的组织所再利用。专利计数和引用记录了两所机构的产出，却未记录二者之间的差异（Griliches, 1990; Hall et al., 2005; Nagaoka et al., 2010）。因此，要理解制度性知识结构如何变迁，就需要将专利作为关系性文献来阅读——将其与分类、文本、在先参考文献、在后引用记录以及日期联系起来——而非仅仅作为可计数的单位。

信息科学早已以这种方式处理文献。文献耦合和共被引分析用以识别思想联系（Kessler, 1963; Price, 1965; Small, 1973）；知识图谱用以表征领域及其随时间的变化（Börner et al., 2003; Chen, 2006; van Eck & Waltman, 2010）；专利叠加地图将这些方法延伸至技术领域（Kay et al., 2014; Leydesdorff et al., 2014; Rafols et al., 2010; Yan & Luo, 2017）。所缺少的是一种从图谱——展示一所机构在某一时刻所处位置——走向轨迹的方法，后者展示其知识关系如何变化，以及这种变化是否超过了抽样和测量噪声。

本文针对中国高校专利提出这样一种联结。核心思路很简单。不同类型的专利关系——共享分类、文本邻近性和引用——表达不同的知识关系，并在不同时间变得可观测。将它们保持分离、并各自标注日期，就有可能用四个过程维度来描述一所机构，这些维度在一项发明公开时或公开后不久即可观测（外部知识获取、技术要素重组、早期涌现和有记录的再利用），并独立地以该机构跨期技术构成的持续性变化来评估结构性转型。两个研究问题是：

**RQ1.** 如何从专利关系中测量获取、重组、涌现和再利用，使每一维度保留各自的含义和各自的观测时间？

**RQ2.** 在考虑专利数量、技术构成和覆盖范围之后，一个仅含高校的专利与引用语料库支持哪些高校知识画像和轨迹？

其贡献在于知识组织与纵向制度分析之间一个可追溯的联结：每一个画像值和每一条轨迹陈述都可以追溯至带日期的专利记录以及支撑它的具体关系。本文规定了框架、测度和报告设计，并明确指出仅含高校的语料库能支持和不能支持的部分。实证值尚待计算；下文不主张任何发现。

---

## 相关工作

专利是知识生产的选择性记录。并非所有发明都申请了专利，质量参差不齐，且法律与组织策略会影响记录（Griliches, 1990; Nagaoka et al., 2010）。引用尤须谨慎：审查员添加的参考文献削弱了将其解读为发明者学习的依据（Alcácer & Gittelman, 2006），而知识溢出的估计则取决于技术控制和比较组（Jaffe et al., 1993; Thompson & Fox-Kean, 2005）。因此，本文将专利视为带有日期关系、有文献记录的技术对象，而非发明的完整历史。

专利图谱中使用三类关系。分类系统组织技术类别（Leydesdorff, 2008）；文本揭示共享分类号所遗漏的相似性（Kelly et al., 2021; Sarica et al., 2020; Whalen et al., 2020）；引用记录来源和后续使用。叠加地图将组织置于一个共同的知识空间中（Kay et al., 2014; Rafols et al., 2010），关联性研究将该空间中的位置与进入和退出联系起来（Kogler et al., 2013; Rigby, 2015）。然而，布局变动可能源于样本或算法的改变，而非知识的变化。本研究保持视觉坐标固定，并在底层分布中测量变化。

过程词汇来自创新研究。吸收能力涉及对外部知识的识别和利用（W. M. Cohen & Levinthal, 1990）；探索与利用（March, 1991）以及搜索深度和搜索范围（Katila & Ahuja, 2002）描述学习取向；组合式发明和非常规组合研究促使将不寻常的连接与其后续影响分开测量（Fleming, 2001; Uzzi et al., 2013; Verhoeven et al., 2016; Wang et al., 2017; Youn et al., 2015）。涌现不止于新颖性：其属性包括增长、连贯性、影响和不确定性（Rotolo et al., 2015），科学计量方法将其中的子集操作化（Small et al., 2014）。首次被引与后续累积携带不同的时间信息（Huang et al., 2019）。多层网络研究表明，为何异质关系不应被合并为单一邻接矩阵（Boccaletti et al., 2014; Kivela et al., 2014）。本框架借鉴这些来源，但提出了更窄的主张：专利参考文献标示有记录的来源，而非能力；罕见分类号对标示不寻常组合，而非有用性；后续引用记录标示有界的再利用，而非学习。

---

## 框架：关系、时间与转型

技术知识演化在此被定义为一所机构技术知识在来源、组合、被认可的方向和有记录的再利用方面的变化，以及该知识组织方式的持续性变化。专利是可观测的对象；高校是这些对象积累和连接的情境。不赋予任何专利或机构一种内在的发展类型。

图 1 展示了该设计。四个维度描述一个高校—时段画像，

$$\mathbf{x}_{ut} = (A_{ut}, R_{ut}, E_{ut}, D_{ut})^{T}, \quad (1)$$

其中 $A$（获取）和 $R$（重组）在发明公开时即可观测，$E$（涌现）以当前队列对照其自身的历史参考来度量，$D$（再利用）需要一个固定的后续追踪时间窗。转型 $T_{u,t\to t+1}$ 不是第五个输入。它是一个跨期统计量，作用于技术类别和对的分布，以自身的原假设单独评估。将 $T$ 置于画像之外，可避免一种循环解读：用未来的结构性变化描述一个状态，然后声称该状态解释了这一变化。

由此得出两条时间规则。第一，每个维度以其确定它的最早观测日期标注，且没有任何指标使用其自身观测窗口之后才公开的信息。第二，某一时期的一个画像是一个状态，而非一条轨迹；轨迹陈述需要同一机构的有序画像，以及观测变化超过一个高校内部原假设的证据。

四类解释性轨迹类别作为假设被保留，以待这些可观测量检验，而非作为被强加的类别。维持路径显示一个稳定的技术核心（低 $T$，无持续的覆盖范围增长）。扩展路径显示在稀有子类覆盖范围上持续增长而无异常配对。重组路径显示反复出现的高 $R$，并有新要素连接的文本证据支撑。转型路径要求 $T$ 在一次过渡中高于其原假设，且新组合在下一时期持续。一所机构在不同时间可遵循不同类别，混合情形保持可见，且这些类别不构成绩效排名。

> **图 1.** 框架。四个过程维度被置于其可观测的时间，并取自不同的专利关系；转型是一个独立的跨期统计量，而非第五个输入。没有任何箭头表示因果效应或强制阶段。

---

## 数据与可观测关系

### 语料库及其边界

预期的来源是本课题组关于中国高校专利及其引用记录的数据库。表 1 列出在分析前必须审计的覆盖项目。其各行决定了框架中哪些关系是可观测的，因而属于设计本身的一部分，而非一种形式手续。

主要队列由已公开的中国发明专利申请构成，要求在首次公开时至少有一个高校申请人，不论后续授权状态如何；实用新型和外观设计被排除在外。机构覆盖范围由一份带日期的高校名录定义，历史名称、合并和附属医院通过具有时间特异性的联结加以解决；模糊匹配保持可审计，而非被静默指派。一个申请的公开版本和授权版本被合并。若家族标识符可用，发明单位是以其最早合格文献为代表的简单族；否则为单位去重后的申请，并对此加以声明。一项有 $m_p$ 个高校申请人的专利对每个申请人贡献 $\omega_{up}=1/m_p$；全额计数作为一种敏感性分析。

仅含高校语料库的三个性质约束了设计，并在此声明而非留待日后发现。(i) 高校专利的向后引用是可观测的，但被引文献自身的属性只有在被引记录本身处于语料库中、或其分类号被携带在引用字段中时才可用。(ii) 指向高校专利的向前引用是可观测的；引用文献的申请人只有在引用记录携带申请人字段时才可观测，而引用文献自身的向前链接通常不可得。因此，超出一步引用之外的再利用深度被排除在主要测度之外。(iii) 中国发明专利在首年获得的向前引用很少，故任何以早期认可为条件的指标对大多数记录都为零。因此，涌现以一种不依赖认可的早期信息形式测量，而以认可型变体作为次要测度。

| 覆盖项目 | 取值 | 所需定义或审计 |
|---|---|---|
| 数据库/提供者；抽取日期 | TBD | 冻结的来源与查询清单 |
| 检索日期；分析日期 | TBD | 首次公开队列；成熟截止日期 |
| 名录机构；关联机构 | TBD | 带日期的名录和名称对照表 |
| 原始公开记录 | TBD | 公开/申请去重前 |
| 合格发明单位 | TBD | 家族，或家族不可得时的申请 |
| 合格高校—时段 | TBD | 三年不重叠队列 |
| IPC 子类和主组 | TBD | 版本协调后的词表规模 |
| 可用标题/摘要记录 | TBD | 数量和覆盖百分比 |
| 向后引用链接 | TBD | 已解析的在先公开发明单位 |
| $H$ 内的向前引用链接 | TBD | 唯一家族对，范围已声明 |
| 外部引用组织 | TBD | 仅高校或更广覆盖 |
| 按原因排除的单位 | TBD | 互斥的首次失败计数 |

> **表 1.** 数据集规模与覆盖范围，待从冻结的源数据库计算。本表中没有任何值或日期范围是实证估计。

### 观测时间

首次公开是主时钟。$W_t = [b_t, b_{t+1})$ 是一个不重叠的三年队列，$B_t = [b_t - 3, b_t)$ 是其历史参考；再利用使用 $H = 5$ 年的时间窗。成熟画像要求 $b_{t+1} + H \le d_{\text{extract}}$，且缺乏完整历史参考的队列被排除。由此留下的成熟队列数是数据库的一个属性，将在表 1 中报告；若连续成熟队列不足三个，轨迹分析仅限于描述，转型检验被报告为不可行而非近似。

一个高校—时段进入画像分析，须至少有 20 项归属发明，且各维度所需字段的可用归属质量至少达 80%。确认缺失引用记为零；不可用字段记为缺失，且绝不进入分母。对于维度 $j$，合格子集为 $P_{ut}^{j}$，质量为

$$M_{ut}^{j} = \sum_{p \in P_{ut}^{j}} \omega_{up},$$

以占总质量的份额报告。

### 三类关系层

图 2 展示了语料库如何被分解。技术层以 IPC 主组为节点，通过分数共现链接，

$$w_{ij}^{(t)} = \sum_{p \in W_t: m_p^{C} \geq 2} \frac{I\{i, j \in C_p\}}{\binom{m_p^{C}}{2}}, \quad i < j, \quad (2)$$

其中 $C_p$ 是专利 $p$ 上不同主组的集合；每项多编码发明贡献一个单位的对质量。语义层以专利为节点，通过归一化标题和摘要的字符 2–4-gram TF–IDF 向量的余弦相似度链接，词表和 IDF 仅在 $B_t$ 上拟合（特征出现在至少 5 篇且至多 80% 的参考文献中，上限 100,000；对数 TF、平滑 IDF、L2 归一化）。引用层以专利为节点，有向边从被引文献指向引用文献，重复家族对合并、族内链接移除，且要求引用文献的公开严格晚于被引文献。申请人重叠的自引用被排除在主要再利用图之外。一项专利—IPC 关联关系联结各层；它们的邻接矩阵绝不求和。显示图（归一化边、top-10 邻居并集；互为 15 近邻的语义图；Leiden 社区，Traag et al., 2019）跨期使用固定坐标；所有指标使用未剪枝的权重。

> **图 2.** 数据到推断的工作流。三类关系层在到达画像之前保持分离；转型仅从技术层跨期计算。

---

## 测度

### 获取

令 $q_{ut}$ 为至少含一条已解析外部向后引用的有效发明的归属份额，$\pi_{ut,k}$ 为这些引用在一个固定、版本协调的、规模为 $K_t$ 的 IPC 子类词表上的分数分布。则

$$A_{ut} = q_{ut} \frac{1}{2} + \frac{1}{2} \left[ \frac{1 - \sum_{k} \pi_{ut,k} \log \pi_{ut,k}}{\log K_t} \right], \quad (3)$$

使得确认无外部来源时 $A = 0$，而正的基线将狭窄来源与无来源区分开来。两个分量分别报告。$A$ 测度有记录的来源触及范围和多样性（Shannon, 1948; Stirling, 2007），而非吸收能力（W. M. Cohen & Levinthal, 1990）。

### 重组

令 $c_{ij,t}^{-}$ 为 $B_t$ 中主组 $(i, j)$ 的历史分数对质量，$Q_t$ 为预设词表中可能的对数，$C_t = \sum_{i<j} c_{ij,t}^{-} > 0$。取 $\alpha = 1/2$，

$$p_{ij,t}^{-} = \frac{c_{ij,t}^{-} + \alpha}{C_t + \alpha Q_t}, \quad r_{ij,t} = \frac{-\log p_{ij,t}^{-}}{-\log\{\alpha/(C_t + \alpha Q_t)\}}, \quad (4)$$

$$R_{ut} = \frac{1}{M_{ut}^{R}} \sum_{p \in P_{ut}^{R}} \omega_{up} \frac{\sum_{(i,j) \in L_p} r_{ij,t}}{|L_p|}, \quad (5)$$

其中 $L_p$ 是专利 $p$ 上有效的已映射对集合。未解析的分类号映射到一个记录的词外类别；无有效对的专利记为缺失，而非零。稀有性标示不寻常组合，而非新颖性或有用性（Fleming, 2001; Verhoeven et al., 2016; Youn et al., 2015）。首次出现对率和专利—IPC 关联的保度置换提供互补检验。

### 涌现

语义新颖度为 $n_{p,t} = 1 - \max_{q \in B_t} s_{pq}$，在整个历史索引上计算，排除同族比较对象。对于子类 $k$，当前队列的分数份额为 $\rho_{k,t}$，参考队列为 $\rho_{k,t}^{-}$，

$$g_{k,t} = \max\left\{0, \frac{\rho_{k,t} - \rho_{k,t}^{-}}{\rho_{k,t} + \rho_{k,t}^{-} + 10^{-12}}\right\}, \quad (6)$$

$$E_{ut} = \frac{1}{M_{ut}^{E}} \sum_{p \in P_{ut}^{E}} \omega_{up} \, n_{p,t} \, g_{p,t},$$

其中 $g_{p,t}$ 对专利的各子类取平均。因此 $E$ 是专利级新颖度—增长乘积的均值：新颖性和领域增长必须重合于同一发明之中。它是一个在公开时即可获得的早期信息测度。认可型变体 $E^{\text{rec}}$ 将每个乘积乘以一年内外部引用的指示量；鉴于第 节的约束 (iii)，它连同其非零份额作为次要测度报告，并非主要的涌现指标。两个变体均不覆盖完整的涌现构念（Rotolo et al., 2015; Small et al., 2014）；技术连贯性通过案例评估。

### 再利用

在 $(\tau_p, \tau_p + H]$ 内，令 $b_p$ 计数不同的外部引用组织——在申请人字段可用时——否则计数不同的外部引用家族（层级被记录）；令 $v_p = 1 - \Delta_p / H$，其中首次外部引用在 $\Delta_p$ 年后到来，未被引用的专利 $v_p = 0$。每个分量被变换为在同一主子类和队列中正值之间的中秩（$\phi(0) = 0$；在正例少于 30 时回退到 IPC 部类再到队列），且

$$D_{ut} = \frac{1}{2 M_{ut}^{D}} \sum_{p \in P_{ut}^{D}} \omega_{up} \left[ \phi_b(b_p) + \phi_v(v_p) \right]. \quad (7)$$

$D$ 测度在可观测引用者中有记录的再利用。由于仅含高校语料库的引用侧是不完整的，$D$ 不测度全经济范围的扩散，两步深度分量不属于主要测度；它仅在后代向前链接存在时作为一种敏感性分析来计算。首次 uptake 与累积广度携带不同信息（Huang et al., 2019），也分别报告。

### 转型

令 $a_{ut}$ 和 $r_{ut}$ 为高校在共享词表上的归一化子类和对分布。则

$$T_{u,t\to t+1} = \frac{\text{JSD}(a_{ut}, a_{u,t+1}) + \text{JSD}(r_{ut}, r_{u,t+1})}{2 \log 2} \in [0,1], \quad (8)$$

其中 JSD 为 Jensen–Shannon 散度（Lin, 1991）。一个转型事件要求 $T$ 高于一个高校内部原假设的第 95 百分位——该原假设将两个相邻队列合并并置换其时期标签、同时保持队列规模——并在规模匹配的子抽样下确认。一个持续事件还要求第三时期更接近新组合而非旧组合，且仍可与旧组合区分。合并和 IPC 修订事件在任何事件被保留前都经过审计。$T$ 测度的是组合层面的机构性重组，而非技术范式转移（Dosi, 1982; Funk & Owen-Smith, 2017）；多样性是一个不同的属性（Porter & Rafols, 2009; Stirling, 2007）。

---

## 分析与报告设计

分析分三步进行，每一步均可从上述语料库作答。

**景观（Landscape）。** 技术层在合并语料上一次性布局（图 3A）；分时段叠加复用相同坐标（图 3B），使技术组的进入、持续和退出反映数据而非布局。覆盖范围增长对照稀疏子类覆盖范围和组合规模来评估，因为仅样本变大就会让更多领域可见。语义视图与分类视图之间的不一致标记出待检视的案例。

**画像（Profiles）。** 对合格高校—时段报告 $A$、$R$、$E$、$D$ 的分布、零值份额和分母（表 2），连同两两相关及其与对数专利数量、领域构成和时期的关联。这些调整后的残差变异是关系性画像在规模和领域之外增添信息的证据。随后画像以原始尺度显示，配以全校层面的 bootstrap 区间（Efron, 1979），并将高校置于画像空间中（图 4A）。画像的模型化分组（例如带稳定性检验的高斯混合，Fraley & Raftery, 2002; Hennig, 2007）在已知成熟高校—时段数量后是一种可能的扩展；它对本文提出的问题并非必需，也不预先主张。

**轨迹（Trajectories）。** 对具有连续合格队列的高校，有序画像与 $T$ 及其原假设一并显示（图 4B）。第 节的四类轨迹类别对照其声明的可观测标准加以检验；支持、混合和不支持的案例计数被报告。"持续重组先于转型"这一命题通过比较"高 $R$ 随后持续 $T$ 事件"的观测频率与在保持各高校画像值的高校内部顺序置换下的频率来检验。非正或不稳定的对比使该命题不被支持。

**案例与敏感性。** 跨画像区域和规模层级抽样的 12 条轨迹由两名技术合格的评定者依据带日期的专利证据、在不含模型值的情况下评估；一致性、分歧和裁决被报告（J. Cohen, 1960）。敏感性覆盖发明单位、归属、文本表示（TF–IDF 对冻结的中文可用编码器，Reimers & Gurevych, 2019）、窗口长度、引用时间窗和自引范围、合格阈值，以及 $E$ 和 $D$ 的变体（表 3）。同样本一致性与样本保留分别报告。所有次要关联均为探索性。

---

## 结果

**证据状态。** 数值尚未计算；以下段落固定将要报告的内容，不包含任何观测到的发现。

### 覆盖范围与景观

分析总体包括 [Pending: 高校数]、[Pending: 唯一发明数] 和 [Pending: 高校—时段数]，分布于 [Pending: 成熟队列] 中。表 1 区分原始检索、去重和合格性，前列排除原因为 [Pending: 原因和计数]。在引用层中，[Pending: 份额] 的向前链接携带引用申请人字段，这决定了 $b_p$ 计算的层级。图 3 报告 [Pending: 节点、边和社区计数] 及保留质量；技术组的进入、持续和退出为 [Pending: 观测到的模式]。

| 测度 | 有效 n | 均值 | 标准差 | 中位数 | IQR | 零值% |
|---|---|---|---|---|---|---|
| 获取 ($A$) | TBD | TBD | TBD | TBD | TBD | TBD |
| 重组 ($R$) | TBD | TBD | TBD | TBD | TBD | TBD |
| 涌现 ($E$) | TBD | TBD | TBD | TBD | TBD | TBD |
| 认可型涌现 ($E^{\text{rec}}$, 次要) | TBD | TBD | TBD | TBD | TBD | TBD |
| 再利用 ($D$) | TBD | TBD | TBD | TBD | TBD | TBD |
| 转型 ($T$, 每次过渡) | TBD | TBD | TBD | TBD | TBD | — |

> **表 2.** 各过程维度在合格高校—时段上的分布，以及 $T$ 在连续合格过渡上的分布。各分量汇总、缺失计数和覆盖份额在输出文件中随每行给出。

### 画像

表 2 报告各维度的分布和零值份额。$A$、$R$、$E$、$D$ 之间的相关为 [Pending: 系数和区间]，调整数量、领域和时期后剩余的方差份额为 [Pending: 估计]。图 4A 显示高校在画像空间中的位置及哪些区域被填充；$E^{\text{rec}}$ 在 [Pending: 份额] 的高校—时段上非零。

> **图 3.** 技术知识空间：等待源数据的分析规范。各面板不含任何合成节点、虚构聚类或实证坐标。

### 轨迹与转型

在 [Pending: 计数] 个具有连续合格队列的高校中，[Pending: 计数] 个显示至少一个高于其原假设的 $T$ 事件，[Pending: 计数] 个显示一个持续事件；[Pending: 计数] 个事件被合并和 IPC 修订审计移除。由其可观测标准支持的轨迹类别计数为 [Pending: 按类别、混合、不支持的计数]。观测与置换后的"重组随后转型"序列之间的对比为 [Pending: 效应和区间]。图 4B 显示抽样的有序画像及其 $T$ 值。

> **图 4.** 画像与轨迹展示：分析规范。轨迹类别从声明的可观测标准和独立的 $T$ 检验读取，而非从拟合的聚类读取。

### 案例与敏感性

[Pending: 计数] 个案例上的评定者一致性为 [Pending: 一致性和 kappa]；主要分歧涉及 [Pending: 主题]。表 3 报告最能改变画像值或轨迹计数的设置；对单一表示、稀疏引用或单一合格阈值的依赖限定了结果的解释。

| 检验族 | 备择与比较 | 观测结果 |
|---|---|---|
| 发明单位 | 申请对家族；同样本画像变化 | TBD |
| 归属 | 高校分数化对全部申请人和全额计数 | TBD |
| 文本表示 | 字符 TF–IDF 对冻结的中文可用编码器；新颖度秩一致性 | TBD |
| 窗口长度 | 不重叠的 2、3、4 年队列；轨迹类别一致性 | TBD |
| 再利用时间窗与范围 | $H=3$ 对 5；自引排除；组织级对家族级 $b_p$ | TBD |
| 合格性 | 最低 10/20/30 项发明；完整度 70/80/90% | TBD |
| 涌现变体 | $E$ 对 $E^{\text{rec}}$；非零份额 | TBD |
| 转型原假设 | 标签置换对规模匹配子抽样；事件计数 | TBD |
| 案例 | 盲法评定者一致性；拒绝类别解读的案例 | TBD |

> **表 3.** 敏感性与案例结果，待计算。每行报告同样本规模、画像值或轨迹计数的变化、适用时的区间，以及覆盖范围的变化。

---

## 讨论

该框架对信息科学的贡献是表征性的。每一项推断都与其所依据的关系绑定：一对不寻常的 IPC 支持一项组合主张；与带日期参考语料之间的语义距离支持一项相对新颖性主张；其后的一则外部引用记录支持一项有界再利用主张；相继类别分布之间、对照一个高校内部原假设的散度支持一项重组主张。保留这些来源使表示之间的一致与不一致变得可见，并将专利图谱（Kay et al., 2014; Leydesdorff et al., 2014; Yan & Luo, 2017）与纵向制度分析联系起来，而不将各关系坍缩为一个得分。

该设计还声明仅含高校的语料库能支持什么。它能描述来源、组合、早期涌现和可观测引用者中的再利用，能检验一个组合的构成变化是否超过其自身的逐年变异。它不能确立全经济范围的扩散、超出一步的再利用链，或变化的原因。若反复出现的画像或有序序列未超过其原假设，该框架仍是证据的描述性组织，而非对发展机制的解释，且这一结果如此报告。

其他局限持续存在。专利省略了科学的、隐性的和未获专利的知识。引用不观测学习或契约性转移（Alcácer & Gittelman, 2006）。新颖性相对于一个语料库和一种表示。合并、招聘和政策等制度事件同时影响画像和后续变化。因此，画像应连同其覆盖范围和不确定性一起解读，与研究度量的负责任使用相一致（Hicks et al., 2015），而非作为一种排名。

---

## 结论

本文将专利记录的内容、其带日期的关系、以及每种关系变得可观测的时间，联结为一个描述高校知识结构如何变化的框架。四个过程维度从分离的关系层测量；转型作为持续的构成性变化独立评估。该框架针对仅含高校的专利与引用语料库的实际边界加以规定，使其在计算时的实证主张限于数据所观测的内容。以企业引用记录进行扩展将允许再利用被追踪至学术系统之外，而文献—专利链接将把科学来源与技术来源分离开来。

---

## 数据与代码可用性

本次修订时源数据库和计算输出不可得；数据库权限和任何存储须由作者核实。随附的 LaTeX 包仅含手稿和展示源。来源、输出字段和审计要求遵循可追溯的数据管理原则（Wilkinson et al., 2016）。

---

## 参考文献

Alcácer, J., & Gittelman, M. (2006). Patent citations as a measure of knowledge flows: The influence of examiner citations. *Review of Economics and Statistics, 88*(4), 774–779. https://doi.org/10.1162/rest.88.4.774

Boccaletti, S., Bianconi, G., Criado, R., del Genio, C., Gómez-Gardeñes, J., Romance, M., Sendiña-Nadal, I., Wang, Z., & Zanin, M. (2014). The structure and dynamics of multilayer networks. *Physics Reports, 544*(1), 1–122. https://doi.org/10.1016/j.physrep.2014.07.001

Börner, K., Chen, C., & Boyack, K. W. (2003). Visualizing knowledge domains. *Annual Review of Information Science and Technology, 37*(1), 179–255. https://doi.org/10.1002/aris.1440370106

Chen, C. (2006). CiteSpace II: Detecting and visualizing emerging trends and transient patterns in scientific literature. *Journal of the American Society for Information Science and Technology, 57*(3), 359–377. https://doi.org/10.1002/asi.20317

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement, 20*(1), 37–46. https://doi.org/10.1177/001316446002000104

Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly, 35*(1), 128–152. https://doi.org/10.2307/2393553

Dosi, G. (1982). Technological paradigms and technological trajectories. *Research Policy, 11*(3), 147–162. https://doi.org/10.1016/0048-7333(82)90016-6

Efron, B. (1979). Bootstrap methods: Another look at the jackknife. *The Annals of Statistics, 7*(1), 1–26. https://doi.org/10.1214/aos/1176344552

Fleming, L. (2001). Recombinant uncertainty in technological search. *Management Science, 47*(1), 117–132. https://doi.org/10.1287/mnsc.47.1.117.10671

Fraley, C., & Raftery, A. E. (2002). Model-based clustering, discriminant analysis, and density estimation. *Journal of the American Statistical Association, 97*(458), 611–631. https://doi.org/10.1198/016214502760047131

Funk, R. J., & Owen-Smith, J. (2017). A dynamic network measure of technological change. *Management Science, 63*(3), 791–817. https://doi.org/10.1287/mnsc.2015.2366

Griliches, Z. (1990). Patent statistics as economic indicators: A survey. *Journal of Economic Literature, 28*(4), 1661–1707. https://www.jstor.org/stable/2727442

Hall, B. H., Jaffe, A., & Trajtenberg, M. (2005). Market value and patent citations. *The RAND Journal of Economics, 36*(1), 16–38. https://www.jstor.org/stable/1593752

Hennig, C. (2007). Cluster-wise assessment of cluster stability. *Computational Statistics & Data Analysis, 52*(1), 258–271. https://doi.org/10.1016/j.csda.2006.11.025

Hicks, D., Wouters, P., Waltman, L., de Rijcke, S., & Rafols, I. (2015). Bibliometrics: The Leiden manifesto for research metrics. *Nature, 520*(7548), 429–431. https://doi.org/10.1038/520429a

Huang, Y., Bu, Y., Ding, Y., & Lu, W. (2019). From zero to one: A perspective on citing. *Journal of the Association for Information Science and Technology, 70*(10), 1098–1107. https://doi.org/10.1002/asi.24177

Jaffe, A. B., Trajtenberg, M., & Henderson, R. (1993). Geographic localization of knowledge spillovers as evidenced by patent citations. *The Quarterly Journal of Economics, 108*(3), 577–598. https://doi.org/10.2307/2118401

Katila, R., & Ahuja, G. (2002). Something old, something new: A longitudinal study of search behavior and new product introduction. *Academy of Management Journal, 45*(6), 1183–1194. https://doi.org/10.2307/3069433

Kay, L., Newman, N., Youtie, J., Porter, A. L., & Rafols, I. (2014). Patent overlay mapping: Visualizing technological distance. *Journal of the Association for Information Science and Technology, 65*(12), 2432–2443. https://doi.org/10.1002/asi.23146

Kelly, B., Papanikolaou, D., Seru, A., & Taddy, M. (2021). Measuring technological innovation over the long run. *American Economic Review: Insights, 3*(3), 303–320. https://doi.org/10.1257/aeri.20190499

Kessler, M. M. (1963). Bibliographic coupling between scientific papers. *American Documentation, 14*(1), 10–25. https://doi.org/10.1002/asi.5090140103

Kivela, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). Multilayer networks. *Journal of Complex Networks, 2*(3), 203–271. https://doi.org/10.1093/comnet/cnu016

Kogler, D. F., Rigby, D. L., & Tucker, I. (2013). Mapping knowledge space and technological relatedness in US cities. *European Planning Studies, 21*(9), 1374–1391. https://doi.org/10.1080/09654313.2012.755832

Leydesdorff, L. (2008). Patent classifications as indicators of intellectual organization. *Journal of the American Society for Information Science and Technology, 59*(10), 1582–1597. https://doi.org/10.1002/asi.20814

Leydesdorff, L., Kushnir, D., & Rafols, I. (2014). Interactive overlay maps for US patent (USPTO) data based on International Patent Classification (IPC). *Scientometrics, 98*(3), 1583–1599. https://doi.org/10.1007/s11192-012-0923-2

Lin, J. (1991). Divergence measures based on the Shannon entropy. *IEEE Transactions on Information Theory, 37*(1), 145–151. https://doi.org/10.1109/18.61115

March, J. G. (1991). Exploration and exploitation in organizational learning. *Organization Science, 2*(1), 71–87. https://doi.org/10.1287/orsc.2.1.71

Nagaoka, S., Motohashi, K., & Goto, A. (2010). Patent statistics as an innovation indicator. In *Handbook of the economics of innovation* (pp. 1083–1127, Vol. 2). Elsevier. https://doi.org/10.1016/s0169-7218(10)02009-5

Porter, A. L., & Rafols, I. (2009). Is science becoming more interdisciplinary? Measuring and mapping six research fields over time. *Scientometrics, 81*(3), 719–745. https://doi.org/10.1007/s11192-008-2197-2

Price, D. J. d. S. (1965). Networks of scientific papers. *Science, 149*(3683), 510–515. https://doi.org/10.1126/science.149.3683.510

Rafols, I., Porter, A. L., & Leydesdorff, L. (2010). Science overlay maps: A new tool for research policy and library management. *Journal of the American Society for Information Science and Technology, 61*(9), 1871–1887. https://doi.org/10.1002/asi.21368

Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using siamese BERT-networks. *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*, 3980–3990. https://doi.org/10.18653/v1/d19-1410

Rigby, D. L. (2015). Technological relatedness and knowledge space: Entry and exit of US cities from patent classes. *Regional Studies, 49*(11), 1922–1937. https://doi.org/10.1080/00343404.2013.854878

Rotolo, D., Hicks, D., & Martin, B. R. (2015). What is an emerging technology? *Research Policy, 44*(10), 1827–1843. https://doi.org/10.1016/j.respol.2015.06.006

Sarica, S., Luo, J., & Wood, K. L. (2020). TechNet: Technology semantic network based on patent data. *Expert Systems with Applications, 142*, 112995. https://doi.org/10.1016/j.eswa.2019.112995

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal, 27*(3), 379–423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

Small, H. (1973). Co-citation in the scientific literature: A new measure of the relationship between two documents. *Journal of the American Society for Information Science, 24*(4), 265–269. https://doi.org/10.1002/asi.4630240406

Small, H., Boyack, K. W., & Klavans, R. (2014). Identifying emerging topics in science and technology. *Research Policy, 43*(8), 1450–1467. https://doi.org/10.1016/j.respol.2014.02.005

Stirling, A. (2007). A general framework for analysing diversity in science, technology and society. *Journal of The Royal Society Interface, 4*(15), 707–719. https://doi.org/10.1098/rsif.2007.0213

Thompson, P., & Fox-Kean, M. (2005). Patent citations and the geography of knowledge spillovers: A reassessment. *American Economic Review, 95*(1), 450–460. https://doi.org/10.1257/0002828053828509

Traag, V. A., Waltman, L., & van Eck, N. J. (2019). From Louvain to Leiden: Guaranteeing well-connected communities. *Scientific Reports, 9*(1), 5233. https://doi.org/10.1038/s41598-019-41695-z

Uzzi, B., Mukherjee, S., Stringer, M., & Jones, B. (2013). Atypical combinations and scientific impact. *Science, 342*(6157), 468–472. https://doi.org/10.1126/science.1240474

van Eck, N. J., & Waltman, L. (2010). Software survey: VOSviewer, a computer program for bibliometric mapping. *Scientometrics, 84*(2), 523–538. https://doi.org/10.1007/s11192-009-0146-3

Verhoeven, D., Bakker, J., & Veugelers, R. (2016). Measuring technological novelty with patent-based indicators. *Research Policy, 45*(3), 707–723. https://doi.org/10.1016/j.respol.2015.11.010

Wang, J., Veugelers, R., & Stephan, P. (2017). Bias against novelty in science: A cautionary tale for users of bibliometric indicators. *Research Policy, 46*(8), 1416–1436. https://doi.org/10.1016/j.respol.2017.06.006

Whalen, R., Lungeanu, A., DeChurch, L., & Contractor, N. (2020). Patent similarity data and innovation metrics. *Journal of Empirical Legal Studies, 17*(3), 615–639. https://doi.org/10.1111/jels.12261

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR guiding principles for scientific data management and stewardship. *Scientific Data, 3*(1), 160018. https://doi.org/10.1038/sdata.2016.18

Yan, B., & Luo, J. (2017). Measuring technological distance for patent mapping. *Journal of the Association for Information Science and Technology, 68*(2), 423–437. https://doi.org/10.1002/asi.23664

Youn, H., Strumsky, D., Bettencourt, L. M. A., & Lobo, J. (2015). Invention as a combinatorial process: Evidence from US patents. *Journal of The Royal Society Interface, 12*(106), 20150272. https://doi.org/10.1098/rsif.2015.0272
