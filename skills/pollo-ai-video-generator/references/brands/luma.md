# Luma

Brand path segment: `luma`
Models: 3

## luma-ray-1-6

- **Endpoint**: `POST /generation/luma/luma-ray-1-6`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `prompt` (string) — maxLength: 2000
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`
  - `imageTail` (string)
    URL of the tail image for video generation.
            Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `21:9`; default: `16:9`

## luma-ray-2-0

- **Endpoint**: `POST /generation/luma/luma-ray-2-0`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `prompt` (string) — maxLength: 2000
    The prompt of the generation
  - `resolution` (string) — enum: `540p`, `720p`, `1080p`, `4k`; default: `540p`
    The resolution of the generation
  - `length` (number) — enum: `5`, `9`; default: `5`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `9:21`; default: `16:9`
  - `imageTail` (string)
    URL of the tail image for video generation.
            Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
**Text To Video**:
  - `length` (number) — enum: `5`, `9`; default: `5`
    The length of the generation
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `9:21`; default: `16:9`
  - `resolution` (string) — enum: `540p`, `720p`, `1080p`, `4k`; default: `540p`
    The resolution of the generation

## luma-ray-2-0-flash

- **Endpoint**: `POST /generation/luma/luma-ray-2-0-flash`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `prompt` (string) — maxLength: 2000
    The prompt of the generation
  - `resolution` (string) — enum: `540p`, `720p`, `1080p`, `4k`; default: `540p`
    The resolution of the generation
  - `length` (number) — enum: `5`, `9`; default: `5`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `9:21`; default: `16:9`
  - `imageTail` (string)
    URL of the tail image for video generation.
            Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
**Text To Video**:
  - `length` (number) — enum: `5`, `9`; default: `5`
    The length of the generation
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `9:21`; default: `16:9`
  - `resolution` (string) — enum: `540p`, `720p`, `1080p`, `4k`; default: `540p`
    The resolution of the generation
