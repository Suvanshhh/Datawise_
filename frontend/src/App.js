import React, { useEffect, useState } from "react";
import {
  fetchDatasets, createDataset, fetchDataset,
  updateDataset, deleteDataset
} from "./api";
import DatasetForm from "./components/DatasetForm";
import DatasetList from "./components/DatasetList";
import DatasetDetails from "./components/DatasetDetails";
import "./App.css";


function App() {
  const [datasets, setDatasets] = useState([]);
  const [selected, setSelected] = useState(null);
  const [editMode, setEditMode] = useState(false);
  const [error, setError] = useState("");

  function loadDatasets() {
    fetchDatasets()
      .then(setDatasets)
      .catch((e) => setError(e.message));
  }

  useEffect(() => {
    loadDatasets();
  }, []);

  function handleSelect(ds) {
    fetchDataset(ds._id)
      .then(setSelected)
      .catch((e) => setError(e.message));
    setEditMode(false);
  }

  function handleCreate(data) {
    createDataset(data)
      .then(() => {
        loadDatasets();
        setError("");
      })
      .catch((e) => setError(e.message));
  }

  function handleDelete(id) {
    deleteDataset(id)
      .then(() => {
        loadDatasets();
        setSelected(null);
        setError("");
      })
      .catch((e) => setError(e.message));
  }

  function handleUpdate(ds) {
    setEditMode(true);
    setSelected(ds);
  }

  function handleEditSubmit(data) {
    updateDataset(selected._id, data)
      .then(() => {
        loadDatasets();
        setEditMode(false);
        setSelected(null);
        setError("");
      })
      .catch((e) => setError(e.message));
  }

  return (
    <div style={{ maxWidth: 700, margin: "2em auto", fontFamily: "sans-serif" }}>
      <h1>Datawise Dataset Catalog</h1>
      <h2>Create New Dataset</h2>
      <DatasetForm onSubmit={handleCreate} submitText="Create" />
      <h2>All Datasets</h2>
      <DatasetList datasets={datasets} onSelect={handleSelect} onDelete={handleDelete} />
      <hr />
      {editMode && selected ? (
        <div>
          <h2>Edit Dataset</h2>
          <DatasetForm
            onSubmit={handleEditSubmit}
            initialData={selected}
            submitText="Update"
          />
        </div>
      ) : (
        <DatasetDetails dataset={selected} onUpdate={handleUpdate} />
      )}
      {error && <div style={{ color: "red" }}>{error}</div>}
    </div>
  );
}

export default App;
