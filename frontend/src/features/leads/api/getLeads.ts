import { api } from "@/lib/axios";
import type { Lead } from "../types";

export async function getLeads(): Promise<Lead[]> {
  const response = await api.get<Lead[]>("/leads/");
  return response.data;
}
