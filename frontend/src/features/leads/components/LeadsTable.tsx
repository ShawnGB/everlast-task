import type { Lead } from "../types";
import { useUpdateLeadStatus } from "@/features/leads";

export function LeadsTable({ leads }: { leads: Lead[] }) {
  const { mutate } = useUpdateLeadStatus();

  if (!Array.isArray(leads)) {
    console.error("LeadsTable: expected array, got", leads);
    return <p>Ungültige Daten vom Server.</p>;
  }

  if (leads.length === 0) {
    return <p className="text-gray-500">Keine Leads vorhanden.</p>;
  }

  const statusColors: Record<Lead["status"], string> = {
    new: "bg-blue-100 text-blue-800",
    qualified: "bg-green-100 text-green-800",
    lost: "bg-red-100 text-red-800",
  };

  return (
    <ul className="space-y-2">
      {leads.map((lead) => (
        <li
          key={lead.id}
          className="border rounded p-3 flex justify-between items-center"
        >
          <div>
            <p className="font-medium">{lead.name}</p>
            <p className="text-sm text-gray-500">{lead.domain}</p>
          </div>

          <div>
            <select
              value={lead.status}
              onChange={(e) =>
                mutate({
                  id: lead.id,
                  status: e.target.value as Lead["status"],
                })
              }
              className={`px-2 py-1 rounded text-sm font-medium ${statusColors[lead.status]}`}
            >
              <option value="new" className="text-blue-800">
                Neu
              </option>
              <option value="qualified" className="text-green-800">
                Qualifiziert
              </option>
              <option value="lost" className="text-red-800">
                Verloren
              </option>
            </select>
          </div>
        </li>
      ))}
    </ul>
  );
}
