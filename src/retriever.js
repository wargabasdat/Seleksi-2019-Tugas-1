/**
 * Raw web page retriever
 * @author Muhammad Aditya Hilmy, NIM 18217025
 */
const axios = require('axios');
const moment = require('moment');
const qs = require('querystring');

const URL = "https://fiskal.kemenkeu.go.id/dw-kurs-db.asp";

module.exports = async function(date) {
    if(date)
        return retrieve_with_date(date);
    else
        return retrieve_without_date();
};

async function retrieve_with_date(date) {
    console.log(" [*] Retrieving raw HTML page from " + URL + ", with date = " + date + "...");

    let parsed_date = moment(date);
    let str_date = parsed_date.format('YYYYMMDD');
    let id = parsed_date.format('MM/DD/YYYY');

    let raw = await axios.post(URL, qs.stringify({strDate: str_date, id: id}));
    console.log(" [*] HTML retrieved.");
    return raw.data;
}

async function retrieve_without_date() {
    console.log(" [*] Retrieving raw HTML page from " + URL + "...");
    let raw = await axios.get(URL);
    console.log(" [*] HTML retrieved.");
    return raw.data;
}