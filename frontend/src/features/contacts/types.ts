import { z } from "zod";

// 🔹 Email Schema
export const ContactEmailSchema = z.object({
  id: z.number().int().optional(), // optional bei Create
  contact_id: z.number().int().optional(), // Backend vergibt das
  value: z.string().email("Bitte gültige E-Mail angeben"),
  is_primary: z.boolean(),
});

// 🔹 Contact Schema (Read-Model)
export const ContactSchema = z.object({
  id: z.number().int(),
  first_name: z.string().min(1, "Vorname ist erforderlich"),
  last_name: z.string().min(1, "Nachname ist erforderlich"),
  contact_emails: z.array(ContactEmailSchema),
});

export const ContactsSchema = z.array(ContactSchema);

// 🔹 Create Schema (für Form / POST)
export const CreateContactSchema = z.object({
  first_name: z.string().min(1, "Vorname ist erforderlich"),
  last_name: z.string().min(1, "Nachname ist erforderlich"),
  contact_emails: z
    .array(
      z.object({
        value: z.string().email("Bitte gültige E-Mail angeben"),
        is_primary: z.boolean(),
      }),
    )
    .min(1, "Mindestens eine E-Mail erforderlich"),
});

// 🔹 Update Schema (alles optional)
export const UpdateContactSchema = CreateContactSchema.partial().extend({
  contact_emails: z.array(ContactEmailSchema).optional(),
});

// 🔹 Types
export type ContactEmail = z.infer<typeof ContactEmailSchema>;
export type Contact = z.infer<typeof ContactSchema>;
export type CreateContactInput = z.infer<typeof CreateContactSchema>;
export type UpdateContactInput = z.infer<typeof UpdateContactSchema>;
