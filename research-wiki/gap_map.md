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

## G4 — 新意须来自构念与研究设计而非增加指标或模型
最新文献已经覆盖预测时点、CD、SPNP、文本和技术新颖性；可辩护的新意应来自构念与研究设计，而不是再增加指标或模型。
- Addressed by: `paper:lai2026_identification_valuable_patents` (covers prediction timepoints/CD/SPNP — evidences crowded space), `paper:hu2023_evaluation_identification_potential` (indicator fusion + ML — crowded), `idea:potential_realization_gap`
