import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

type SceneZoomProps = {
  /** Frame indices where scene cuts occur. */
  sceneChanges: number[];
  /** Peak scale at the start of each zoom (eases back toward 1). */
  zoomIntensity: number;
  /** Approximate settle length for the zoom spring. */
  zoomDurationInFrames: number;
  children: React.ReactNode;
};

/**
 * Applies an After Effects-style punch-in zoom on each scene change.
 * Uses Remotion spring physics so the scale overshoots slightly then settles.
 */
export const SceneZoom: React.FC<SceneZoomProps> = ({
  sceneChanges,
  zoomIntensity,
  zoomDurationInFrames,
  children,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Find the most recent scene change that still influences the current frame.
  const activeCut = [...sceneChanges]
    .filter((cut) => frame >= cut && frame < cut + zoomDurationInFrames * 2)
    .sort((a, b) => b - a)[0];

  let scale = 1;
  let panX = 0;
  let panY = 0;

  if (activeCut !== undefined) {
    const localFrame = frame - activeCut;
    const progress = spring({
      frame: localFrame,
      fps,
      config: {
        damping: 18,
        stiffness: 120,
        mass: 0.7,
      },
      durationInFrames: zoomDurationInFrames,
    });

    // Start punched-in, ease toward 1 with a slight overshoot from the spring.
    scale = interpolate(progress, [0, 1], [zoomIntensity, 1], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });

    // Subtle directional drift based on which cut index for variety.
    const cutIndex = sceneChanges.indexOf(activeCut);
    const direction = cutIndex % 2 === 0 ? 1 : -1;
    const drift = interpolate(progress, [0, 1], [12 * direction, 0], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });
    panX = drift;
    panY = drift * 0.35;
  }

  return (
    <AbsoluteFill
      style={{
        transform: `translate(${panX}px, ${panY}px) scale(${scale})`,
        transformOrigin: "50% 50%",
      }}
    >
      {children}
    </AbsoluteFill>
  );
};
