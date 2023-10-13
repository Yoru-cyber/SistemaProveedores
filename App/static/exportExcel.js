function exportExcel() {
  
  let sheet = XLSX.utils.table_to_sheet(document.getElementById("TableProducts"));
  let range = XLSX.utils.decode_range(sheet['!fullref']);
  const { r } = range.e;
  for (let i = 0; i <= r; i++) {
    delete(sheet[`G${i + 1}`]);
  }
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, sheet, "Ventas");
  XLSX.writeFile(workbook, `Ventas ${new Date()}.xlsx`);
}
