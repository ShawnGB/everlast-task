import { useState } from "react";
import { Modal } from "@/components/ui/Modal";
import { useDeleteLead } from "@/features/leads";
import type { Lead } from "../types";

type Props = {
  lead: Lead;
  open: boolean;
  onClose: () => void;
};

export function DeleteLeadModal({ lead, open, onClose }: Props) {
  const [confirmText, setConfirmText] = useState("");
  const { mutate, isPending } = useDeleteLead();

  const handleDelete = () => {
    mutate(lead.id, {
      onSuccess: () => {
        setConfirmText("");
        onClose();
      },
    });
  };

  return (
    <Modal open={open} onClose={onClose} title="Lead löschen">
      <p className="mb-4">
        Um <span className="font-semibold">{lead.name}</span> wirklich zu
        löschen, tippe bitte den Namen ein:
      </p>
      <input
        type="text"
        value={confirmText}
        onChange={(e) => setConfirmText(e.target.value)}
        className="border rounded w-full px-3 py-2 mb-4"
        placeholder={lead.name}
      />
      <button
        onClick={handleDelete}
        disabled={confirmText !== lead.name || isPending}
        className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 disabled:opacity-50"
      >
        {isPending ? "Wird gelöscht..." : "Löschen"}
      </button>
    </Modal>
  );
}
