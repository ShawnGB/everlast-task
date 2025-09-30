import { useMutation, useQueryClient } from "@tanstack/react-query";
import { createContact } from "@/features/contacts";
import type { CreateContactInput } from "../types";

export const useCreateContact = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (data: CreateContactInput) => createContact(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["contacts"] });
      queryClient.invalidateQueries({ queryKey: ["leads"] }); // weil Leads Contact referenzieren
    },
  });
};
