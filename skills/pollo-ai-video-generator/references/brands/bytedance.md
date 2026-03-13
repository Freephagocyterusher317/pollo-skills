# Seedance (ByteDance)

Brand path segment: `bytedance`
Models: 4

## seedance

- **Endpoint**: `POST /generation/bytedance/seedance`
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
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `cameraFixed` (boolean) — default: `False`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 1000
    The prompt of the generation
  - `resolution` (string) **(required)** — enum: `480p`, `720p`, `1080p`
    The resolution of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`; default: `16:9`
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `cameraFixed` (boolean) — default: `False`

## seedance-1-5-pro

- **Endpoint**: `POST /generation/bytedance/seedance-1-5-pro`
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
  - `prompt` (string) — maxLength: 2000
    The prompt of the generation
  - `resolution` (string) — enum: `480p`, `720p`, `1080p`; default: `480p`
    The resolution of the generation
  - `length` (number) — enum: `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`; default: `5`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `21:9`; default: `16:9`
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `cameraFixed` (boolean) — default: `False`
  - `generateAudio` (boolean) — default: `False`
    Generate natural-sounding, fitting audio for the output video.
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `resolution` (string) **(required)** — enum: `480p`, `720p`, `1080p`
    The resolution of the generation
  - `length` (number) — enum: `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`; default: `5`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `21:9`; default: `16:9`
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `cameraFixed` (boolean) — default: `False`
  - `generateAudio` (boolean) — default: `False`
    Generate natural-sounding, fitting audio for the output video.

## seedance-pro

- **Endpoint**: `POST /generation/bytedance/seedance-pro`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `prompt` (string) — maxLength: 1000
    The prompt of the generation
  - `resolution` (string) — enum: `480p`, `720p`, `1080p`; default: `480p`
    The resolution of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `cameraFixed` (boolean) — default: `False`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 1000
    The prompt of the generation
  - `resolution` (string) **(required)** — enum: `480p`, `720p`, `1080p`
    The resolution of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`, `21:9`; default: `16:9`
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `cameraFixed` (boolean) — default: `False`

## seedance-pro-fast

- **Endpoint**: `POST /generation/bytedance/seedance-pro-fast`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
  - `prompt` (string) — maxLength: 1000
    The prompt of the generation
  - `resolution` (string) — enum: `480p`, `720p`, `1080p`; default: `480p`
    The resolution of the generation
  - `length` (number) — enum: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`; default: `5`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`, `21:9`; default: `16:9`
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `cameraFixed` (boolean) — default: `False`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 1000
    The prompt of the generation
  - `resolution` (string) **(required)** — enum: `480p`, `720p`, `1080p`
    The resolution of the generation
  - `length` (number) — enum: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`; default: `5`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`, `21:9`; default: `16:9`
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `cameraFixed` (boolean) — default: `False`
