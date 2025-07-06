import { useEffect, useState } from "react";
import { getEntries } from "../api/api";

export default function EntryList() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    getEntries().then(setEntries);
  }, []);

  return (
    <div className="space-y-4 mt-6">
      {entries.map((entry, idx) => (
        <div key={idx} className="border p-4 rounded shadow">
          <p>{entry.message}</p>
          <p className="text-sm text-gray-500">Open on: {entry.openDate}</p>
        </div>
      ))}
    </div>
  );
}
