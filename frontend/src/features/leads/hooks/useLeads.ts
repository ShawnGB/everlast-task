import { useQuery } from "@tanstack/react-query";
import { getLeads } from "../api/getLeads";
import type { Lead } from "../types";

export function useLeads() {
  return useQuery<Lead[]>({
    queryKey: ["leads"],
    queryFn: getLeads,
    initialData: [],
  });
}
