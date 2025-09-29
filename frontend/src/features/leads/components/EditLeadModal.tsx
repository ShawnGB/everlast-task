import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import type { Lead, UpdateLeadInput } from "../types";
import { UpdateLeadSchema } from "../types";
import { useUpdateLead } from "@/features/leads";

type Props = {
  lead: Lead;
  open: boolean;
  onClose: () => void;
};

export function EditLeadModal({ lead, open, onClose }: Props) {
  const { mutate, isPending } = useUpdateLead();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<UpdateLeadInput>({
    resolver: zodResolver(UpdateLeadSchema),
    defaultValues: {
      name: lead.name,
      domain: lead.domain,
      status: lead.status,
    },
  });

  const onSubmit = (data: UpdateLeadInput) => {
    mutate(
      { id: lead.id, data },
      {
        onSuccess: () => onClose(),
      },
    );
  };

  if (!open) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black/40 z-50">
      <div className="bg-white rounded-xl p-6 shadow-lg w-full max-w-md">
        <h2 className="text-lg font-bold mb-4">Lead bearbeiten</h2>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label className="block text-sm font-medium">Name</label>
            <input
              type="text"
              {...register("name")}
              className="border rounded w-full px-3 py-2"
            />
            {errors.name && (
              <p className="text-red-500 text-sm">{errors.name.message}</p>
            )}
          </div>

          <div>
            <label className="block text-sm font-medium">Domain</label>
            <input
              type="text"
              {...register("domain")}
              className="border rounded w-full px-3 py-2"
            />
            {errors.domain && (
              <p className="text-red-500 text-sm">{errors.domain.message}</p>
            )}
          </div>

          <div>
            <label className="block text-sm font-medium">Status</label>
            <select
              {...register("status")}
              className="border rounded w-full px-3 py-2"
            >
              <option value="new">Neu</option>
              <option value="qualified">Qualifiziert</option>
              <option value="lost">Verloren</option>
            </select>
            {errors.status && (
              <p className="text-red-500 text-sm">{errors.status.message}</p>
            )}
          </div>

          <div className="flex justify-end gap-2">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 rounded border"
            >
              Abbrechen
            </button>
            <button
              type="submit"
              disabled={isPending}
              className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:opacity-50"
            >
              {isPending ? "Speichern..." : "Speichern"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
