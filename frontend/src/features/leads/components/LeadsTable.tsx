import type { Lead } from "../types";

export function LeadsTable({ leads }: { leads: Lead[] }) {
  if (!Array.isArray(leads)) {
    console.error("LeadsTable: expected array, got", leads);
    return <p>Ungültige Daten vom Server.</p>;
  }

  if (leads.length === 0) {
    return <p className="text-gray-500">Keine Leads vorhanden.</p>;
  }

  return (
    <ul className="space-y-2">
      {leads.map((lead) => (
        <li key={lead.id} className="border rounded p-3">
          <p className="font-medium">{lead.name}</p>
          <p className="text-sm text-gray-500">{lead.domain}</p>
          <p className="text-xs text-gray-400">{lead.status}</p>
        </li>
      ))}
    </ul>
  );
}
