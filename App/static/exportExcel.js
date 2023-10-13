function exportExcel() {
  
  let sheet = XLSX.utils.table_to_sheet(document.getElementById("TableProducts"));
  delete(sheet['G1']);
  delete(sheet['G2']);
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, sheet, "Ventas");
  XLSX.writeFile(workbook, `Ventas ${new Date()}.xlsx`);
}
