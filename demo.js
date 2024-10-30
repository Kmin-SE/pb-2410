const express = require('express');
const https = require('https');
const fs = require('fs');

const app = express();

app.get('/download', (req, res) => {
    const fileUrl = 'https://s4-media1.study4.com/media/e24/audio/questions/Test_1/Test_1-32-34.mp3';
    https.get(fileUrl, (fileStream) => {
        res.setHeader('Content-Disposition', 'attachment; filename="Test_1-32-34.mp3"');
        fileStream.pipe(res);
    });
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));
