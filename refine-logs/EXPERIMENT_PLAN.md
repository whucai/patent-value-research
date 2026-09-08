# 实验计划

**Problem**: 识别并解释中国高校专利的技术潜力—市场实现缺口  
**Method Thesis**: 在公开时冻结信息、在未来队列生成技术潜力分数，再估计相近潜力专利的商业化事件与高校异质性。  
**Date**: 2026-09-04

## Claim Map

| Claim | Why It Matters | Minimum Convincing Evidence | Linked Blocks |
|---|---|---|---|
| C1：公开时信息可识别未来技术潜力 | 没有可靠潜力测量，后续“实现缺口”没有基础 | 两个未来队列上相对领域基准提升，且校准和跨领域结果稳定 | B1, B2 |
| C2：高校能力造成相近潜力的不同市场实现 | 这是从预测问题到知识转移机制的关键 | 高校层增量在未来队列改善商业化模型，方差成分与缺口分布稳健 | B3, B4 |
| A1：结果不是未来信息泄漏或声望记忆造成 | 排除最可能的伪解释 | 时间可用性审计、去主体特征、跨高校外推和负面对照 | B0, B2, B4 |

## Paper Storyline

- **Main paper must prove**: 时间一致的潜力测量；高潜力未实现专利的规模；高校层实现差异。
- **Appendix can support**: incoPat 一致性、更多阈值和窗口、文本模型细节、不同专利类型。
- **Experiments intentionally cut**: 多智能体比较、LLM 解释生成、供需匹配、政策 DID、交易价格机制。

## Experiment Blocks

### B0：数据与时间泄漏审计

- **Claim tested**: A1。
- **Dataset / split / task**: 全部源表；为每个字段建立首次可用时间和事件时间。
- **Compared systems**: 不适用。
- **Metrics**: 主键重复率、跨表匹配率、日期逆序率、缺失率、成熟队列覆盖率、右删失比例。
- **Success criterion**: 主键和时间逻辑可追溯；主特征在公开时可用；主要结果具有足够五年窗口。
- **Failure interpretation**: 若时间戳不可靠，停止“早期识别”主张；若商业化覆盖不足，转向标签一致性审计。
- **Table / figure target**: Table 1 数据构建流程；Figure 1 信息时间线。
- **Priority**: MUST-RUN。

### B1：技术潜力的时间外推基线

- **Claim tested**: C1。
- **Dataset / split / task**: 成熟发明专利；按公开年份 rolling-origin。
- **Compared systems**: 领域—年份基准、Elastic Net/负二项模型、XGBoost/LightGBM。
- **Metrics**: AP、Precision@top10%、Recall@top10%、NDCG@10%、校准误差；领域宏平均。
- **Setup details**: 未来五年标准化外部前向引用为主结果；至少两个未来测试队列；超参仅在历史验证期选择。
- **Success criterion**: 树模型或正则化模型在两个测试队列均超过领域基准，且校准可接受。
- **Failure interpretation**: 转为 Idea 2 的构念审计，不构造高潜力群体。
- **Table / figure target**: Main Table 2；校准图。
- **Priority**: MUST-RUN。

### B2：文本与主体特征增量及反记忆检验

- **Claim tested**: C1、A1。
- **Dataset / split / task**: 与 B1 相同。
- **Compared systems**: 表格专利特征；+ 文本嵌入；+ 主体历史；去除高校身份；leave-university-out。
- **Metrics**: B1 指标、最差高校组召回、宏平均召回、组间校准差。
- **Success criterion**: 文本或专利本体特征产生可重复增量；结论不依赖记忆高校声望。
- **Failure interpretation**: 若增量全由主体历史驱动，只能声称机构先验预测，不能声称技术内容识别。
- **Table / figure target**: Main Table 3 或附录消融表。
- **Priority**: MUST-RUN。

### B3：潜力条件下的转让、许可与失效

