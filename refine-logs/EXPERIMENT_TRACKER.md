# 实验跟踪表

| Run ID | Milestone | Purpose | System / Variant | Split | Metrics | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| R001 | M0 | 数据画像 | 主键、表关系、规模 | 全量 | 重复率、匹配率、缺失率 | MUST | BLOCKED | 待提供数据 |
| R002 | M0 | 时间泄漏审计 | available-date map | 全量字段 | 泄漏字段数、日期逆序率 | MUST | BLOCKED | 待提供字段字典 |
| R003 | M0 | 队列成熟度 | cohort matrix | 按公开年 | 五年覆盖率、删失率 | MUST | BLOCKED | 待提供数据 |
| R004 | M0 | 事件有效性 | 转让/许可/失效抽查 | 分层样本 | 事件准确率、内部转移率 | MUST | BLOCKED | 待提供事件表 |
| R005 | M1 | 朴素基准 | 领域×年份基准 | 未来队列 A/B | AP、P@10%、校准 | MUST | TODO | M0 通过后 |
| R006 | M1 | 可解释基线 | Elastic Net/GLM | 未来队列 A/B | 同上 | MUST | TODO |  |
| R007 | M1 | 强表格基线 | XGBoost | 未来队列 A/B | 同上 | MUST | TODO |  |
| R008 | M1 | 强表格基线 | LightGBM/CatBoost | 未来队列 A/B | 同上 | MUST | TODO | 选一项即可 |
| R009 | M2 | 文本增量 | 表格 + 文本嵌入 | 未来队列 A/B | ΔAP、Δ校准 | MUST | TODO |  |
| R010 | M2 | 主体增量 | + 申请人/发明人历史 | 未来队列 A/B | ΔAP、组间校准 | MUST | TODO |  |
| R011 | M2 | 反声望消融 | 去高校身份/规模 | 未来队列 A/B | 宏召回、最差组召回 | MUST | TODO |  |
| R012 | M2 | 跨高校外推 | leave-university-out | 全队列 | AP、校准 | MUST | TODO |  |
| R013 | M2 | 潜力模型冻结 | 最佳简约模型 | 锁定未来队列 | 全部主指标 | MUST | TODO | 完成后不可回看调参 |
| R014 | M3 | 商业化基准 | M0 | 事件队列 | Brier、校准、AUC(t) | MUST | TODO |  |
| R015 | M3 | 潜力增量 | M1 | 事件队列 | ΔBrier、Δlog-loss | MUST | TODO |  |
| R016 | M3 | 高校异质性 | M2 分层模型 | 事件队列 | 方差成分、校准 | MUST | TODO |  |
| R017 | M3 | 历史能力 | M3 | 事件队列 | 样本外增益 | MUST | TODO |  |
| R018 | M3 | 竞争风险 | 转让/许可/失效 | 事件队列 | CIF、cause-specific HR | MUST | TODO |  |
| R019 | M4 | 阈值稳健性 | top 5/10/20% | 事件队列 | 缺口率、稳定率 | MUST | TODO |  |
| R020 | M4 | 窗口稳健性 | 3/5/7 年 | 成熟队列 | 缺口率、CIF | MUST | TODO |  |
| R021 | M4 | 事件定义 | 转让与许可分开 | 事件队列 | 方向与量级 | MUST | TODO |  |
| R022 | M4 | 自引与内部事件 | 排除口径 | 事件队列 | 方向与量级 | MUST | TODO |  |
| R023 | M4 | 小校收缩 | 最小样本/部分池化 | 事件队列 | 后验区间、稳定性 | MUST | TODO |  |
| R024 | M4 | 外部一致性 | incoPat 等级 | 可匹配样本 | 相关、top-k 重叠 | NICE | TODO | 先审计等级构成 |
| R025 | M4 | 结果可视化 | 四象限与校准 | 锁定结果 | 图表 QA | MUST | TODO |  |
| R026 | M4 | 人工案例核查 | 100–200 件 | 分层抽样 | 编码一致率 | MUST | TODO | 需作者核验 |
