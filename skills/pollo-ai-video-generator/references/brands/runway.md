# Runway

Brand path segment: `runway`
Models: 2

## runway-gen-3-turbo

- **Endpoint**: `POST /generation/runway/runway-gen-3-turbo`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

- `image` (string) **(required)**
  Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `prompt` (string) — maxLength: 1000
  The prompt of the generation
- `imageTail` (string)
  URL of the tail image for video generation.
            Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `length` (number) — enum: `5`, `10`; default: `5`
  The length of the generation
- `aspectRatio` (string) — enum: `5:3`, `3:5`; default: `5:3`
- `seed` (number)
  The seed of the generation

## runway-gen-4-turbo

- **Endpoint**: `POST /generation/runway/runway-gen-4-turbo`
- **Summary**: create video by text or image or reference image
- **Supports webhook**: yes (`webhookUrl` in request body)

### Input Parameters

- `image` (string) **(required)**
  Only image URLs are accepted (HTTPS preferred); base64 is not allowed.
            Supported formats include JPG, PNG, and JPEG.
            Image aspect ratio must be less than 1:4 or 4:1.
- `prompt` (string) — maxLength: 1000
  The prompt of the generation
- `length` (number) — enum: `5`, `10`; default: `5`
  The length of the generation
- `aspectRatio` (string) — enum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`; default: `16:9`
- `seed` (number)
  The seed of the generation
