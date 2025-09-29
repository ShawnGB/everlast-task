import { useMutation, useQueryClient } from "@tanstack/react-query";
import { updateLead } from "@/features/leads";
import type { Lead } from "../types";

export const useUpdateLead = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, data }: { id: number; data: Partial<Lead> }) =>
      updateLead(id, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["leads"] });
    },
  });
};
