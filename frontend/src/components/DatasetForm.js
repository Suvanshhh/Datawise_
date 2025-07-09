import React, { useState } from "react";

export default function DatasetForm({ onSubmit, initialData, submitText }) {
  const [form, setForm] = useState(
    initialData || { name: "", owner: "", description: "", tags: "" }
  );
  const [error, setError] = useState("");

  function handleChange(e) {
    const { name, value } = e.target;
    setForm((f) => ({ ...f, [name]: value }));
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (!form.name || !form.owner) {
      setError("Name and Owner are required.");
      return;
    }
    const tags = form.tags.split(",").map((t) => t.trim()).filter(Boolean);
    onSubmit({ ...form, tags });
    setForm({ name: "", owner: "", description: "", tags: "" });
    setError("");
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" placeholder="Name" value={form.name} onChange={handleChange} />
      <input name="owner" placeholder="Owner" value={form.owner} onChange={handleChange} />
      <input name="description" placeholder="Description" value={form.description} onChange={handleChange} />
      <input name="tags" placeholder="Tags (comma separated)" value={form.tags} onChange={handleChange} />
      <button type="submit">{submitText || "Submit"}</button>
      {error && <div style={{color:"red"}}>{error}</div>}
    </form>
  );
}
