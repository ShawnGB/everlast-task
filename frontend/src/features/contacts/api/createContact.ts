import { api } from "@/lib/axios";
import type { Contact, CreateContactInput } from "../types";

export const createContact = async (
  data: CreateContactInput,
): Promise<Contact> => {
  const res = await api.post("/contacts/", data);
  return res.data;
};
