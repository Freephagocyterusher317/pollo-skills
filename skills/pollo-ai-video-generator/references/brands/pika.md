# Pika

Brand path segment: `pika`
Models: 2

## pika-v2-1

- **Endpoint**: `POST /generation/pika/pika-v2-1`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `prompt` (string) — maxLength: 2000
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 2000
    The negative prompt of the generation
  - `seed` (number)
    The seed of the generation
  - `resolution` (string) — enum: `1080p`; default: `1080p`
    The resolution of the generation
  - `length` (number) — enum: `5`; default: `5`
    The length of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 2000
    The negative prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default: `1:1`
  - `seed` (number)
    The seed of the generation
  - `resolution` (string) — enum: `720p`, `1080p`; default: `1080p`
    The resolution of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation

## pika-v2-2

- **Endpoint**: `POST /generation/pika/pika-v2-2`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `prompt` (string) — maxLength: 2000
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 2000
    The negative prompt of the generation
  - `seed` (number)
    The seed of the generation
  - `resolution` (string) — enum: `720p`, `1080p`; default: `720p`
    The resolution of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 2000
    The negative prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default: `1:1`
  - `seed` (number)
    The seed of the generation
  - `resolution` (string) — enum: `720p`, `1080p`; default: `720p`
    The resolution of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
