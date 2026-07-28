import React from "react";
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import type { LowerThirdProps } from "../types";

/**
 * Animated lower-third graphic: accent bar + title/subtitle plate.
 * Slides in from the left with spring physics, holds, then exits.
 */
export const LowerThird: React.FC<LowerThirdProps> = ({
  title,
  subtitle = "",
  startFrame = 30,
  durationInFrames = 120,
  accentColor = "#E8A54B",
  backgroundColor = "rgba(12, 18, 28, 0.92)",
  textColor = "#FFFFFF",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const localFrame = frame - startFrame;
  if (localFrame < 0 || localFrame > durationInFrames) {
    return null;
  }

  const entrance = spring({
    frame: localFrame,
    fps,
    config: {
      damping: 16,
      stiffness: 130,
      mass: 0.65,
    },
  });

  const exitLead = 22;
  const exitStart = Math.max(0, durationInFrames - exitLead);
  const exitProgress = spring({
    frame: localFrame - exitStart,
    fps,
    config: {
      damping: 18,
      stiffness: 120,
      mass: 0.7,
    },
  });

  const isExiting = localFrame >= exitStart;

  const slideIn = interpolate(entrance, [0, 1], [-420, 0]);
  const slideOut = interpolate(exitProgress, [0, 1], [0, -420], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const translateX = isExiting ? slideOut : slideIn;

  const opacity = isExiting
    ? interpolate(exitProgress, [0, 1], [1, 0], {
        extrapolateLeft: "clamp",
        extrapolateRight: "clamp",
      })
    : interpolate(entrance, [0, 1], [0, 1]);

  // Accent bar grows ahead of the plate for a staged AE reveal.
  const barScaleY = interpolate(
    spring({
      frame: localFrame,
      fps,
      config: { damping: 12, stiffness: 180, mass: 0.4 },
    }),
    [0, 1],
    [0.15, 1],
  );

  const textReveal = spring({
    frame: Math.max(0, localFrame - 6),
    fps,
    config: { damping: 16, stiffness: 140, mass: 0.5 },
  });
  const textOpacity = isExiting
    ? opacity
    : interpolate(textReveal, [0, 1], [0, 1]);
  const textX = isExiting
    ? 0
    : interpolate(textReveal, [0, 1], [24, 0]);

  return (
    <AbsoluteFill
      style={{
        justifyContent: "flex-end",
        alignItems: "flex-start",
        paddingBottom: 72,
        paddingLeft: 56,
        pointerEvents: "none",
      }}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          alignItems: "stretch",
          opacity,
          transform: `translateX(${translateX}px)`,
          boxShadow: "0 12px 40px rgba(0,0,0,0.35)",
        }}
      >
        <div
          style={{
            width: 6,
            backgroundColor: accentColor,
            transform: `scaleY(${barScaleY})`,
            transformOrigin: "center bottom",
            borderRadius: 1,
          }}
        />
        <div
          style={{
            backgroundColor,
            padding: "16px 28px 18px 22px",
            minWidth: 280,
            maxWidth: 520,
          }}
        >
          <div
            style={{
              opacity: textOpacity,
              transform: `translateX(${textX}px)`,
              fontFamily:
                '"DM Sans", "Helvetica Neue", Helvetica, Arial, sans-serif',
              fontSize: 32,
              fontWeight: 700,
              color: textColor,
              letterSpacing: 0.3,
              lineHeight: 1.15,
            }}
          >
            {title}
          </div>
          {subtitle ? (
            <div
              style={{
                opacity: textOpacity,
                transform: `translateX(${textX}px)`,
                marginTop: 6,
                fontFamily:
                  '"DM Sans", "Helvetica Neue", Helvetica, Arial, sans-serif',
                fontSize: 18,
                fontWeight: 500,
                color: accentColor,
                letterSpacing: 1.2,
                textTransform: "uppercase",
              }}
            >
              {subtitle}
            </div>
          ) : null}
        </div>
      </div>
    </AbsoluteFill>
  );
};
