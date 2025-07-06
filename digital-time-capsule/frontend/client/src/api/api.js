const API_URL = "http://localhost:5000/api";

export async function createEntry(entry) {
  return fetch(`${API_URL}/entry`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(entry),
  }).then((res) => res.json());
}

export async function getEntries() {
  return fetch(`${API_URL}/entries`).then((res) => res.json());
}
