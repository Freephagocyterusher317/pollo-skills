# Google Veo

Brand path segment: `google`
Models: 5

## veo2

- **Endpoint**: `POST /generation/google/veo2`
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
  - `length` (number) — enum: `5`, `8`; default: `5`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `9:16`
  - `resolution` (string) — enum: `720p`; default: `720p`
    The resolution of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `length` (number) — enum: `5`, `8`; default: `5`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
  - `resolution` (string) — enum: `720p`; default: `720p`
    The resolution of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation

## veo3

- **Endpoint**: `POST /generation/google/veo3`
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
  - `length` (number) — enum: `4`, `6`, `8`; default: `8`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
  - `resolution` (string) — enum: `720p`, `1080p`; default: `720p`
    The resolution of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `generateAudio` (boolean) — default: `True`
    Generate natural-sounding, fitting audio for the output video.
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 2000
    The negative prompt of the generation
  - `length` (number) — enum: `4`, `6`, `8`; default: `8`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
  - `resolution` (string) — enum: `720p`, `1080p`; default: `720p`
    The resolution of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `generateAudio` (boolean) — default: `True`
    Generate natural-sounding, fitting audio for the output video.

## veo3-1

- **Endpoint**: `POST /generation/google/veo3-1`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

Variant 1:
  **Reference To Video**:
    - `images` (array[string]) **(required)**
      Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
    - `prompt` (string) — maxLength: 2000
      The prompt of the generation
    - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
    - `resolution` (string) — enum: `720p`, `1080p`, `4k`; default: `720p`
      The resolution of the generation
    - `duration` (number) — enum: `8`; default: `8`
    - `seed` (number) — range: -2147483647
      The seed of the generation
    - `generateAudio` (boolean) — default: `True`
      Generate natural-sounding, fitting audio for the output video.
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
    - `length` (number) — enum: `4`, `6`, `8`; default: `8`
      The length of the generation
    - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
    - `resolution` (string) — enum: `720p`, `1080p`, `4k`; default: `720p`
      The resolution of the generation
    - `seed` (number) — range: -2147483647
      The seed of the generation
    - `generateAudio` (boolean) — default: `True`
      Generate natural-sounding, fitting audio for the output video.
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `length` (number) — enum: `4`, `6`, `8`; default: `8`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
  - `resolution` (string) — enum: `720p`, `1080p`, `4k`; default: `720p`
    The resolution of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `generateAudio` (boolean) — default: `True`
    Generate natural-sounding, fitting audio for the output video.

## veo3-1-fast

- **Endpoint**: `POST /generation/google/veo3-1-fast`
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
  - `length` (number) — enum: `4`, `6`, `8`; default: `8`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
  - `resolution` (string) — enum: `720p`, `1080p`, `4k`; default: `720p`
    The resolution of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `generateAudio` (boolean) — default: `True`
    Generate natural-sounding, fitting audio for the output video.
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `length` (number) — enum: `4`, `6`, `8`; default: `8`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
  - `resolution` (string) — enum: `720p`, `1080p`, `4k`; default: `720p`
    The resolution of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `generateAudio` (boolean) — default: `True`
    Generate natural-sounding, fitting audio for the output video.

## veo3-fast

- **Endpoint**: `POST /generation/google/veo3-fast`
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
  - `length` (number) — enum: `4`, `6`, `8`; default: `8`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
  - `resolution` (string) — enum: `720p`, `1080p`; default: `720p`
    The resolution of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `generateAudio` (boolean) — default: `True`
    Generate natural-sounding, fitting audio for the output video.
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2000
    The prompt of the generation
  - `negativePrompt` (string) — maxLength: 2000
    The negative prompt of the generation
  - `length` (number) — enum: `4`, `6`, `8`; default: `8`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
  - `resolution` (string) — enum: `720p`, `1080p`; default: `720p`
    The resolution of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `generateAudio` (boolean) — default: `True`
    Generate natural-sounding, fitting audio for the output video.
