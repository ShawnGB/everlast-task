import { LeadsTable, LeadsSearch, LeadsForm, useLeads } from ".";

export function LeadsPage() {
  const { data: leads = [], isLoading, isError } = useLeads();

  if (isLoading) return <p>Lade Leads...</p>;
  if (isError) return <p>Fehler beim Laden der Leads.</p>;

  return (
    <div className="p-6 space-y-6">
      <header>
        <h1 className="text-2xl font-bold">Leads</h1>
        <p className="text-gray-600">
          Verwalte deine Kontakte und Firmen-Leads
        </p>
      </header>

      <section>
        <LeadsSearch />
      </section>

      <section>
        <div className="p-6">
          <h1 className="text-2xl font-bold mb-4">Leads</h1>
          <LeadsTable leads={leads} />
        </div>
      </section>

      <section>
        <h2 className="text-xl font-semibold">Neuen Lead hinzufügen</h2>
        <LeadsForm />
      </section>
    </div>
  );
}
