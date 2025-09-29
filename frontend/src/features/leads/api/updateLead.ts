import { api } from "@/lib/axios";
import type { Lead } from "../types";

export const updateLead = async (
  id: number,
  data: Partial<Lead>,
): Promise<Lead> => {
  const res = await api.put(`/leads/${id}`, data);
  return res.data;
};
