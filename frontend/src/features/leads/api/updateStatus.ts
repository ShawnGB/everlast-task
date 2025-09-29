import { api } from "@/lib/axios";
import type { Lead } from "../types";

export const updateLeadStatus = async (
  id: number,
  status: Lead["status"],
): Promise<Lead> => {
  const res = await api.post(`/leads/${id}/status`, null, {
    params: { status },
  });
  return res.data;
};
