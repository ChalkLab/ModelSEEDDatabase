def filterText(unfilteredText):
   filteredText = str(unfilteredText[2:-3])
   finishedText = filteredText.replace('\\n', ' ')
   if 'Status: 404' in finishedText:
      finishedText = ""
   if 'Status: 503' in finishedText:
      finishedText = "503: Server Busy Error"
   return(finishedText)

def filterSeperateText(unfilteredText):
   filteredText = str(unfilteredText[2:-3])
   finishedText = filteredText.replace('\\n', '; ')
   if 'Status: 404' in finishedText:
      finishedText = ""
   if 'Status: 503' in finishedText:
      finishedText = "503: Server Busy Error"
   return(finishedText)
