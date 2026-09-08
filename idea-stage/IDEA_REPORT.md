# 中国高校专利价值研究：选题发现报告

**Direction**: 中国高校全量专利数据；首投 iConference，后续实质扩展至 Technovation  
**Date**: 2026-09-04  
**Pipeline**: research-lit → idea-creator → novelty-check → research-review → research-refine-pipeline

## Executive Summary

推荐研究“从潜在技术价值到市场实现：哪些中国高校专利成为被遗漏的高潜力专利”。核心不是再训练一个更复杂的高价值分类器，而是用公开时可获得的信息预测后续技术影响，再观察具有相近技术潜力的专利是否以及何时被转让或许可。该设计把专利质量测量、时间信息泄漏和高校知识转移放在同一框架中，既符合 iConference 的信息计量、知识管理、知识产权与数据科学议题，也为 Technovation 的组织能力和商业化机制研究保留清晰扩展空间。

现阶段没有原始数据、字段字典或既有实验结果，全部候选的 pilot 状态均为 `SKIPPED: DATA NOT PRESENT`。推荐结论基于现有指标体系、公开文献查新和可执行性审查，不代表经验结论。

## Literature Landscape

本地 `papers/`、`literature/` 及自定义论文库均未提供 PDF；本轮文献证据来自在线期刊页面、开放全文和官方会议信息。

