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

/**
 * Retrieve webpage WITH date parameter set
 * @param date date in YYYY-MM-DD
 * @returns {Promise<*>}
 */
async function retrieve_with_date(date) {
    console.log(" [*] Retrieving raw HTML page from " + URL + ", with date = " + date + "...");

    let parsed_date = moment(date);
    let str_date = parsed_date.format('YYYYMMDD');
    let id = parsed_date.format('MM/DD/YYYY');

    let raw = await axios.post(URL, qs.stringify({strDate: str_date, id: id}), {
        headers: {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64); Basis Data/Admin Basis Data/basisdata@std.stei.itb.ac.id'
        }
    });
    console.log(" [*] HTML retrieved.");
    return raw.data;
}

/**
 * Retrieve webpage WITHOUT date parameter set
 * @returns {Promise<*>}
 */
async function retrieve_without_date() {
    console.log(" [*] Retrieving raw HTML page from " + URL + "...");
    let raw = await axios.get(URL, null, {
        headers: {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64); Basis Data/Admin Basis Data/basisdata@std.stei.itb.ac.id'
        }
    });
    console.log(" [*] HTML retrieved.");
    return raw.data;
}