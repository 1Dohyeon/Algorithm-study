const express = require('express')  // express 모듈 가져옴
const app = express()  
const port = 5000

app.get('/', (req, res) => {
  res.send('Hello World! ~ 안녕하세요') // npm run start
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})