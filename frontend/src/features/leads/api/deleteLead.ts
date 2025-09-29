import { api } from "@/lib/axios";

export const deleteLead = async (id: number): Promise<void> => {
  await api.delete(`/leads/${id}`);
};
