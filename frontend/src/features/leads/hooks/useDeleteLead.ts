import { useMutation, useQueryClient } from "@tanstack/react-query";
import { deleteLead } from "@/features/leads";

export const useDeleteLead = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (id: number) => deleteLead(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["leads"] });
    },
  });
};
