import React, { useCallback, useMemo, useState } from "react";
import { Player } from "@remotion/player";
import { VideoWithMotionGraphics } from "./VideoWithMotionGraphics";
import type { VideoWithMotionGraphicsProps } from "./types";
import { defaultProps } from "./Root";

export type VideoUploadPlayerProps = {
  /** Composition width in pixels. */
  width?: number;
  /** Composition height in pixels. */
  height?: number;
  /** Total duration in frames. */
  durationInFrames?: number;
  fps?: number;
  /** Override motion-graphics defaults (merged with upload src). */
  motionProps?: Partial<Omit<VideoWithMotionGraphicsProps, "videoSrc">>;
};

/**
 * Host-app wrapper: pick a local video file, then preview it inside Remotion
 * with scene-change zooms, spring overlay text, and an animated lower-third.
 *
 * Example:
 * ```tsx
 * <VideoUploadPlayer width={960} height={540} />
 * ```
 */
export const VideoUploadPlayer: React.FC<VideoUploadPlayerProps> = ({
  width = 960,
  height = 540,
  durationInFrames = 540,
  fps = 30,
  motionProps,
}) => {
  const [objectUrl, setObjectUrl] = useState<string | null>(null);
  const [fileName, setFileName] = useState<string | null>(null);

  const onFileChange = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      const file = event.target.files?.[0];
      if (!file) {
        return;
      }
      setObjectUrl((prev) => {
        if (prev) {
          URL.revokeObjectURL(prev);
        }
        return URL.createObjectURL(file);
      });
      setFileName(file.name);
    },
    [],
  );

  const inputProps: VideoWithMotionGraphicsProps = useMemo(
    () => ({
      ...defaultProps,
      ...motionProps,
      videoSrc: objectUrl ?? defaultProps.videoSrc,
      lowerThird: {
        ...defaultProps.lowerThird!,
        ...motionProps?.lowerThird,
        title:
          motionProps?.lowerThird?.title ??
          fileName?.replace(/\.[^.]+$/, "") ??
          defaultProps.lowerThird!.title,
      },
    }),
    [objectUrl, fileName, motionProps],
  );

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: 16,
        fontFamily:
          '"DM Sans", "Helvetica Neue", Helvetica, Arial, sans-serif',
        color: "#1a1a1a",
        maxWidth: width,
      }}
    >
      <label
        style={{
          display: "inline-flex",
          alignItems: "center",
          gap: 10,
          padding: "12px 18px",
          background: "#0C121C",
          color: "#F5E6C8",
          cursor: "pointer",
          width: "fit-content",
          letterSpacing: 0.4,
          fontSize: 14,
          fontWeight: 600,
        }}
      >
        <input
          type="file"
          accept="video/*"
          onChange={onFileChange}
          style={{ display: "none" }}
        />
        {fileName ? `Replace video · ${fileName}` : "Upload video asset"}
      </label>

      {objectUrl ? (
        <Player
          component={VideoWithMotionGraphics}
          inputProps={inputProps}
          durationInFrames={durationInFrames}
          compositionWidth={width * 2}
          compositionHeight={height * 2}
          fps={fps}
          style={{ width, height }}
          controls
          loop
        />
      ) : (
        <div
          style={{
            width,
            height,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            background:
              "linear-gradient(145deg, #0C121C 0%, #1a2433 55%, #2a1f14 100%)",
            color: "#F5E6C8",
            fontSize: 18,
            letterSpacing: 0.6,
          }}
        >
          Upload a video to preview motion graphics
        </div>
      )}
    </div>
  );
};

export default VideoUploadPlayer;
