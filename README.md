# ChatGPTCrawler
Simple crawler for ChatGPT.
​
Due to the fact that ChatGPT's server is located overseas and cannot be accessed directly, there are many free mirror sites available in China that can be accessed directly.

This [GitHub project](https://github.com/LiLittleCat/awesome-free-chatgpt) collects a list of free ChatGPT mirror sites, which is continuously updated.

The demo here, which uses Selenium to automatically send questions and capture answers, however, not supporting context. 

All you need to do is set the URL of the mirror site, the XPath of the input box, and the XPath of the first reply message box.

​These mirror sites have usage limits for unregistered users (mainly based on IP address). You may consider using a proxy to access them.

Alternatively, you could modify the code to directly scrape answers from OpenAI's ChatGPT, which may be more stable than directly using the OpenAI API to retrieve answers.
