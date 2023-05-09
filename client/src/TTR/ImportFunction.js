import XLSX from 'xlsx';

function TimetableButtons({ timetable }) {
  const handleImport = () => {
    const worksheet = XLSX.utils.json_to_sheet(timetable);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Timetable');
    XLSX.writeFile(workbook, 'timetable.xlsx');
  }

  return (
    <div>
      <Button
        variant="contained"
        color="primary"
        startIcon={<CloudDownload />}
        onClick={handleImport}
      >
        Import Timetable
      </Button>
    </div>
  );
}
