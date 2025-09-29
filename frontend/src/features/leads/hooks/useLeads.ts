import { useQuery } from "@tanstack/react-query";
import { getLeads } from "../api/getLeads";
import type { Lead } from "../types";

export const useLeads = (search?: string) =>
  useQuery<Lead[], Error>({
    queryKey: ["leads", search],
    queryFn: () => getLeads(search),
    placeholderData: [],
  });
