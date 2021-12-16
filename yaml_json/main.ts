import langcfg from './langcfg.json';
let keywordLst: any[] = [];
let keywordDocLst: any[] = [];
let regexPattern: string = '\\b';
let val: number = 1;
for (var keyword of langcfg.keywords) {
    var curKeyword = {
        label: keyword.name,
        kind: 'CompletionItemKind.Text',
        data: val
    }
    keywordLst.push(curKeyword);
    var curKeywordDoc = {
        det: keyword.det,
        doc: keyword.doc,
    }
    keywordDocLst.push(curKeywordDoc);
    ++val;
    regexPattern += keyword.name[0].toUpperCase() + keyword.name.slice(1) + '|';
}
regexPattern = regexPattern.slice(0, -1);
regexPattern += '\\b';
console.log(regexPattern);
console.log(keywordLst);
var item = {
    data: 1,
    detail: '',
    documentation: '',
}
let idx: number = item.data - 1;
item.detail = keywordDocLst[idx].det;
item.documentation = keywordDocLst[idx].doc;
console.log(item);
// console.log(keywordDocLst[idx]);

let text = "Typescript is typescript\nnot Javascript";
let pattern = new RegExp(regexPattern, 'gm');
console.log(pattern)
let m: RegExpExecArray | null;
let problems = 0;
while ((m = pattern.exec(text)) && problems < 20) {
    ++problems;
    console.log(m);
}
