import { z } from "zod";

const domainRegex = /^(https?:\/\/)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

export const LeadSchema = z.object({
  id: z.number().int(),
  name: z.string().min(1, "Name ist erforderlich"),
  domain: z
    .string()
    .min(1, "Domain ist erforderlich")
    .regex(
      domainRegex,
      "Bitte eine gültige Domain angeben (z.B. acme.com oder https://acme.com)",
    ),
  status: z.enum(["new", "qualified", "lost"]),
  created_at: z.string(), // robust: ISO-String
  primary_contact_id: z.number().nullable().optional(),
  primary_contact: z.any().nullable().optional(),
});

export const LeadsSchema = z.array(LeadSchema);

export const CreateLeadSchema = z.object({
  name: z.string().min(2, "Name muss mindestens 2 Zeichen haben"),
  domain: z
    .string()
    .min(1, "Domain ist erforderlich")
    .regex(
      domainRegex,
      "Bitte eine gültige Domain angeben (z.B. acme.com oder https://acme.com)",
    ),
  status: z.enum(["new", "qualified", "lost"]),
});

export type Lead = z.infer<typeof LeadSchema>;
export type CreateLeadInput = z.infer<typeof CreateLeadSchema>;

export const UpdateLeadSchema = CreateLeadSchema.partial();
export type UpdateLeadInput = z.infer<typeof UpdateLeadSchema>;
