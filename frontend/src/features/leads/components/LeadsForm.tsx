export function LeadsForm() {
  return (
    <form className="space-y-2">
      <input className="border p-2 w-full" placeholder="Lead Name" />
      <input className="border p-2 w-full" placeholder="Domain" />
      <button className="bg-blue-500 text-white px-4 py-2 rounded">
        Speichern
      </button>
    </form>
  );
}
