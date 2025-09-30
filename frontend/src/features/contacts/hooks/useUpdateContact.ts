import { useMutation, useQueryClient } from "@tanstack/react-query";
import { updateContact } from "@/features/contacts";
import type { UpdateContactInput } from "../types";

export const useUpdateContact = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, data }: { id: number; data: UpdateContactInput }) =>
      updateContact(id, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["contacts"] });
      queryClient.invalidateQueries({ queryKey: ["leads"] });
    },
  });
};
