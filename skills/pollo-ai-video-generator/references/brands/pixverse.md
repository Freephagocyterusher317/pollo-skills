# Pixverse

Brand path segment: `pixverse`
Models: 5

## pixverse-v3-5

- **Endpoint**: `POST /generation/pixverse/pixverse-v3-5`
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
  - `prompt` (string) **(required)** — maxLength: 2048
    The prompt of the generation
  - `length` (number) — enum: `5`, `8`; default: `5`
    The length of the generation
  - `negativePrompt` (string) — maxLength: 2048
    The negative prompt of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `resolution` (string) — enum: `360p`, `540p`, `720p`, `1080p`; default: `360p`
    In Fast mode or 8s video, 1080p resolution isn't supported.
  - `style` (string) — enum: `auto`, `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`; default: `auto`
  - `mode` (string) — enum: `normal`, `fast`; default: `normal`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2048
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default: `16:9`
  - `length` (number) — enum: `5`, `8`; default: `5`
    The length of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `style` (string) — enum: `auto`, `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`; default: `auto`
  - `resolution` (string) — enum: `360p`, `540p`, `720p`, `1080p`; default: `360p`
    In Fast mode or 8s video, 1080p resolution isn't supported.
  - `mode` (string) — enum: `normal`, `fast`; default: `normal`

## pixverse-v4

- **Endpoint**: `POST /generation/pixverse/pixverse-v4`
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
  - `prompt` (string) **(required)** — maxLength: 2048
    The prompt of the generation
  - `length` (number) — enum: `5`, `8`; default: `5`
    The length of the generation
  - `negativePrompt` (string) — maxLength: 2048
    The negative prompt of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `resolution` (string) — enum: `360p`, `540p`, `720p`, `1080p`; default: `360p`
    In Fast mode or 8s video, 1080p resolution isn't supported.
  - `style` (string) — enum: `auto`, `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`; default: `auto`
  - `mode` (string) — enum: `normal`, `fast`; default: `normal`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2048
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default: `16:9`
  - `length` (number) — enum: `5`, `8`; default: `5`
    The length of the generation
  - `negativePrompt` (string) — maxLength: 2048
    The negative prompt of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `style` (string) — enum: `auto`, `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`; default: `auto`
  - `resolution` (string) — enum: `360p`, `540p`, `720p`, `1080p`; default: `360p`
    In Fast mode or 8s video, 1080p resolution isn't supported.
  - `mode` (string) — enum: `normal`, `fast`; default: `normal`

## pixverse-v4-5

- **Endpoint**: `POST /generation/pixverse/pixverse-v4-5`
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
  - `prompt` (string) **(required)** — maxLength: 2048
    The prompt of the generation
  - `length` (number) — enum: `5`, `8`; default: `5`
    The length of the generation
  - `negativePrompt` (string) — maxLength: 2048
    The negative prompt of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `resolution` (string) — enum: `360p`, `540p`, `720p`, `1080p`; default: `360p`
    In Fast mode or 8s video, 1080p resolution isn't supported.
  - `style` (string) — enum: `auto`, `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`; default: `auto`
  - `mode` (string) — enum: `normal`, `fast`; default: `normal`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2048
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default: `16:9`
  - `length` (number) — enum: `5`, `8`; default: `5`
    The length of the generation
  - `negativePrompt` (string) — maxLength: 2048
    The negative prompt of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `style` (string) — enum: `auto`, `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`; default: `auto`
  - `resolution` (string) — enum: `360p`, `540p`, `720p`, `1080p`; default: `360p`
    In Fast mode or 8s video, 1080p resolution isn't supported.
  - `mode` (string) — enum: `normal`, `fast`; default: `normal`

## pixverse-v5

- **Endpoint**: `POST /generation/pixverse/pixverse-v5`
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
  - `prompt` (string) **(required)** — maxLength: 2048
    The prompt of the generation
  - `length` (number) — enum: `5`, `8`; default: `5`
    The length of the generation
  - `negativePrompt` (string) — maxLength: 2048
    The negative prompt of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `resolution` (string) — enum: `360p`, `540p`, `720p`, `1080p`; default: `360p`
    The resolution of the generation
  - `style` (string) — enum: `auto`, `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`; default: `auto`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2048
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default: `16:9`
  - `length` (number) — enum: `5`, `8`; default: `5`
    The length of the generation
  - `negativePrompt` (string) — maxLength: 2048
    The negative prompt of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `style` (string) — enum: `auto`, `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`; default: `auto`
  - `resolution` (string) — enum: `360p`, `540p`, `720p`, `1080p`; default: `360p`
    The resolution of the generation

## pixverse-v5-5

- **Endpoint**: `POST /generation/pixverse/pixverse-v5-5`
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
  - `prompt` (string) **(required)** — maxLength: 2048
    The prompt of the generation
  - `length` (number) — enum: `5`, `8`, `10`; default: `5`
    The length of the generation
  - `negativePrompt` (string) — maxLength: 2048
    The negative prompt of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `resolution` (string) — enum: `360p`, `540p`, `720p`, `1080p`; default: `360p`
    In 10s video, 1080p resolution isn't supported.
  - `style` (string) — enum: `auto`, `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`; default: `auto`
  - `mode` (string) — enum: `normal`, `fast`; default: `normal`
  - `multiClip` (boolean) — default: `False`
  - `generateAudio` (boolean)
    Generate natural-sounding, fitting audio for the output video.
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 2048
    The prompt of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default: `16:9`
  - `length` (number) — enum: `5`, `8`, `10`; default: `5`
    The length of the generation
  - `negativePrompt` (string) — maxLength: 2048
    The negative prompt of the generation
  - `seed` (number) — range: -2147483647
    The seed of the generation
  - `style` (string) — enum: `auto`, `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`; default: `auto`
  - `resolution` (string) — enum: `360p`, `540p`, `720p`, `1080p`; default: `360p`
    In 10s video, 1080p resolution isn't supported.
  - `mode` (string) — enum: `normal`, `fast`; default: `normal`
  - `multiClip` (boolean) — default: `False`
  - `generateAudio` (boolean)
    Generate natural-sounding, fitting audio for the output video.
