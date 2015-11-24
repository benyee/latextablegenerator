import numpy as np

def print_table_preamble( caption, colformat, loc = '!ht', numcols = None ):
  #If given # of columns, check that colformat has that many columns
  if numcols != None:
    numcols2 = 0
    for char in colformat:
      if char in 'clr':
        numcols2 += 1
    assert(numcols == numcols2)

  print '\\begin{table}['+loc+']'
  print '\\caption{'+caption+'}'
  print '\\centering'
  print '\\begin{tabular}{'+colformat+'}'

def print_table_end( label = None ):
  print '\\end{tabular}'
  if label != None:
    print '\\label{tab:'+label+'}'
  print '\\end{table}'

def print_first_row( titles, colformat, numcols = None, numhlines = 1 ):
  numcols2 = 0
  for char in colformat:
    if char in 'clr':
      numcols2 += 1

  #If we aren't given numcols, set it equal to numcols2
  if numcols == None:
    numcols = numcols2
  #If we are given numcols, check that they match
  else:
    assert(numcols == numcols2)
  
  assert( len(titles)==numcols ) 

  #Split up colformat:
  colformat_split = [ '' for i in range(numcols) ]

  #Find the first character and put everything before the first
  # character in the entry of colformat_split
  char_indx = 0
  while colformat[char_indx] not in 'clr':
    colformat_split[0] += colformat[char_indx]
    char_indx += 1

  #Distribute colformat into colformat_split:
  col_indx = -1
  for char in colformat[char_indx:]:
    if char in 'clr':
      col_indx += 1
    colformat_split[col_indx] += char

  outstring = ''
  for (title, colformat_piece) in zip(titles, colformat_split):
    outstring += '\\multicolumn{1}{'+colformat_piece+'}{\\bf '+title+'} & '
  print outstring[:-2] + '\\\\ '+ numhlines*'\\hline'

def print_table_line( entries, islastline = False, numhlines = 0, numcols = None ):
  if numcols != None:
    assert( len(entries) == numcols )

  outstring = ''
  for entry in entries:
    outstring += entry + ' & '

  outstring = outstring[:-2]
  
  if numhlines > 0:
    outstring += '\\\\ ' + numhlines*'\\hline'
  elif not islastline:
    outstring += '\\\\'

  print outstring


colformat = 'c||c|r|l'
numcols = 4
print_table_preamble( 'test caption', colformat , numcols = numcols)
print_first_row( ['name','date','keff','$\\Delta$ keff'], colformat, numcols=numcols)
print_table_line( ['S01','Nov. 24','2.4444','+15 pcm'] )
print_table_line( ['S01','Nov. 24','2.4444','+15 pcm'] , numhlines = 1)
print_table_line( ['S06A','Nov. 24','2.4444','+15 pcm'] )
print_table_line( ['S06A','Nov. 24','2.4444','+15 pcm'] , numhlines = 1)
print_table_line( ['S06B','Nov. 24','2.4444','+15 pcm'] )
print_table_line( ['S06B','Nov. 24','2.4444','+15 pcm'] , islastline = True)
print_table_end( 'test' )
