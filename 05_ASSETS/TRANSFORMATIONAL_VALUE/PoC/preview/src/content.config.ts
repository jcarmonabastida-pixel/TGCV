import { defineCollection, z } from "astro:content";
import { docsSchema } from "@astrojs/starlight/schema";

export const collections = {
  docs: defineCollection({
    schema: docsSchema({
      // Preserve the canonical TGCV editorial metadata in generated preview pages.
      extend: z.object({}).passthrough()
    })
  })
};
