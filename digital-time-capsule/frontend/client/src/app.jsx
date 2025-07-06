import React, { useState } from "react";
import CreateCapsule from "./components/CreateCapsule";
import EntryList from "./components/EntryList";

export default function App() {
  const [reload, setReload] = useState(false);

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Digital Time Capsule</h1>
      <CreateCapsule onAdd={() => setReload(!reload)} />
      <EntryList key={reload} />
    </div>
  );
}
