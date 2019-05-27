const retriever = require('./retriever');
const parser = require('./parser');

const ITERATE = 6;

async function retrieve() {
    let date;
    let data = [];
    for(let i = 0; i < ITERATE; i++) {
        let str = await retriever(date);
        let begin_date = parser.extract_begin_date(str);
        let end_date = parser.extract_end_date(str);
        let tables = parser.extract_tables(str);

        data.push({
            begin_date: begin_date,
            end_date: end_date,
            data: tables
        });

        date = begin_date;
    }

    console.log(data);
}

retrieve();