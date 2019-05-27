/**
 * Main program file
 * Acts as an entrypoint to the program
 *
 * @author Muhammad Aditya Hilmy, NIM 18217025
 */
const moment = require('moment');
const retriever = require('./retriever');
const parser = require('./parser');
const fs = require("fs");

// This constant specifies how many date ranges should be retrieved from the server
const ITERATE = 60;

/**
 * Main function/entrypoint
 * Retrieves data from website and build appropriate object
 * @returns {Promise<void>}
 */
async function main() {
    let date;
    let nested_data = [];
    for(let i = 0; i < ITERATE; i++) {
        let str = await retriever(date);
        let begin_date = parser.extract_begin_date(str);
        let end_date = parser.extract_end_date(str);
        let tables = parser.extract_tables(str);

        nested_data.push({
            begin_date: begin_date,
            end_date: end_date,
            data: tables
        });

        let yesterday = moment(begin_date).subtract(1, 'days');
        date = yesterday.format('YYYY-MM-DD');
    }

    write_json('../data/kurs_pajak.json', nested_data);
    write_normalized('../data/kurs_pajak_rdb_normalized.json', nested_data);
}

/**
 * Writes normalized format of data
 * @param filename file name
 * @param data nested data
 */
function write_normalized(filename, data) {
    let normalized_data = normalize_to_rdb(data);
    write_json(filename, normalized_data);
}

/**
 * Write JSON to file
 * @param filename file name
 * @param data data to serialize and write
 */
function write_json(filename, data) {
    let str_write = JSON.stringify(data, null, 4);
    fs.writeFileSync(filename, str_write);
}

/**
 * Normalize nested data to relational, normalized format
 * @param data nested data
 * @returns {{currencies: Array, records: Array}}
 */
function normalize_to_rdb(data) {
    let currency_map = {};
    let currency_records = [];
    let currency_names = [];

    // Iterate date
    data.forEach((row) => {
        let records = row.data;
        records.forEach((record) => {
            // Add currency to currency map if not exists
            if(!currency_map[record.currency_code]) {
                // Push to currency names
                currency_names.push({
                    currency: record.currency,
                    currency_code: record.currency_code
                });

                // Record on map, flag as added
                currency_map[record.currency_code] = true;
            }

            // Add record
            currency_records.push({
                currency_code: record.currency_code,
                value: record.value,
                change: record.change,
                begin_date: row.begin_date,
                end_date: row.end_date
            })
        });
    });

    return {
        currencies: currency_names,
        records: currency_records
    }
}

main();