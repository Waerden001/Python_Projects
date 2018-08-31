const fs = require('fs');

console.log(show('songs'));
console.log(show('scales'));
console.log(show('chords'));


function show(path) {
    let contents = fs.readdirSync(path);
    if (contents.length === 0) return '';
    let i = Math.floor(Math.random() * contents.length);
    let content = contents[i];
    return content + ':\n' + fs.readFileSync(path + '/' + content, 'utf-8') + '\n';
}
process.stdin.read();