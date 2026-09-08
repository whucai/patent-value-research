# Research Wiki Query Pack

_Auto-generated. Do not edit._

## Project Direction
# 研究任务书

## 研究问题

利用中国高校专利全量数据，识别在公开时已显示出较高技术潜力、但在后续观察期内未实现转让或许可的专利，并解释高校及区域环境为何使相近技术潜力转化为不同的市场结果。

## 核心研究对象

- 分析单位：高校发明专利。
- 时间原点：专利公开日；任何预测变量必须在该日已经可观测。
- 技术潜力结果：公开后五年、按技术领域与公开年份标准化的前向引用表现；扩散广度、扩散质量和维持状态仅作稳健性结果。
- 市场实现结果：公开后五年内首次转让或许可；转让、许可分开建模，交易金额仅在覆盖率足够时使用。
- 关键概念：高技术潜力但未商业化的“价值实现缺口”，而非把商业化等同于专利的全部社会价值。

## 现有资源

- 中国高校专利全量数据。
- 已整理的 11 类专利指标：技术新颖性、知识重组、知识吸收、知识扩散、知识网络结构、文本控制、技术范围、权利保护与申请布局、创新主体与团队、市场运用、法律状态与稳定性。
- incoPat 专利质量等级，可作为外部一致性检验，不作为唯一真值。

## 约束

- 不把前向引用、转让、许可、后续法律状态或未来主体信息泄漏到公开时预测特征中。
- 不重复设置 TCT 与前沿性，也不同时把前向引用次数与扩散强度作为独立指标。
- 首阶段面向 iConference 2027 的信息计量、知识管理、知识产权和数据科学议题。
-
## Open Gaps
# Gap Map

_Field gaps with stable IDs._

## G1 — 潜力与实现未分离
现有预测研究常把事后可见指标混入"早期价值识别"，或主要比较预测准确率；管理研究多直接解释转让/许可，较少先把专利自身的技术潜力与组织实现能力分开。
- Addressed by: `paper:hsu2021_benchmarking_university_patent` (nearest neighbor — US university potential vs realized licensing), `paper:wu2015_commercialization_university_inventions` (org factors determine licensing), `paper:sine2003_halo_effect_technology` (institutional prestige → licensing — prior art, surfaced post-review), `idea:potential_realization_gap`

## G2 — 中国高校"同等潜力、不同实现"未被专利层级系统识别
已有中国高校研究证明数量、技术质量与商业价值会脱钩，但尚未在全国专利层级系统识别"同等潜力、不同实现"的专利和高校。
- Addressed by: `paper:lin2025_patent_gold_rush` (decoupling proven at university-year level, not patent level), `paper:yang2024_technological_novelty_technology` (China university novelty-transfer), `paper:gong2020_innovation_value_chain` (Chinese university commercialization trap — same-context nearest neighbor, surfaced post-review), `idea:potential_realization_gap`

## G3 — incoPat 评分作真值会把未来信息编码进标签
incoPat 评分的构成和时间截面不透明，若直接作为真值，可能把未来引用、法律和市场事件再次编码进标签。
- Addressed by: `idea:potential_realization_gap` (audits incoPat composition; uses only for external consistency, never as ground truth)

## G4 — 
## Key Papers (12 total)
- [paper:gong2020_innovation_value_chain] The innovation value chain of patents: Breakthrough in the patent commercialization trap in Chinese universities: Innovation value chain of patents; identifies a commercialization trap in Chinese universities and breakthrough mechanisms — same-context nearest neig
- [paper:gu2022_spatial_interactions_commercialisation] Spatial Interactions and the Commercialisation of Academic Patents: 1,815 universities spatial model; commercialization has spatial spillover.
- [paper:guo2026_intellectual_property_services] Intellectual property services and the commercialization of patents: Insights from Chinese scientists: A university IP-services policy increases commercialization through specialization and university-industry matching.
- [paper:hsu2021_benchmarking_university_patent] Benchmarking U.S. university patent value and commercialization efforts: A new approach: Benchmarks potential university patent value against corporate patents and compares it with realized licensing value.
- [paper:hu2023_evaluation_identification_potential] Evaluation and identification of potential high-value patents: Multi-dimensional indicator pre-screening + ML to identify high-value integrated-circuit patents.
- [paper:lai2026_identification_valuable_patents] Identification of valuable patents: New indicators and effects of prediction time points: Patent examination, citation-network and claim-text indicators improve value prediction across patent ages; CD and SPNP are already covered.
- [paper:lin2025_patent_gold_rush] The patent gold rush? An empirical study of patent bubbles in Chinese universities (1990–2019): University patent quantity growth in China is associated with lower subsequent citation, licensing and collateralization outcomes.
- [paper:liu
## Recent Relationships (16 total)
  idea:potential_realization_gap --inspired_by--> paper:hsu2021_benchmarking_university_patent
  idea:potential_realization_gap --inspired_by--> paper:lin2025_patent_gold_rush
  idea:dynamic_patent_value_prediction --inspired_by--> paper:lai2026_identification_valuable_patents
  idea:novelty_transfer_inverted_u --inspired_by--> paper:yang2024_technological_novelty_technology
  paper:hsu2021_benchmarking_university_patent --addresses_gap--> gap:G1
  paper:wu2015_commercialization_university_inventions --addresses_gap--> gap:G1
  paper:lin2025_patent_gold_rush --addresses_gap--> gap:G2
  paper:yang2024_technological_novelty_technology --addresses_gap--> gap:G2
  paper:lai2026_identification_valuable_patents --addresses_gap--> gap:G4
  paper:hu2023_evaluation_identification_potential --addresses_gap--> gap:G4
  idea:potential_realization_gap --addresses_gap--> gap:G1
  idea:potential_realiz
