export type LeadStatus = "new" | "qualified" | "lost";

export type Lead = {
  id: string;
  name: string;
  domain: string;
  status: LeadStatus;
  created_at: string;
};
