# Pollo Skills

Official [Agent Skills](https://agentskills.io/specification) by [Pollo AI](https://pollo.ai) — give your AI coding agent the ability to generate videos, process media, and more.

## Quick Start

```bash
npx skills add polloaiofficial/pollo-skills
```

Then just ask your agent:

> "Generate a 10-second cinematic ocean wave video"

The agent handles model selection, API calls, polling, and delivers the video URL — all in one conversation.

## Available Skills

### pollo-ai-video-generator

Generate AI videos through the [Pollo AI API](https://pollo.ai/api-platform) with a single natural-language request.

**What it can do:**

- **Text to Video** — describe a scene and get a video back
- **Image to Video** — animate any image into motion
- **Audio Generation** — several models support generating audio with the video
- **Credit Management** — check balance and cost estimates

**Supported Models (13):**

| Brand | Highlights |
|-------|-----------|
| **Pollo** | Fast, affordable, audio support, up to 10s, up to 1080p |
| **Kling AI** | 9 model versions including v2.6 with audio |
| **Google Veo** | Veo 2/3/3.1, up to 4K resolution |
| **Sora** | Sora 2 and Sora 2 Pro |
| **Runway** | Gen-3 Turbo, Gen-4 Turbo |
| **Pixverse** | 5 versions from v3.5 to v5.5 |
| **Hailuo** | MiniMax-powered, including Live2D |
| **Wan** | 5 variants, flash and plus tiers |
| **Vidu** | Up to 2K resolution, 6 model versions |
| **Seedance** | ByteDance models, including 1.5 Pro (up to 12s) |
| **Luma** | Ray 1.6, 2.0, 2.0 Flash |
| **Pika** | v2.1 and v2.2 |
| **Hunyuan** | Tencent's video model |

**50+ model versions** across all leading models. The skill automatically recommends the best model for your use case.

## Prerequisites

1. Get your API key at [pollo.ai/api-platform/keys](https://pollo.ai/api-platform/keys)
2. Provide the key when the skill prompts you — it's stored for the session only

## License

[MIT](./LICENSE) — Pollo AI