- **Claim tested**: C2。
- **Dataset / split / task**: 具有完整事件史的未来队列；离散时间风险或 cause-specific hazard。
- **Compared systems**: M0 基础控制；M1 + 潜力；M2 + 高校随机效应；M3 + 高校历史转化能力。
- **Metrics**: 五年累积发生率、时间依赖 AUC、integrated Brier score、对数损失、校准。
- **Success criterion**: M2/M3 对 M1 有稳定样本外增益，且高校方差成分非微小。
- **Failure interpretation**: 高校能力主张被否定；保留对潜力与市场实现关系的描述。
- **Table / figure target**: Main Table 4；累积发生曲线。
- **Priority**: MUST-RUN。

### B4：高潜力未实现专利的稳健性与诊断

- **Claim tested**: C2、A1。
- **Dataset / split / task**: B3 队列。
- **Compared systems**: top 5/10/20%；三/五/七年；转让与许可分开；剔除自引、内部转移和已失效专利。
- **Metrics**: 缺口比例、大学间方差、排名相关、分类稳定率及置信区间。
- **Success criterion**: 核心分布与高校差异不由单一阈值、窗口或少数大校驱动。
- **Failure interpretation**: 若高度敏感，只报告连续缺口指标，不使用二元“隐藏宝石”标签。
- **Table / figure target**: Figure 3 四象限；Figure 4 高校后验区间；附录稳健性。
- **Priority**: MUST-RUN。

### B5：外部一致性与机制扩展

- **Claim tested**: 仅支持外部有效性和 Technovation 机制。
- **Dataset / split / task**: incoPat 等级；后续新增 TTO、区域产业和买方数据。
- **Metrics**: 等级相关、top-k 重叠、交互效应、异质性和准实验估计。
- **Priority**: NICE-TO-HAVE；不阻塞 iConference 阶段。

## Run Order and Milestones

| Milestone | Goal | Runs | Decision Gate | Cost | Risk |
|---|---|---|---|---|---|
| M0 | 数据可用性 | R001–R004 | 主键、日期、标签与五年窗口均可用 | 0 GPU；0.5–2 天 | 事件覆盖不足 |
| M1 | 复现简单基线 | R005–R008 | 两个未来队列超过领域基准 | 5–20 CPU 小时 | cohort shift |
| M2 | 冻结潜力模型 | R009–R013 | 文本/结构增量可重复且无主体记忆依赖 | 2–6 GPU 小时 | 文本字段不全 |
| M3 | 实现模型 | R014–R018 | 高校层增量和方差成分稳定 | 10–30 CPU 小时 | 右删失、事件误码 |
| M4 | 稳健性与图表 | R019–R026 | 结论跨阈值、窗口和事件定义稳定 | 10–30 CPU 小时 | 小校噪声 |

## First Three Runs

1. `R001`：字段、主键、表间关系和样本行数画像。
2. `R002`：所有变量的 `available_date` 与潜在泄漏清单。
3. `R003`：公开年份 × 五年成熟窗口 × 转让/许可覆盖率矩阵。

## Compute and Data Budget

- **Total estimated GPU-hours**: 4–12 小时，仅用于可选文本嵌入。
- **CPU / memory**: 预计 30–100 CPU 小时；全量引文网络与实体消歧的内存需求取决于数据规模。
- **Data preparation needs**: 专利主表、引文、法律事件、权利转移/许可、主体消歧和字段字典。
- **Human evaluation needs**: 抽查 100–200 条转让许可事件、大学映射和高潜力未实现案例。
- **Biggest bottleneck**: 事件覆盖与字段首次可用时间，而不是模型算力。

## Stop / Go Rules

- B0 不通过：停止建模，修复数据或改做标签审计。
- B1 无稳定信号：不构造“潜力”分数，转向 Idea 2。
- B3 高校增量接近零：删除组织能力主张，保留测量研究。
- B4 对定义高度敏感：使用连续指标并限制结论。

## Final Checklist

- [ ] 主表时间边界完成审计
- [ ] 未来测试队列完全隔离
- [ ] 技术潜力结果与商业化结果分开
- [ ] 转让与许可分开报告
- [ ] 右删失和竞争风险得到处理
- [ ] 主体记忆和声望依赖得到检验
- [ ] 小样本高校使用部分池化与区间
- [ ] nice-to-have 不阻塞核心证据
