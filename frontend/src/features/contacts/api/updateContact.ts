import { api } from "@/lib/axios";
import type { Contact, UpdateContactInput } from "../types";

export const updateContact = async (
  id: number,
  data: UpdateContactInput,
): Promise<Contact> => {
  const res = await api.put(`/contacts/${id}`, data);
  return res.data;
};
