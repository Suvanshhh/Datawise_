const API_BASE = "https://your-backend-domain.com";


export async function fetchDatasets() {
  const res = await fetch(`${API_BASE}/datasets`);
  if (!res.ok) throw new Error("Failed to fetch datasets");
  return res.json();
}

export async function createDataset(data) {
  const res = await fetch(`${API_BASE}/datasets`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to create dataset");
  return res.json();
}

export async function fetchDataset(id) {
  const res = await fetch(`${API_BASE}/datasets/${id}`);
  if (!res.ok) throw new Error("Dataset not found");
  return res.json();
}

export async function updateDataset(id, data) {
  const res = await fetch(`${API_BASE}/datasets/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to update dataset");
  return res.json();
}

export async function deleteDataset(id) {
  const res = await fetch(`${API_BASE}/datasets/${id}`, { method: "DELETE" });
  if (!res.ok) throw new Error("Failed to delete dataset");
  return res.json();
}

export async function fetchQualityLogs(datasetId) {
  const res = await fetch(`${API_BASE}/datasets/${datasetId}/quality-1`);
  if (!res.ok) throw new Error("Failed to fetch quality logs");
  return res.json();
}

export async function createQualityLog(datasetId, data) {
  const res = await fetch(`${API_BASE}/datasets/${datasetId}/quality-1`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to add quality log");
  return res.json();
}
