import { z } from "zod";

export const LeadSchema = z.object({
  id: z.number(),
  name: z.string(),
  domain: z.string().url().nullable(),
  status: z.enum(["new", "qualified", "lost"]),
  createdAt: z.string().datetime(),
  updatedAt: z.string().datetime(),
});

export const LeadsSchema = z.array(LeadSchema);

export const CreateLeadSchema = z.object({
  name: z.string().min(2, "Name muss mindestens 2 Zeichen haben"),
  domain: z.string().url("Bitte eine gültige Domain angeben"),
  status: z.enum(["new", "qualified", "lost"]),
});

export type Lead = z.infer<typeof LeadSchema>;
export type CreateLeadInput = z.infer<typeof CreateLeadSchema>;
