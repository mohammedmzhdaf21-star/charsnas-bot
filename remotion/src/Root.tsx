import React from "react";
import { Composition, Folder } from "remotion";
import { VideoWithMotionGraphics } from "./VideoWithMotionGraphics";
import { EarAnatomyMotion } from "./EarAnatomyMotion";
import {
  VideoWithMotionGraphicsSchema,
  type VideoWithMotionGraphicsProps,
} from "./types";

export const defaultProps: VideoWithMotionGraphicsProps = {
  // Place your uploaded clip at remotion/public/upload.mp4 (or change this path).
  videoSrc: "upload.mp4",
  sceneChanges: [0, 90, 180, 300, 420],
  zoomIntensity: 1.18,
  zoomDurationInFrames: 36,
  overlayTexts: [
    {
      text: "OPENING SHOT",
      startFrame: 12,
      durationInFrames: 70,
      y: 0.28,
      fontSize: 76,
      color: "#FFFFFF",
    },
    {
      text: "SCENE CHANGE",
      startFrame: 100,
      durationInFrames: 65,
      y: 0.3,
      fontSize: 68,
      color: "#F5E6C8",
    },
    {
      text: "SPRING PHYSICS",
      startFrame: 190,
      durationInFrames: 70,
      y: 0.32,
      fontSize: 64,
      color: "#FFFFFF",
    },
  ],
  lowerThird: {
    title: "Alex Rivera",
    subtitle: "Creative Director",
    startFrame: 45,
    durationInFrames: 130,
    accentColor: "#E8A54B",
    backgroundColor: "rgba(12, 18, 28, 0.92)",
    textColor: "#FFFFFF",
  },
};

export const earAnatomyDefaultProps = {
  imageSrc: "ear-anatomy-poster.png",
  headline: "گرنگی؟",
  body: "وەک وردەکارییەکی پێشکەوتووی توێکاریی گوێ، بە بێدەنگی پاڵپشتی بیستن و هاوسەنگی دەکات",
  lowerThirdTitle: "توێکاریی گوێ",
  lowerThirdSubtitle: "بیستن و هاوسەنگی",
};

export const RemotionRoot: React.FC = () => {
  return (
    <Folder name="Motion-Graphics">
      <Composition
        id="VideoWithMotionGraphics"
        component={VideoWithMotionGraphics}
        durationInFrames={540}
        fps={30}
        width={1920}
        height={1080}
        schema={VideoWithMotionGraphicsSchema}
        defaultProps={defaultProps}
      />
      <Composition
        id="EarAnatomyMotion"
        component={EarAnatomyMotion}
        durationInFrames={240}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={earAnatomyDefaultProps}
      />
    </Folder>
  );
};
