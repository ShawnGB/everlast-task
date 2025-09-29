import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useCreateLead } from "../hooks/useCreateLead";

// Zod Schema (kein leerer String mehr erlaubt!)
const leadSchema = z.object({
  name: z.string().min(2, "Name muss mindestens 2 Zeichen haben"),
  domain: z
    .string()
    .min(1, "Domain ist erforderlich")
    .url("Bitte eine gültige Domain angeben (z.B. https://acme.com)"),
  status: z.enum(["new", "qualified", "lost"]),
});

type LeadFormData = z.infer<typeof leadSchema>;

export function LeadsForm() {
  const { mutate, isPending } = useCreateLead();

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm<LeadFormData>({
    resolver: zodResolver(leadSchema),
  });

  const onSubmit = (data: LeadFormData) => {
    mutate(data, {
      onSuccess: () => reset(),
    });
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div>
        <label className="block text-sm font-medium">Name</label>
        <input
          type="text"
          {...register("name")}
          required
          className="border rounded w-full px-3 py-2"
        />
        {errors.name && (
          <p className="text-red-500 text-sm">{errors.name.message}</p>
        )}
      </div>

      <div>
        <label className="block text-sm font-medium">Domain</label>
        <input
          type="url"
          {...register("domain")}
          required
          placeholder="https://example.com"
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

      <button
        type="submit"
        disabled={isPending}
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:opacity-50"
      >
        {isPending ? "Wird gespeichert..." : "Erstellen"}
      </button>
    </form>
  );
}
