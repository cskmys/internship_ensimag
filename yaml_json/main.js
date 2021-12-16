"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var langcfg_json_1 = __importDefault(require("./langcfg.json"));
var keywordLst = [];
var keywordDocLst = [];
var regexPattern = '\\b';
var val = 1;
for (var _i = 0, _a = langcfg_json_1["default"].keywords; _i < _a.length; _i++) {
    var keyword = _a[_i];
    var curKeyword = {
        label: keyword.name,
        kind: 'CompletionItemKind.Text',
        data: val
    };
    keywordLst.push(curKeyword);
    var curKeywordDoc = {
        det: keyword.det,
        doc: keyword.doc
    };
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
    documentation: ''
};
var idx = item.data - 1;
item.detail = keywordDocLst[idx].det;
item.documentation = keywordDocLst[idx].doc;
console.log(item);
// console.log(keywordDocLst[idx]);
var text = "Typescript is typescript\nnot Javascript";
var pattern = new RegExp(regexPattern, 'gm'); // /\b[A-Z]{2,}\b/g;
// let pattern = /\bJavascript|Typescript|Coffeescript|Mochascript\b/gm
console.log(pattern);
var m;
var problems = 0;
while ((m = pattern.exec(text)) && problems < 20) {
    ++problems;
    console.log(m);
}
