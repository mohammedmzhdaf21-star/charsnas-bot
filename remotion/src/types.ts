import { z } from "zod";

/** A timed overlay caption with spring-driven entrance/exit. */
export const OverlayTextSchema = z.object({
  text: z.string(),
  startFrame: z.number().int().nonnegative(),
  durationInFrames: z.number().int().positive().default(90),
  /** Vertical position as a fraction of composition height (0–1). */
  y: z.number().min(0).max(1).default(0.35),
  fontSize: z.number().positive().default(72),
  color: z.string().default("#FFFFFF"),
});

/** Lower-third name plate content and timing. */
export const LowerThirdSchema = z.object({
  title: z.string(),
  subtitle: z.string().default(""),
  startFrame: z.number().int().nonnegative().default(30),
  durationInFrames: z.number().int().positive().default(120),
  accentColor: z.string().default("#E8A54B"),
  backgroundColor: z.string().default("rgba(12, 18, 28, 0.92)"),
  textColor: z.string().default("#FFFFFF"),
});

/**
 * Props for the main composition.
 * Place the uploaded video in `public/` (or pass a Remotion staticFile path / URL).
 */
export const VideoWithMotionGraphicsSchema = z.object({
  /** Path relative to `public/`, e.g. `upload.mp4`, or an absolute URL. */
  videoSrc: z.string(),
  /** Frame indices where a scene cut occurs — each triggers a dynamic zoom-in. */
  sceneChanges: z.array(z.number().int().nonnegative()).default([0, 90, 180, 300]),
  /** Peak scale during a scene-change zoom (1 = no zoom). */
  zoomIntensity: z.number().min(1).max(2).default(1.18),
  /** How many frames the zoom spring takes to settle. */
  zoomDurationInFrames: z.number().int().positive().default(36),
  overlayTexts: z.array(OverlayTextSchema).default([
    {
      text: "SCENE ONE",
      startFrame: 15,
      durationInFrames: 75,
      y: 0.28,
      fontSize: 72,
      color: "#FFFFFF",
    },
    {
      text: "DYNAMIC ZOOM",
      startFrame: 105,
      durationInFrames: 70,
      y: 0.32,
      fontSize: 64,
      color: "#F5E6C8",
    },
  ]),
  lowerThird: LowerThirdSchema.default({
    title: "Alex Rivera",
    subtitle: "Creative Director",
    startFrame: 45,
    durationInFrames: 120,
    accentColor: "#E8A54B",
    backgroundColor: "rgba(12, 18, 28, 0.92)",
    textColor: "#FFFFFF",
  }),
});

export type OverlayTextProps = z.infer<typeof OverlayTextSchema>;
export type LowerThirdProps = z.infer<typeof LowerThirdSchema>;
export type VideoWithMotionGraphicsProps = z.infer<
  typeof VideoWithMotionGraphicsSchema
>;
