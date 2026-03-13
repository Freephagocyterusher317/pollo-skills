# Wan

Brand path segment: `wanx`
Models: 5

## wan-v2-2-flash

- **Endpoint**: `POST /generation/wanx/wan-v2-2-flash`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

- `image` (string) **(required)**
  Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `prompt` (string) **(required)** — maxLength: 800
  The prompt of the generation
- `negativePrompt` (string) — maxLength: 500
  The negative prompt of the generation
- `resolution` (string) — enum: `480P`, `720P`; default: `720P`
  The resolution of the generation
- `length` (number) — enum: `5`; default: `5`
  The length of the generation
- `seed` (number) — range: -2147483647
  The seed of the generation

## wan-v2-2-plus

- **Endpoint**: `POST /generation/wanx/wan-v2-2-plus`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `prompt` (string) **(required)** — maxLength: 800
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 500
    The negative prompt of the generation
  - `resolution` (string) — enum: `480P`, `1080P`; default: `1080P`
    The resolution of the generation
  - `length` (number) — enum: `5`; default: `5`
    The length of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 800
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 500
    The negative prompt of the generation
  - `length` (number) — enum: `5`; default: `5`
    The length of the generation
  - `resolution` (string) — enum: `480P`, `1080P`; default: `1080P`
    The resolution of the generation
  - `aspectRatio` (string) — enum: `1:1`, `4:3`, `3:4`, `16:9`, `9:16`; default: `16:9`
    The aspect ratio of the generation.

Wanx 2.2 in 480p does not support 4:3 or 3:4 aspect ratios.
  - `seed` (number) — range: -2147483647
    The seed of the generation

## wan-v2-5-preview

- **Endpoint**: `POST /generation/wanx/wan-v2-5-preview`
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
  - `negativePrompt` (string) — maxLength: 500
    The negative prompt of the generation
  - `length`:
    The length of the generation
  - `resolution` (string) — enum: `480P`, `720P`, `1080P`; default: `1080P`
    The resolution of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `audioUrl` (string)
    Audio URL for audio-driven generation
  - `wanAudio` (boolean) — default: `True`
    Enable audio generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 500
    The negative prompt of the generation
  - `length`:
    The length of the generation
  - `resolution` (string) — enum: `480P`, `720P`, `1080P`; default: `1080P`
    The resolution of the generation
  - `aspectRatio` (string) — enum: `1:1`, `4:3`, `3:4`, `16:9`, `9:16`; default: `16:9`
    The aspect ratio of the generation.

Wan 2.5 supports all aspect ratios across all resolutions.
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `audioUrl` (string)
    Audio URL for audio-driven generation
  - `wanAudio` (boolean) — default: `True`
    Enable audio generation

## wan-v2-6

- **Endpoint**: `POST /generation/wanx/wan-v2-6`
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
  - `negativePrompt` (string) — maxLength: 500
    The negative prompt of the generation
  - `length` (number) — enum: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`; default: `5`
    The length of the generation
  - `resolution` (string) — enum: `720P`, `1080P`; default: `1080P`
    The resolution of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `audioUrl` (string)
    Audio URL for audio-driven generation
  - `multiClip` (boolean) — default: `False`
  - `generateAudio` (boolean) — default: `True`
    Generate natural-sounding, fitting audio for the output video.
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 500
    The negative prompt of the generation
  - `length` (number) — enum: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`; default: `5`
    The length of the generation
  - `resolution` (string) — enum: `720P`, `1080P`; default: `1080P`
    The resolution of the generation
  - `aspectRatio` (string) — enum: `1:1`, `4:3`, `3:4`, `16:9`, `9:16`; default: `16:9`
    The aspect ratio of the generation.

Wan 2.6 supports all aspect ratios across all resolutions.
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `audioUrl` (string)
    Audio URL for audio-driven generation
  - `multiClip` (boolean) — default: `False`
  - `generateAudio` (boolean) — default: `True`
    Generate natural-sounding, fitting audio for the output video.

## wanx-v2-1

- **Endpoint**: `POST /generation/wanx/wanx-v2-1`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `prompt` (string) **(required)** — maxLength: 800
    The prompt of the generation
  - `mode` (string) — enum: `fast`, `pro`; default: `fast`
  - `length` (number) — enum: `5`; default: `5`
    The length of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 800
    The prompt of the generation
  - `mode` (string) — enum: `fast`, `pro`; default: `fast`
  - `length` (number) — enum: `5`; default: `5`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`; default: `16:9`
  - `seed` (number) — range: -2147483647
    The seed of the generation
