import React, { useState } from "react";
import CreateCapsule from "./components/CreateCapsule";
import EntryList from "./components/EntryList";
import Header from "./components/Header"

export default function App() {
  const [reload, setReload] = useState(false);

  return (
    <div className="container mx-auto p-6">
      <Header />
      <main className="container mx-auto p-6">
      <CreateCapsule onAdd={() => setReload(!reload)} />
      </main>
    </div>
  );
}
