# Pollo

Brand path segment: `pollo`
Models: 3

## pollo-v1-5

- **Endpoint**: `POST /generation/pollo/pollo-v1-5`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `prompt` (string) — maxLength: 2500
    The prompt of the generation
  - `imageTail` (string)
    URL of the tail image for video generation.
            Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2500
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`

## pollo-v1-6

- **Endpoint**: `POST /generation/pollo/pollo-v1-6`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `imageTail` (string)
    URL of the tail image for video generation.
            Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `prompt` (string) — maxLength: 1000
    The prompt of the generation
  - `resolution` (string) — enum: `480p`, `720p`, `1080p`; default: `480p`
    The resolution of the generation
  - `mode` (string) — enum: `basic`, `pro`; default: `basic`
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 1000
    The prompt of the generation
  - `resolution` (string) **(required)** — enum: `480p`, `720p`, `1080p`
    The resolution of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `mode` (string) — enum: `basic`, `pro`; default: `basic`
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`; default: `16:9`
  - `seed` (number) — range: -2147483647
    The seed of the generation

## pollo-v2-0

- **Endpoint**: `POST /generation/pollo/pollo-v2-0`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `prompt` (string) — maxLength: 2000
    The prompt of the generation
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `seed` (number)
    The seed of the generation
  - `generateAudio` (boolean)
    Generate natural-sounding, fitting audio for the output video.
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `resolution` (string) — enum: `480p`, `720p`, `1080p`; default: `720p`
    The resolution of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `seed` (number)
    The seed of the generation
  - `generateAudio` (boolean)
    Generate natural-sounding, fitting audio for the output video.
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `resolution` (string) — enum: `480p`, `720p`, `1080p`; default: `720p`
    The resolution of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`; default: `16:9`
