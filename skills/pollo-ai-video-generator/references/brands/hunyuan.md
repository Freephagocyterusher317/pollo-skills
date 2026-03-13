# Hunyuan

Brand path segment: `hunyuan`
Models: 1

## hunyuan

- **Endpoint**: `POST /generation/hunyuan/hunyuan`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `prompt` (string) — maxLength: 200
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 200
    The negative prompt of the generation
  - `length` (number) — enum: `5`; default: `5`
    The length of the generation
  - `mode` (string) — enum: `fast`, `high`; default: `fast`
  - `soundEffects` (boolean) — default: `True`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 200
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 200
    The negative prompt of the generation
  - `length` (number) — enum: `5`; default: `5`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`
  - `directorMode` (boolean) — default: `False`
