# Research Contract: 从潜在技术价值到市场实现

## Selected Idea

- **Description**: 在专利公开日冻结可用信息，用历史队列预测五年技术影响并在未来队列生成潜力分数；随后估计转让、许可和失效事件，识别高潜力未实现专利及高校实现能力差异。
- **Source**: `idea-stage/IDEA_REPORT.md`, Idea 1。
- **Selection rationale**: 利用中国高校全量数据的覆盖优势，避开已拥挤的纯预测、动态时点和单一新颖性路线；即使组织差异不显著也能产生可解释结果。

## Core Claims

1. 公开时可获得的信息能够在未来队列中稳定识别后续技术潜力。
2. 控制技术潜力后，高校间仍存在系统性的市场实现差异。
3. 高潜力未转让或许可表示可观测的市场实现缺口，不等同于无社会价值。

## Method Summary

主结果为公开后五年、按技术领域和公开年份标准化的外部前向引用；转让和许可作为独立市场事件。潜力模型只使用公开时可见的文本、分类、后向引用和主体历史，通过 rolling-origin 训练并冻结到未来队列。

商业化阶段使用离散时间风险或竞争风险模型，逐步加入潜力分数、高校随机效应和高校历史转化能力。高潜力未实现专利采用领域—年份内 top 10% 潜力且五年内无转让/许可的主定义，并做阈值、窗口、事件和法律状态稳健性。

## Experiment Design

- **Datasets**: 中国高校发明专利成熟队列；专利、引用、法律、交易和主体消歧表。
- **Baselines**: 领域—年份基准、正则化模型、XGBoost/LightGBM；商业化阶段的 M0–M3 分层事件模型。
- **Metrics**: AP、P@10%、NDCG、校准误差、Brier score、时间依赖 AUC、累计发生率和高校方差成分。
- **Key hyperparameters**: 五年主窗口、top 10% 主阈值、rolling-origin 年份切分、经验贝叶斯部分池化。
- **Compute budget**: 30–100 CPU 小时；可选文本嵌入 4–12 GPU 小时。

## Baselines

| Method | Dataset | Metric | Score | Source |
|---|---|---|---|---|
| 领域×年份基准率 | 待接入 | AP / calibration | 待运行 | 本研究基线 |
| 正则化 GLM | 待接入 | AP / calibration | 待运行 | 本研究基线 |
| XGBoost/LightGBM | 待接入 | AP / calibration | 待运行 | 本研究强表格基线 |

## Current Results

| Method | Dataset | Metric | Score | Notes |
|---|---|---|---|---|
| — | — | — | — | 原始数据尚未进入项目目录 |

## Key Decisions

- 公开日是主信息边界；授权日仅作稳健性边界。
- incoPat 等级只做外部一致性检验，不作为唯一训练真值。
- 转让与许可分开建模，失效作为竞争事件或删失敏感性。
- 首稿不加入政策 DID、供需匹配或多智能体模块。

## Status

- [x] Idea selected
- [ ] Data schema audited
- [ ] Baseline reproduced
- [ ] Potential model frozen
- [ ] Commercialization model completed
- [ ] Robustness studies completed
- [ ] Author-generated paper draft
