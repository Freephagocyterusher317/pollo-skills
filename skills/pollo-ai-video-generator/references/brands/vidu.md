# Vidu

Brand path segment: `vidu`
Models: 6

## vidu-q1

- **Endpoint**: `POST /generation/vidu/vidu-q1`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `prompt` (string) — maxLength: 2500
    The prompt of the generation
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `imageTail` (string)
    URL of the tail image for video generation.
            Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `movementAmplitude` (string) — enum: `auto`, `small`, `medium`, `large`; default: `auto`
  - `length` (number) — enum: `5`; default: `5`
    The length of the generation
  - `resolution` (string) — enum: `1080p`; default: `1080p`
    The resolution of the generation
  - `seed` (number)
    The seed of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2500
    The prompt of the generation
  - `style` (string) — enum: `general`, `anime`; default: `general`
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`
  - `movementAmplitude` (string) — enum: `auto`, `small`, `medium`, `large`; default: `auto`
  - `length` (number) — enum: `5`; default: `5`
    The length of the generation
  - `resolution` (string) — enum: `1080p`; default: `1080p`
    The resolution of the generation
  - `seed` (number)
    The seed of the generation

## vidu-v1-5

- **Endpoint**: `POST /generation/vidu/vidu-v1-5`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `prompt` (string) — maxLength: 2500
    The prompt of the generation
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `imageTail` (string)
    URL of the tail image for video generation.
            Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `length` (number) — enum: `4`, `8`; default: `4`
    The length of the generation
  - `resolution` (string) — enum: `360p`, `720p`, `1080p`; default: `360p`
    The resolution of the generation
  - `movementAmplitude` (string) — enum: `auto`, `small`, `medium`, `large`; default: `auto`
  - `seed` (number)
    The seed of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2500
    The prompt of the generation
  - `style` (string) — enum: `general`, `anime`; default: `general`
  - `length` (number) — enum: `4`, `8`; default: `4`
    The length of the generation
  - `resolution` (string) — enum: `360p`, `720p`, `1080p`; default: `360p`
    The resolution of the generation
  - `movementAmplitude` (string) — enum: `auto`, `small`, `medium`, `large`; default: `auto`
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`
  - `seed` (number)
    The seed of the generation

## vidu-v2-0

- **Endpoint**: `POST /generation/vidu/vidu-v2-0`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

- `prompt` (string) — maxLength: 2500
  The prompt of the generation
- `image` (string) **(required)**
  Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `length` (number) — enum: `4`, `8`; default: `4`
  The length of the generation
- `resolution`:
  The resolution of the generation
- `imageTail` (string)
  URL of the tail image for video generation.
            Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `movementAmplitude` (string) — enum: `auto`, `small`, `medium`, `large`; default: `auto`
- `seed` (number)
  The seed of the generation

## viduq2-pro

- **Endpoint**: `POST /generation/vidu/viduq2-pro`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

- `prompt` (string) — maxLength: 2000
  The prompt of the generation
- `image` (string) **(required)**
  Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `imageTail` (string)
  URL of the tail image for video generation.
            Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `length` (number) — enum: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`; default: `5`
  The length of the generation
- `resolution` (string) — enum: `540p`, `720p`, `1080p`; default: `720p`
  The resolution of the generation
- `seed` (number)
  The seed of the generation
- `generateAudio` (boolean)
  Generate natural-sounding, fitting audio for the output video.

## viduq2-turbo

- **Endpoint**: `POST /generation/vidu/viduq2-turbo`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

- `prompt` (string) — maxLength: 2000
  The prompt of the generation
- `image` (string) **(required)**
  Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `length` (number) — enum: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`; default: `5`
  The length of the generation
- `resolution` (string) — enum: `540p`, `720p`, `1080p`; default: `720p`
  The resolution of the generation
- `seed` (number)
  The seed of the generation
- `generateAudio` (boolean)
  Generate natural-sounding, fitting audio for the output video.

## viduq3-pro

- **Endpoint**: `POST /generation/vidu/viduq3-pro`
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
  - `length` (number) — enum: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`; default: `5`
    The length of the generation
  - `resolution` (string) — enum: `360p`, `540p`, `720p`, `1080p`, `2K`; default: `720p`
    The resolution of the generation
  - `seed` (number)
    The seed of the generation
  - `generateAudio` (boolean) — default: `True`
    Generate natural-sounding, fitting audio for the output video.
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `length` (number) — enum: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`; default: `5`
    The length of the generation
  - `seed` (number)
    The seed of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default: `16:9`
  - `resolution` (string) — enum: `360p`, `540p`, `720p`, `1080p`, `2K`; default: `720p`
    The resolution of the generation
  - `generateAudio` (boolean) — default: `True`
    Generate natural-sounding, fitting audio for the output video.
