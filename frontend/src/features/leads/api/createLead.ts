import { api } from "@/lib/axios";
import {
  LeadSchema,
  type Lead,
  CreateLeadSchema,
  type CreateLeadInput,
} from "../types";

export async function createLead(input: CreateLeadInput): Promise<Lead> {
  const validInput = CreateLeadSchema.parse(input);

  const res = await api.post("/leads/", validInput);

  return LeadSchema.parse(res.data);
}
