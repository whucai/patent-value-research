# 研究细化报告

**Problem**: 中国高校专利技术潜力与市场实现的专利层级缺口  
**Date**: 2026-09-04  
**Final Verdict**: REVISE BEFORE EMPIRICAL CLAIMS

## Problem Anchor

识别中国高校中在公开时具有较高未来技术潜力、但在后续观察期内未实现转让或许可的专利，并解释相近潜力为何产生不同市场结果。

## Final Proposal Snapshot

- 以专利公开日冻结信息，排除未来事件泄漏。
- 用历史队列训练并冻结技术潜力模型，再应用于未来队列。
- 将许可、转让和失效作为后续事件，检验高校层实现差异。
- 用阈值、窗口、事件定义和小校收缩检验高潜力未实现群体的稳健性。
- incoPat 等级仅用于外部一致性，不作为唯一真值。

## Deliverables

- `refine-logs/FINAL_PROPOSAL.md`
- `refine-logs/EXPERIMENT_PLAN.md`
- `refine-logs/EXPERIMENT_TRACKER.md`
- `refine-logs/DATA_REQUIREMENTS.md`
- `idea-stage/docs/research_contract.md`

## Remaining Weaknesses

- 数据可用性和事件覆盖未验证。
- 没有 pilot 或独立评审凭证。
- 潜力构念与最近邻文献的差异需要用实证结果进一步证明。
