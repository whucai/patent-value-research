# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project nature

This is a **research workspace** for studying high-value patent identification — not a software codebase. There is no source code, no build system, no tests, and no git history. The working materials are:

- `高价值专利判断.docx` — research notes surveying related work on patent value/quality prediction (XGBoost regression with `objective='reg:gamma'` over incoPat quality ratings; a binary-classification variant of the same task; patent lifetime as an innovation-quality proxy). Target journals named inside: 知识产权, 现代情报, 科学管理研究.
- `分类思路与指标体系0828.docx` — the patent indicator system and the four reclassification principles (attribute homogeneity, hierarchical consistency, indicator independence, process continuity).
- `research-wiki/` — persistent ARIS knowledge base (papers / ideas / experiments / claims / graph), initialized 2026-09-04.

Because there is no code here, "build / lint / test" does not apply. The reusable commands are docx extraction and research-wiki mutations, below.

## Domain context

Ground any modeling or literature work by reading the two `.docx` files first. The project predicts patent value from a multi-dimensional indicator system. Ground truth is the **incoPat** database quality rating. The modeling task is either regression (XGBoost `objective='reg:gamma'`, predicts a continuous positive value) or binary classification of high-value patents.

The indicator system is organized into four logical layers, in process order:
1. **技术知识形成与传播** — technical novelty, knowledge recombination, absorption, diffusion, network structure.
2. **文本与技术表征** — text-control and technology-scope features of the patent itself.
3. **权利与主体属性** — claim protection, filing layout, inventor/team, applicant.
4. **市场与法律表现** — market utilization, legal status and stability.

Known indicator merges (do **not** re-add as independent variables — they were collapsed deliberately under the indicator-independence principle): TCT ≈ 前沿性 (both measure recency); 前向引用次数 ≈ 扩散强度 (both measure forward-citation scale).

## Reading the .docx notes

The notes are Word documents; read them with python-docx (available in the base `python3`, no conda env needed):

```bash
python3 -c "import docx; [print(p.text) for p in docx.Document('高价值专利判断.docx').paragraphs if p.text.strip()]"
```

Tables are not paragraphs — if tabular content is needed, iterate `Document(...).tables`.

## Research wiki

`research-wiki/` is the single source of truth for papers / ideas / experiments / claims and their relationships. Never hand-edit `graph/edges.jsonl` or the `## Connections` sections on pages — both are auto-generated. All mutations go through the canonical helper:

```bash
WIKI_SCRIPT="/home/caile/.claude/Auto-claude-code-research-in-sleep/tools/research_wiki.py"
python3 "$WIKI_SCRIPT" ingest_paper research-wiki/ --arxiv-id <id> --thesis "..."
python3 "$WIKI_SCRIPT" add_edge    research-wiki/ --from paper:<slug> --to paper:<slug> --type extends --evidence "..."
python3 "$WIKI_SCRIPT" sync        research-wiki/ --arxiv-ids <id1>,<id2>
python3 "$WIKI_SCRIPT" stats        research-wiki/
python3 "$WIKI_SCRIPT" lint         research-wiki/
```

Prefer the `/research-wiki`, `/arxiv`, `/research-lit`, `/alphaxiv`, `/deepxiv` skills over running the helper by hand — they call the same helper internally and stay in sync with its schema.

## Environment notes

- The **global** `~/.claude/CLAUDE.md` documents a GPU `lzz` conda env and code at `/mnt/mydisk/PycharmProjects/lzz/HC_ARF_20250723`. That context is for a **sibling project**, not this one. This patent workspace has no Python package of its own; plain `python3` is enough for docx reading and the wiki helper. If XGBoost experiment code lives in the `lzz` directory, run it there under `conda activate lzz`, not here.
- `.claude/settings.local.json` grants Read access to `~/.codex/**` and `~/.gemini/**` so foreign-tool configs can be inspected by skills that need them.
