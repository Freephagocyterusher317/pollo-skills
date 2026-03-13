# Hailuo (Minimax)

Brand path segment: `minimax`
Models: 5

## minimax-hailuo-02

- **Endpoint**: `POST /generation/minimax/minimax-hailuo-02`
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
  - `promptOptimizer` (boolean) — default: `True`
  - `resolution` (string) — enum: `512P`, `768P`, `1080P`; default: `768P`
    The resolution of the generation
  - `length` (number) — enum: `6`, `10`; default: `6`
    The length of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `resolution` (string) — enum: `768P`, `1080P`; default: `768P`
    The resolution of the generation
  - `length` (number) — enum: `6`, `10`; default: `6`
    The length of the generation

## minimax-hailuo-2.3

- **Endpoint**: `POST /generation/minimax/minimax-hailuo-2.3`
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
  - `promptOptimizer` (boolean) — default: `True`
  - `resolution` (string) — enum: `768P`, `1080P`; default: `768P`
    The resolution of the generation
  - `length` (number) — enum: `6`, `10`; default: `6`
    The length of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `resolution` (string) — enum: `768P`, `1080P`; default: `768P`
    The resolution of the generation
  - `length` (number) — enum: `6`, `10`; default: `6`
    The length of the generation

## minimax-hailuo-2.3-fast

- **Endpoint**: `POST /generation/minimax/minimax-hailuo-2.3-fast`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

- `image` (string) **(required)**
  Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `prompt` (string) — maxLength: 2000
  The prompt of the generation
- `promptOptimizer` (boolean) — default: `True`
- `resolution` (string) — enum: `768P`, `1080P`; default: `768P`
  The resolution of the generation
- `length` (number) — enum: `6`, `10`; default: `6`
  The length of the generation

## video-01

- **Endpoint**: `POST /generation/minimax/video-01`
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
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation

## video-01-live2d

- **Endpoint**: `POST /generation/minimax/video-01-live2d`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

- `prompt` (string) — maxLength: 2000
  The prompt of the generation
- `image` (string) **(required)**
  Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
