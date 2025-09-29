import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/axios";

export type Contact = {
  id: number;
  first_name: string;
  last_name: string;
  emails: { id: number; value: string; is_primary: boolean }[];
};

async function fetchContacts(): Promise<Contact[]> {
  const res = await api.get("/contacts");
  return res.data;
}

export function useContactsQuery() {
  return useQuery<Contact[]>({
    queryKey: ["contacts"],
    queryFn: fetchContacts,
  });
}
