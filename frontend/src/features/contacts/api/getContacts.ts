import { api } from "@/lib/axios";
import { ContactsSchema, type Contact } from "../types";

export const getContacts = async (): Promise<Contact[]> => {
  const res = await api.get("/contacts/");
  return ContactsSchema.parse(res.data);
};
