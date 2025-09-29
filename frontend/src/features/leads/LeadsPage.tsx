import { useState } from "react";
import { LeadsTable, LeadsSearch, LeadsForm, useLeads } from ".";
import { Modal } from "@/components/ui/Modal";

export function LeadsPage() {
  const [search, setSearch] = useState("");
  const { data: leads = [], isLoading, isError } = useLeads(search);
  const [open, setOpen] = useState(false);

  if (isLoading) return <p>Lade Leads...</p>;
  if (isError) return <p>Fehler beim Laden der Leads.</p>;

  return (
    <div className="p-6 space-y-6">
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold">Leads</h1>
          <p className="text-gray-600">
            Verwalte deine Kontakte und Firmen-Leads
          </p>
        </div>
        <button
          onClick={() => setOpen(true)}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          + Neuen Lead hinzufügen
        </button>
      </header>

      <section>
        <LeadsSearch onSearch={setSearch} />
      </section>

      <section>
        <div className="p-6">
          <h2 className="text-xl font-semibold mb-4">Alle Leads</h2>
          <LeadsTable leads={leads} />
        </div>
      </section>

      {/* Modal für Formular */}
      <Modal
        open={open}
        onClose={() => setOpen(false)}
        title="Neuen Lead hinzufügen"
      >
        <LeadsForm />
      </Modal>
    </div>
  );
}
