import React, { useMemo } from "react";
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

const BAR_COUNT = 48;

const barColor = (t: number): string => {
  // Rainbow: purple → pink → blue → orange/red → yellow → green
  const stops = [
    [124, 58, 237], // purple
    [236, 72, 153], // pink
    [59, 130, 246], // blue
    [249, 115, 22], // orange
    [239, 68, 68], // red
    [234, 179, 8], // yellow
    [132, 204, 22], // green
  ];
  const scaled = t * (stops.length - 1);
  const i = Math.min(Math.floor(scaled), stops.length - 2);
  const f = scaled - i;
  const a = stops[i];
  const b = stops[i + 1];
  const r = Math.round(a[0] + (b[0] - a[0]) * f);
  const g = Math.round(a[1] + (b[1] - a[1]) * f);
  const bl = Math.round(a[2] + (b[2] - a[2]) * f);
  return `rgb(${r},${g},${bl})`;
};

type SoundWaveBarsProps = {
  startFrame?: number;
  /** Vertical center of the wave as fraction of height. */
  y?: number;
  /** Left edge as fraction of width. */
  x?: number;
  widthFraction?: number;
  maxBarHeight?: number;
};

/**
 * AE-style animated frequency bars with spring entrance + continuous bounce.
 */
export const SoundWaveBars: React.FC<SoundWaveBarsProps> = ({
  startFrame = 20,
  y = 0.58,
  x = 0.42,
  widthFraction = 0.52,
  maxBarHeight = 160,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const local = frame - startFrame;

  const heights = useMemo(() => {
    return Array.from({ length: BAR_COUNT }, (_, i) => {
      const envelope = Math.sin((i / (BAR_COUNT - 1)) * Math.PI);
      const peakBoost = Math.exp(-Math.pow((i - BAR_COUNT * 0.55) / 8, 2)) * 0.55;
      return 0.25 + envelope * 0.55 + peakBoost;
    });
  }, []);

  if (local < 0) {
    return null;
  }

  const entrance = spring({
    frame: local,
    fps,
    config: { damping: 14, stiffness: 120, mass: 0.55 },
  });

  const containerWidth = width * widthFraction;
  const barGap = 3;
  const barWidth = (containerWidth - barGap * (BAR_COUNT - 1)) / BAR_COUNT;

  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      <div
        style={{
          position: "absolute",
          left: width * x,
          top: height * y,
          width: containerWidth,
          height: maxBarHeight,
          display: "flex",
          alignItems: "flex-end",
          gap: barGap,
          opacity: interpolate(entrance, [0, 1], [0, 1]),
          transform: `translateY(${interpolate(entrance, [0, 1], [24, 0])}px)`,
        }}
      >
        {heights.map((base, i) => {
          const pulse =
            0.65 +
            0.35 *
              Math.sin(local * 0.22 + i * 0.45) *
              Math.sin(local * 0.11 + i * 0.2);
          const barSpring = spring({
            frame: Math.max(0, local - i * 0.6),
            fps,
            config: { damping: 12, stiffness: 160, mass: 0.4 },
          });
          const h =
            maxBarHeight *
            base *
            pulse *
            interpolate(barSpring, [0, 1], [0.08, 1]);

          return (
            <div
              key={i}
              style={{
                width: barWidth,
                height: Math.max(4, h),
                borderRadius: barWidth / 2,
                backgroundColor: barColor(i / (BAR_COUNT - 1)),
                boxShadow: `0 0 8px ${barColor(i / (BAR_COUNT - 1))}55`,
              }}
            />
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
