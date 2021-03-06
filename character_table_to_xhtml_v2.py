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
#single character variable names to reduce character count of the code (shortest code wins)

t = [] #table
l = raw_input() #line
r = [] #row
while l:
	if '-' in l:
		if r:
			t.append(r)
			r = []
	else:
		if not r:
			r = [c.strip() for c in l.split('|')[1:-1]]
		else:
			l = l.split('|')[1:-1]
			r = ["<br />".join([r[i],l[i].strip()]) if l[i].strip() and r[i] else r[i] if r[i] else l[i].strip() for i in range(len(l))]
	l = raw_input()
			
h = "<table>" #corresponding html code
for r in t:
	h += "\n<tr>\n<td>" + "</td>\n<td>".join(r) + "</td>\n</tr>"
h += "\n</table>"

print h
