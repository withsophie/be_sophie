import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Think with Sophie",
  description: "May the Sophie be with you!",
  head: [['link', { rel: 'icon', href: '/favicon.ico' }]],
  cleanUrls: true,
  transformPageData(pageData) {
    // https://blog.withsophie.ai
    const canonicalUrl = `/${pageData.relativePath}`
      .replace(/index\.md$/, '')
      .replace(/\.md$/, '')

    pageData.frontmatter.head ??= []
    pageData.frontmatter.head.push([
      'link',
      { rel: 'canonical', href: canonicalUrl }
    ])
  },
  themeConfig: {
    logo: "/icon.png",
    logoLink: "http://think.withsophie.ai",
    lastUpdated: true,
    externalLinkIcon: false,
    socialLinks: [
      { icon: 'x', link: 'https://x.com/ThinkWithSophie' },
      { icon: 'discord', link: 'https://discord.gg/93NPYytEsJ' },
      { icon: 'github', link: 'https://github.com/withsophie' }
    ],
    footer: {
      copyright:"Copyright © 2024 WithSophie, Inc."
    }
  },
  locales: {
    root: {
      label: 'English',
      lang: 'en',
      link: '/en/',
      themeConfig: {
        nav: [
          { text: 'To Inspire', link: 'http://think.withsophie.ai' },
          {
            text: 'Applications',
            items: [
              { text: 'Sophie Mindmap', link: 'http://mm.withsophie.ai' },
              { text: 'Bubble Burster', link: 'http://bb.withsophie.ai' },
              { text: 'Sophie Reader', link: 'http://reader.withsophie.ai' },
              { text: 'Publish', link: 'http://publish.withsophie.ai/' },
            ]
          },
          { text: 'Roadmap', link: 'https://feedback.withsophie.ai/roadmap' },
          { text: 'Feedback', link: 'https://feedback.withsophie.ai' }
        ],

        sidebar: [
          {
            text: 'ABOUT',
            items: [
              { text: 'Vision and Slogans', link: '/en/about/slogan' },
              { text: 'Releases Notes', link: '/en/about/releasenotes' },
              
            ],
          },
          {
            text: 'SOPHIE STORY',
            items: [
              { text: 'Why we create WithSophie', link: '/en/about/why-do-i-want-to-create-withsophie' },
              { text: 'Exploring Ambiguity Reduction in Language with AI', link: '/en/about/Exploring-Ambiguity-Reduction-in-Language-with-AI' },
              
            ],
          },
          {
            text: 'THINKING STORY',
            items: [
              { text: 'The Eternal Wisdom', link: '/en/think/eternal_wisdom_knowledge' },
              { text: 'New Magellan Project', link: '/en/think/new_magellan_project' },
              { text: 'Reading need Understand the Author’s Intent', link: '/en/think/reading_understand_author_intention' },
              { text: 'The Story of SWOT Analysis', link: '/en/think/The_Story_of_SWOT_Analysis' },
              { text: 'The Story of Deconstructive Thinking Method', link: '/en/think/The_story_of_deconstructive_thinking_method' },
            ]
          } 
        ],
      }
    },
    zh: {
      label: '简体中文',
      lang: 'zh', // 可选，将作为 `lang` 属性添加到 `html` 标签中
      link: '/zh/',
      themeConfig: {
        nav: [
          { text: '首页', link: '/zh/index' },
          { text: '思考', link: '/zh/think/eternal_wisdom_knowledge' }
        ],

        sidebar: [
          {
            text: 'SOPHIE故事',
            items: [
              { text: 'WithSophie起源', link: '/zh/about/why-do-i-want-to-create-withsophie' },
              { text: '语言歧义和人工智能', link: '/zh/about/Exploring-Ambiguity-Reduction-in-Language-with-AI' },
              
            ],
          },
          {
            text: '思考故事',
            items: [
              { text: '智者永生，知识永生', link: '/zh/think/eternal_wisdom_knowledge' },
              { text: '新麦哲伦计划 🚀', link: '/zh/think/new_magellan_project' },
              { text: '读书要洞悉作者的用意', link: '/zh/think/reading_understand_author_intention' },
              { text: 'SWOT分析法', link: '/en/think/The_Story_of_SWOT_Analysis' },
              { text: '解构思考法的故事', link: '/zh/think/The_story_of_deconstructive_thinking_method' },
            ]
          } 
        ],
      }
    }
  },
  
})
