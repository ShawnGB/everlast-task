import { api } from "@/lib/axios";

export const deleteContact = async (id: number): Promise<void> => {
  await api.delete(`/contacts/${id}`);
};
