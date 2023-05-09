import XLSX from 'xlsx';

function TimetableButtons() {
  const handleExport = () => {
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = '.xlsx';
    fileInput.addEventListener('change', (event) => {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = (event) => {
        const data = new Uint8Array(event.target.result);
        const workbook = XLSX.read(data, { type: 'array' });
        const worksheet = workbook.Sheets[workbook.SheetNames[0]];
        const timetable = XLSX.utils.sheet_to_json(worksheet);
        // Handle timetable data
      }
      reader.readAsArrayBuffer(file);
    });
    fileInput.click();
  }

  return (
    <div>
      <Button
        variant="contained"
        color="primary"
        startIcon={<CloudUpload />}
        onClick={handleExport}
      >
        Export Timetable
      </Button>
    </div>
  );
}
