import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
  srcDir: "./src",
  outDir: "./dist",
  integrations: [
    starlight({
      title: "Transformational Value — Chapter 3 PoC",
      defaultLocale: "es",
      locales: {
        es: { label: "Español", lang: "es" },
        en: { label: "English", lang: "en" }
      },
      sidebar: [
        {
          label: "Capítulo 3 / Chapter 3",
          items: [
            { label: "Español", link: "/es/chapter-03/" },
            { label: "English", link: "/en/chapter-03/" }
          ]
        }
      ]
    })
  ]
});