| 文献 | 载体 | 方法或发现 | 对本项目的约束 | Source |
|---|---|---|---|---|
| Lai, Wei, & Hwang (2026), “Identification of valuable patents: New indicators and effects of prediction time points” | Research Policy 55(8), 105512 | 结合审查、引文网络和权利要求文本，并比较授权后多个预测时点；CD、SPNP 等指标已有直接证据 | “新增 CD/SPNP + 动态时点”不能作为主创新 | [DOI](https://doi.org/10.1016/j.respol.2026.105512) |
| Hu, Zhou, & Lin (2023), “Evaluation and identification of potential high-value patents…” | Journal of Informetrics 17(2), 101406 | 多维指标预筛选与机器学习识别集成电路高价值专利 | 单纯指标融合和模型比较已高度拥挤 | [DOI](https://doi.org/10.1016/j.joi.2023.101406) |
| Hsu, Hsu, Zhou, & Ziedonis (2021), “Benchmarking U.S. university patent value and commercialization efforts” | Research Policy 50(1), 104076 | 区分大学专利的潜在经济价值与许可收入实现，估计美国大学平均捕获约 16% 的潜在价值 | “潜在—实现”概念已有先例；新意须落在中国全量专利、专利层级、时间一致测量及异质转化 | [DOI](https://doi.org/10.1016/j.respol.2020.104076) |
| Lin, Ding, & Chen (2025), “The patent gold rush?” | Journal of Technology Transfer 50(4), 1602–1632 | 769,133 件、538 所高校，发现数量增长与引用、许可和质押下降相关 | 中国高校“质量—商业价值脱钩”已被证明；不能只复述专利泡沫 | [DOI](https://doi.org/10.1007/s10961-024-10071-z) |
| Yang, Chen, & Zhang (2024), “Technological Novelty and Technology Transfer of University Patents” | Academy of Management Proceedings | 2,635,464 件中国高校专利；技术新颖性与转移呈倒 U 型，并检验产学合作、市场化与战略新兴产业调节 | 单独研究“新颖性如何影响转移”重叠严重 | [DOI](https://doi.org/10.5465/AMPROC.2024.104bp) |
| Shen, Coreynen, & Huang (2023), “Prestige and technology-transaction prices” | Technovation 123, 102710 | 浙江高校专利交易；发明团队、高校和买方声望影响交易价格 | Technovation 扩展必须超越声望主效应，处理供需和组织能力 | [DOI](https://doi.org/10.1016/j.technovation.2023.102710) |
| Liu, Li, Yang, & Zhang (2025), “How does patent mixed ownership impact university technology commercialization?” | Technovation 145, 103259 | 2017–2022 年改革的 DID 研究；混合所有制提升发明人主导的商业化 | 制度扩展需要不同政策冲击或不同机制 | [DOI](https://doi.org/10.1016/j.technovation.2025.103259) |
| Guo, Zhong, Zhou, Xiang, & Leng (2026), “Intellectual property services and the commercialization of patents” | China Economic Review 98, 102726 | 利用知识产权示范高校政策做 DID，发现 IP 服务促进商业化 | 泛化的 TTO/IP 服务主效应已拥挤；应研究其是否缩小高潜力专利的实现缺口 | [DOI](https://doi.org/10.1016/j.chieco.2026.102726) |
| Gu (2022), “Spatial Interactions and the Commercialisation of Academic Patents” | Science, Technology and Society 27(4), 543–562 | 1,815 所高校的空间模型，发现商业化存在空间溢出 | 区域变量可作为扩展，但普通空间主效应不是新意 | [DOI](https://doi.org/10.1177/09717218221124890) |
| Wu, Welch, & Huang (2015), “Commercialization of university inventions” | Technovation 36–37, 12–25 | 个体、合作与 TTO 因素共同决定许可 | 支持用组织互补能力解释相近专利潜力的不同实现结果 | [DOI](https://doi.org/10.1016/j.technovation.2014.09.004) |

### 结构性空缺

1. 现有预测研究往往把事后可见指标混入“早期价值识别”，或主要比较预测准确率；管理研究则多直接解释转让/许可，较少先把专利自身的技术潜力与组织实现能力分开。
2. 已有中国高校研究证明数量、技术质量与商业价值会脱钩，但尚未在全国专利层级系统识别“同等潜力、不同实现”的专利和高校。
3. incoPat 评分的构成和时间截面不透明，若直接作为真值，可能把未来引用、法律和市场事件再次编码进标签。
4. 最新文献已经覆盖预测时点、CD、SPNP、文本和技术新颖性；可辩护的新意应来自构念与研究设计，而不是再增加指标或模型。

## Ranked Ideas

共形成 9 个候选方向，其中 6 个保留、2 个因直接文献重叠而淘汰、1 个归档。以下排序综合问题价值、与目标载体的匹配、数据可执行性和最近邻重叠风险；由于数据尚未接入，排序不包含经验 pilot 信号。

### Idea 1: 从潜在技术价值到市场实现——中国高校“被遗漏的高潜力专利”

- **Method (what we actually do)**: ① 按公开日冻结可用特征；② 用历史队列预测五年技术影响并在未来队列生成潜力分数；③ 将转让和许可作为后续事件建模；④ 在相同潜力下估计高校与区域的实现差异，识别高潜力但未实现的专利。
- **Hypothesis**: 专利技术潜力只能解释部分商业化差异，高校的价值实现能力会造成大量系统性的高潜力未转化。
- **Minimum experiment**: 选取具有至少五年观察窗的发明专利，按年份滚动训练与测试；比较“仅专利潜力”与“潜力 + 高校效应”对五年转让/许可的解释和校准。
- **Expected outcome**: 无论高校差异显著与否都具有信息价值；显著说明组织转化摩擦重要，不显著则说明专利属性或市场需求足以解释结果。
- **Novelty**: 6.5/10，`PROCEED WITH CAUTION`。最接近 Hsu et al. (2021) 的潜在—实现框架和 Lin et al. (2025) 的中国高校质量—商业价值脱钩；可验证差异是全国专利层级、严格时间冻结、显式识别高潜力未实现专利及高校实现能力。
- **Feasibility**: 高；主体为表格模型、事件史和分层模型，文本嵌入可选。
- **Risk**: MEDIUM。
- **Contribution type**: 测量 + 经验机制。
- **Pilot result**: `SKIPPED: DATA NOT PRESENT`。
- **Reviewer's likely objection**: 潜力分数是模型构造物，且未商业化不等于没有社会价值。
- **Why we should do this**: 它直接利用全量高校数据的独特性，并避开已拥挤的纯预测精度赛道。

### Idea 2: “高价值”标签是否在测量同一事物——高校专利标签一致性审计

- **Method**: 对 incoPat 等级、五年引用、维持、转让、许可和交易金额进行时间对齐；比较标签间一致性、排名交换与不同群体的误差；分析采用某一标签会把哪些专利系统性排除。
- **Hypothesis**: 不同“高价值”标签只具有有限一致性，并对应技术影响、法律稳定和市场实现等不同构念。
- **Minimum experiment**: 同一成熟队列上的相关性、重叠率、潜类或多任务预测、按年份/领域/高校类型分层。
- **Novelty**: 6/10，`PROCEED WITH CAUTION`；构念审计适合 iConference，但必须避免仅做描述性相关。
- **Risk**: LOW–MEDIUM。
- **Pilot result**: `SKIPPED: DATA NOT PRESENT`。

### Idea 3: 声望依赖的专利筛选是否遗漏非头部高校的“隐藏宝石”

- **Method**: 比较包含和排除高校身份、历史规模与声望特征的模型；进行跨高校外推、群组校准和固定筛选预算下的召回分析。
- **Hypothesis**: 主体历史特征能提高总体准确率，却会降低对非头部高校未来高影响专利的召回。
- **Minimum experiment**: leave-university-out 和时间外推测试；报告宏平均召回、最差组召回与校准误差。
- **Novelty**: 6.5/10，`PROCEED WITH CAUTION`；需要把公平性解释成资源配置风险，而不是泛化的算法公平。
- **Risk**: MEDIUM。
- **Pilot result**: `SKIPPED: DATA NOT PRESENT`。

### Idea 4: 转让、许可与失效的竞争风险路径

- **Method**: 从公开日起建立多状态/竞争风险模型，区分首次转让、许可和失效，分析技术属性如何改变路径与速度。
- **Novelty**: 5.5/10；方法成熟，需有独特发现才能成立。
- **Risk**: LOW。
- **Pilot result**: `SKIPPED: DATA NOT PRESENT`。

### Idea 5: 高潜力专利的沉睡期与迟发实现

- **Method**: 识别五年内未转化但更长窗口内转化的专利，研究技术复杂性与市场成熟度对迟发商业化的关系。
- **Novelty**: 6/10；需要足够长的完整观察窗。
- **Risk**: MEDIUM。
- **Pilot result**: `SKIPPED: DATA NOT PRESENT`。

### Idea 6: 高校技术组合与区域产业需求的匹配

- **Method**: 将高校专利语义/IPC 组合与城市企业专利或产业结构对齐，检验需求邻近性是否缩小高潜力专利实现缺口。
- **Novelty**: 7/10；需要企业专利或产业数据，适合作为 Technovation 扩展。
- **Risk**: MEDIUM–HIGH。
- **Pilot result**: `SKIPPED: EXTERNAL DATA REQUIRED`。

### Idea 7: 仅用公开时信息的动态预测模型

- **Status**: `ELIMINATED AS PRIMARY IDEA`。
- **Reason**: Lai, Wei, & Hwang (2026) 已直接研究不同预测时点，并纳入 CD、SPNP、审查和权利要求文本。

### Idea 8: 技术新颖性与高校专利转让的倒 U 型关系

- **Status**: `ELIMINATED AS PRIMARY IDEA`。
- **Reason**: Yang, Chen, & Zhang (2024) 已用 2,635,464 件中国高校专利研究该关系及多个调节变量。

### Idea 9: 多智能体识别高价值专利

- **Status**: `ARCHIVED`。
- **Reason**: 如果没有新的评价任务、可验证机制或人机协作证据，只是替换分类器外壳；不适合作为当前数据优势的主线。

## Novelty Verification

### 核心主张与最近邻

1. **公开时技术潜力与后续市场实现应被分开测量**。最近邻是 Hsu et al. (2021)，其在美国大学层面用企业匹配估计潜在经济价值；本研究拟在中国高校专利层级用严格时间信息集识别潜力与实际事件的缺口。
2. **中国高校存在系统性的技术质量—商业价值脱钩**。Lin et al. (2025) 已在高校—年份层面证明专利泡沫，因而该命题本身不新；可检验的新内容是哪些具体高潜力专利被遗漏、遗漏是否集中于特定高校，以及预测筛选能否识别它们。
3. **高校能力会影响相近技术潜力的实现**。Wu et al. (2015)、Gu (2022)、Guo et al. (2026) 已支持组织和区域因素，但尚未发现一篇已发表论文完整执行“专利潜力冻结 → 条件商业化 → 全国高校实现缺口”的组合设计。
4. **时间一致性是有效识别的前提**。Lai et al. (2026) 已覆盖预测时点，因此本研究只能把它作为设计约束，不能把它单独声称为创新。

### Overall Novelty Assessment

- **Score**: 6.5/10。
- **Recommendation**: `PROCEED WITH CAUTION`。
- **Key differentiator**: 在专利层级、严格公开时信息集下，把“未来技术潜力”与“高校把该潜力转化为市场事件的能力”分开估计，并识别高潜力未实现专利。
- **Risk**: Hsu et al. (2021) 和 Lin et al. (2025) 会被审稿人视为概念与情境最近邻；若只报告相关性或模型准确率，差异不足。
- **Suggested positioning**: 本研究不提出新的通用专利估值算法，而是建立时间一致的专利信息测量框架，揭示中国高校技术潜力与市场实现之间的专利层级缺口。

### Post-review nearest neighbors (Codex second-opinion, DOI-verified)

A fresh-context Codex review surfaced two nearest neighbors this report had missed; both verified real via CrossRef/PLOS:

- **Sine, Shane & Di Gregorio (2003), Management Science** (DOI 10.1287/mnsc.49.4.478.14416) — "The Halo Effect and Technology Licensing": institutional prestige influences university invention licensing conditional on invention characteristics. Prior art for the "university realization capacity" angle — pressures its novelty claim; the proposal must cite and differentiate.
- **Gong et al. (2020), PLOS ONE** (DOI 10.1371/journal.pone.0230805) — "The innovation value chain of patents: Breakthrough in the patent commercialization trap in Chinese universities": same-context (Chinese universities) nearest neighbor to the value realization gap; may be closer than Lin et al. (2025) for the China angle.

Independent novelty score: 5.5/10 (from both a Claude/Anthropic and a Codex/OpenAI fresh-context review), below the 6.5 self-score above. Full verdicts in `idea-stage/INDEPENDENT_REVIEWS.md`.

## External Critical Review

**Assurance status**: `RESOLVED` — independent cross-family reviews now in `idea-stage/INDEPENDENT_REVIEWS.md` (Claude/Anthropic + Codex/OpenAI; both PROCEED_WITH_CAUTION on novelty, both REVISE_BEFORE_EMPIRICAL_CLAIMS on the design). The same-context review below is retained as the record.

本轮最初只能完成同一执行上下文内的对抗性审查；独立评审凭证现已取得（见上）。同上下文审查结论如下：

- 最强优点：问题真实、全量数据具有优势、负结果也可解释、与两个目标载体均有连接。
- 首要风险：把预测分数重新命名为“潜力”会造成构念循环。必须用严格的未来技术结果、时间外推和外部一致性检验约束该分数。
- 第二风险：把未转让/许可解释成失败。正文必须使用“市场实现缺口”，并承认开放传播、科研使用、创办企业和公共价值可能未被观察。
- 第三风险：组织效应容易沦为高校排名。需要经验贝叶斯收缩、最小样本阈值和不确定区间，避免把小样本噪声解释为能力。
- 最便宜的判别实验：在一个成熟申请队列中，仅用公开时特征预测五年标准化引用；冻结模型后，在下一时间队列计算潜力，并检验加入高校随机截距是否实质改善五年转让/许可的校准与解释。
- 当前判断：`REVISE BEFORE EMPIRICAL CLAIMS`；研究设计可执行，但没有数据审计和 pilot，不能宣称 READY。

## Refined Proposal

- Proposal: `refine-logs/FINAL_PROPOSAL.md`
- Experiment plan: `refine-logs/EXPERIMENT_PLAN.md`
- Tracker: `refine-logs/EXPERIMENT_TRACKER.md`
- Data handoff: `refine-logs/DATA_REQUIREMENTS.md`

## Venue Strategy



### Technovation 实质扩展

期刊版本应增加至少一条新的理论机制和一套新数据：高校技术转移机构能力、地方市场化与产业需求、买方特征或政策冲击。优先问题是“何种组织与区域互补能力能缩小高潜力专利的实现缺口”，并采用分层事件史、准实验或供需匹配设计。会议稿与期刊稿需清楚披露关系并避免重叠发表。

## Next Steps

1. 提供专利主表、引用表、法律事件表、转让许可表、申请人/发明人消歧表和字段字典。
2. 先运行字段可用时点与右删失审计，再确定最终队列和标签。
3. 完成 1%–5% 分层样本 pilot 后再冻结研究问题和主表结构。

<!-- ARIS_IDEA_DISCOVERY_EVIDENCE_GATE:START -->
## Evidence Gate
**Status:** PASSED

Both previously-`done`-but-unaccepted sub-stages closed by cross-family review
(reviewer: fresh-context Claude / Anthropic family ≠ codex-gpt-5.6-sol executor /
OpenAI family — satisfies `assert_cross_family`). Full verdict text in
`idea-stage/INDEPENDENT_REVIEWS.md`.

- novelty-check: **accepted** — PROCEED_WITH_CAUTION, 5.5/10 (down from 6.5 self-score; differentiator partially holds; circularity partially mitigated).
- research-review: **accepted** — REVISE_BEFORE_EMPIRICAL_CLAIMS, 6/10 (independently confirms prior same-context verdict; construct-circularity only partially addressed; iConference 2027 fit marginal; data-state claims OK — no empirical over-assertion).

A second OpenAI-direction pass via Codex MCP was rate-limited at close-out
(usage limit, resets ~21:19 local) and can be added later as an extra datapoint;
the cross-family invariant is already met.
<!-- ARIS_IDEA_DISCOVERY_EVIDENCE_GATE:END -->
