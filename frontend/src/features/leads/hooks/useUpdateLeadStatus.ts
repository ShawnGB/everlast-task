import { useMutation, useQueryClient } from "@tanstack/react-query";
import { updateLeadStatus } from "@/features/leads";
import type { Lead } from "../types";

export const useUpdateLeadStatus = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, status }: { id: number; status: Lead["status"] }) =>
      updateLeadStatus(id, status),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["leads"] });
    },
  });
};
