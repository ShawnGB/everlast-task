import { useState, useEffect } from "react";

type Props = {
  onSearch: (term: string) => void;
};

export const LeadsSearch = ({ onSearch }: Props) => {
  const [term, setTerm] = useState("");

  // Debounce: warte 300ms nach Tipp
  useEffect(() => {
    const timeout = setTimeout(() => {
      onSearch(term);
    }, 300);
    return () => clearTimeout(timeout);
  }, [term, onSearch]);

  return (
    <input
      type="text"
      value={term}
      onChange={(e) => setTerm(e.target.value)}
      placeholder="Leads durchsuchen..."
      className="border rounded px-3 py-2 w-full"
    />
  );
};
