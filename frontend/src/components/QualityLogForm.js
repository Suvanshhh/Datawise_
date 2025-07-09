import React, { useState } from "react";

export default function QualityLogForm({ onSubmit }) {
  const [form, setForm] = useState({ status: "PASS", details: "" });
  const [error, setError] = useState("");

  function handleChange(e) {
    const { name, value } = e.target;
    setForm((f) => ({ ...f, [name]: value }));
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (!form.status) {
      setError("Status is required.");
      return;
    }
    onSubmit(form);
    setForm({ status: "PASS", details: "" });
    setError("");
  }

  return (
    <form onSubmit={handleSubmit}>
      <select name="status" value={form.status} onChange={handleChange}>
        <option value="PASS">PASS</option>
        <option value="FAIL">FAIL</option>
      </select>
      <input name="details" placeholder="Details" value={form.details} onChange={handleChange} />
      <button type="submit">Add Log</button>
      {error && <div style={{color:"red"}}>{error}</div>}
    </form>
  );
}
