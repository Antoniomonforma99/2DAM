const http = require('http');

const hostname = '127.0.0.1';
const port = 1337;

http.createServer((req, res) => {
    res.writeHead(200,{
        'Content-Type' : 'text/html'
    });
    res.end('<h1>Hola Mundo</h1>')
}).listen(port, hostname, () => {
    console.log(`Servidor ejecutandose en http://${hostname}:${port}/`)
})