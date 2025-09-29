import { useQuery } from "@tanstack/react-query";
import { getLeads } from "../api/getLeads";
import { LeadsSchema, type Lead } from "../types";

export const useLeads = (search?: string) =>
  useQuery<Lead[], Error>({
    queryKey: ["leads", search],
    queryFn: async () => {
      const data = await getLeads(search);

      return LeadsSchema.parse(data);
    },
    placeholderData: [],
  });
