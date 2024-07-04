import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "withsophie",
  description: "withsophie site description",
  themeConfig: {
    logo: "/img/icon.png",
    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ],
    footer: {
      copyright:"Copyright © 2023 withsophie"
    }
  },
  locales: {
    root: {
      label: 'English',
      lang: 'en',
      link: '/en/',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/' },
          { text: 'Thinks', link: '/en/think/eternal_wisdom_knowledge' }
        ],

        sidebar: [
          {
            text: 'Thinks',
            items: [
              { text: 'The Wisdom of Eternal Life, the Knowledge of Eternal Life', link: '/en/think/eternal_wisdom_knowledge' },
              { text: 'New Magellan Project 🚀', link: '/en/think/new_magellan_project' },
              { text: 'Reading Should Aim to Understand the Author’s Intent', link: '/en/think/reading_understand_author_intention' },
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
          { text: '首页', link: '/' },
          { text: '思考', link: '/zh/think/eternal_wisdom_knowledge' }
        ],

        sidebar: [
          {
            text: '思考',
            items: [
              { text: '智者永生，知识永生', link: '/zh/think/eternal_wisdom_knowledge' },
              { text: '新麦哲伦计划 🚀', link: '/zh/think/new_magellan_project' },
              { text: '读书要洞悉作者的用意', link: '/zh/think/reading_understand_author_intention' },
            ]
          } 
        ],
      }
    }
  },
  
})
