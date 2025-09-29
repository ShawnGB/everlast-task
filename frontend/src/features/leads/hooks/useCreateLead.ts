import { useMutation, useQueryClient } from "@tanstack/react-query";
import { createLead } from "../api/createLead";
import type { CreateLeadInput, Lead } from "../types";

export const useCreateLead = () => {
  const queryClient = useQueryClient();

  return useMutation<Lead, Error, CreateLeadInput>({
    mutationFn: (data) => createLead(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["leads"] });
    },
  });
};
