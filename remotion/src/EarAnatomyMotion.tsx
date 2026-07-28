import React from "react";
import {
  AbsoluteFill,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadFont } from "@remotion/google-fonts/NotoSansArabic";
import { SoundWaveBars } from "./components/SoundWaveBars";
import { LowerThird } from "./components/LowerThird";

const { fontFamily } = loadFont("normal", {
  weights: ["500", "800"],
  subsets: ["arabic"],
  ignoreTooManyRequestsWarning: true,
});

export type EarAnatomyMotionProps = {
  imageSrc: string;
  headline: string;
  body: string;
  lowerThirdTitle: string;
  lowerThirdSubtitle: string;
};

/**
 * Vertical motion graphic inspired by the ear-anatomy education poster:
 * Ken Burns zoom into the canal, spring Kurdish titles, animated sound wave,
 * and a broadcast-style lower-third.
 */
export const EarAnatomyMotion: React.FC<EarAnatomyMotionProps> = ({
  imageSrc,
  headline,
  body,
  lowerThirdTitle,
  lowerThirdSubtitle,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height, durationInFrames } = useVideoConfig();

  // Scene punches: intro settle → canal zoom → pull back slightly.
  const zoomA = spring({
    frame,
    fps,
    config: { damping: 200, stiffness: 40, mass: 1.2 },
  });
  const zoomB = spring({
    frame: frame - 70,
    fps,
    config: { damping: 28, stiffness: 90, mass: 0.8 },
  });
  const zoomC = spring({
    frame: frame - 160,
    fps,
    config: { damping: 22, stiffness: 80, mass: 0.85 },
  });

  const scale =
    interpolate(zoomA, [0, 1], [1.08, 1.0]) *
    interpolate(zoomB, [0, 1], [1, 1.22], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    }) *
    interpolate(zoomC, [0, 1], [1, 0.94], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });

  const panX = interpolate(zoomB, [0, 1], [0, width * 0.04], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const panY = interpolate(zoomB, [0, 1], [0, height * 0.06], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const headlineIn = spring({
    frame: frame - 8,
    fps,
    config: { damping: 14, stiffness: 150, mass: 0.55 },
  });
  const bodyIn = spring({
    frame: frame - 18,
    fps,
    config: { damping: 16, stiffness: 130, mass: 0.6 },
  });

  // Soft fade-out at the end.
  const outro = interpolate(
    frame,
    [durationInFrames - 20, durationInFrames - 1],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  const src = imageSrc.startsWith("http") ? imageSrc : staticFile(imageSrc);

  return (
    <AbsoluteFill style={{ backgroundColor: "#D8D8D8", opacity: outro }}>
      {/* Poster with dynamic zoom on “scene” beats */}
      <AbsoluteFill
        style={{
          transform: `translate(${panX}px, ${panY}px) scale(${scale})`,
          transformOrigin: "55% 62%",
        }}
      >
        <Img
          src={src}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
          }}
        />
      </AbsoluteFill>

      {/* Soft vignette so overlay type stays readable */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(220,220,220,0.55) 0%, rgba(220,220,220,0.05) 28%, rgba(220,220,220,0) 48%, rgba(40,40,40,0.18) 100%)",
          pointerEvents: "none",
        }}
      />

      {/* Spring headline */}
      <AbsoluteFill
        style={{
          justifyContent: "flex-start",
          alignItems: "center",
          paddingTop: height * 0.08,
          pointerEvents: "none",
        }}
      >
        <div
          dir="rtl"
          style={{
            fontFamily,
            fontWeight: 800,
            fontSize: Math.round(width * 0.11),
            color: "#1B2A4A",
            textAlign: "center",
            opacity: interpolate(headlineIn, [0, 1], [0, 1]),
            transform: `translateY(${interpolate(headlineIn, [0, 1], [36, 0])}px) scale(${interpolate(headlineIn, [0, 1], [0.86, 1])})`,
            textShadow: "0 2px 18px rgba(255,255,255,0.35)",
            lineHeight: 1.1,
          }}
        >
          {headline}
        </div>
        <div
          dir="rtl"
          style={{
            marginTop: 18,
            maxWidth: width * 0.82,
            fontFamily,
            fontWeight: 500,
            fontSize: Math.round(width * 0.038),
            color: "#243656",
            textAlign: "center",
            lineHeight: 1.55,
            opacity: interpolate(bodyIn, [0, 1], [0, 1]),
            transform: `translateY(${interpolate(bodyIn, [0, 1], [22, 0])}px)`,
          }}
        >
          {body}
        </div>
      </AbsoluteFill>

      <SoundWaveBars startFrame={28} y={0.56} x={0.4} widthFraction={0.55} />

      <LowerThird
        title={lowerThirdTitle}
        subtitle={lowerThirdSubtitle}
        startFrame={55}
        durationInFrames={110}
        accentColor="#E85D4C"
        backgroundColor="rgba(18, 28, 44, 0.92)"
        textColor="#FFFFFF"
        fontFamily={fontFamily}
        rtl
      />
    </AbsoluteFill>
  );
};
