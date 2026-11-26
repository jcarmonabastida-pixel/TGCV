import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";

export default defineConfig({
  srcDir: "./src",
  outDir: "./dist",
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex]
  },
  integrations: [
    starlight({
      title: "Transformational Value — Chapter 3 PoC",
      customCss: ["./src/styles/katex.css"],
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
