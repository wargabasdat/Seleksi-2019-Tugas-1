/**
 * Page parser
 * @author Muhammad Aditya Hilmy, NIM 18217025
 */

const cheerio = require('cheerio');

const months = {
    'Januari': 1,
    'Februari': 2,
    'Maret': 3,
    'April': 4,
    'May': 5,
    'Juni': 6,
    'Juli': 7,
    'Agustus': 8,
    'September': 9,
    'Oktober': 10,
    'November': 11,
    'Desember': 12
};

/**
 * Extracts <table/> element from raw HTML string
 * @param raw Raw HTML string
 * @returns Array of Cheerio <table> DOMs
 */
module.exports.extract_tables = function(raw) {
    const $ = cheerio.load(raw);
    let table = $('table');
    let rows = extract_rows($, table);

    // Exclude row 0
    delete rows[0];

    let data = [];

    rows.forEach((row) => {
        let fields = extract_fields($, row);
        let parsed_row = parse_row(fields);

        data.push(parsed_row);
    });

    return data;
};

/**
 * Extract the begin date of the records
 * @param raw Raw HTML string
 * @returns YYYY-MM-DD representation of the date
 */
module.exports.extract_begin_date = function(raw) {
    const $ = cheerio.load(raw);
    let em_block = $('.text-muted > em');
    let html_text = em_block.text().trim();
    let date_range_str = html_text.replace("Tanggal Berlaku: ", '');
    let dates = date_range_str.split(' - ');
    let begin_date = dates[0];

    return format_date(begin_date);
};

/**
 * Extract the end date of the records
 * @param raw Raw HTML string
 * @returns YYYY-MM-DD representation of the date
 */
module.exports.extract_end_date = function(raw) {
    const $ = cheerio.load(raw);
    let em_block = $('.text-muted > em');
    let html_text = em_block.text().trim();
    let date_range_str = html_text.replace("Tanggal Berlaku: ", '');
    let dates = date_range_str.split(' - ');
    let end_date = dates[1];

    return format_date(end_date);
};

/**
 * Format date
 * @param str (Inconsistent) date string in the webpage
 * @returns Standardized date, format: YYYY-MM-DD
 */
function format_date(str) {
    let date_components = str.split(' ');
    if(!months[date_components[1]]) throw "Month not found!";
    let month_int = months[date_components[1]];
    let date_str = `${date_components[2]}-${pad(month_int, 2)}-${date_components[0]}`;
    return date_str;
}

/**
 * Extract rows from table
 * @param cheerio Cheerio instance
 * @param table Cheerio table DOM
 * @returns Array of Cheerio <tr> DOMs
 */
function extract_rows(cheerio, table) {
    let rows = [];
    table.find('tr').each(function(i, elem) {
        rows.push(cheerio(this));
    });

    return rows;
}

/**
 * Extract fields from table's td
 * @param cheerio Cheerio instance
 * @param row Cheerio <tr> DOM
 * @returns Array of String of retrieved fields
 */
function extract_fields(cheerio, row) {
    let fields = [];
    row.find('td').each(function(i, elem) {
        fields.push(cheerio(this).text());
    });

    return fields;
}

/**
 * Parse row
 * Convert row fields into Object
 * @param row row fields
 * @returns {{currency: *, currency_code: *, value, change}}
 */
function parse_row(row) {
    return {
        currency: get_currency_name(row[1]),
        currency_code: get_currency_code(row[1]),
        value: preprocess_value(row[2]),
        change: preprocess_value(row[3])
    }
}

/**
 * Preprocess currency value
 * @param value_str unformatted value string
 * @returns float of value
 */
function preprocess_value(value_str) {
    let value_str_clean = value_str.replace(/ /g, '').replace(/,/g, '');
    return parseFloat(value_str_clean);
}

/**
 * Extract currency name from combined currency name string
 * @param str Combined currency name string
 * @returns Currency name
 */
function get_currency_name(str) {
    return str.replace(` (${get_currency_code(str)})`, '');
}

/**
 * Extract currency code from combined currency name string
 * @param str Combined currency name string
 * @returns Currency code
 */
function get_currency_code(str) {
    return str.match(/\((.*?)\)/)[1];
}

/**
 * Pad integer with zeroes
 * @param n
 * @param width
 * @param z
 * @returns {*}
 */
function pad(n, width, z) {
    z = z || '0';
    n = n + '';
    return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}
