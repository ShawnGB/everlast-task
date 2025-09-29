import { api } from "@/lib/axios";
import { LeadsSchema, type Lead } from "../types";

export const getLeads = async (q?: string): Promise<Lead[]> => {
  const res = await api.get("/leads/", {
    params: q ? { q } : {},
  });

  return LeadsSchema.parse(res.data);
};
