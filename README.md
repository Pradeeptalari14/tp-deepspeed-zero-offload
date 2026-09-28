# Microsoft DeepSpeed ZeRO-3 & NVMe Offload Studio

[![CI SRE Validation](https://github.com/Pradeeptalari14/tp-deepspeed-zero-offload/actions/workflows/sre-validation.yml/badge.svg)](https://github.com/Pradeeptalari14/tp-deepspeed-zero-offload/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Optimization: DeepSpeed ZeRO-3](https://img.shields.io/badge/Optimization-DeepSpeed%20ZeRO--Infinity-emerald.svg)](https://talaripradeep.info)

Production-grade **DeepSpeed ZeRO-3 (Zero Redundancy Optimizer)** and **NVMe / CPU Asynchronous Offload** engine for massive distributed LLM training and fine-tuning.

![DeepSpeed Architecture Flow](docs/deepspeed_zero_flow.png)

## Key Technical Highlights
- **8x VRAM Footprint Reduction:** Partitions optimizer states (ZeRO-1), gradients (ZeRO-2), and model parameters (ZeRO-3) across nodes, keeping only active layer weights in GPU memory.
- **ZeRO-Infinity NVMe Offload:** Streams model parameters directly from high-speed PCIe Gen5 NVMe arrays with asynchronous prefetching.
- **70B Training on Budget GPUs:** Trains and fine-tunes 70B parameter models on small GPU footprints without out-of-memory (OOM) crashes.
- **Communication Overlapping:** Overlaps gradient reduce-scatter and parameter all-gather collectives with forward and backward computation.

## Quickstart
```bash
git clone https://github.com/Pradeeptalari14/tp-deepspeed-zero-offload.git
cd tp-deepspeed-zero-offload
bash scripts/validate.sh
```
