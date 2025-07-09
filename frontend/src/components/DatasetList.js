import React from "react";

export default function DatasetList({ datasets, onSelect, onDelete }) {
  if (!datasets.length) return <div>No datasets found.</div>;
  return (
    <ul>
      {datasets.map((ds) => (
        <li key={ds._id}>
          <span onClick={() => onSelect(ds)} style={{cursor:"pointer", fontWeight:"bold"}}>
            {ds.name}
          </span>
          {" "} (Owner: {ds.owner})
          <button onClick={() => onDelete(ds._id)} style={{marginLeft:"1em"}}>Delete</button>
        </li>
      ))}
    </ul>
  );
}
