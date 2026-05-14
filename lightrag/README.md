# LightRAG — Tolstoy Research Platform

Local semantic search and knowledge graph over the Obsidian vault. Uses LightRAG with Ollama (Qwen2.5:7b + bge-m3) — fully local, no API costs.

> **Previous setup.** Switched from Qwen2.5-14B + nomic-embed-text to Qwen2.5:7b + bge-m3 on 2026-04-25 (commit `9775cab5`). The 14B model does not fit alongside other macOS processes on 24 GB unified memory; bge-m3 (1024 dims) gives substantially better Russian retrieval than nomic-embed-text (768 dims).

## Prerequisites

- Python >= 3.10
- Mac Mini M4 24GB (or similar Apple Silicon with >= 16GB unified memory)
- Ollama installed and running (`ollama serve`)
- Two Ollama models pulled:
  ```bash
  ollama pull qwen2.5:7b
  ollama pull bge-m3
  ```

### Recommended Ollama settings (Mac)

Set these environment variables for reliable operation on 24GB Apple Silicon:

```bash
# Add to ~/.zshrc:
export OLLAMA_KEEP_ALIVE=-1           # Don't unload models after idle timeout
export OLLAMA_MAX_LOADED_MODELS=1     # One model at a time — prevents memory pressure
export OLLAMA_NUM_GPU=99              # Offload all layers to Metal GPU
```

Restart your terminal after adding these. With `OLLAMA_MAX_LOADED_MODELS=1` the LLM and embedding model swap rather than coexist. A 7B Q4_K_M LLM plus bge-m3 fits comfortably on the 24 GB Mac Mini M4; concrete footprint and throughput figures will be added once a post-2026-04-25 perf report exists.

## Installation

```bash
cd lightrag/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick start

### 1. Verify Ollama is running

```bash
curl http://localhost:11434/api/tags
```

### 2. Dry run (check what will be indexed)

```bash
python ingest.py --dry-run
```

### 3. Full initial indexing

```bash
python ingest.py
```

With ~30 files this takes a few minutes. At scale (~26,500 files) expect ~110 hours across multiple overnight runs.

### 4. Start the query API

```bash
python server.py
```

### 5. Query

```bash
curl -X POST http://localhost:8420/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What was Sophia Tolstaya'\''s role in transcribing War and Peace?", "mode": "hybrid"}'
```

## Scripts

| Script | Purpose |
|---|---|
| `ingest.py` | Full batch indexing of all vault files |
| `sync.py` | Incremental sync (only changed files) |
| `server.py` | HTTP query API server |
| `vault_reader.py` | Vault file reader (used by ingest/sync) |
| `config.py` | All configuration in one place |
| `rag.py` | LightRAG instance factory |

## Incremental sync

After the initial indexing, use `sync.py` for daily updates:

```bash
python sync.py              # Sync only changed files
python sync.py --dry-run    # Preview changes
python sync.py --full       # Force full re-index
```

### Cron job (nightly sync)

```bash
# Add to crontab -e:
0 3 * * * cd /Volumes/Graugear/Tolstoy/lightrag && ./venv/bin/python sync.py >> /tmp/lightrag-sync.log 2>&1
```

## Query modes

| Mode | What it searches |
|---|---|
| `naive` | Flat vector similarity (standard RAG) |
| `local` | Entity-level retrieval from the knowledge graph |
| `global` | High-level themes and cross-entity relationships |
| `hybrid` | Combines local + global (recommended) |
| `mix` | Integrates KG + vector retrieval |

## Data storage

All LightRAG data (index, vectors, graph) is stored in `lightrag/data/`. This directory is gitignored (via `lightrag/.gitignore`) and fully regenerable from the vault. Delete `data/` and re-run `python ingest.py` to rebuild from scratch.

## Environment variables

| Variable | Default | Purpose |
|---|---|---|
| `TOLSTOY_VAULT` | `<project-root>/website/src` (computed from script location) | Override vault path for cron jobs, testing, or if the directory structure changes |
| `OLLAMA_KEEP_ALIVE` | `5m` | Set to `-1` to keep models loaded between calls |
| `OLLAMA_MAX_LOADED_MODELS` | `0` (auto) | Set to `1` on 24GB Macs to prevent memory pressure |
| `OLLAMA_NUM_GPU` | auto | Set to `99` to offload all layers to Metal GPU |

## Architecture

```
website/src/wiki/*.md  ─┐
website/src/works/*.md ─┴─ vault_reader.py  →  LightRAG  →  lightrag/data/
                                                  │
                                                  ↓
                                          server.py :8420
                                              │
                                    Claude / scripts / apps query via HTTP
```
