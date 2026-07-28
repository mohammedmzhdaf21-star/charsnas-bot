import React from "react";
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import type { OverlayTextProps } from "../types";

type Props = OverlayTextProps & {
  /** Extra delay (in frames) before the exit spring begins relative to duration. */
  exitLeadInFrames?: number;
};

/**
 * Custom overlay title with spring keyframe physics for entrance and exit.
 * Mirrors AE-style text animators: scale + opacity + slight Y travel.
 */
export const OverlayText: React.FC<Props> = ({
  text,
  startFrame,
  durationInFrames,
  y = 0.35,
  fontSize = 72,
  color = "#FFFFFF",
  exitLeadInFrames = 18,
}) => {
  const frame = useCurrentFrame();
  const { fps, height } = useVideoConfig();

  const localFrame = frame - startFrame;
  if (localFrame < 0 || localFrame > durationInFrames) {
    return null;
  }

  const entrance = spring({
    frame: localFrame,
    fps,
    config: {
      damping: 14,
      stiffness: 160,
      mass: 0.55,
    },
  });

  const exitStart = Math.max(0, durationInFrames - exitLeadInFrames);
  const exitProgress = spring({
    frame: localFrame - exitStart,
    fps,
    config: {
      damping: 20,
      stiffness: 140,
      mass: 0.6,
    },
  });

  const enterScale = interpolate(entrance, [0, 1], [0.82, 1]);
  const enterOpacity = interpolate(entrance, [0, 1], [0, 1]);
  const enterY = interpolate(entrance, [0, 1], [28, 0]);

  const exitScale = interpolate(exitProgress, [0, 1], [1, 0.92], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const exitOpacity = interpolate(exitProgress, [0, 1], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const exitY = interpolate(exitProgress, [0, 1], [0, -16], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const isExiting = localFrame >= exitStart;
  const scale = isExiting ? exitScale : enterScale;
  const opacity = isExiting ? exitOpacity : enterOpacity;
  const translateY = isExiting ? exitY : enterY;

  // Soft letter-spacing bloom on entrance for a broadcast feel.
  const letterSpacing = interpolate(entrance, [0, 1], [10, 2]);

  return (
    <AbsoluteFill
      style={{
        justifyContent: "flex-start",
        alignItems: "center",
        paddingTop: height * y,
        pointerEvents: "none",
      }}
    >
      <div
        style={{
          opacity,
          transform: `translateY(${translateY}px) scale(${scale})`,
          fontFamily: '"Bebas Neue", "Arial Narrow", Impact, sans-serif',
          fontSize,
          fontWeight: 700,
          color,
          letterSpacing,
          textTransform: "uppercase",
          textAlign: "center",
          textShadow:
            "0 2px 24px rgba(0,0,0,0.55), 0 1px 2px rgba(0,0,0,0.8)",
          maxWidth: "90%",
          lineHeight: 1.05,
        }}
      >
        {text}
      </div>
    </AbsoluteFill>
  );
};
