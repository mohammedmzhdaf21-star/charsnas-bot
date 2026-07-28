# Remotion Motion Graphics

After Effects–style motion graphics for an uploaded video asset, built with [Remotion](https://www.remotion.dev/).

## Features

1. **Dynamic zoom on scene changes** — punch-in scale + subtle pan with spring settle on each cut in `sceneChanges`
2. **Overlay text with spring keyframes** — entrance/exit scale, opacity, Y travel, and letter-spacing bloom
3. **Animated lower-third** — accent bar reveal, plate slide-in, staged title/subtitle

## Quick start

```bash
cd remotion
npm install
# Put your clip here:
#   public/upload.mp4
npm start
```

Open Remotion Studio and select the `VideoWithMotionGraphics` composition.

### Render

```bash
npm run render
```

## Props

| Prop | Description |
|------|-------------|
| `videoSrc` | File under `public/` (e.g. `upload.mp4`) or an absolute/`blob:` URL |
| `sceneChanges` | Frame indices that trigger a zoom-in |
| `zoomIntensity` | Peak scale at cut (default `1.18`) |
| `zoomDurationInFrames` | Zoom spring settle length |
| `overlayTexts` | Array of timed titles (`text`, `startFrame`, `durationInFrames`, …) |
| `lowerThird` | Name plate (`title`, `subtitle`, timing, colors) |

## Upload in a host React app

Use `VideoUploadPlayer` to pick a local file and preview with `@remotion/player`:

```tsx
import { VideoUploadPlayer } from "./remotion/src/VideoUploadPlayer";

export function App() {
  return (
    <VideoUploadPlayer
      width={960}
      height={540}
      motionProps={{
        sceneChanges: [0, 60, 150, 240],
        lowerThird: {
          title: "Guest Name",
          subtitle: "Role / Title",
          startFrame: 30,
          durationInFrames: 120,
        },
      }}
    />
  );
}
```

## Project layout

```
remotion/
  public/                 # drop upload.mp4 here for Studio
  src/
    VideoWithMotionGraphics.tsx   # main composition
    VideoUploadPlayer.tsx         # file-upload + Player wrapper
    components/
      SceneZoom.tsx
      OverlayText.tsx
      LowerThird.tsx
    Root.tsx
    types.ts
```
