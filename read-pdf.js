const fs = require('fs');
const pdfParse = require('pdf-parse');

const pdfPath = 'C:\\Users\\danie\\.openclaw\\media\\outbound\\34828ee3-e47c-43fc-bcb9-9b4cb6657992.pdf';

const dataBuffer = fs.readFileSync(pdfPath);

console.log('PDF loaded, size:', dataBuffer.length);

pdfParse(dataBuffer).then(function(data) {
  console.log('===PDF TEXT===');
  console.log(data.text);
  console.log('===END===');
}).catch(function(err) {
  console.error('Error:', err.message);
  console.error(err.stack);
});