import React, { useEffect, useState } from "react";
import { fetchQualityLogs, createQualityLog } from "../api";
import QualityLogForm from "./QualityLogForm";

export default function DatasetDetails({ dataset, onUpdate }) {
  const [logs, setLogs] = useState([]);
  const [error, setError] = useState("");
  const [refresh, setRefresh] = useState(0);

  useEffect(() => {
    if (dataset) {
      fetchQualityLogs(dataset._id)
        .then(setLogs)
        .catch((e) => setError(e.message));
    }
  }, [dataset, refresh]);

  function handleAddLog(data) {
    createQualityLog(dataset._id, data)
      .then(() => setRefresh((r) => r + 1))
      .catch((e) => setError(e.message));
  }

  if (!dataset) return <div>Select a dataset to view details.</div>;
  return (
    <div>
      <h2>{dataset.name}</h2>
      <div><b>Owner:</b> {dataset.owner}</div>
      <div><b>Description:</b> {dataset.description}</div>
      <div><b>Tags:</b> {dataset.tags && dataset.tags.join(", ")}</div>
      <h3>Quality Logs</h3>
      {logs.length === 0 ? <div>No logs yet.</div> :
        <ul>
          {logs.map((log) => (
            <li key={log._id}>
              [{log.status}] {log.details} <i>{new Date(log.timestamp).toLocaleString()}</i>
            </li>
          ))}
        </ul>
      }
      <QualityLogForm onSubmit={handleAddLog} />
      {error && <div style={{color:"red"}}>{error}</div>}
      <button onClick={() => onUpdate(dataset)}>Edit Dataset</button>
    </div>
  );
}
