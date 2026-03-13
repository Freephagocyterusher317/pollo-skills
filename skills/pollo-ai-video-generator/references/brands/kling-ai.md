# Kling AI

Brand path segment: `kling-ai`
Models: 9

## kling-v1

- **Endpoint**: `POST /generation/kling-ai/kling-v1`
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
  - `negativePrompt` (string) — maxLength: 2500
    The negative prompt of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `strength` (number) — default: `50`; range: 0-100
    The prompt strength of the generation
  - `mode` (string) — enum: `std`, `pro`; default: `std`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2500
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`
  - `negativePrompt` (string) — maxLength: 2500
    The negative prompt of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `strength` (number) — default: `50`; range: 0-100
    The prompt strength of the generation
  - `mode`:
  - `cameraControl`:
    Variant 1:
      - `type` (string) **(required)** — enum: `simple`
      - `config` (object) **(required)**
        - `subType` (string) **(required)** — enum: `horizontal`, `vertical`, `pan`, `tilt`, `roll`, `zoom`
        - `value` (number) **(required)** — range: -10-10
    Variant 2:
      - `type` (string) **(required)** — enum: `down_back`
    Variant 3:
      - `type` (string) **(required)** — enum: `forward_up`
    Variant 4:
      - `type` (string) **(required)** — enum: `left_turn_forward`
    Variant 5:
      - `type` (string) **(required)** — enum: `right_turn_forward`

## kling-v1-5

- **Endpoint**: `POST /generation/kling-ai/kling-v1-5`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

- `image` (string) **(required)**
  Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `imageTail` (string)
  URL of the tail image for video generation.
            Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `prompt` (string) — maxLength: 2500
  The prompt of the generation
- `negativePrompt` (string) — maxLength: 2048
  The negative prompt of the generation
- `length` (number) — enum: `5`, `10`; default: `5`
  The length of the generation
- `strength` (number) — default: `50`; range: 0-100
  The prompt strength of the generation
- `mode` (string) — enum: `std`, `pro`; default: `std`

## kling-v1-6

- **Endpoint**: `POST /generation/kling-ai/kling-v1-6`
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
  - `prompt` (string) — maxLength: 2500
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 2048
    The negative prompt of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `strength` (number) — default: `50`; range: 0-100
    The prompt strength of the generation
  - `mode` (string) — enum: `std`, `pro`; default: `std`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2500
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`
  - `negativePrompt` (string) — maxLength: 2500
    The negative prompt of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `strength` (number) — default: `50`; range: 0-100
    The prompt strength of the generation

## kling-v2

- **Endpoint**: `POST /generation/kling-ai/kling-v2`
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
  - `negativePrompt` (string) — maxLength: 2500
    The negative prompt of the generation
  - `strength` (number) — default: `50`; range: 0-100
    The prompt strength of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2500
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`
  - `negativePrompt` (string) — maxLength: 2500
    The negative prompt of the generation
  - `strength` (number) — default: `50`; range: 0-100
    The prompt strength of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation

## kling-v2-1

- **Endpoint**: `POST /generation/kling-ai/kling-v2-1`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

- `image` (string) **(required)**
  Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `imageTail` (string)
  URL of the tail image for video generation.
            Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `prompt` (string) — maxLength: 2500
  The prompt of the generation
- `negativePrompt` (string) — maxLength: 2048
  The negative prompt of the generation
- `strength` (number) — default: `50`; range: 0-100
  The prompt strength of the generation
- `length` (number) — enum: `5`, `10`; default: `5`
  The length of the generation
- `mode` (string) — enum: `std`, `pro`; default: `std`

## kling-v2-1-master

- **Endpoint**: `POST /generation/kling-ai/kling-v2-1-master`
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
  - `negativePrompt` (string) — maxLength: 2500
    The negative prompt of the generation
  - `strength` (number) — default: `50`; range: 0-100
    The prompt strength of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2500
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`
  - `negativePrompt` (string) — maxLength: 2500
    The negative prompt of the generation
  - `strength` (number) — default: `50`; range: 0-100
    The prompt strength of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation

## kling-v2-5-turbo

- **Endpoint**: `POST /generation/kling-ai/kling-v2-5-turbo`
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
  - `prompt` (string) — maxLength: 1500
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 1500
    The negative prompt of the generation
  - `strength` (number) — default: `50`; range: 0-100
    The prompt strength of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `mode` (string) — enum: `std`, `pro`; default: `std`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 1500
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`
  - `negativePrompt` (string) — maxLength: 1500
    The negative prompt of the generation
  - `strength` (number) — default: `50`; range: 0-100
    The prompt strength of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation

## kling-v2-6

- **Endpoint**: `POST /generation/kling-ai/kling-v2-6`
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
  - `prompt` (string) — maxLength: 2500
    The prompt of the generation
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `generateAudio` (boolean) — default: `False`
    Generate natural-sounding, fitting audio for the output video.
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2500
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `generateAudio` (boolean) — default: `False`
    Generate natural-sounding, fitting audio for the output video.

## kling-video-o1

- **Endpoint**: `POST /generation/kling-ai/kling-video-o1`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

Variant 1:
  **Reference To Video**:
    - `images` (array[string]) **(required)**
      Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
    - `prompt` (string) — maxLength: 2500
      The prompt of the generation
    - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`
    - `length` (number) — enum: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`; default: `5`
      The length of the generation
    - `mode` (string) — enum: `pro`; default: `pro`
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
    - `prompt` (string) **(required)** — maxLength: 2500
      The prompt of the generation
    - `length` (number) — enum: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`; default: `5`
      The length of the generation
    - `mode` (string) — enum: `pro`; default: `pro`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2500
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`; default: `16:9`
  - `length` (number) — enum: `5`, `10`; default: `5`
    The length of the generation
  - `mode` (string) — enum: `pro`; default: `pro`
