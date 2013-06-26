"""
http://codegolf.stackexchange.com/questions/11843/convert-this-character-based-table-into-html-one

Take a following character table:

-------------------------------------------------------
|       |1233456 | abc    | xyz    |        |         |
|-------|--------|--------|--------|--------|---------|
|       |abcdefgh| 1234567|        | 12345  |         |
|   abc |xyzabcqw|        |        |        |         |
|       |zzzz    |        |        |        |         |
|-------|--------|--------|--------|--------|---------|
It can have a variable number of columns or rows. Column width and row height can vary. Cells can be empty or have text, but the row height is optimized to wrap the text. So, second row has three lines because second cell content in second row is three lines high.

Input is ASCII text as shown in example. Cells can not contain | or - characters. Cell content should be escaped, but no need to worry about rowspan and colspan, since the table structure is always simple (every row same number of columns and every column same number of rows).

Output should be well-formed xhtml. Html table should reflect the table structure, content and line breaks. So, resulting html based on the sample input above is the following:

<table>
<tr>
    <td></td>
    <td>1233456</td>
    <td>abc</td>
    <td>xyz</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>abc</td>
    <td>abcdefgh<br/>xyzabcqw<br/>zzzz</td>
    <td>1234567</td>
    <td></td>
    <td>12345</td>
    <td></td>
</tr>
</table>
Shortest code which takes this table and turns it into an xhtml table wins.
"""


table = []
line = raw_input()
row = []
while line:
  if '-' in line:
		if row:
			table.append(row)
			row = []
	else:
		if not row:
			row = [cell.strip() for cell in line.split('|')[1:-1]]
		else:
			line = line.split('|')[1:-1]
			row = ["<br />".join([row[i],line[i].strip()]) if line[i].strip() and row[i] else row[i] if row[i] else line[i].strip() for i in range(len(line))]
	line = raw_input()
			
html = "<table>"
for row in table:
	html += "\n<tr>\n<td>" + "</td>\n<td>".join(row) + "</td>\n</tr>"
html += "\n</table>"

print html
