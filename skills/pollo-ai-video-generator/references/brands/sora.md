# Sora

Brand path segment: `sora`
Models: 2

## sora-2

- **Endpoint**: `POST /generation/sora/sora-2`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
            Videos with human faces are not permitted.
                  Images with an incorrect aspect ratio will be auto-cropped.
  - `prompt` (string) — maxLength: 4000
    The prompt of the generation
  - `length` (number) **(required)** — enum: `4`, `8`, `12`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 4000
    The prompt of the generation
  - `length` (number) **(required)** — enum: `4`, `8`, `12`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`

## sora-2-pro

- **Endpoint**: `POST /generation/sora/sora-2-pro`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

**Image To Video**:
  - `image` (string) **(required)**
    Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
            Videos with human faces are not permitted.
                  Images with an incorrect aspect ratio will be auto-cropped.
  - `prompt` (string) — maxLength: 4000
    The prompt of the generation
  - `length` (number) **(required)** — enum: `4`, `8`, `12`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
  - `resolution` (string) — enum: `720p`, `1080p`; default: `1080p`
    The resolution of the generation
**Text To Video**:
  - `prompt` (string) **(required)** — maxLength: 4000
    The prompt of the generation
  - `length` (number) **(required)** — enum: `4`, `8`, `12`
    The length of the generation
  - `aspectRatio` (string) — enum: `16:9`, `9:16`; default: `16:9`
  - `resolution` (string) — enum: `720p`, `1080p`; default: `1080p`
    The resolution of the generation
