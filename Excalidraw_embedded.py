import React, { useRef } from "react";
import Excalidraw from "@excalidraw/excalidraw";

export default function Whiteboard() {
  const excalidrawRef = useRef(null);

  const handleExport = () => {
    if (excalidrawRef.current) {
      const api = excalidrawRef.current;
      const scene = api.getSceneElements();
      console.log("Exported elements:", scene);
    }
  };

  return (
    <div style={{ height: "100vh" }}>
      <Excalidraw
        ref={excalidrawRef}
        initialData={{
          elements: [],
          appState: { viewBackgroundColor: "#f9f9f9" }
        }}
      />
      <button onClick={handleExport} style={{ position: "absolute", top: 10, right: 10 }}>
        Export
      </button>
    </div>
  );
}
