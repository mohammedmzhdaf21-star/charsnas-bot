import React from "react";
import {
  AbsoluteFill,
  OffthreadVideo,
  staticFile,
  useVideoConfig,
  Video,
} from "remotion";
import { SceneZoom } from "./components/SceneZoom";
import { OverlayText } from "./components/OverlayText";
import { LowerThird } from "./components/LowerThird";
import type { VideoWithMotionGraphicsProps } from "./types";

/**
 * Resolves a user-uploaded asset path.
 * - Relative paths (e.g. `upload.mp4`) are loaded from Remotion's `public/` folder.
 * - Absolute URLs (http/https/blob/data) are used as-is for Player uploads.
 */
function resolveVideoSrc(src: string): string {
  if (
    src.startsWith("http://") ||
    src.startsWith("https://") ||
    src.startsWith("blob:") ||
    src.startsWith("data:") ||
    src.startsWith("/")
  ) {
    return src;
  }
  return staticFile(src);
}

function isBrowserOnlySrc(src: string): boolean {
  return src.startsWith("blob:") || src.startsWith("data:");
}

/**
 * Remotion composition: uploaded video + AE-style motion graphics.
 *
 * Features
 * - Dynamic zoom-in on each scene change (`sceneChanges`)
 * - Overlay titles with spring keyframe physics
 * - Animated lower-third name plate
 *
 * Drop a file into `remotion/public/` and set `videoSrc` (or pass a blob URL
 * when driving this from `@remotion/player` after a file upload).
 */
export const VideoWithMotionGraphics: React.FC<VideoWithMotionGraphicsProps> = ({
  videoSrc,
  sceneChanges = [0, 90, 180, 300],
  zoomIntensity = 1.18,
  zoomDurationInFrames = 36,
  overlayTexts = [],
  lowerThird,
}) => {
  const { width, height } = useVideoConfig();
  const src = resolveVideoSrc(videoSrc);
  const mediaStyle: React.CSSProperties = {
    width,
    height,
    objectFit: "cover",
  };

  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      <SceneZoom
        sceneChanges={sceneChanges}
        zoomIntensity={zoomIntensity}
        zoomDurationInFrames={zoomDurationInFrames}
      >
        <AbsoluteFill>
          {/* Blob uploads need HTML5 <Video>; file renders use OffthreadVideo. */}
          {isBrowserOnlySrc(src) ? (
            <Video src={src} style={mediaStyle} />
          ) : (
            <OffthreadVideo src={src} style={mediaStyle} />
          )}
        </AbsoluteFill>
      </SceneZoom>

      {overlayTexts.map((overlay, index) => (
        <OverlayText key={`overlay-${index}-${overlay.startFrame}`} {...overlay} />
      ))}

      {lowerThird ? <LowerThird {...lowerThird} /> : null}
    </AbsoluteFill>
  );
};
