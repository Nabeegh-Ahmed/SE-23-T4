import axios from 'axios';
import * as XLSX from 'xlsx/xlsx.mjs';

export function uploadLabPreferences({ name, number, email, labs }) {

    axios.post('http://127.0.0.1:5000/uploadLabInstructorsPreferences', {
        name, number, email, labs 
    }, {
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
    },
    )
}

export function uploadLabExcelFile(selectedFile) {
    const fileReader = new FileReader();

    fileReader.onload = () => {
        const data = new Uint8Array(fileReader.result);
        const workbook = XLSX.read(data, { type: 'array' });
        const worksheet = workbook.Sheets[workbook.SheetNames[0]];
        const rows = XLSX.utils.sheet_to_json(worksheet);
        console.log(rows)
    
        axios.post('http://127.0.0.1:5000/uploadLabInstructorsPreferences', rows, {
            headers: {
                'Content-Type': 'application/json',
                'Accept': '*/*'
            }
        })
    }

    fileReader.readAsArrayBuffer(selectedFile);

   


}