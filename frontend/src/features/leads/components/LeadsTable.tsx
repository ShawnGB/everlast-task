import { useState } from "react";
import type { Lead } from "../types";
import { useUpdateLead } from "@/features/leads";
import { EditLeadModal } from "./EditLeadModal";
import { DeleteLeadModal } from "./DeleteLeadModal";

export function LeadsTable({ leads }: { leads: Lead[] }) {
  const { mutate: updateStatus } = useUpdateLead();
  const [editLead, setEditLead] = useState<Lead | null>(null);
  const [deleteLead, setDeleteLead] = useState<Lead | null>(null);

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
    <>
      <ul className="space-y-2">
        {leads.map((lead) => (
          <li
            key={lead.id}
            className="border rounded p-3 flex justify-between items-center"
          >
            {/* Lead Info */}
            <div>
              <p className="font-medium">{lead.name}</p>
              <p className="text-sm text-gray-500">{lead.domain}</p>
            </div>

            {/* Status & Actions */}
            <div className="flex items-center gap-2">
              <select
                value={lead.status}
                onChange={(e) =>
                  updateStatus({
                    id: lead.id,
                    data: { status: e.target.value as Lead["status"] },
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

              {/* Bearbeiten Button */}
              <button
                onClick={() => setEditLead(lead)}
                className="px-2 py-1 text-sm text-blue-600 hover:underline"
              >
                Bearbeiten
              </button>

              {/* Löschen Button */}
              <button
                onClick={() => setDeleteLead(lead)}
                className="px-2 py-1 text-sm text-red-600 hover:underline"
              >
                Löschen
              </button>
            </div>
          </li>
        ))}
      </ul>

      {/* Edit Modal */}
      {editLead && (
        <EditLeadModal
          lead={editLead}
          open={!!editLead}
          onClose={() => setEditLead(null)}
        />
      )}

      {/* Delete Modal */}
      {deleteLead && (
        <DeleteLeadModal
          lead={deleteLead}
          open={!!deleteLead}
          onClose={() => setDeleteLead(null)}
        />
      )}
    </>
  );
}
