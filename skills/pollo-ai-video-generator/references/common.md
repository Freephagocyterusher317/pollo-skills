# Common API Reference

## Authentication

All requests require the `X-API-KEY` header.

```
X-API-KEY: <your-api-key>
```

Get your API key at: https://pollo.ai/api-platform/keys

## Base URL

```
https://pollo.ai/api/platform
```

## Task Status

After creating a generation task, poll the status endpoint until completion.

### Query task generation status

- **Endpoint**: `GET /generation/{taskId}/status`

#### Response

- `taskId` (string) **(required)**
- `generations` (array[object]) **(required)**
  - `id` (string) **(required)**
  - `createdDate` (string)
  - `updatedDate` (string)
  - `status` (string) **(required)** — enum: `waiting`, `succeed`, `failed`, `processing`
  - `failMsg` (string) **(required)**
  - `url` (string) **(required)**
    All generated videos and images are stored for up to 14 days only; we cannot guarantee storage beyond that period.
  - `mediaType` (string) **(required)** — enum: `image`, `video`, `text`, `audio`

### Status Values

- `waiting` — task queued
- `processing` — generation in progress
- `succeed` — completed, video/image URL available
- `failed` — generation failed

### Polling Strategy

- Poll every 5-10 seconds
- Videos are stored for **2 weeks** — download promptly

## Credits

### get credit

- **Endpoint**: `POST /credit`

#### Request

- `taskType` (string) **(required)**
- `generationConfig` ()
- `templateId` (string)
- `templateCode` (string)
- `actualDuration` (number)
- `numOutputs` (number) — default: `1`
- `scale` (number)
- `imageUrl` (string)
- `videoUrl` (string)
- `addAudioAuto` (boolean)
- `audioPrompt` (string)
- `startClipTime` (number)
- `endClipTime` (number)

#### Response

- `cost` (number) **(required)**
- `singleCost` (number) **(required)**
- `discountCost` (number) **(required)**
- `discountSingleCost` (number) **(required)**

### get credit balance

- **Endpoint**: `GET /credit/balance`

#### Response

- `availableCredits` (number) **(required)**
- `totalCredits` (number) **(required)**

## File Upload

- **Endpoint**: `POST /file/sign`

#### Request

- `action` (string) **(required)**
- `filename` (string) **(required)**
- `type` (string) **(required)**
- `userId` (string)

## Webhooks

Instead of polling, you can configure a `webhookUrl` in the generation request.
The webhook will be called when the task completes.

### Signature Verification

Webhooks include an `X-Signature` header for HMAC-SHA-256 verification.
Get your Secret Key at: https://pollo.ai/api-platform/keys (Secret Key tab).

```python
import hmac, hashlib

signature = hmac.new(secret_key.encode(), request_body, hashlib.sha256).hexdigest()
# Compare with X-Signature header
```

### Retry Mechanism

Failed webhook deliveries are retried up to 10 times with exponential backoff.

## Response Wrapper

All successful API responses are wrapped in a standard envelope:

```json
{
  "code": "SUCCESS",
  "message": "success",
  "data": { ... }
}
```

Always extract the actual payload from the `data` field. The schemas documented below describe the contents of `data`, not the top-level response.

## Error Response Format

```json
{
  "code": "ERROR_CODE",
  "message": "error description"
}
```
