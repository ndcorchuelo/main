def autofit_column(self):
    workbook = self.Workbook(self.dataDir + 'Book1.xls')
    worksheet = workbook.getWorksheets().get(0)
    worksheet.autoFitColumn(3)
    workbook.save(self.dataDir + "Autofit Column.xls")
  
 print "Autofit Column Successfully."

  
