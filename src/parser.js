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

module.exports.extract_begin_date = function(raw) {
    const $ = cheerio.load(raw);
    let em_block = $('.text-muted > em');
    let html_text = em_block.text().trim();
    let date_range_str = html_text.replace("Tanggal Berlaku: ", '');
    let dates = date_range_str.split(' - ');
    let begin_date = dates[0];

    return format_date(begin_date);
};

module.exports.extract_end_date = function(raw) {
    const $ = cheerio.load(raw);
    let em_block = $('.text-muted > em');
    let html_text = em_block.text().trim();
    let date_range_str = html_text.replace("Tanggal Berlaku: ", '');
    let dates = date_range_str.split(' - ');
    let end_date = dates[1];

    return format_date(end_date);
};

function format_date(str) {
    let date_components = str.split(' ');
    if(!months[date_components[1]]) throw "Month not found!";
    let month_int = months[date_components[1]];
    let date_str = `${date_components[2]}-${pad(month_int, 2)}-${date_components[0]}`;
    return date_str;
}

function extract_rows(cheerio, table) {
    let rows = [];
    table.find('tr').each(function(i, elem) {
        rows.push(cheerio(this));
    });

    return rows;
}

function extract_fields(cheerio, row) {
    let fields = [];
    row.find('td').each(function(i, elem) {
        fields.push(cheerio(this).text());
    });

    return fields;
}

function parse_row(row) {
    return {
        currency: get_currency_name(row[1]),
        currency_code: get_currency_code(row[1]),
        value: preprocess_value(row[2]),
        change: preprocess_value(row[3])
    }
}

function preprocess_value(value_str) {
    let value_str_clean = value_str.replace(/ /g, '').replace(/,/g, '');
    return parseFloat(value_str_clean);
}

function get_currency_name(str) {
    return str.replace(` (${get_currency_code(str)})`, '');
}

function get_currency_code(str) {
    return str.match(/\((.*?)\)/)[1];
}

function pad(n, width, z) {
    z = z || '0';
    n = n + '';
    return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}
